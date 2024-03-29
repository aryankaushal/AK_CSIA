import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import login

# **************************************** Main Window ****************************************
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        self.setWindowTitle("Climaware")
        self.setGeometry(512, 100, 500, 900)
        self.setStyleSheet("background-color: lightblue;")

        self.database_conn = sqlite3.connect("user_data.db")
        self.create_tables()
        self.create_default_user()

        self.registration_page = login.RegistrationPage(self.database_conn)
        self.sign_in_page = login.SignInPage(self.database_conn)

        self.show_registration_page()

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.setSpacing(1)
        layout.addStretch(1)
        self.setLayout(layout)
    
    def show_registration_page(self):
        reg_page = login.RegistrationPage(self.database_conn)
        reg_page.exec_()
        return

    def create_tables(self):
        cursor = self.database_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT NOT NULL,
                           password TEXT NOT NULL,
                           points INTEGER DEFAULT 0)"""
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
