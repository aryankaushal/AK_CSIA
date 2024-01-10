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

# *************************************** Home Page ***************************************
class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        title_label = QLabel("<h1>Climaware</h1>")
        additional_text = QLabel(
            "Welcome to Climaware! Explore and learn about environmental issues."
        )

        self.points_label = QLabel("Points: 0")

        self.learn_button = QPushButton("Learn")
        self.test_button = QPushButton("Test")

        layout = QVBoxLayout(self)
        layout.addWidget(self.points_label)
        layout.addWidget(self.learn_button)
        layout.addWidget(self.test_button)

        self.setLayout(layout)


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

        layout = QVBoxLayout()
        layout.addWidget(self.learn_label)
        layout.addWidget(self.causes_button)
        layout.addWidget(self.effects_button)
        layout.addWidget(self.solutions_button)

        self.setLayout(layout)


# ******************************* Learn Page --> Causes Pages *******************************
class CausePage(QDialog):
    def __init__(self, cause_name):
        super().__init__()

        self.setWindowTitle(cause_name)

        self.info_label = QLabel(f"Information about {cause_name}:")

        self.info_text_browser = QTextBrowser()
        self.info_text_browser.setPlainText(self.generate_random_info())

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info_text_browser)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def generate_random_info(self):
        # For simplicity, generate random information about the cause
        return f"Random information about {self.windowTitle()}"

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

        self.setWindowTitle(effect_name)

        self.info_label = QLabel(f"Information about {effect_name}:")

        self.info_text_browser = QTextBrowser()
        self.info_text_browser.setPlainText(self.generate_random_info())

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info_text_browser)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def generate_random_info(self):
        # For simplicity, generate random information about the effect
        return f"Random information about {self.windowTitle()}"

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

        self.setWindowTitle(solution_name)

        self.info_label = QLabel(f"Information about {solution_name}:")

        self.info_text_browser = QTextBrowser()
        self.info_text_browser.setPlainText(self.generate_random_info())

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info_text_browser)
        layout.addWidget(self.back_button)
        layout.addWidget(self.test_button)

        self.test_button = QPushButton("Let's Test")
        self.test_button.clicked.connect(self.show_test_page)
        self.setLayout(layout)

    def generate_random_info(self):
        # For simplicity, generate random information about the solution
        return f"Random information about {self.windowTitle()}"

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


# *********************************** Test Page --> Quizzes ***********************************
class TestPage(QDialog):
    def __init__(self):
        super().__init__()

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
            lambda: self.initiate_test("Air Pollution", "air_questions.txt")
        )
        self.water_button.clicked.connect(
            lambda: self.initiate_test("Water Pollution", "water_questions.txt")
        )
        self.land_button.clicked.connect(
            lambda: self.initiate_test("Land Pollution", "land_questions.txt")
        )
        self.global_button.clicked.connect(
            lambda: self.initiate_test("Global Warming", "global_questions.txt")
        )

        self.setLayout(layout)

    def initiate_test(self, topic, file_name):
        test_dialog = TestDialog(topic, file_name)
        result = test_dialog.exec_()

        # Handle the result if needed


class TestDialog(QDialog):
    def __init__(self, topic, file_name):
        super().__init__()

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
                lines = file.readlines()

                # Randomly select 5 questions
                selected_questions = sample(lines, 5)

                for line in selected_questions:
                    data = line.strip().split(";")
                    question = {
                        "question": data[0],
                        "options": data[1:5],
                        "correct": int(data[5]),
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
        super().__init__("Air Pollution Quiz", "air_quiz.txt")


class WaterQuiz(TestPage):
    def __init__(self):
        super().__init__("Water Pollution Quiz", "water_quiz.txt")


class LandQuiz(TestPage):
    def __init__(self):
        super().__init__("Land Pollution Quiz", "land_quiz.txt")


class GlobalQuiz(TestPage):
    def __init__(self):
        super().__init__("Global Warming Quiz", "global_quiz.txt")
# *********************************************************************************************


# **************************************** Main Window ****************************************
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.database_conn = sqlite3.connect("user_data.db")
        self.create_tables()
        self.create_default_user()

        self.auth_handler = AuthHandler(self.database_conn)

        self.stacked_widget = QStackedWidget()
        # self.learn_page = LearnUI()
        self.test_page = TestUI()
        self.home_page = HomeUI()

        # self.stacked_widget.addWidget(self.learn_page)
        self.stacked_widget.addWidget(self.auth_handler.sign_in_page)
        self.stacked_widget.addWidget(self.test_page)
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.auth_handler.sign_in_page)

        self.auth_handler.registration_page.sign_in_button.clicked.connect(
            self.show_sign_in_page
        )

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)

    def show_learn_page(self):
        learn_page = LearnPage()

        self.stacked_widget.addWidget(learn_page)
        self.stacked_widget.setCurrentWidget(learn_page)

        learn_page.causes_button.clicked.connect(self.show_causes_page)
        learn_page.effects_button.clicked.connect(self.show_effects_page)
        learn_page.solutions_button.clicked.connect(self.show_solutions_page)
        self.stacked_widget.setCurrentIndex(4)

    def show_test_page(self):
        test_page = TestPage()
        test_page.exec_()  # Show the TestPage
        self.stacked_widget.setCurrentIndex(3)

    def show_registration_page(self):
        self.stacked_widget.addWidget(self.registration_page)
        self.stacked_widget.setCurrentWidget(self.registration_page)
        self.stacked_widget.setCurrentIndex(0)

    def show_sign_in_page(self):
        self.stacked_widget.addWidget(self.sign_in_page)
        self.stacked_widget.setCurrentWidget(self.sign_in_page)
        self.stacked_widget.setCurrentIndex(1)

    def show_home_page(self):
        self.home_page.learn_button.clicked.connect(self.show_learn_page)
        self.home_page.test_button.clicked.connect(self.show_test_page)
        self.stacked_widget.setCurrentIndex(2)

    def show_air_pollution_page(self):
        air_pollution_page = AirCauses()
        self.stacked_widget.addWidget(air_pollution_page)
        self.stacked_widget.setCurrentWidget(air_pollution_page)

    def show_water_pollution_page(self):
        water_pollution_page = WaterCauses()
        self.stacked_widget.addWidget(water_pollution_page)
        self.stacked_widget.setCurrentWidget(water_pollution_page)

    def show_land_pollution_page(self):
        land_pollution_page = LandCauses()
        self.stacked_widget.addWidget(land_pollution_page)
        self.stacked_widget.setCurrentWidget(land_pollution_page)

    def show_global_warming_page(self):
        global_warming_page = GlobalCauses()
        self.stacked_widget.addWidget(global_warming_page)
        self.stacked_widget.setCurrentWidget(global_warming_page)

    def create_tables(self):
        cursor = self.database_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           email TEXT NOT NULL,
                           password TEXT NOT NULL)"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS scores 
                          (user_id INTEGER,
                           topic TEXT NOT NULL,
                           score INTEGER,
                           FOREIGN KEY (user_id) REFERENCES users(id))"""
        )
        self.database_conn.commit()

    def create_default_user(self):
        # Check if a default user already exists
        cursor = self.database_conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]

        if user_count == 0:
            # Create a default user
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                ("test@example.com", "testpassword"),
            )
            self.database_conn.commit()
            print("Default user created.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
