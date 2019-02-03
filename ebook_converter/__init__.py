import chinese_converter as converter
import ebooklib
from ebooklib import epub
from lxml import etree

__all__ = ['book_to_traditional']


def book_to_traditional(book: epub.EpubBook) -> epub.EpubBook:
    try:
        title = book.get_metadata('DC', 'title')[0][0]
        book.set_unique_metadata('DC', 'title', converter.to_traditional(title))
    except IndexError:
        pass

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            doc = etree.fromstring(item.get_content())
            for t in doc.xpath('//text()'):
                p = t.getparent()
                if p.text:
                    p.text = converter.to_traditional(p.text)
                if p.tail:
                    p.tail = converter.to_traditional(p.tail)

            item.set_content(etree.tostring(doc, pretty_print=True))

    return book
