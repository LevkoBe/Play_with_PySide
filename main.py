import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QSlider, QFontDialog, QTextEdit
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.config_text_edit = QTextEdit(self)  # Initialize the QTextEdit attribute
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color, Size, Font, and Corner Rounding Change Button')
        self.setGeometry(100, 100, 600, 400)

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

        self.corner_slider = QSlider(Qt.Horizontal, self)
        self.corner_slider.setMinimum(0)
        self.corner_slider.setMaximum(100)  # Maximum corner rounding size in percentage
        self.corner_slider.setValue(50)     # Initial corner rounding size (50%)
        self.corner_slider.setTickPosition(QSlider.TicksBelow)
        self.corner_slider.setTickInterval(5)
        self.corner_slider.valueChanged.connect(self.changeCornerRounding)

        layout.addWidget(self.corner_slider)

        self.border_thickness_slider = QSlider(Qt.Horizontal, self)
        self.border_thickness_slider.setMinimum(0)
        self.border_thickness_slider.setMaximum(10)  # Maximum border thickness
        self.border_thickness_slider.setValue(0)      # Initial border thickness
        self.border_thickness_slider.setTickPosition(QSlider.TicksBelow)
        self.border_thickness_slider.setTickInterval(1)
        self.border_thickness_slider.valueChanged.connect(self.changeBorder)

        layout.addWidget(self.border_thickness_slider)

        self.border_color_dialog = QColorDialog(self)
        self.border_color_dialog.setOption(QColorDialog.NoButtons)
        self.border_color_dialog.currentColorChanged.connect(self.changeBorderColor)  # Connect to changeBorderColor method

        layout.addWidget(self.border_color_dialog)  # Add the border color dialog to the layout

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
        self.border_color_dialog.show()

        # Set the initial view of the button with rounded corners (50%)
        self.changeCornerRounding(self.corner_slider.value())

        # Add QTextEdit widget to display the selected configurations
        self.config_text_edit = QTextEdit(self)
        layout.addWidget(self.config_text_edit)

    def openColorDialog(self):
        self.color_dialog.show()

    def changeColor(self, color):
        self.button.setStyleSheet(f'background-color: {color.name()};')
        self.updateConfigurations()

    def changeWindowColor(self, color):
        self.setStyleSheet(f'background-color: {color.name()};')
        self.updateConfigurations()

    def changeTextColor(self, color):
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'color: {color.name()};')
        self.updateConfigurations()

    def changeCornerRounding(self, value):
        # Calculate the border radius based on the minimum of button width and height
        min_dimension = min(self.button.width(), self.button.height())
        rounded_value = value / 100.0 * min_dimension / 2
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'border-radius: {rounded_value}px;'
                                  f'border: {self.border_thickness_slider.value()}px solid {self.border_color_dialog.currentColor().name()};'
                                  f'color: {self.button.palette().color(self.button.foregroundRole()).name()};')
        self.updateConfigurations()

    def changeBorder(self):
        # Call changeCornerRounding to update border thickness and color
        self.changeCornerRounding(self.corner_slider.value())

    def changeBorderColor(self, color):
        # Call changeCornerRounding to update border color
        self.changeCornerRounding(self.corner_slider.value())

    def changeSize(self, value):
        size = f'{value}px'
        rounded_value = self.corner_slider.value() / 100.0 * value / 2
        self.button.setStyleSheet(f'background-color: {self.button.palette().color(self.button.backgroundRole()).name()};'
                                  f'border-radius: {rounded_value}px;'
                                  f'border: {self.border_thickness_slider.value()}px solid {self.border_color_dialog.currentColor().name()};'
                                  f'min-width: {size}; max-width: {size};'
                                  f'min-height: {size}; max-height: {size};')
        self.updateConfigurations()

    def changeFont(self):
        font_dialog = QFontDialog(self.button.font(), self)
        if font_dialog.exec():
            font = font_dialog.selectedFont()
            self.button.setFont(font)
            self.updateConfigurations()

    def updateConfigurations(self):
        configurations = (
            f'Button background-color: {self.button.palette().color(self.button.backgroundRole()).name()}\n'
            f'Button Text color: {self.button.palette().color(self.button.foregroundRole()).name()}\n'
            f'Window background-color: {self.palette().color(self.backgroundRole()).name()}\n'
            f'font: {self.button.font().family()}, {self.button.font().pointSize()}pt\n'
            f'Button min-width, min-height, max...: {self.slider.value()}px\n'
            f'Corner border-radius: {self.corner_slider.value()}%\n'
            f'border: {self.border_thickness_slider.value()}px solid (color): {self.border_color_dialog.currentColor().name()}'
        )
        self.config_text_edit.setPlainText(configurations)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec())


# Button background-color: #d6a770
# Button Text color: #356d7c
# Window background-color: #f1a64a
# font: Old English Text MT, 24pt
# Button min-width, min-height, max...: 100px
# Corner border-radius: 50%
# border: 2px solid (color): #356d7c
