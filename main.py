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
from login import SignInPage, RegistrationPage
import learn, tests

# *************************************** Home Page ***************************************
class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Climaware")
        self.setGeometry(100, 100, 500, 1000)
        # self.setStyleSheet("background-color: grey;")
        # self.setFixedSize(500, 1000)

        thisis_label = QLabel("This is")
        thisis_label.setFont(QFont("Arial", 20, QFont.Bold))
        thisis_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        thisis_label.setStyleSheet("color: grey;")

        title_label = QLabel("Climaware")
        title_label.setFont(QFont("Arial", 60, QFont.Bold))
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label.setStyleSheet("color: black;")
        title_label.contentsMargins()
        # self.points_label = QLabel("Points: 0")

        welcome_label = QLabel(
            "Welcome to the best place to learn about climate change!\nWe are glad you're joining us!"
        )
        welcome_label.setFont(QFont("Arial", 16))
        welcome_label.setStyleSheet("color: black;")
        welcome_label.setAlignment(Qt.AlignHCenter)

        instruction_label = QLabel(
            "Would you like to learn about climate change\nor test your understanding?"
        )
        instruction_label.setFont(QFont("Arial", 16))
        instruction_label.setStyleSheet("color: black;")
        instruction_label.setAlignment(Qt.AlignHCenter)

        self.learn_button = QPushButton("Learn")
        self.test_button = QPushButton("Test")
        button_width = 20
        button_height = 40
        self.learn_button.setGeometry(50, 50, button_width, button_height)
        self.learn_button.setStyleSheet(
            "background-color: green; color: white; border-radius: 20px; font-size: 16px; min-width: 20; min-height: 50px;"
        )
        self.test_button.setGeometry(50, 50, button_width, button_height)
        self.test_button.setStyleSheet(
            "background-color: green; color: white; border-radius: 20px; font-size: 16px; min-width: 30; min-height: 50px;"
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
        self.setGeometry(100, 100, 500, 1000)
        # self.setFixedSize(500, 1000)

        # self.database_conn = sqlite3.connect("user_data.db")
        # self.create_tables()
        # self.create_default_user()
        # self.auth_handler = AuthHandler(self.database_conn)

        self.home_page = HomePage()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.home_page)
        self.setStyleSheet("background-color: lightblue;")

        # self.learn_page = LearnUI()
        # self.test_page = TestUI()
        # self.home_page = HomeUI()

        # self.stacked_widget.addWidget(self.learn_page)
        # self.stacked_widget.addWidget(self.auth_handler.sign_in_page)

        # self.auth_handler.registration_page.sign_in_button.clicked.connect(
        #     self.show_sign_in_page
        # )

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.setSpacing(1)
        layout.addStretch(1)
        self.setLayout(layout)

    def show_learn_page(self):
        learn_page = learn.LearnPage()
        learn_page.exec_()
        # self.stacked_widget.addWidget(learn_page)
        # self.stacked_widget.setCurrentWidget(learn_page)
        # self.stacked_widget.setCurrentIndex(4)

    def show_test_page(self):
        test_page = tests.TestPage()
        test_page.exec_()  # Show the TestPage
        # self.stacked_widget.setCurrentIndex(3)

    def show_registration_page(self):
        registration = RegistrationPage(self.database_conn)
        
        self.stacked_widget.addWidget(self.registration_page)
        self.stacked_widget.setCurrentWidget(self.registration_page)
        self.stacked_widget.setCurrentIndex(0)

    def show_sign_in_page(self):
        signup = SignInPage(self.database_conn)
        self.stacked_widget.addWidget(self.sign_in_page)
        self.stacked_widget.setCurrentWidget(self.sign_in_page)
        self.stacked_widget.setCurrentIndex(1)

    # def show_home_page(self):
    #     self.home_page.learn_button.clicked.connect(self.show_learn_page)
    #     self.home_page.test_button.clicked.connect(self.show_test_page)
    #     # self.stacked_widget.setCurrentIndex(0)

    # def show_air_pollution_page(self):
    #     air_pollution_page = learn.AirCauses()
    #     self.stacked_widget.addWidget(air_pollution_page)
    #     self.stacked_widget.setCurrentWidget(air_pollution_page)

    # def show_water_pollution_page(self):
    #     water_pollution_page = learn.WaterCauses()
    #     self.stacked_widget.addWidget(water_pollution_page)
    #     self.stacked_widget.setCurrentWidget(water_pollution_page)

    # def show_land_pollution_page(self):
    #     land_pollution_page = learn.LandCauses()
    #     self.stacked_widget.addWidget(land_pollution_page)
    #     self.stacked_widget.setCurrentWidget(land_pollution_page)

    # def show_global_warming_page(self):
    #     global_warming_page = learn.GlobalCauses()
    #     self.stacked_widget.addWidget(global_warming_page)
    #     self.stacked_widget.setCurrentWidget(global_warming_page)

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
