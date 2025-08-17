import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, 
    QVBoxLayout, QHBoxLayout, QPushButton
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    """Main application window for the Sudoku Solver."""

    # Window configuration constants
    WINDOW_WIDTH = 550
    WINDOW_HEIGHT = 300
    WINDOW_X = 700
    WINDOW_Y = 300

    # UI element sizes
    LOGO_SIZE = 140
    RIGHT_PANEL_WIDTH = 350
    START_BUTTON_WIDTH = 400
    START_BUTTON_HEIGHT = 100
    OPTION_BUTTON_WIDTH = 250
    OPTION_BUTTON_HEIGHT = 100

    def __init__(self) -> None:
        super().__init__()
        self._setup_window()
        self.button_layout = QHBoxLayout()
        self._init_ui()

    def _setup_window(self) -> None:
        """Configure the main window properties."""
        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(self.WINDOW_X, self.WINDOW_Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowIcon(QIcon("assets/logo.png"))

    def _init_ui(self) -> None:
        """Initialize the user interface layout."""
        # Create main layout and central widget
        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Create and add sections
        top_section = self._create_header_section()
        bottom_section = self._create_button_section()

        # Assemble main layout
        main_layout.addLayout(top_section)
        main_layout.addStretch()  # Push button to bottom
        main_layout.addLayout(bottom_section)

    def _create_header_section(self) -> QHBoxLayout:
        """Create the top section with logo and title/slogan."""
        header_layout = QHBoxLayout()

        # Add logo and text sections
        logo_widget = self._create_logo_widget()
        text_widget = self._create_text_widget()

        header_layout.addWidget(logo_widget)
        header_layout.addWidget(text_widget)

        # Align both widgets to top-left
        header_layout.setAlignment(logo_widget, Qt.AlignTop | Qt.AlignLeft)
        header_layout.setAlignment(text_widget, Qt.AlignTop | Qt.AlignLeft)

        return header_layout

    def _create_logo_widget(self) -> QLabel:
        """Create and configure the logo widget."""
        logo_label = QLabel()
        logo_label.setPixmap(QIcon("assets/logo.png").pixmap(self.LOGO_SIZE, self.LOGO_SIZE))
        logo_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return logo_label

    def _create_text_widget(self) -> QVBoxLayout:
        """Create the widget containing title and slogan."""
        # Create text layout
        text_layout = QVBoxLayout()

        # Create title
        title_label = self._create_title_label()
        slogan_label = self._create_slogan_label()

        # Add widgets to layout
        text_layout.addWidget(title_label)
        text_layout.addWidget(slogan_label)
        text_layout.addStretch()  # Push text to top

        # Wrap layout in widget
        text_widget = QWidget()
        text_widget.setLayout(text_layout)
        text_widget.setFixedWidth(self.RIGHT_PANEL_WIDTH)

        return text_widget

    def _create_title_label(self) -> QLabel:
        """Create and style the main title label."""
        title_label = QLabel("GridGuru")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 40, QFont.Bold))
        return title_label

    def _create_slogan_label(self) -> QLabel:
        """Create and style the slogan label."""
        slogan_label = QLabel("Master the Puzzle")
        slogan_label.setAlignment(Qt.AlignCenter)
        slogan_label.setFont(QFont("Arial", 15))
        return slogan_label

    def _create_button_section(self) -> QHBoxLayout:
        """Create the bottom section with centered start button."""
        self.button_layout = QHBoxLayout()
    
        # Create and configure buttons
        start_button = QPushButton("START")
        start_button.setFont(QFont("Arial", 25, QFont.Bold))
        start_button.setFixedSize(self.START_BUTTON_WIDTH, self.START_BUTTON_HEIGHT)
        
        # Center the button horizontally
        self.button_layout.addWidget(start_button)
        
        # Add functionality when clicked
        start_button.clicked.connect(self._start_button_clicked)
        
        # Make instance variable
        self.start_button = start_button
        
        return self.button_layout
    
    def _start_button_clicked(self) -> None:
        self.start_button.deleteLater()
        self._option_button()

    def _option_button(self) -> QHBoxLayout:
        print("Display buttons")
        # Use the same layout to place the buttons
        buttons_layout = self.button_layout

        import_manually = QPushButton("IMPORT PUZZLE\nMANUALLY")
        import_manually.setFont(QFont("Arial", 16, QFont.Bold))
        import_manually.setFixedSize(self.OPTION_BUTTON_WIDTH, self.OPTION_BUTTON_HEIGHT)
        
        import_image = QPushButton("IMPORT IMAGE\n(UNDER DEVELOPMENT)")
        import_image.setFont(QFont("Arial", 12, QFont.Bold))
        import_image.setFixedSize(self.OPTION_BUTTON_WIDTH, self.OPTION_BUTTON_HEIGHT)
        
        buttons_layout.addWidget(import_manually)
        buttons_layout.addStretch()
        buttons_layout.addWidget(import_image)
        
        return buttons_layout
        

class ImportHandler:
    """Handles different import options for Sudoku puzzles."""

    def import_from_image(self):
        """Import Sudoku puzzle from an image file."""
        # TODO: Implement image import functionality
        pass

    def import_manually(self):
        """Import Sudoku puzzle through manual input."""
        # TODO: Implement manual input functionality
        pass


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()