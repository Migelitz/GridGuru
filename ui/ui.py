import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("ui\Logo.png"))
        
        # Logo design
        Logo_title = QLabel("GridGuru", self)
        Logo_title.setFont(QFont("Calibri", 30))
        Logo_title.setGeometry(0, 0, 500, 200)
        Logo_title.setAlignment(Qt.AlignCenter)
        
        # Logo slogan desing
        Logo_slogan = QLabel("Master the Puzzle", self)
        Logo_slogan.setFont(QFont("Calibri", 20))
        Logo_title.setGeometry(0, 0, 500, 200)
        Logo_title.setAlignment(Qt.AlignCenter)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()