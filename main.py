import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QSlider, QFontDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color, Size, and Font Change Button')
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.button = QPushButton('Change Color', self)
        layout.addWidget(self.button)

        self.color_dialog = QColorDialog(self)
        self.color_dialog.setOption(QColorDialog.NoButtons)
        self.color_dialog.currentColorChanged.connect(self.changeColor)

        layout.addWidget(self.color_dialog)

        self.window_color_dialog = QColorDialog(self)
        self.window_color_dialog.setOption(QColorDialog.NoButtons)
        self.window_color_dialog.currentColorChanged.connect(self.changeWindowColor)

        layout.addWidget(self.window_color_dialog)

        self.text_color_dialog = QColorDialog(self)
        self.text_color_dialog.setOption(QColorDialog.NoButtons)
        self.text_color_dialog.currentColorChanged.connect(self.changeTextColor)

        layout.addWidget(self.text_color_dialog)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(700)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(25)
        self.slider.valueChanged.connect(self.changeSize)

        layout.addWidget(self.slider)

        self.button_font = QPushButton('Change Font', self)
        layout.addWidget(self.button_font)
        self.button_font.clicked.connect(self.changeFont)

        self.setLayout(layout)

        self.button.clicked.connect(self.openColorDialog)
        self.window_color_dialog.show()
        self.text_color_dialog.show()

    def openColorDialog(self):
        self.color_dialog.show()

    def changeColor(self, color):
        self.button.setStyleSheet(f'background-color: {color.name()};')

    def changeWindowColor(self, color):
        self.setStyleSheet(f'background-color: {color.name()};')

    def changeTextColor(self, color):
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'color: {color.name()};')

    def changeSize(self, value):
        size = f'{value}px'
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'min-width: {size}; max-width: {size};'
                                  f'min-height: {size}; max-height: {size};')

    def changeFont(self):
        font_dialog = QFontDialog(self.button.font(), self)
        if font_dialog.exec():
            font = font_dialog.selectedFont()
            self.button.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec())
