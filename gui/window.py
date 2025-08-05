import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(700, 300, 550, 300)
        self.setFixedSize(550, 300)
        self.setWindowIcon(QIcon("assets/logo.png"))
        self.initUI()
        
    # Main Title & Slogan
    def initUI(self):
        # Create the main vertical layout for the window.
        # This layout will stack the top section (logo + text) and the bottom section (button) vertically.
        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # --- Top section: image and text side by side ---
        # Use a horizontal layout to place the logo on the left and the title/slogan on the right.
        top_layout = QHBoxLayout()

        # Image on the left
        image_label = QLabel()
        # Load and size the logo image (140x140 pixels)
        image_label.setPixmap(QIcon("assets/logo.png").pixmap(140, 140))
        # Align the image to the top-left within its cell
        image_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Right side: vertical layout for title and slogan
        right_layout = QVBoxLayout()
        # Title label
        title_label = QLabel("GridGuru")
        # Align the text inside the label to the center (within the label's area)
        title_label.setAlignment(Qt.AlignCenter)
        # Set a large, bold font for the title
        title_label.setFont(QFont("Arial", 40, QFont.Bold))
        # Slogan label
        slogan_label = QLabel("Master the Puzzle")
        # Align the text inside the label to the center
        slogan_label.setAlignment(Qt.AlignCenter)
        # Set a smaller font for the slogan
        slogan_label.setFont(QFont("Arial", 15))
        # Add the title and slogan to the right_layout (vertical stack)
        right_layout.addWidget(title_label)
        right_layout.addWidget(slogan_label)
        # Add a stretch to push the title/slogan to the top of the right_layout
        right_layout.addStretch()

        # Wrap right_layout in a QWidget so it can be added to the horizontal top_layout
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        # Optionally set a fixed width for the right side to control spacing
        right_widget.setFixedWidth(350)

        # Add image and right_widget to the horizontal top_layout
        top_layout.addWidget(image_label)
        top_layout.addWidget(right_widget)
        # Align both widgets to the top-left of their cells in the layout
        top_layout.setAlignment(image_label, Qt.AlignTop | Qt.AlignLeft)
        top_layout.setAlignment(right_widget, Qt.AlignTop | Qt.AlignLeft)

        # --- Bottom section: centered button ---
        # Use a horizontal layout to center the button horizontally
        bottom_layout = QHBoxLayout()
        start_button = QPushButton("Start")
        # Set a large font for the button text
        start_button.setFont(QFont("Arial", 20))
        # Set a fixed size for the button
        start_button.setFixedSize(400, 100)
        # Add stretchable space to the left and right to center the button
        bottom_layout.addStretch()
        bottom_layout.addWidget(start_button)
        bottom_layout.addStretch()

        # --- Add both sections to the main layout ---
        # Add the top section (image and text)
        main_layout.addLayout(top_layout)
        # Add a stretch to push the button to the bottom of the window
        main_layout.addStretch()
        # Add the bottom section (centered button)
        main_layout.addLayout(bottom_layout)

        # The result:
        # - The top section (image and text) stays at the top of the window.
        # - The button is always centered horizontally at the bottom.
        # - The layout stretches as the window size changes, keeping everything in place.
        
class ImportOption:
    def import_image(self):
        image_button = QPushButton("Import Image")
    
    def import_manually(self):
        manual_button = QPushButton("Import Manually")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()