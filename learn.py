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
from login import AuthHandler


# *************************************** Learn Page ***************************************
class LearnPage(QDialog):
    def __init__(self):
        super().__init__()

        self.learn_title = QLabel("Climaware Learn")
        self.learn_title.setFont(QFont("Arial", 50, QFont.Bold))
        self.learn_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.learn_title.setStyleSheet("color: black;")

        self.learn_label = QLabel(
            "Welcome to the Climaware Learn page.\nThis is where you can study your climate change material.\nWhat do you want to learn about?"
        )
        self.learn_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.learn_label.setAlignment(Qt.AlignHCenter)
        self.learn_label.setStyleSheet("color: #004894;")

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)
        self.setStyleSheet("background-color: #F4B970;")

        self.causes_button = QPushButton("Causes")
        self.effects_button = QPushButton("Effects")
        self.solutions_button = QPushButton("Solutions")

        self.causes_button.clicked.connect(self.show_causes_page)
        self.effects_button.clicked.connect(self.show_effects_page)
        self.solutions_button.clicked.connect(self.show_solutions_page)

        self.causes_button.setStyleSheet(
            "background-color: yellow; color: black; border-radius: 20px; font-size: 16px; min-width: 30; min-height: 50px;"
        )
        self.effects_button.setStyleSheet(
            "background-color: blue; color: black; border-radius: 20px; font-size: 16px; min-width: 30; min-height: 50px;"
        )
        self.solutions_button.setStyleSheet(
            "background-color: lightgreen; color: black; border-radius: 20px; font-size: 16px; min-width: 30; min-height: 50px;"
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

        self.causes_label = QLabel(
            "Which phenomenon's causes do you want to learn about?"
        )

        self.airC_button = QPushButton("Air Pollution")
        self.waterC_button = QPushButton("Water Pollution")
        self.landC_button = QPushButton("Land Pollution")
        self.globalC_button = QPushButton("Land Pollution")

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        layout = QVBoxLayout()
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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/air_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/land_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/water_causes.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/global_causes.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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

        self.airE_button = QPushButton("Air Pollution")
        self.waterE_button = QPushButton("Water Pollution")
        self.landE_button = QPushButton("Land Pollution")
        self.globalE_button = QPushButton("Land Pollution")

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        layout = QVBoxLayout()
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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/air_effects.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/land_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/water_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(
            self.read_info_from_file("Text Files/global_effects.txt")
        )

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        # layout.addWidget(self.test_button)

        # self.test_button = QPushButton("Let's Test")
        # self.test_button.clicked.connect(self.show_test_page)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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

        self.airS_button = QPushButton("Air Pollution")
        self.waterS_button = QPushButton("Water Pollution")
        self.landS_button = QPushButton("Land Pollution")
        self.globalS_button = QPushButton("Land Pollution")

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        layout = QVBoxLayout()
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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/air_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/land_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/water_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

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
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("Text Files/global_sol.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def go_back(self):
        self.parent().stacked_widget.setCurrentIndex(
            1
        )  # Assuming index 1 is the CourseMaterialPage

    def read_info_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Information not available."


# *********************************************************************************************
