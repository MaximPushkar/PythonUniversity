import re

EMAIL = r'[\w\.-]+@[\w\.-]+\.\w+'


def find_email(string):
    emails_list = re.findall(EMAIL, string)
    emails = set(emails_list)
    strng = "\n".join(emails)
    return strng


if __name__ == '__main__':
    find_email("first-email@gmail.com WRGAEHDHBADNBZDBDFB second-email@mail.ru SDFGYUIOIUGFDFGHJKL;.,"
               "mnBV third-email@ukr.net QWERTYUIOJHBV NKI8YTGHJK;./;JHGB NB B NB NB NHGFDX ,"
               "KJUYTFC second-email@mail.ru QWERTYUIJHGCXZXCVBNMKIUTRDVBN LL;DXHVAKDJ LDIVBHAD third-email@ukr.net "
               "lalalalalalalalalalalalalalal first-email@gmail.com What's going in here?")
