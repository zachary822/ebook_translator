from tkinter import Button, Tk, filedialog

from ebooklib import epub

import ebook_converter


def convert_book():
    ebook_file = filedialog.askopenfilename()

    if ebook_file:
        book = epub.read_epub(ebook_file)
        conv_book = ebook_converter.book_to_traditional(book)

        save_file = filedialog.asksaveasfilename(defaultextension=".epub")
        if save_file:
            epub.write_epub(save_file, conv_book)


root = Tk()
root.title('Ebook Simplified to Tradition Chinese')

button = Button(root, text="Browse", command=convert_book, width=10)
button.pack()

close = Button(root, text="Exit", command=root.quit, width=10)
close.pack()

root.mainloop()
