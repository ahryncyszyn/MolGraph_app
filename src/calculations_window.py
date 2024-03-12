from PyQt5.QtWidgets import \
    QMainWindow, QGridLayout, QComboBox, QPushButton, QWidget, QSizePolicy, QLabel
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt
import src.reading_xyz as xyz

class CalculationsWindow(QMainWindow):
    def __init__(self, results, main_window):
        super().__init__()
        self.main_window = main_window

        #create a label
        my_label = QLabel("Select a molecule:")
        my_label.setAlignment(Qt.AlignCenter)
        my_label.setFont(qtg.QFont('SF Pro', 25))

        #combo box for choosing a molecule
        self.combo_box = QComboBox(self)
        self.combo_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.combo_box.setMinimumWidth(200)
        self.combo_box.setMinimumHeight(50)
        for molecule_name, molecule_object in results.items():
            self.combo_box.addItem(molecule_name, molecule_object)

        #combo box for choosing the precision
        self.precision_combo_box = QComboBox(self)
        self.precision_combo_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.precision_combo_box.setMinimumWidth(200)
        self.precision_combo_box.setMinimumHeight(50)
        for i in range(11):
            self.precision_combo_box.addItem(f'Precision: {i} decimal places', i)

        #button for calculating molecular mass
        calculate_mass_button = QPushButton("Calculate Molecular Mass")
        calculate_mass_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        calculate_mass_button.clicked.connect(self.calculate_mass)

        #add a label to display the result
        self.mass_result_label = QLabel("Result will appear here")
        self.mass_result_label.setAlignment(Qt.AlignCenter)
        self.mass_result_label.setFont(qtg.QFont('SF Pro', 25)) 

        #button for visualizing the molecule
        visualize_button = QPushButton("Visualize")
        visualize_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        visualize_button.clicked.connect(self.visualize)

        #button to go back to the main window
        go_back_button = QPushButton("Go back to menu")
        go_back_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        go_back_button.clicked.connect(self.go_back)

        #sets layout
        self.layout = QGridLayout()
        self.layout.addWidget(my_label, 0, 0, Qt.AlignCenter)
        self.layout.addWidget(self.combo_box, 0, 1, Qt.AlignCenter)
        self.layout.addWidget(self.precision_combo_box, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(calculate_mass_button, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(visualize_button, 3, 0, 1, 2, Qt.AlignCenter)
        self.layout.addWidget(go_back_button, 4, 0, 1, 2, Qt.AlignCenter)

        #sets a central widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Calculations")
        self.setGeometry(100, 100, 600, 250)

    def calculate_mass(self):
        chosen_molecule_text = self.combo_box.currentText()
        chosen_molecule_obj = self.combo_box.currentData()
        precision = self.precision_combo_box.currentData()
        mass = round(chosen_molecule_obj.calculate_mol_mass(), precision)
        self.layout.addWidget(self.mass_result_label, 2, 0, 1, 2, Qt.AlignCenter)
        self.mass_result_label.setText(f'Molecular mass of {chosen_molecule_text} is {mass}')


    def visualize(self):
        try:
            chosen_molecule_obj = self.combo_box.currentData()
            chosen_molecule_obj.plot_molecule()
        except Exception as e:
            print("An eror occured during visualization: ", e)

    def go_back(self):
        self.close()
        self.main_window.show()



            

