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
import time, datetime
import secrets

# from login import SignInPage, RegistrationPage
import learn, tests


# *************************************** Home Page ***************************************
class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Climaware")
        self.setGeometry(512, 100, 500, 900)
        # self.setStyleSheet("background-color: grey;")
        # self.setFixedSize(500, 1000)

        thisis_label = QLabel("This is")
        thisis_label.setFont(QFont("Arial", 30))
        thisis_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        thisis_label.setStyleSheet("color: grey;")

        title_label = QLabel("Climaware")
        title_label.setFont(QFont("Arial", 80, QFont.Bold))
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label.setStyleSheet("color: black;")
        title_label.contentsMargins()
        # self.points_label = QLabel("Points: 0")

        welcome_label = QLabel(
            "\nWelcome to the best place to learn about climate change!\n\n\nWe are glad you're joining us!\n\n\n"
        )
        welcome_label.setFont(QFont("Arial", 25, QFont.Bold))
        welcome_label.setStyleSheet("color: #15098A;")
        welcome_label.setAlignment(Qt.AlignHCenter)

        instruction_label = QLabel(
            "Would you like to learn about climate change\nthrough some concise study material\nor test your understanding via short quizzes?\n\n"
        )
        instruction_label.setFont(QFont("Arial", 25))
        instruction_label.setStyleSheet("color: black;")
        instruction_label.setAlignment(Qt.AlignHCenter)

        self.learn_button = QPushButton("Learn")
        self.test_button = QPushButton("Test")
        button_width = 20
        button_height = 40
        self.learn_button.setGeometry(50, 50, button_width, button_height)
        self.learn_button.setStyleSheet(
            "background-color: #EB711E; color: white; border-radius: 20px; font-size: 20px; min-width: 20; min-height: 50px;"
        )
        self.test_button.setGeometry(50, 50, button_width, button_height)
        self.test_button.setStyleSheet(
            "background-color: #972E6E; color: white; border-radius: 20px; font-size: 20px; min-width: 20; min-height: 50px;"
        )

        self.learn_button.clicked.connect(MainWindow.show_learn_page)
        self.test_button.clicked.connect(MainWindow.show_test_page)

        layout = QVBoxLayout(self)
        layout.addWidget(thisis_label)
        layout.addWidget(title_label)
        layout.addWidget(welcome_label)
        layout.addWidget(instruction_label)
        layout.addWidget(self.learn_button)
        layout.addWidget(self.test_button)
        # layout.addWidget(self.points_label)

        self.setLayout(layout)


# **************************************** Main Window ****************************************
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Climaware")
        self.setGeometry(512, 100, 500, 900)

        self.database_conn = sqlite3.connect("user_data.db")
        self.create_tables()
        self.create_default_user()

        self.home_page = HomePage()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.home_page)
        self.setStyleSheet("background-color: lightblue;")

        # # self.registration_page = RegistrationPage(self.database_conn)
        # # self.sign_in_page = SignInPage(self.database_conn)

        # self.registration_page.registration_successful.connect(self.show_home_page)
        # self.sign_in_page.sign_in_successful.connect(self.show_home_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.setSpacing(1)
        layout.addStretch(1)
        self.setLayout(layout)

        # self.home_page.learn_button.clicked.connect(self.show_registration_page)
        # self.home_page.test_button.clicked.connect(self.show_sign_in_page)

    def show_learn_page(self):
        learn_page = learn.LearnPage()
        learn_page.exec_()
        # self.stacked_widget.addWidget(learn_page)
        # self.stacked_widget.setCurrentWidget(learn_page)
        # self.stacked_widget.setCurrentIndex(4)

    def show_test_page(self):
        test_page = tests.TestPage()
        test_page.exec_()
        # self.stacked_widget.setCurrentIndex(3)

    # def show_registration_page(self):
    #     self.home_page.learn_button.clicked.connect(self.show_registration_page)
    #     self.home_page.test_button.clicked.connect(self.show_sign_in_page)
    #     # registration = RegistrationPage(self.database_conn)
    #     # self.stacked_widget.addWidget(self.registration_page)
    #     self.stacked_widget.setCurrentWidget(self.registration_page)
    #     self.stacked_widget.setCurrentIndex(0)

    # def show_sign_in_page(self):
    #     signup = SignInPage(self.database_conn)
    #     self.stacked_widget.addWidget(self.sign_in_page)
    #     self.stacked_widget.setCurrentWidget(self.sign_in_page)
    #     self.stacked_widget.setCurrentIndex(1)

    def create_tables(self):
        cursor = self.database_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT NOT NULL,
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
        print(user_count)

        if user_count == 0:

            username = "aryankkk"
            password = "Aryan_2982"
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            self.database_conn.commit()
            print("Default user created.")
            print(f"Username: {username}")
            print(f"Password: {password}")

            # # Create a default user
            # cursor.execute(
            #     "INSERT INTO users (username, password) VALUES (?, ?)",
            #     ("test@example.com", "testpassword"),
            # )
            # self.database_conn.commit()
            # print("Default user created.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # registration_page = RegistrationPage(window.database_conn)
    # registration_page.switch_to_sign_in_page.connect(window.show_sign_in_page)
    # registration_page.show()
    window.show()
    sys.exit(app.exec_())
