import sqlite3
import hashlib

user_choose = input('1 - Log in / 2 - Sing up: ')
user_login = input('Login: ')
user_password = input('Password: ')

hash_object = hashlib.sha224(user_password.encode())


a = sqlite3.connect("server.a")
b = a.cursor()

b.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    XP TEXT
)""")

a.commit()

def LogIn():
    b.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if b.fetchone() is None:
        b.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, hash_object.hexdigest() + "4ea68hf", 0))
        a.commit()
        print('Зарегистрировано!')
    else:
        print('Такая запись уже имеется!')

        for value in b.execute("SELECT * FROM users"):
            print(value)


def SingUp():
    b.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    b.execute(f"SELECT password FROM users WHERE password = '{hash_object.hexdigest() + '4ea68hf'}'")
    if b.fetchone() is not None:
        print(f'Вы вошли в свой аккаунт {user_login}! ')
    else:
        print('Неправильно введены данные, попробуйте ещё раз!')

        for value in b.execute("SELECT * FROM users"):
            print(value)


if user_choose == '2':
    SingUp()

elif user_choose == '1':
    LogIn()

























