from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt

class InstructionsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instructions")
        self.setGeometry(300, 300, 300, 200)
        
        layout = QVBoxLayout()

        instructions_label = QLabel(
            "This app allows you to create a database of molecules from .xyz file(s) and extract insights about them.\n\n"
            "Click on the 'Choose file(s)' button to select you data.\n\n" 
            "If your file contains one molecule, it will be saved under the name of the file.\n" 
            "If it contains mutiple molecules, they will be stored as file_name1, file_name2, etc.\n"
            "You can also change the names later!\n\n"
            "Clicking 'Let's convert!' opens a new window that allows you to choose the desired molecule\n"
            "from the database as well as select the operations", self)
        
        instructions_label.setFont(qtg.QFont('SF Pro', 18))
        instructions_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(instructions_label)

        self.setLayout(layout)