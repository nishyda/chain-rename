import os
import sys
from PySide6.QtWidgets import (QLabel, QLineEdit, QApplication, QGridLayout, QDialog)
from PySide6.QtGui import QPixmap
from PySide6 import QtCore

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.old = "No file yet"
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.pixmap = QPixmap("placeholder.jpeg").scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl1 = QLabel(self)
        self.lbl1.setFixedSize(500, 500)
        self.lbl1.setPixmap(self.pixmap)
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Enter directory path:")
        self.lbl3 = QLabel(self)
        self.lbl3.setText(self.old)
        self.lbl4 = QLabel(self)
        self.lbl4.setText("Enter new name:")

        layout = QGridLayout()

        layout.addWidget(self.edit1, 1, 3, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(self.edit2, 3, 3, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(self.lbl1, 1, 1, 3, 1, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.lbl2, 1, 2, alignment=QtCore.Qt.AlignRight)
        layout.addWidget(self.lbl3, 2, 2, 2, 3, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.lbl4, 3, 2, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

        self.edit1.returnPressed.connect(self.dir)
        self.edit2.returnPressed.connect(self.name)
    
    def dir(self):
        self.directory = self.edit1.text()
        self.file_names = os.listdir(self.directory)
        self.count = 0
        self.old = self.directory + self.file_names[self.count]
        self.lbl3.setText(self.old)
        self.pixmap = QPixmap(self.old).scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl1.setPixmap(self.pixmap)
        
    def name(self):
        new_name = self.edit2.text()
        self.new = self.directory + new_name
        os.rename(self.old, self.new)
        self.edit2.clear()
        self.count = self.count + 1
        try:
            self.old = self.directory + self.file_names[self.count]
        except IndexError:
            sys.exit()
        self.lbl3.setText(self.old)
        self.pixmap = QPixmap(self.old).scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl1.setPixmap(self.pixmap)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())