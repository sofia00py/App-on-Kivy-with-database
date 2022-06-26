import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3 as sql
from convolutional1 import *

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [30,200,30,250]
        Label:
            text: 'Hello, happy to see u!'
            font_size: 10
            size: 250, 20
        Label:
            text: 'If u alrady have a profile, u can LogIn'
            font_size: 10
            size: 250, 20
        Button:
            text: 'LogIn'
            font_size: 10
            size: 250, 20
            on_press: root.manager.current = 'login'
        Label:
            font_size: 10
            size: 250, 20
            text: 'If u have never been here before, we would like to know u, sweety!'
        Button:
            text: 'Registration'
            font_size: 10
            size: 250, 20
            on_press: root.manager.current = 'registration'

<RegistrationMenu>:
    BoxLayout:
        orientation: 'vertical'
        padding: [30,230,30,230]
        TextInput:
            id: name_for_reg
            font_size: 10
            size: 250, 30
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            hint_text: 'Name:'
            multiline: False
        TextInput:
            id: pass_for_reg
            font_size: 10
            size: 250, 30
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            hint_text: 'Password:'
            password: True
            multiline: False
        Button:
            text: 'Register'
            font_size: 10
            size: 250, 25
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            on_press: root.registration()
        Button:
            text: 'Back to menu'
            font_size: 10
            size: 250, 25
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'menu'

<LoginMenu>:
    BoxLayout:
        orientation: 'vertical'
        padding: [30,230,30,230]
        TextInput:
            id: login
            font_size: 10
            size: 250, 30
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            hint_text: 'Name:'
            multiline: False
        TextInput:
            id: password
            font_size: 10
            size: 250, 30
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            hint_text: 'Password:'
            password: True
            multiline: False
        Button:
            text: 'Login'
            font_size: 10
            size: 250, 25
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            on_press: root.login()
        Button:
            text: 'Back to menu'
            font_size: 10
            size: 250, 25
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'menu'
            
<PS>:
    FloatLayout:
        id:fl1
        orientation: 'vertical'
        canvas:
            Rectangle:
                source: 'fon2.jpg'
                size: self.size
                pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        padding: [250,250]
        Label:
            font_size: 10
            size: 250, 30
            text: 'Невозможно победить того, кто не сдается.'
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
    BoxLayout:
        orientation: 'vertical'
        padding: [270,230]
        Label:
            font_size: 10
            size: 250, 30
            text: '(Мы точно не уйдем в академ)'
            size_hint: None,None
            pos_hint: {'center_x': 0.5}
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'LogOut'
            font_size: 10
            size: 50, 20
            size_hint: None,None
            pos_hint: {'left_x': 0.5}
            on_press: root.manager.current = 'menu'
""")


class MenuScreen(Screen):
    pass

class LoginMenu(Screen):
    def login(self):
        s = convolotional()
        from turbo import compression
        username = s.encode(text_bin(self.ids.login.text))
        password = compression(self.ids.password.text)
        con = sql.connect("data1.db")
        cur = con.cursor()
        statement = f"SELECT Name from users WHERE Name='{username}' AND Password = '{password}';"
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            sm.current = 'ps'
        return

class RegistrationMenu(Screen):
    def insert_varible_into_table(self, username, password):
        try:
            con = sqlite3.connect('data1.db')
            cur = con.cursor()
            print("Подключен к SQLite")

            sqlite_insert_with_param = """INSERT INTO users
                                          (Name, Password)
                                          VALUES (?,?);"""

            data_tuple = (username, password)
            cur.execute(sqlite_insert_with_param, data_tuple)
            con.commit()
            print("Переменные Python успешно вставлены в таблицу")

            cur.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                print("Соединение с SQLite закрыто")
                sm.current = 'menu'

    def registration(self):
        s = convolotional()
        from turbo import compression
        u_for_c = self.ids.name_for_reg.text
        p_for_c = self.ids.pass_for_reg.text
        m = text_bin(u_for_c)
        username = s.encode(m)
        password = compression(p_for_c)
        con = sql.connect("data1.db")
        cur = con.cursor()
        self.insert_varible_into_table(username, password)

class PS(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginMenu(name='login'))
sm.add_widget(RegistrationMenu(name='registration'))
sm.add_widget(PS(name='ps'))

class App(App):
    def build(self):
        return sm

if __name__ == '__main__':
    App().run()
