import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialog,
    QMessageBox,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from random import randint, sample
# from main import HomePage

# import time
# import datetime
import pyotp
import re


class RegistrationPage(QDialog):
    registration_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        self.setWindowTitle("Climaware Registration")
        self.setGeometry(512, 100, 500, 900)
        self.setStyleSheet("background-color: #B5B5C8;")
        self.reg_title = QLabel("\nWelcome to\nClimaware!")
        self.reg_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.reg_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.reg_title.setStyleSheet("color: black;")

        self.instruction_label = QLabel(
            "Enter your desired username and password to join us!"
        )
        self.instruction_label.setFont(QFont("Arial", 25))
        self.instruction_label.setStyleSheet("color: black;")
        self.instruction_label.setAlignment(Qt.AlignHCenter)

        # print("INSIDE REG CLASS")
        self.database_conn = database_conn
        self.max_attempts = 3
        self.attempts = 0

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: #444444;")
        self.username_label.setFont(QFont("Arial", 25, QFont.Bold))
        self.username_label.setStyleSheet("color: black;")

        self.instruction2_label = QLabel(
            "Password must:\n1. Be at least 8 characters long\n2. Contain at least one uppercase letter, one lowercase letter,\none digit, and one special character (#, _, /)."
        )
        self.instruction2_label.setFont(QFont("Arial", 14))
        self.instruction2_label.setStyleSheet("color: #444444;")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("background-color: #444444;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_label.setFont(QFont("Arial", 25, QFont.Bold))
        self.password_label.setStyleSheet("color: black;")

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setStyleSheet("background-color: #444444;")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_label.setFont(QFont("Arial", 25, QFont.Bold))
        self.confirm_password_label.setStyleSheet("color: black;")

        self.password_strength_label = QLabel()
        self.password_strength_label.setAlignment(Qt.AlignCenter)
        self.password_strength_label.setFont(QFont("Arial", 14, QFont.Bold))

        self.register_button = QPushButton("Join us!")
        self.register_button.clicked.connect(self.register_user)
        self.register_button.setFont(QFont("Arial", 25, QFont.Bold))
        self.register_button.setStyleSheet(
            "background-color: #1FD38C; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )

        self.sign_in_button = QPushButton("Sign In, instead")
        self.sign_in_button.clicked.connect(self.show_sign_in_page)
        self.sign_in_button.setFont(QFont("Arial", 25, QFont.Bold))
        self.sign_in_button.setStyleSheet(
            "background-color: #1F94D3; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )

        # switch_to_sign_in_page = pyqtSignal()

        layout = QVBoxLayout()
        layout.addWidget(self.reg_title)
        layout.addWidget(self.instruction_label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.instruction2_label)
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
            "Very Weak": "red",
            "Weak": "orange",
            "Slightly Weak": "yellow",
            "Slightly Strong": "lightgreen",
            "Strong": "green",
        }

        self.password_strength_label.setText(
            f"Password Strength: {strength.capitalize()}"
        )
        self.password_strength_label.setStyleSheet(
            f"color: {colors[strength]}; font-weight: bold;"
        )

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
            return "Very Weak"
        elif criteria_met == 1:
            return "Weak"
        elif criteria_met == 2:
            return "Slightly Weak"
        elif criteria_met == 3:
            return "Slightly Strong"
        else:
            return "Strong"

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

        QMessageBox.information(
            self,
            "Registration Successful",
            "Congratulations! Registration successful!\nClose this, run the app, and use the Sign In button",
        )

        self.registration_successful.emit()
        # Close the RegistrationPage
        self.accept()


# Placeholder for storing OTPs (Replace this with a secure storage mechanism)
# OTP_STORE = {}


class SignInPage(QDialog):
    sign_in_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        self.setWindowTitle("Climaware Sign In")
        self.setGeometry(512, 100, 500, 900)
        self.setStyleSheet("background-color: #B5B5C8;")
        self.reg_title = QLabel("\nWelcome back to\nClimaware!")
        self.reg_title.setFont(QFont("Arial", 40, QFont.Bold))
        self.reg_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.reg_title.setStyleSheet("color: black;")

        self.instruction_label = QLabel("Enter your username and password to sign in!")
        self.instruction_label.setFont(QFont("Arial", 25))
        self.instruction_label.setStyleSheet("color: black;")
        self.instruction_label.setAlignment(Qt.AlignHCenter)

        self.database_conn = database_conn

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: #444444;")
        self.username_label.setFont(QFont("Arial", 25, QFont.Bold))
        self.username_label.setStyleSheet("color: #444444;")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("background-color: #444444;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_label.setFont(QFont("Arial", 25, QFont.Bold))
        self.password_label.setStyleSheet("color: #444444;")

        self.sign_in_button = QPushButton("Sign In")
        self.sign_in_button.clicked.connect(self.sign_in_user)
        self.sign_in_button.setFont(QFont("Arial", 25, QFont.Bold))
        self.sign_in_button.setStyleSheet(
            "background-color: #1F94D3; color: black; border-radius: 20px; font-size: 30px; min-width: 30; min-height: 50px;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.reg_title)
        layout.addWidget(self.instruction_label)
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
            # self.home_page = HomePage()
            # self.home_page.show()
            # self.hide()
        else:
            QMessageBox.warning(
                self, "Invalid Credentials", "Invalid username and/or password."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_page = RegistrationPage(None)
    registration_page.show()
    sys.exit(app.exec_())
