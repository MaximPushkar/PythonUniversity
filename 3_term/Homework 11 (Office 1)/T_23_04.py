# У документі Word містяться дати у форматі dd.mm.yyyy або
# підкреслення для запису дат вручну __.__.____ Знайти всі дати у тексті.
# Замість підкреслень вставити поточну дату. Зберегти оновлений документ.


from docx import Document
import re
from datetime import datetime


DATE1 = r"\b\d{1,2}\.\d{1,2}\.\d{1,4}"  # 12.3.1999
DATE2 = r"\b_{1,2}\._{1,2}\._{1,4}"  # __.__.____
# datetime.today()


def _fill_date(match):
    date = match.group()
    y, m, d = str(datetime.today().date()).split('-')
    date = ".".join((d, m, y))
    return date


def fill_date(string):
    return re.sub(DATE2, _fill_date, string)


def fill_date_docx(inp, outp):
    doc = Document(inp)

    for paragraph in doc.paragraphs:
        paragraph.text = fill_date(paragraph.text)

    doc.save(outp)


if __name__ == '__main__':
    fill_date_docx("input.docx", "output.docx")





