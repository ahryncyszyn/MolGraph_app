import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
    

        #adds a title
        self.setWindowTitle("Welcome to the molecular converter :)")

        #sets a layout
        form_layout = qtw.QVBoxLayout()
        self.setLayout(form_layout)

        #create a welcome label
        my_label = qtw.QLabel("How would you like to load the molecular data?")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #create a label
        my_label = qtw.QLabel("Please choose one of the options below:")
        #change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #create a combo box
        my_combo = qtw.QComboBox(self)
        #add items
        my_combo.addItem("Multiple .xyz files, each storing one molecule", "mult")
        my_combo.addItem("One .xyz file, storing multiple molecules", "singl")
        self.layout().addWidget(my_combo)

        #create a label
        my_label = qtw.QLabel("Here, please specify the path to your file(s)")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #open a file browser window
        self.fileOpenButton = qtw.QPushButton('Click to open File Dialog',self)
        self.layout().addWidget(self.fileOpenButton)
        #self.fileOpenButton.clicked.connect(self.buttonClicked)
        

        def openFileBrowserWindow(self):
            options = qtw.QFileDialog.Options()
        
        def buttonClicked():
            print("hihi")




        #create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("file_path")
        my_entry.setText("")       
        self.layout().addWidget(my_entry)

        #create a button
        my_button = qtw.QPushButton("Let's load in the data!", 
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #increase button size
        my_button.setStyleSheet("QPushButton { padding: 10px; }")

        #show the app  
        self.show()

        def press_it():
            #adds name to the label
            my_label.setText(f'Hello {my_entry.text()}')
            #clear the entry box
            my_entry.setText("")

        def example():
            #grab whats on the screen
            #screen = self.outputLabel.text()
            #call some other function
            #store the output in a variable
            #print the output using 
            #label_name.setTest(f'The output is {variable_name}')
            #self.outputLabel.setText(str)
            pass

app = qtw.QApplication([])
mw = MainWindow()

#Running the app
app.exec_()
