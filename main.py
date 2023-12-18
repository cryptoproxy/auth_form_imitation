from user_managment import UserManager
import sys


class Menu:

    def __init__(self):
        self.um = UserManager()
        self.flag = False
        # self.user_flag: bool = user_flag

    def is_user(self, command, rh=0):
        if rh:
            if self.flag:
                return command(self.flag)
            else:
                print('Вы не авторизованы!')
                return False

        else:
            if self.flag:
                return command()
            else:
                print('Вы не авторизованы!')
                return False

    def main_menu(self):
        while True:
            print(f'\nАвторизован: {self.flag}')
            print('1. Зарегистрироваться')
            print('2. Войти')
            print('3. Обновить учетную запись')
            print('4. Удалить учетную запись')
            print('0. Выйти')
            choice = input('Выберите действие: ')

            match choice:
                case '1':
                    self.um.register_user()
                case '2':
                    session = self.um.authorization_user(self.flag)
                    self.flag = session
                case '3':
                    self.flag = self.is_user(self.um.update_user, rh=1)
                case '4':
                    self.flag = self.is_user(self.um.delete_user, rh=1)
                case '0':
                    sys.exit('Гудбаай')
                case _:
                    print('Неверный вариант!')


def main():
    menu = Menu()
    try:
        menu.main_menu()
    except KeyboardInterrupt:
        menu.flag = False
        print('\nПокеда')


if __name__ == '__main__':
    main()

# def change_flag_false():
#     with open('flag.py', 'w', encoding='utf-8') as f:
#         f.write('user_flag = False')


# def change_flag_true():
#     with open('flag.py', 'w', encoding='utf-8') as f:
#         f.write('user_flag = True')
