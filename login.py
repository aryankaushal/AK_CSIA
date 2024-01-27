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
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from email.mime.text import MIMEText
from random import randint, sample
# from UI import LearnUI, TestUI, HomeUI
# import time
# import datetime
import pyotp
import re


class SignInPage(QDialog):
    sign_in_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        self.database_conn = database_conn

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.sign_in_button = QPushButton("Sign In")
        self.sign_in_button.clicked.connect(self.sign_in_user)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.sign_in_button)

        self.setLayout(layout)

    def sign_in_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if the username and password match in the database
        cursor = self.database_conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user_data = cursor.fetchone()

        if user_data:
            print("Sign in successful!")
            self.sign_in_successful.emit()
            self.accept()  # Close the SignInPage
        else:
            QMessageBox.warning(
                self, "Invalid Credentials", "Invalid username or password."
            )

class RegistrationPage(QDialog):
    registration_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        # print("INSIDE REG CLASS")
        self.database_conn = database_conn
        self.max_attempts = 3
        self.attempts = 0

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.password_strength_label = QLabel()
        self.password_strength_label.setAlignment(Qt.AlignCenter)

        self.register_button = QPushButton("Join us!")
        self.register_button.clicked.connect(self.register_user)

        self.sign_in_button = QPushButton("Sign In, instead")
        self.sign_in_button.clicked.connect(self.show_sign_in_page)

        # switch_to_sign_in_page = pyqtSignal()

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.password_strength_label)
        layout.addWidget(self.register_button)
        layout.addWidget(self.sign_in_button)

        self.setLayout(layout)

        self.password_input.textChanged.connect(self.update_password_strength)

    def show_sign_in_page(self):
            page = SignInPage(self.database_conn)
            page.exec_()

    def update_password_strength(self):
        password = self.password_input.text()
        strength = self.calculate_password_strength(password)

        colors = {
            "very_weak": "red",
            "weak": "orange",
            "slightly_weak": "yellow",
            "slightly_strong": "lightgreen",
            "strong": "green",
        }

        self.password_strength_label.setText(f"Password Strength: {strength.capitalize()}")
        self.password_strength_label.setStyleSheet(f"color: {colors[strength]}; font-weight: bold;")

    def calculate_password_strength(self, password):
        criteria_met = 0

        # Check uppercase and lowercase
        if any(c.isupper() for c in password) and any(c.islower() for c in password):
            criteria_met += 1

        # Check one digit
        if any(c.isdigit() for c in password):
            criteria_met += 1

        # Check one special character
        if re.search(r"[#_/]", password):
            criteria_met += 1

        # Check 8 characters long
        if len(password) >= 8:
            criteria_met += 1

        # Determine strength based on the number of criteria met
        if criteria_met == 0:
            return "very_weak"
        elif criteria_met == 1:
            return "weak"
        elif criteria_met == 2:
            return "slightly_weak"
        elif criteria_met == 3:
            return "slightly_strong"
        else:
            return "strong"

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Validate password and confirm password match
        if password != confirm_password:
            QMessageBox.warning(
                self, "Password Mismatch", "Password and Confirm Password do not match."
            )
            return

        # Check if the username already exists in the database
        cursor = self.database_conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            QMessageBox.warning(
                self, "User Exists", "User with the same username already exists."
            )
            return

        # Registration successful
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
        )
        self.database_conn.commit()
        print("Registration successful!")

        self.registration_successful.emit()
        # Close the RegistrationPage
        self.accept()


# Placeholder for storing OTPs (Replace this with a secure storage mechanism)
# OTP_STORE = {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_page = RegistrationPage(None)
    registration_page.show()
    sys.exit(app.exec_())
