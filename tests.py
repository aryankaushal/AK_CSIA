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