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
from PyQt5.QtGui import QPixmap, QColor
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

        self.learn_label = QLabel(
            "Welcome to the Climaware Learn page. This is where you can study your climate change material. What do you want to learn about?"
        )

        self.causes_button = QPushButton("Causes")
        self.effects_button = QPushButton("Effects")
        self.solutions_button = QPushButton("Solutions")

        self.causes_button.clicked.connect(self.show_causes_page)
        self.effects_button.clicked.connect(self.show_effects_page)
        self.solutions_button.clicked.connect(self.show_solutions_page)

        layout = QVBoxLayout()
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
    def __init__(self, cause_name):
        super().__init__()

        self.causes_label = QLabel(
            "Which phenomenon's causes do you want to learn about?"
        )

        self.airC_button = QPushButton("Air Pollution")
        self.waterC_button = QPushButton("Water Pollution")
        self.landC_button = QPushButton("Land Pollution")
        self.globalC_button = QPushButton("Land Pollution")

        layout = QVBoxLayout()
        layout.addWidget(self.airC_button)
        layout.addWidget(self.waterC_button)
        layout.addWidget(self.landC_button)
        layout.addWidget(self.globalC_button)
        layout.addWidget(self.learn_label)

        self.setLayout(layout)

    def go_back(self):
        self.close()


class AirCauses(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Causes")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("air_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class LandCauses(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Causes")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("land_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class WaterCauses(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Causes")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("water_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class GlobalCauses(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Causes")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("global_causes.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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
    def __init__(self, effect_name):
        super().__init__()

        self.effects_label = QLabel(
            "Which phenomenon's effects do you want to learn about?"
        )

        self.airE_button = QPushButton("Air Pollution")
        self.waterE_button = QPushButton("Water Pollution")
        self.landE_button = QPushButton("Land Pollution")
        self.globalE_button = QPushButton("Land Pollution")

        layout = QVBoxLayout()
        layout.addWidget(self.airE_button)
        layout.addWidget(self.waterE_button)
        layout.addWidget(self.landE_button)
        layout.addWidget(self.globalE_button)
        layout.addWidget(self.learn_label)

        self.setLayout(layout)

    def go_back(self):
        self.close()


class AirEffects(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Effects")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("air_effects.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class LandEffects(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Effects")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("land_effects.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class WaterEffects(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Effects")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("water_effects.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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


class GlobalEffects(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Effects")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("global_effects.txt"))

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)

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
    def __init__(self, solution_name):
        super().__init__()

        self.sol_label = QLabel(
            "Which phenomenon's solutions do you want to learn about?"
        )

        self.airS_button = QPushButton("Air Pollution")
        self.waterS_button = QPushButton("Water Pollution")
        self.landS_button = QPushButton("Land Pollution")
        self.globalS_button = QPushButton("Land Pollution")

        layout = QVBoxLayout()
        layout.addWidget(self.airS_button)
        layout.addWidget(self.waterS_button)
        layout.addWidget(self.landS_button)
        layout.addWidget(self.globalS_button)
        layout.addWidget(self.learn_label)

        self.setLayout(layout)

    def go_back(self):
        self.close()


class AirSol(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Air Pollution Solutions")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("air_sol.txt"))

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


class LandSol(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Land Pollution Solutions")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("land_sol.txt"))

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


class WaterSol(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Pollution Solutions")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("water_sol.txt"))

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


class GlobalSol(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Global Warming Solutions")

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.info_label = QLabel(self.read_info_from_file("global_sol.txt"))

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
