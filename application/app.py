# Basic gui app to test model on sample images
import sys
import numpy as np
import tensorflow as tf
import os
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QDesktopWidget, \
    QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt

IMAGE_RECOGNITION_MODEL = R'..\model\image_recognition_model.h5'

FAVICON_PATH = R'.\favicon.ico'


class ImageSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.recognition_model = tf.keras.models.load_model(IMAGE_RECOGNITION_MODEL)

    def initUI(self):
        self.setWindowTitle('Image - Selection, Recognition')
        self.resize(1920, 1080)
        self.setWindowIcon(QIcon(FAVICON_PATH))
        self.center()

        # Set the style
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: yellow;
            }
            QPushButton {
                background-color: yellow;
                color: black;
                border: 1px solid black;
                height: 50px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #222222;
                color: yellow;
            }
            QLabel {
                color: yellow;
            }
        """)

        # Layout
        layout = QVBoxLayout()

        # Label for displaying the image
        self.imageLabel = QLabel('Image will appear here')
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setScaledContents(False)
        layout.addWidget(self.imageLabel)
        layout.setStretchFactor(self.imageLabel, 5)

        # Button layout
        button_layout = QHBoxLayout()

        # Button to open the file dialog
        btnOpenFileDialog = QPushButton('Open photo', self)
        btnOpenFileDialog.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(btnOpenFileDialog)

        # Button to download the photo
        btnDownloadPhoto = QPushButton('Download photo', self)
        btnDownloadPhoto.clicked.connect(self.download_photo)
        button_layout.addWidget(btnDownloadPhoto)

        # Set button layout spacing and margins
        button_layout.setSpacing(10)
        button_layout.setContentsMargins(10, 10, 10, 10)
        layout.addLayout(button_layout)

        # Set button stretch factors
        button_layout.setStretch(0, 4)
        button_layout.setStretch(1, 4)

        # Status label at the bottom
        self.statusLabel = QLabel('Select an image to display')
        self.statusLabel.setAlignment(Qt.AlignCenter)
        font = QFont('Arial', 16, QFont.Bold)
        self.statusLabel.setFont(font)
        self.statusLabel.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose a photo", "",
                                                   "Image Files (*.jpg *.jpeg *.png *.bmp)", options=options)
        if file_name:
            # Process the image as needed
            image = self.prepare_image(file_name)
            prediction = self.recognition_model.predict(image)
            self.get_and_display_prediction(prediction)

            # Get predicted class
            predicted_class = self.get_and_display_prediction(prediction)

            # Add text to the image
            temp_output_path = "temp_image_with_text.png"
            self.add_text_to_image(file_name, predicted_class, temp_output_path)

            # Load the modified image with QPixmap
            pixmap = QPixmap(temp_output_path)
            self.imageLabel.setPixmap(
                pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            # Clean up temporary file
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)

    def download_photo(self):
        current_pixmap = self.imageLabel.pixmap()
        if current_pixmap:
            options = QFileDialog.Options()
            save_path, _ = QFileDialog.getSaveFileName(self, "Save photo", "",
                                                       "PNG Files (*.png);;All Files (*)", options=options)
            if save_path:
                current_pixmap.save(save_path)
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("There is no image to save.")
            msg.setWindowTitle("No Image")
            msg.setStandardButtons(QMessageBox.Ok)

            # Apply custom styles to the QMessageBox
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: black;
                    color: yellow;
                }
                QLabel {
                    color: yellow;
                    font-size: 18px;
                }
            """)

            ok_button = msg.button(QMessageBox.Ok)
            ok_button.setMinimumWidth(200)

            msg.exec_()

    def add_text_to_image(self, image_path, text, output_path):
        # Open the original image
        original_image = Image.open(image_path).convert('RGB')
        original_width, original_height = original_image.size

        # Define font size
        font = ImageFont.load_default()

        # Draw the text background onto the new image
        draw = ImageDraw.Draw(original_image)
        if text == "":
            bbox = draw.textbbox((0, 0), "None", font=font)
        else:
            bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate the new height for the image
        new_height = original_height + text_height + 20

        # Create a new image with the adjusted height
        new_image = Image.new('RGB', (original_width, new_height), color=(255, 255, 255))
        new_image.paste(original_image, (0, 0))

        # Draw the full-width yellow rectangle
        background_position = (0, original_height, original_width, original_height + text_height + 20)
        draw = ImageDraw.Draw(new_image)
        if text == "":
            draw.rectangle(background_position, fill="red")
        else:
            draw.rectangle(background_position, fill="yellow")

        # Draw the text onto the new image, centered within the yellow background
        text_x_position = (original_width - text_width) // 2
        text_y_position = original_height + 8
        draw.text((text_x_position, text_y_position), text, font=font, fill="black")

        # Save the new image
        new_image.save(output_path)

    def prepare_image(self, path):
        img = tf.keras.preprocessing.image.load_img(path, target_size=(128, 128))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def get_and_display_prediction(self, prediction):
        class_labels = [
            "A10", "A400M", "AV8B", "B1", "B2", "B52", "C17", "C2", "C5", "E2", "E7",
            "EF2000", "F117", "F14", "F15", "F16", "F18", "F22", "F35", "F4", "J10",
            "J20", "JAS39", "KC135", "Mig31", "Mirage2000", "MQ9", "P3", "Rafale",
            "RQ4", "SR71", "Su24", "Su25", "Su34", "Su57", "Tornado", "Tu160", "Tu95",
            "U2", "US2", "V22", "Vulcan", "XB70", "YF23"
        ]

        predicted_class_index = np.argmax(prediction)
        max_prediction_value = prediction[0][predicted_class_index]

        print(prediction)
        if max_prediction_value >= 0.9:
            predicted_class = class_labels[predicted_class_index]
            self.statusLabel.setText(f'Predicted class: {predicted_class}')
        else:
            predicted_class = ""
            self.statusLabel.setText('Cannot predict class')

        return predicted_class


app = QApplication(sys.argv)
ex = ImageSelector()
ex.show()
sys.exit(app.exec_())
