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

import learn, tests

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
        learn_page = learn.LearnPage()

        self.stacked_widget.addWidget(learn_page)
        self.stacked_widget.setCurrentWidget(learn_page)

        learn_page.causes_button.clicked.connect(learn.LearnPage.show_causes_page)
        learn_page.effects_button.clicked.connect(learn.LearnPage.show_effects_page)
        learn_page.solutions_button.clicked.connect(learn.LearnPage.show_solutions_page)

        self.stacked_widget.setCurrentIndex(4)

    def show_causes_page(self):
        page = learn.CausePage()
        page.exec_()  
        self.stacked_widget.setCurrentIndex(0)

    def show_effects_page(self):
        page = learn.EffectsPage()
        page.exec_() 
        self.stacked_widget.setCurrentIndex(1)

    def show_solutions_page(self):
        page = learn.SolutionsPage()
        page.exec_() 
        self.stacked_widget.setCurrentIndex(2)

    def show_test_page(self):
        test_page = tests.TestPage()
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
        air_pollution_page = learn.AirCauses()
        self.stacked_widget.addWidget(air_pollution_page)
        self.stacked_widget.setCurrentWidget(air_pollution_page)

    def show_water_pollution_page(self):
        water_pollution_page = learn.WaterCauses()
        self.stacked_widget.addWidget(water_pollution_page)
        self.stacked_widget.setCurrentWidget(water_pollution_page)

    def show_land_pollution_page(self):
        land_pollution_page = learn.LandCauses()
        self.stacked_widget.addWidget(land_pollution_page)
        self.stacked_widget.setCurrentWidget(land_pollution_page)

    def show_global_warming_page(self):
        global_warming_page = learn.GlobalCauses()
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
