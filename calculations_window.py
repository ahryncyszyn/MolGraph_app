from PyQt5.QtWidgets import QMainWindow, QGridLayout, QComboBox, QPushButton, QWidget, QHBoxLayout, QFileDialog, QLabel
import PyQt5.QtGui as qtg
import sys
import reading_xyz as xyz

class CalculationsWindow(QMainWindow):
    def __init__(self, results):
        super().__init__()

        self.setWindowTitle("Calculations")
        self.setGeometry(100, 100, 600, 300)

        #sets a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        #sets layout
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        #create a label
        my_label = QLabel("Select a molecule:")
        #change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout.addWidget(my_label)

        #combo box for choosing a molecule
        self.combo_box = QComboBox(self)
        for molecule_name, molecule_object in results.items():
            self.combo_box.addItem(molecule_name, molecule_object)
        self.layout.addWidget(self.combo_box)

        self.mol_choice = self.combo_box.currentData()

        #button for calculating molecular mass
        calculate_mass_button = QPushButton("Calculate Molecular Mass")
        print(f'you selected {self.mol_choice}')
        calculate_mass_button.clicked.connect(self.calculate_mass)
        self.layout.addWidget(calculate_mass_button)

        #button for visualizing the molecule
        visualize_button = QPushButton("Visualize")
        #visualize_button.clicked.connect(self.visualize)
        self.layout.addWidget(visualize_button)

    def calculate_mass(self):
        mass = self.mol_choice.calculate_mol_mass()
        print(mass)


    def visualized(self):
        pass


            

