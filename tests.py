from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLabel,
    QPushButton,
    QDialog,
    QRadioButton,
    QMessageBox,
)
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from email.mime.text import MIMEText
import random
import time, datetime
import csv


# *********************************** Test Page --> Quizzes ***********************************
class TestPage(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Climaware Test")
        self.test_title = QLabel("\nClimaware Test")
        self.test_title.setFont(QFont("Arial", 60, QFont.Bold))
        self.test_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.test_title.setStyleSheet("color: black;")

        self.test_label = QLabel(
            "Welcome to the Climaware Test page.\n\nThis is where you can \ntest your climate change knowledge.\n\nWhat do you want to test?"
        )
        self.test_label.setFont(QFont("Arial", 25))
        self.test_label.setAlignment(Qt.AlignHCenter)
        self.test_label.setStyleSheet("color: #004894;")

        self.setGeometry(512, 100, 500, 900)
        # self.setStyleSheet("background-color: grey;")
        self.setStyleSheet("background-color: #F4B970;")

        self.setGeometry(512, 100, 500, 900)
        self.setStyleSheet("background-color: #F3A3DB;")
        # self.setStyleSheet("background-color: grey;")
        self.setFixedSize(500, 900)

        self.air_button = QPushButton("Air Pollution")
        self.water_button = QPushButton("Water Pollution")
        self.land_button = QPushButton("Land Pollution")
        self.global_button = QPushButton("Global Warming")
        self.mixed_button = QPushButton("Mixed Timed Quiz")

        self.air_button.setStyleSheet(
            "background-color: #A6AAAA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.water_button.setStyleSheet(
            "background-color: #2194DA; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.land_button.setStyleSheet(
            "background-color: #6C2E19; color: white; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.global_button.setStyleSheet(
            "background-color: #B88E12; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )
        self.mixed_button.setStyleSheet(
            "background-color: #FF6399; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.test_title)
        layout.addWidget(self.test_label)
        layout.addWidget(self.air_button)
        layout.addWidget(self.water_button)
        layout.addWidget(self.land_button)
        layout.addWidget(self.global_button)
        layout.addWidget(self.mixed_button)

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
        self.mixed_button.clicked.connect(
            lambda: self.initiate_test("Mixed", "Text Files/mixed_quiz.csv")
        )

        self.setLayout(layout)

    def initiate_test(self, topic, file_name):
        test_dialog = TestDialog(topic, file_name)
        result = test_dialog.exec_()

class TestDialog(QDialog):
    def __init__(self, topic, file_name):
        super().__init__()

        self.setWindowTitle("Climaware Quiz")
        self.quiz_title = QLabel("\nClimaware Quiz")
        self.quiz_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.quiz_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.quiz_title.setStyleSheet("color: black;")

        self.setGeometry(512, 100, 500, 900)
        self.setStyleSheet("background-color: #DFA528;")

        self.questions = self.load_questions_from_file(file_name)
        self.current_question = 0
        self.score = 0

        self.mixed_bag_mode = topic == "Mixed Bag Test"
        if self.mixed_bag_mode:
            self.initialize_mixed_bag_test()
        else:
            self.initialize_regular_test()

    def initialize_mixed_bag_test(self):
        self.setWindowTitle("Mixed Bag Test")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_handler)
        self.timer_interval = 180000  # 3 minutes
        self.timer.start(self.timer_interval)

        self.question_queue = self.load_questions_from_file("mixed_bag_quiz.csv")
        random.shuffle(self.question_queue)

        self.update_question()

        self.question_label = QLabel(self.questions[self.current_question]["question"])
        self.question_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.question_label.setAlignment(Qt.AlignHCenter)
        self.question_label.setStyleSheet("color: #5A246A;")

        self.option_buttons = []
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            button = QRadioButton(option)
            button.setFont(QFont("Arial", 20))
            button.setStyleSheet("color: black;")
            self.option_buttons.append(button)
            print("\n")

        self.submit_button = QPushButton("Submit")
        self.submit_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.submit_button.setStyleSheet(
            "background-color: #5A246A; color: white; border-radius: 20px; font-size: 20px; min-width: 20; min-height: 50px;"
        )
        self.submit_button.clicked.connect(self.submit_answer)

        layout = QVBoxLayout()
        layout.addWidget(self.quiz_title)
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

        correct_option = int(self.questions[self.current_question]["correct"])

        for i, button in enumerate(self.option_buttons):
            if button.isChecked():
                selected_option = i + 1  # Options are 1-indexed

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
        self.setWindowTitle("Air Pollution Quiz")
        super().__init__("Air Pollution Quiz", "Text Files/air_quiz.csv")


class WaterQuiz(TestPage):
    def __init__(self):
        self.setWindowTitle("Water Pollution Quiz")
        super().__init__("Water Pollution Quiz", "Text Files/water_quiz.csv")


class LandQuiz(TestPage):
    def __init__(self):
        self.setWindowTitle("Land Pollution Quiz")
        super().__init__("Land Pollution Quiz", "Text Files/land_quiz.csv")


class GlobalQuiz(TestPage):
    def __init__(self):
        self.setWindowTitle("Global Warming Quiz")
        super().__init__("Global Warming Quiz", "Text Files/global_quiz.csv")


# *********************************************************************************************
