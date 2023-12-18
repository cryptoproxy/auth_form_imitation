from file_manager import *


class UserManager:
    def __init__(self):
        self.fm = FileManager()

    def register_user(self):
        firstname = input('Firstname: ')
        lastname = input('Lastname: ')
        email = input('Email: ')
        password = input('Password: ')

        data = self.fm.read_data()
        existing_emails = [user["email"] for user in data]
        if email in existing_emails:
            print('Пользователь с такой почтой уже существует.')
        else:
            user = {
                'firstname': firstname,
                'lastname': lastname,
                'email': email.strip(),
                'password': password,
            }
            data.append(user)
            self.fm.write_data(data)
            print('Регистрация успешно завершена,\nЧтобы авторизоваться нажмите 2.')

    def authorization_user(self, flag):
        print('\nЧтобы выйти отправьте "0".')
        if flag:
            print('Вы уже авторизованы ;)')
            return flag
        else:
            while True:
                email = input('Введите почту: ').strip()
                password = input('Введите пароль: ').strip()

                if email == '0' or password == '0':
                    print('Переходим в главное меню')
                    return False

                data = self.fm.read_data()
                for user in data:
                    flags = [user['email'] == email, user['password'] == password]
                    if all(flags):
                        print('Вы успешно авторизировались!')
                        return email
                print('Неверные данные')
                # return False

    def update_user(self, session):
        while True:
            print('\n1. Изменить имя')
            print('2. Изменить фамилию')
            print('3. Изменить почту')
            print('4. Изменить пароль')
            print('0. Назад')
            choice = input('Выберите действие: \n>')

            data = self.fm.read_data()
            for user in data:
                if user['email'] == session:
                    flag_change_email_or_password = 0
                    match choice:
                        case '1':
                            user['firstname'] = input('Введите новое имя: ')
                        case '2':
                            user['lastname'] = input('Введите новую фамилию: ')
                        case '3':
                            new_email = input('Введите новую почту: ').strip()
                            for _user in data:
                                if _user['email'] == new_email:
                                    print('Пользователь с такой почтой уже существует!')
                                    self.update_user(session)

                            user['email'] = new_email
                            flag_change_email_or_password = 1
                        case '4':
                            user['password'] = input('Введите новый пароль: ')
                            flag_change_email_or_password = 1
                        case '0':
                            return session
                        case _:
                            print('Неверный вариант!')
                    self.fm.write_data(data)
                    print('Успешно изменено!')
                    if flag_change_email_or_password:
                        print(
                            'Успешно изменено!\nЧтобы снова войти в аккаунт отправьте "2",\nи зайдите с новыми данными.')
                        return False
                    return session

    def delete_user(self, session):
        data = self.fm.read_data()
        for user in data:
            if user['email'] == session:
                data.remove(user)
                self.fm.write_data(data)
                print('Учетная запись успешно удалена')
                return False