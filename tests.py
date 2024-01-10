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
import random
from UI import LearnUI, TestUI, HomeUI
import time, datetime
from login import AuthHandler
import csv


# *********************************** Test Page --> Quizzes ***********************************
class TestPage(QDialog):
    def __init__(self):
        super().__init__()
        self.test_label = QLabel(
            "Welcome to the Climaware Test page. This is where you can test your climate change knowledge. What do you want to be quizzed on?"
        )

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.air_button = QPushButton("Air Pollution")
        self.water_button = QPushButton("Water Pollution")
        self.land_button = QPushButton("Land Pollution")
        self.global_button = QPushButton("Global Warming")

        layout = QVBoxLayout()
        layout.addWidget(self.air_button)
        layout.addWidget(self.water_button)
        layout.addWidget(self.land_button)
        layout.addWidget(self.global_button)

        self.air_button.clicked.connect(
            lambda: self.initiate_test("Air Pollution", "Text Files/air_quiz.csv")
        )
        self.water_button.clicked.connect(
            lambda: self.initiate_test("Water Pollution", "Text Files/water_quiz.csv")
        )
        self.land_button.clicked.connect(
            lambda: self.initiate_test("Land Pollution", "Text Files/land_quiz.csv")
        )
        self.global_button.clicked.connect(
            lambda: self.initiate_test("Global Warming", "Text Files/global_quiz.csv")
        )

        self.setLayout(layout)

    def initiate_test(self, topic, file_name):
        test_dialog = TestDialog(topic, file_name)
        result = test_dialog.exec_()

        # Handle the result if needed


class TestDialog(QDialog):
    def __init__(self, topic, file_name):
        super().__init__()

        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 1000)

        self.questions = self.load_questions_from_file(file_name)
        self.current_question = 0
        self.score = 0

        self.question_label = QLabel(self.questions[self.current_question]["question"])

        self.option_buttons = []
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            button = QRadioButton(option)
            self.option_buttons.append(button)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_answer)

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        for button in self.option_buttons:
            layout.addWidget(button)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def load_questions_from_file(self, file_path):
        questions = []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                all_questions = list(reader)

                # Randomly select 5 indices
                selected_indices = random.sample(range(1, 20), 5)

                for data in all_questions:
                    if int(data["index"]) in selected_indices:
                        question = {
                            "question": data["question"],
                            "options": [data[f"option{i}"] for i in range(1, 5)],
                            "correct": data["correct"],
                        }
                        questions.append(question)

        except FileNotFoundError:
            QMessageBox.critical(
                self, "File Not Found", f"Question file '{file_path}' not found."
            )
            self.reject()

        return questions

    def submit_answer(self):
        selected_option = None
        for i, button in enumerate(self.option_buttons):
            if button.isChecked():
                selected_option = i + 1  # Options are 1-indexed

        correct_option = self.questions[self.current_question]["correct"]

        if selected_option == correct_option:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def update_question(self):
        self.question_label.setText(self.questions[self.current_question]["question"])

        for i, option in enumerate(self.questions[self.current_question]["options"]):
            self.option_buttons[i].setText(option)
            self.option_buttons[i].setChecked(False)

    def show_result(self):
        QMessageBox.information(
            self, "Quiz Result", f"You scored {self.score} out of {len(self.questions)}"
        )

        if self.score <= 1:
            result_message = "Study some more."
        elif self.score <= 3:
            result_message = "Good job!"
        elif self.score == 4:
            result_message = "Well done!"
        else:
            result_message = "Wow! A perfect score!"

        QMessageBox.information(self, "Result Message", result_message)

        self.accept()


class AirQuiz(TestPage):
    def __init__(self):
        super().__init__("Air Pollution Quiz", "Text Files/air_quiz.csv")


class WaterQuiz(TestPage):
    def __init__(self):
        super().__init__("Water Pollution Quiz", "Text Files/water_quiz.csv")


class LandQuiz(TestPage):
    def __init__(self):
        super().__init__("Land Pollution Quiz", "Text Files/land_quiz.csv")


class GlobalQuiz(TestPage):
    def __init__(self):
        super().__init__("Global Warming Quiz", "Text Files/global_quiz.csv")


# *********************************************************************************************
