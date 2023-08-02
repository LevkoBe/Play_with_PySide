import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Change Button')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton('Change Color', self)
        layout.addWidget(self.button)

        self.color_dialog = QColorDialog(self)
        self.color_dialog.setOption(QColorDialog.NoButtons)
        self.color_dialog.currentColorChanged.connect(self.changeColor)

        layout.addWidget(self.color_dialog)

        self.setLayout(layout)

        self.button.clicked.connect(self.openColorDialog)

    def openColorDialog(self):
        self.color_dialog.show()

    def changeColor(self, color):
        self.button.setStyleSheet(f'background-color: {color.name()};')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec())
