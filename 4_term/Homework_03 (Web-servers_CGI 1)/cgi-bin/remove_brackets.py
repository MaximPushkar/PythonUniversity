# Скласти програму, яка працює в оточенні веб-сервера, для розв’язання задачі.
# Виключити з заданого рядка групи символів, які знаходяться між '(' та ')'. Самі дужки
# теж мають бути виключені. Вважається, що дужки розставлено правильно (парами) та
# всередині кожної пари дужок немає інших дужок.
# Ввести рядок у браузері та показати результат обчислень.


import cgi
from string import Template


def remove_brackets(string: str):
    ans = ''
    add_to_ans = 1
    for char in string:
        if char == "(":
            add_to_ans = 0
        elif char == ")":
            add_to_ans = 1
        ans = ans + char if add_to_ans == 1 else ans
    return ''.join(ans.split(')'))


if __name__ == '__main__':
    form = cgi.FieldStorage()  # Створюємо контейнер і отримуємо дані з форми
    # Беремо перше значення (атрибут value) з ім'ям (атрибут name) "string"
    # якщо такого поля в формі немає, то беремо пустий рядок
    string = form.getfirst("string", "")
    result = remove_brackets(string)  # Визначаємо результат
    # Відкриваємо шаблон
    with open("result.html", encoding="utf-8") as f:
        # Зчитуємо дані і підставляємо результат
        page = Template(f.read()).substitute(result=result)

    import os  # Якщо у нас операційна система Windows, то змінюємо кодування

    if os.name == "nt":
        import sys, codecs

        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)

    # додаємо заголовок та друкуємо сторінку в веб-браузер
    print("Content-type: text/html charset=utf-8\n")
    print(page)
