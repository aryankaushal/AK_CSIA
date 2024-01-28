import sys
import smtplib, ssl
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialog,
    QStackedWidget,
    QRadioButton,
    QTextEdit,
    QTextBrowser,
    QMessageBox,
)
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtCore import pyqtSignal, Qt
from email.mime.text import MIMEText
from random import randint, sample
from UI import LearnUI, TestUI, HomeUI
import time, datetime


# *************************************** Learn Page ***************************************
class LearnPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Climaware Learn")
        self.learn_title = QLabel("\nClimaware Learn")
        self.learn_title.setFont(QFont("Arial", 60, QFont.Bold))
        self.learn_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.learn_title.setStyleSheet("color: black;")

        self.learn_label = QLabel(
            "Welcome to the Climaware Learn page.\n\nThis is where you can \nstudy your climate change material.\n\nWhat do you want to learn about?"
        )
        self.learn_label.setFont(QFont("Arial", 25))
        self.learn_label.setAlignment(Qt.AlignHCenter)
        self.learn_label.setStyleSheet("color: #004894;")

        self.setGeometry(512, 100, 500, 900)
        # self.setStyleSheet("background-color: grey;")
        self.setStyleSheet("background-color: #F4B970;")

        self.causes_button = QPushButton("Causes")
        self.effects_button = QPushButton("Effects")
        self.solutions_button = QPushButton("Solutions")

        self.causes_button.clicked.connect(self.show_causes_page)
        self.effects_button.clicked.connect(self.show_effects_page)
        self.solutions_button.clicked.connect(self.show_solutions_page)

        self.causes_button.setStyleSheet(
            "background-color: #D73701; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.effects_button.setStyleSheet(
            "background-color: #048FB8; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.solutions_button.setStyleSheet(
            "background-color: #96EE85; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        layout = QVBoxLayout()
        layout.addWidget(self.learn_title)
        layout.addWidget(self.learn_label)
        layout.addWidget(self.causes_button)
        layout.addWidget(self.effects_button)
        layout.addWidget(self.solutions_button)

        self.setLayout(layout)

    def show_causes_page(self):
        page = CausePage()

        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_effects_page(self):
        page = EffectsPage()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def show_solutions_page(self):
        page = SolutionsPage()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(2)


# ******************************* Learn Page --> Causes Pages *******************************
class CausePage(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Climaware Learn: Causes")

        self.cause_title = QLabel("\nClimaware Learn: Causes")
        self.cause_title.setFont(QFont("Arial", 60, QFont.Bold))
        self.cause_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.cause_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #F4B970;")

        self.setGeometry(512, 100, 500, 900)

        self.causes_label = QLabel(
            "Which phenomenon's causes do you want to learn about?"
        )
        self.causes_label.setFont(QFont("Arial", 25))
        self.causes_label.setAlignment(Qt.AlignHCenter)
        self.causes_label.setStyleSheet("color: #004894;")

        self.airC_button = QPushButton("Air Pollution")
        self.waterC_button = QPushButton("Water Pollution")
        self.landC_button = QPushButton("Land Pollution")
        self.globalC_button = QPushButton("Global Warming")

        # self.setStyleSheet("background-color: grey;")
        # self.setFixedSize(500, 1000)

        self.airC_button.setStyleSheet(
            "background-color: #A6AAAA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.waterC_button.setStyleSheet(
            "background-color: #2194DA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.landC_button.setStyleSheet(
            "background-color: #6C2E19; color: white; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.globalC_button.setStyleSheet(
            "background-color: #B88E12; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.cause_title)
        layout.addWidget(self.causes_label)
        layout.addWidget(self.airC_button)
        layout.addWidget(self.waterC_button)
        layout.addWidget(self.landC_button)
        layout.addWidget(self.globalC_button)
        # layout.addWidget(self.learn_label)

        self.airC_button.clicked.connect(self.show_airC)
        self.waterC_button.clicked.connect(self.show_waterC)
        self.landC_button.clicked.connect(self.show_landC)
        self.globalC_button.clicked.connect(self.show_globalC)

        self.setLayout(layout)

    def show_airC(self):
        page = AirCauses()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_waterC(self):
        page = WaterCauses()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def show_landC(self):
        page = LandCauses()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_globalC(self):
        page = GlobalCauses()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def go_back(self):
        self.close()


class AirCauses(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Causes")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Air Pollution Causes")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.airC_button = QPushButton("Air Pollution")
        self.waterC_button = QPushButton("Water Pollution")
        self.landC_button = QPushButton("Land Pollution")
        self.globalC_button = QPushButton("Land Pollution")

        self.setGeometry(512, 100, 500, 900)

        self.info_label = QLabel(self.read_info_from_file("Text Files/air_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.airC_title)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class LandCauses(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Causes")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Land Pollution Causes")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(self.read_info_from_file("Text Files/land_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class WaterCauses(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Causes")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Water Pollution Causes")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/water_causes.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class GlobalCauses(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Causes")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Global Warming Causes")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/global_causes.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


# ********************************************************************************************


# ******************************* Learn Page --> Effects Pages *******************************
class EffectsPage(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Climaware Learn: Effects")

        self.effect_title = QLabel("\nClimaware Learn: Effects")
        self.effect_title.setFont(QFont("Arial", 60, QFont.Bold))
        self.effect_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.effect_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #F4B970;")

        self.setGeometry(512, 100, 500, 900)

        self.causes_label = QLabel(
            "Which phenomenon's effects do you want to learn about?"
        )
        self.causes_label.setFont(QFont("Arial", 25))
        self.causes_label.setAlignment(Qt.AlignHCenter)
        self.causes_label.setStyleSheet("color: #004894;")
        self.airE_button = QPushButton("Air Pollution")
        self.waterE_button = QPushButton("Water Pollution")
        self.landE_button = QPushButton("Land Pollution")
        self.globalE_button = QPushButton("Global Warming")

        self.airE_button.setStyleSheet(
            "background-color: #A6AAAA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.waterE_button.setStyleSheet(
            "background-color: #2194DA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.landE_button.setStyleSheet(
            "background-color: #6C2E19; color: white; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.globalE_button.setStyleSheet(
            "background-color: #B88E12; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.setGeometry(512, 100, 500, 900)
        # self.setStyleSheet("background-color: grey;")
        # self.setFixedSize(500, 1000)

        layout = QVBoxLayout()
        layout.addWidget(self.effect_title)
        layout.addWidget(self.causes_label)
        layout.addWidget(self.airE_button)
        layout.addWidget(self.waterE_button)
        layout.addWidget(self.landE_button)
        layout.addWidget(self.globalE_button)
        # layout.addWidget(self.learn_label)

        self.airE_button.clicked.connect(self.show_airE)
        self.waterE_button.clicked.connect(self.show_waterE)
        self.landE_button.clicked.connect(self.show_landE)
        self.globalE_button.clicked.connect(self.show_globalE)

        self.setLayout(layout)

    def show_airE(self):
        page = AirEffects()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_waterE(self):
        page = WaterEffects()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def show_landE(self):
        page = LandEffects()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_globalE(self):
        page = GlobalEffects()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def go_back(self):
        self.close()


class AirEffects(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Effects")
        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Air Pollution Effects")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")
        self.info_label = QLabel(self.read_info_from_file("Text Files/air_effects.txt"))
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class LandEffects(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Effects")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Land Pollution Effects")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/land_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class WaterEffects(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Effects")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Water Pollution Effects")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/water_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class GlobalEffects(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Effects")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Global Warming Effects")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/global_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


# *********************************************************************************************


# ****************************** Learn Page --> Solutions Pages *******************************
class SolutionsPage(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Climaware Learn: Solutions")

        self.sol_title = QLabel("\nClimaware Learn: Solutions")
        self.sol_title.setFont(QFont("Arial", 60, QFont.Bold))
        self.sol_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.sol_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #F4B970;")

        self.setGeometry(512, 100, 500, 900)

        self.causes_label = QLabel(
            "Which phenomenon's solutions do you want to learn about?"
        )
        self.causes_label.setFont(QFont("Arial", 25))
        self.causes_label.setAlignment(Qt.AlignHCenter)
        self.causes_label.setStyleSheet("color: #004894;")
        self.airS_button = QPushButton("Air Pollution")
        self.waterS_button = QPushButton("Water Pollution")
        self.landS_button = QPushButton("Land Pollution")
        self.globalS_button = QPushButton("Global Warming")

        self.airS_button.setStyleSheet(
            "background-color: #A6AAAA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.waterS_button.setStyleSheet(
            "background-color: #2194DA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.landS_button.setStyleSheet(
            "background-color: #6C2E19; color: white; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.globalS_button.setStyleSheet(
            "background-color: #B88E12; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.setGeometry(512, 100, 500, 900)
        # self.setStyleSheet("background-color: grey;")
        # self.setFixedSize(500, 1000)

        layout = QVBoxLayout()
        layout.addWidget(self.sol_title)
        layout.addWidget(self.causes_label)
        layout.addWidget(self.airS_button)
        layout.addWidget(self.waterS_button)
        layout.addWidget(self.landS_button)
        layout.addWidget(self.globalS_button)
        # layout.addWidget(self.learn_label)

        self.airS_button.clicked.connect(self.show_airS)
        self.waterS_button.clicked.connect(self.show_waterS)
        self.landS_button.clicked.connect(self.show_landS)
        self.globalS_button.clicked.connect(self.show_globalS)

        self.setLayout(layout)

    def show_airS(self):
        page = AirSol()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_waterS(self):
        page = WaterSol()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def show_landS(self):
        page = LandSol()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(0)

    def show_globalS(self):
        page = GlobalSol()
        page.exec_()
        # self.stacked_widget.setCurrentIndex(1)

    def go_back(self):
        self.close()


class AirSol(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Solutions")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Air Pollution Solutions")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(self.read_info_from_file("Text Files/air_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class LandSol(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Solutions")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Land Pollution Solutions")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(self.read_info_from_file("Text Files/land_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class WaterSol(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Solutions")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Water Pollution Solutions")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(self.read_info_from_file("Text Files/water_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


class GlobalSol(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Solutions")

        self.setGeometry(512, 100, 500, 900)

        self.airC_title = QLabel("Global Warming Solutions")
        self.airC_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.airC_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.airC_title.setStyleSheet("color: black;")

        self.setStyleSheet("background-color: #493FA7;")

        self.info_label = QLabel(self.read_info_from_file("Text Files/global_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


# *********************************************************************************************
