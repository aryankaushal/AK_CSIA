# ui_elements.py
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QDialog,
    QRadioButton,
)
class HomePageUI(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("<h1>Climaware</h1>")
        self.additional_text = QLabel(
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

        
class SignUpUI(QWidget):
    def __init__(self):
        super().__init__()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.send_code_button = QPushButton("Send Verification Code")
        self.otp_label = QLabel("Enter OTP:")
        self.otp_input = QLineEdit()

        self.verify_button = QPushButton("Verify")
        self.password_label = QLabel("Create Password:")
        self.password_input = QLineEdit()

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()

        self.register_button = QPushButton("Register")

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.send_code_button)
        layout.addWidget(self.otp_label)
        layout.addWidget(self.otp_input)
        layout.addWidget(self.verify_button)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)


class LearnUI(QWidget):
    def __init__(self):
        super().__init__()

        self.learn_label = QLabel("What do you want to learn about?")

        self.causes_button = QPushButton("Causes")
        self.effects_button = QPushButton("Effects")
        self.solutions_button = QPushButton("Solutions")

        layout = QVBoxLayout()
        layout.addWidget(self.learn_label)
        layout.addWidget(self.causes_button)
        layout.addWidget(self.effects_button)
        layout.addWidget(self.solutions_button)

        self.setLayout(layout)


class CourseMaterialUI(QWidget):
    def __init__(self, topic_name):
        super().__init__()

        self.setWindowTitle(topic_name)

        self.back_button = QPushButton("Back")
        self.material_label = QLabel(f"Course Material for {topic_name}")
        self.test_button = QPushButton("Let's Test")

        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.material_label)
        layout.addWidget(self.test_button)

        self.setLayout(layout)


class TestUI(QWidget):
    def __init__(self):
        super().__init__()

        self.mcqs = [
            {
                "question": "Question 1",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct": 1,
            },
            # Add more questions
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = QLabel(self.mcqs[self.current_question]["question"])

        self.option_buttons = []
        for i, option in enumerate(self.mcqs[self.current_question]["options"]):
            button = QRadioButton(option)
            self.option_buttons.append(button)

        self.submit_button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        for button in self.option_buttons:
            layout.addWidget(button)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)


class HomeUI(QWidget):
    def __init__(self):
        super().__init__()

        self.points_label = QLabel("Points: 0")

        self.learn_button = QPushButton("Learn")
        self.test_button = QPushButton("Test")

        layout = QVBoxLayout(self)
        layout.addWidget(self.points_label)
        layout.addWidget(self.learn_button)
        layout.addWidget(self.test_button)

        self.setLayout(layout)
