import queue
import sys
import threading

from PyQt5.QtWidgets import QApplication, QFileDialog, QGridLayout, QPushButton, QWidget
from ebooklib import epub

from ebook_converter import book_to_traditional


class ConvertBook(threading.Thread):
    def __init__(self, name: str, que: queue.Queue):
        super().__init__()

        self.name = name
        self.q = que

    def run(self):
        book = epub.read_epub(self.name)
        book_to_traditional(book)
        self.q.put(book)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(250, 150)
        self.setWindowTitle('Ebook Converter')

        btn = QPushButton('Browse', self)
        btn.clicked.connect(self.make_ebook_button)

        qbtn = QPushButton('Exit', self)
        qbtn.clicked.connect(QApplication.instance().quit)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(btn, 0, 0)
        grid.addWidget(qbtn, 1, 0)

    def make_ebook_button(self):
        name, ftype = QFileDialog.getOpenFileName(self, filter="EPUB (*.epub)")
        if name:
            q = queue.Queue(maxsize=1)

            conv = ConvertBook(name, q)
            conv.start()

            name, ftype = QFileDialog.getSaveFileName(self, directory="Untitled.epub")
            if name:
                conv.join()
                epub.write_epub(name, q.get())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWidget()
    w.show()

    sys.exit(app.exec_())
