import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QSlider
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color and Size Change Button')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton('Change Color', self)
        layout.addWidget(self.button)

        self.color_dialog = QColorDialog(self)
        self.color_dialog.setOption(QColorDialog.NoButtons)
        self.color_dialog.currentColorChanged.connect(self.changeColor)

        layout.addWidget(self.color_dialog)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(50)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(25)
        self.slider.valueChanged.connect(self.changeSize)

        layout.addWidget(self.slider)

        self.setLayout(layout)

        self.button.clicked.connect(self.openColorDialog)

    def openColorDialog(self):
        self.color_dialog.show()

    def changeColor(self, color):
        self.button.setStyleSheet(f'background-color: {color.name()};')

    def changeSize(self, value):
        size = f'{value}px'
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'min-width: {size}; max-width: {size};'
                                  f'min-height: {size}; max-height: {size};')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec())
