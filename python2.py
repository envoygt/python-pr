from IPython.utils.path import random

username = "Oleg"
balance = 0
transactions = []


def print_balance():
    """Выводит баланс пользователя на экран"""
    print(f"Пользователь {username} имеет {balance}$")


def deposit_money(amount):
    """Пополняет баланс пользователя на `amount`"""
    global balance
    balance = balance + amount
    print(
        f"Зачислено {amount}$, текущее количество денег на счету: {balance}$")


def withdraw_money(amount):
    """Выводит со счета деньги в размере `amount`"""
    global balance
    if has_enough_money(amount):
        balance = balance - amount
        print(f"Снято {amount}$, остаток на счету: {balance}$")
    else:
        print(
            f"Недостаточно денег, для снятия {amount}$ не хватает {amount - balance}$")


def has_enough_money(amount):
    """Проверяет, достаточно ли на счете денег для выполнения операции, требующей `amount` денег"""
    if balance - amount >= 0:
        return True
    else:
        return False


def print_transactions():
    """Выводит список последних покупок"""
    print("История покупок:")
    print(list(reversed(transactions)))


def pay(reason, amount):
    """Оплачивает `reason`, требующую `amount` денег"""
    if has_enough_money(amount):
        withdraw_money(amount)
        transactions.append(reason)
        print(f"Оплачено: {reason} ({amount}$)")
    else:
        print(f"Недостаточно денег для оплаты {reason}")


accounts = {}


def print_users():
    """Выводит список пользователей"""
    temp = []
    for key in accounts.keys():
        temp.append(key)
    print("Список пользователей:")
    print(temp)


def print_users_with_passwords():
    """Выводит список пользователей с паролями"""
    print(accounts)


def is_user_exists(name):
    """Проверяет, существует ли пользователь с именем `name`"""
    if name in accounts:
        return True
    else:
        return False


def add_user(name, password):
    """Добавляет пользователя с данными `name` и `password`"""
    if is_user_exists(name):
        print(f"Пользователь с именем {name} уже существует")
        return
    if len(password) < 6:
        print("Слишком легкий пароль")
        return
    accounts[name] = password
    print(f"Создан пользователь с именем {name}")


def get_user_info(name):
    """Выводит информацию о пользователе с именем `name`"""
    if is_user_exists(name):
        print(f"user: {name}; password: {accounts[name]}")


def is_password_correct(name, password):
    """Проверяет, верен ли пароль `password` для пользователя с именем `name`"""
    if accounts[name] == password:
        return True
    else:
        return False


def change_password(name, old_password, new_password):
    """Меняет пароль `old_password` на `new_password` у пользователя с именем `name`"""
    if not is_user_exists(name):
        print(f"Пользователя с именем {name} не существует")
        return
    if not is_password_correct(name, old_password):
        print("Неверный пароль")
        return
    else:
        accounts[name] = new_password
        print(f"Пароль пользователя {name} успешно изменен")


def delete_user(name):
    """Удаляет пользователя `name`"""
    if is_user_exists(name):
        accounts.pop(name)
        print(f"Пользователь {name} удален")
    else:
        print(f"Пользователя с именем {name} не существует")


def rename_user(old_name, new_name):
    """Меняет имя пользователя `old_name` на `new_name`"""
    if not is_user_exists(old_name):
        print(f"Пользователя с именем {old_name} не существует")
        return
    if is_user_exists(new_name):
        print(f"Пользователь с именем {new_name} уже существует")
        return
    accounts[new_name] = accounts[old_name]
    accounts.pop(old_name)
    print(f"Пользователь {old_name} переименован в {new_name}")


if __name__ == "__main__":
    print_balance()
    deposit_money(50)
    withdraw_money(100)
    deposit_money(49.5)
    print_balance()
    withdraw_money(100)
    withdraw_money(60)
    pay("Хлеб", 1)
    print_transactions()
    pay("Оплата за интернет", 8)
    pay("Поездка на такси", 3.50)
    print_transactions()
    print_balance()
    pay("Штаны", 40)
    deposit_money(200)
    pay("Штаны", 40)
    for i in range(1, random.randint(2, 5)):
        pay(f"Подписка на сервис №{i}", random.randint(1, 10))
    print_transactions()
    add_user("Bob", "12345")
    add_user("Bob", "123456")
    add_user("Bob", "1234567")
    print_users_with_passwords()
    add_user("John", "qwerty")
    add_user("Boris", "Y8Wp2y3hSc40")
    add_user("Ivan", "ivan2004")
    print_users()
    print_users_with_passwords()
    get_user_info("John")
    change_password("John23", "qwerty", "zxcvbn")
    change_password("John", "qwertyyyy", "zxcvbn")
    print_users_with_passwords()
    change_password("John", "qwerty", "zxcvbn")
    print_users_with_passwords()
    print_users()
    delete_user("bob")
    print_users()
    delete_user("Bob")
    print_users()
    print_users_with_passwords()
    rename_user("Ivan", "Kolyvan")
    print_users_with_passwords()
