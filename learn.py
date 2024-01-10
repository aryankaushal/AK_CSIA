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