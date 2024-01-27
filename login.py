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
from UI import LearnUI, TestUI, HomeUI
import time
import datetime
import pyotp

class SignInPage(QDialog):
    sign_in_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        self.database_conn = database_conn

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()

        self.sign_in_button = QPushButton("Sign In")
        self.sign_in_button.clicked.connect(self.sign_in_user)

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.sign_in_button)

        self.setLayout(layout)

    def sign_in_user(self):
        email = self.email_input.text()
        password = self.password_input.text()
        # **********************************************************************************************************************
        # Add code to check if the email and password match in the database
        cursor = self.database_conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
        )
        user_data = cursor.fetchone()

        if user_data:
            print("Sign in successful!")
            self.sign_in_successful.emit()
            self.accept()  # Close the SignInPage
        else:
            QMessageBox.warning(
                self, "Invalid Credentials", "Invalid email or password."
            )


class RegistrationPage(QDialog):
    registration_successful = pyqtSignal()

    def __init__(self, database_conn):
        super().__init__()

        self.database_conn = database_conn
        self.max_attempts = 3
        self.attempts = 0

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.otp_label = QLabel("Enter OTP:")
        self.otp_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()

        self.register_button = QPushButton("Join us!")
        self.register_button.clicked.connect(self.register_user)

        self.sign_in_button = QPushButton("Sign In instead")
        self.sign_in_button.clicked.connect(self.show_sign_in_page)

        self.resend_button = QPushButton("Resend OTP")
        self.resend_button.clicked.connect(self.resend_otp)
        self.resend_button.setEnabled(False)

        self.timer_label = QLabel("Time left: ")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.setup_otp()

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.otp_label)
        layout.addWidget(self.otp_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        layout.addWidget(self.sign_in_button)
        layout.addWidget(self.resend_button)
        layout.addWidget(self.timer_label)

        self.setLayout(layout)

    def setup_otp(self):
        otp_setup = RegistrationPage()
        # Generate and send initial OTP
        email = self.email_input.text()
        otp = self.generate_otp(email)
        self.send_otp_email(email, otp)

        # Enable timer for 1 minute
        self.timer.start(60000)

    def generate_otp(self, email):
        otp = str(randint(100000, 999999))
        OTP_STORE[email] = otp
        return otp

    def send_otp_email(self, email, otp):
        port = 587
        sender = "aryan_csia@outlook.com"
        smtp_server = "smtp-mail.outlook.com"
        password = "aryan1711"

        message = f"""\
            Subject: Climaware Account Registration OTP

            We are proud of your endeavor to learn about climate change. Your OTP is {otp} """

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()

            server.login(sender, password)
            server.sendmail(sender, email, message)
        return "OTP sent successfully!"
        # For simplicity, we're printing the OTP here
        print(f"Sending OTP to {email}: {otp}")

    def update_timer(self):
        # Update the timer label
        remaining_time = self.timer.remainingTime() / 1000  # in seconds
        self.timer_label.setText(f"Time left: {int(remaining_time)} seconds")

        # If time is up, disable input and enable resend button
        if remaining_time <= 0:
            self.otp_input.setDisabled(True)
            self.resend_button.setEnabled(True)
            self.timer.stop()

    def register_user(self):
        email = self.email_input.text()
        entered_otp = self.otp_input.text()
        password = self.password_input.text()

        # Validate OTP
        if not self.validate_otp(email, entered_otp):
            self.attempts += 1

            if self.attempts >= self.max_attempts:
                QMessageBox.critical(
                    self, "Registration Failed", "Exceeded maximum attempts."
                )
                self.reject()
            else:
                QMessageBox.warning(
                    self, "Invalid OTP", "Invalid OTP. Please try again."
                )
                self.reset_registration()
        else:
            # Registration successful
            cursor = self.database_conn.cursor()
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)", (email, password)
            )
            self.database_conn.commit()
            print("Registration successful!")

            self.registration_successful.emit()
            # Close the RegistrationPage
            self.accept()

    def validate_otp(self, email, entered_otp):
        stored_otp = OTP_STORE.get(email)
        if not stored_otp:
            print("OTP not found. Registration failed.")
            return False

        # Validate the entered OTP
        totp = pyotp.TOTP(stored_otp)
        return totp.verify(entered_otp)

    def resend_otp(self):
        # Resend OTP
        email = self.email_input.text()
        otp = self.generate_otp(email)
        self.send_otp_email(email, otp)

        # Reset attempts and enable input
        self.attempts = 0
        self.otp_input.setDisabled(False)

        # Enable timer for 1 minute
        self.timer.start(60000)

        # Disable resend button again
        self.resend_button.setEnabled(False)

    def reset_registration(self):
        # Reset input fields and enable timer for 1 minute
        self.otp_input.clear()
        self.otp_input.setDisabled(False)
        self.timer.start(60000)
        self.timer_label.setText("Time left: ")


# Placeholder for storing OTPs (Replace this with a secure storage mechanism)
OTP_STORE = {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_page = RegistrationPage(None)
    registration_page.show()
    sys.exit(app.exec_())


