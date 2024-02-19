# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import hashlib


def passwd_check(passwd):

    spec_symbols=['$','@','#','%','&']
    return_pas = True
    if len(passwd) < 8:
        print('длина пароля меньше 8 символов')
        return_pas = False
    if len(passwd) > 20:
        print('пароль слишком длинный')
        return_pas = False
    if not any(char.isdigit() for char in passwd):
        print('обязательно используйте разный тип символов, в том числе цифры')
        return_pas = False
    if not any(char.isupper() for char in passwd):
        print('обязательно используйте разный тип символов, в том числе прописные буквы')
        return_pas = False
    if not any(char.islower() for char in passwd):
        print('обязательно используйте разный тип символов, в том числе строчные буквы')
        return_pas = False
    if not any(char in spec_symbols for char in passwd):
        print('обязательно используйте разный тип символов, в том числе специальные символы $,@,#,%,&')
        return_pas=False
    if return_pas:
        pass_hash = hashlib.sha256(passwd.encode()).hexdigest()
        print(pass_hash)
passwd = input('Введите пароль: ')
passwd_check(passwd)
