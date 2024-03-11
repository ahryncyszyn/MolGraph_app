from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QVBoxLayout, QFileDialog, QLabel
import PyQt5.QtGui as qtg
import sys

class InstructionsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instructions")
        self.setGeometry(300, 300, 300, 200)
        
        layout = QVBoxLayout()

        instructions_label = QLabel(
            "This app allows you to import the .xyz files of molecule(s) and convert them to graphs.\n"
            "Click on the 'Choose file(s)' button to select you data.\n The file should contain one or more molecules." , self)
        
        instructions_label.setFont(qtg.QFont('Helvetica', 18))
        
        layout.addWidget(instructions_label)

        self.setLayout(layout)