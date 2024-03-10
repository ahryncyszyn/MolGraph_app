from PyQt5.QtWidgets import QMainWindow, QComboBox, QPushButton, QWidget, QVBoxLayout, QFileDialog, QLabel
import PyQt5.QtGui as qtg
import sys
import reading_xyz as xyz

class CalculationsWindow(QMainWindow):
    def __init__(self, results):
        super().__init__()

        self.setWindowTitle("Welcome to the molecular converter :)")
        self.setGeometry(100, 100, 600, 300)

        #sets a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        #sets layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel(f"Calculations window", self)
        self.layout.addWidget(self.label)

