from PyQt5.QtWidgets import \
      QApplication, QSizePolicy, QMainWindow, QMessageBox, QPushButton, QWidget, QVBoxLayout, QFileDialog, QLabel
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt

from instructions_window import InstructionsWindow
from calculations_window import CalculationsWindow
from reading_xyz import xyz_to_mol_graphs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set a window title
        self.setWindowTitle("Welcome to the molecular converter!")
        self.setGeometry(100, 100, 600, 300)

        #sets a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        #sets layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSizeConstraint(QVBoxLayout.SetMinAndMaxSize)
        self.central_widget.setLayout(self.layout)
        self.central_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #create a welcome label
        welcome_label = QLabel("Please load the data :)")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(qtg.QFont('SF Pro', 20))
        self.layout.addWidget(welcome_label)   

        #help pop-up window
        self.button_instructions = QPushButton("How does it work?", self)
        self.layout.addWidget(self.button_instructions)
        self.button_instructions.clicked.connect(self.showInstructionsWindow)

        #open a file browser window
        self.file_paths = None
        self.fileOpenButton = QPushButton('Choose file(s)', self)
        self.layout.addWidget(self.fileOpenButton)
        self.fileOpenButton.clicked.connect(self.select_the_files)
    
        #create a button to load data
        self.data_loading_button = QPushButton("Let's convert the molecules!", self)
        self.data_loading_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.data_loading_button)

        #increase button size
        self.data_loading_button.setStyleSheet("QPushButton { padding: 20px; }")

        #show the app  
        self.show()

    def showInstructionsWindow(self):
        instructions_window = InstructionsWindow()
        instructions_window.exec_()

    def select_the_files(self):
        options = QFileDialog.Option()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "XYZ Files (*.xyz)", options=options)
        if file_paths:
            print("selected file(s): ", file_paths)
            self.file_paths = file_paths

    def load_data(self):

        if not self.file_paths:
            QMessageBox.warning(self, "Warning", "Please select the files before loading data!")
            return
        
        results = xyz_to_mol_graphs(self.file_paths)
        print(results)

        self.calculations_window = CalculationsWindow(results, self)
        self.calculations_window.show()
        self.close()


app = QApplication([])
mw = MainWindow()
app.exec_()
