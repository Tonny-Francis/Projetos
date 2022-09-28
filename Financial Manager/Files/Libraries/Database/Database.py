import sqlite3
import pandas as pd
import os
import random
from Files.Libraries.Qt_Core.Widgets import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Database_Interface:
    def __init__(self):
        #Faz conexão com o banco de dados
        self.Con = sqlite3.connect('Python\Projetos\Financial Manager\Files\Database\Database.db')

        #Cursor
        self.Cur = self.Con.cursor()

    def Insert(self, Tabela, Valores):
        #Insere dados em uma determinada tabela
        self.Cur.execute(f'''
            INSERT INTO {Tabela} VALUES
            ({Valores})
        ''')

        #Executa as alterações
        self.Con.commit()
    
    def Delete(self, Tabela, Id):
        #Deleta um determinada linha de uma tabela
        self.Cur.execute(f'''
            DELETE FROM {Tabela} WHERE ID={Id}
        ''')

        #Executa as alterações
        self.Con.commit()
    
    def Update(self, Tabela, Coluna, Atualização, Id):
        self.Cur.execute(f'''
            UPDATE '{Tabela}' SET '{Coluna}' = '{Atualização}' WHERE ID = '{Id}'
        ''')
        self.Con.commit()

    def Data(self, Colunas, Tabela):
        #Obtem os dados de um determinada tabela
        Data = self.Cur.execute(f'SELECT {Colunas} FROM {Tabela}')

        #Remove um caractre em especifico
        Caractere = ','

        for x in range(len(Caractere)):
            Colunas = Colunas.replace(Caractere[x], '')

        #Cria um dataframe com os dados obtidos
        DataFrame = pd.DataFrame(Data, columns = Colunas.split())

        return DataFrame

class Database_Manipulation():
    def __init__(self):
        self.Di = Database_Interface()

        #Iniciando Widget
        self.Widget = Widgets()
    
    def User_Validation(self, User, Password, Parent):
        self.Di.Cur.execute('''
        SELECT * FROM Login
        ''')

        for Linha in self.Di.Cur.fetchall():
            if Linha[1] == User and Linha[2] == Password:
                self.Di.Update('Login', 'Logged', '1', Linha[0])
                return True

            else:
                continue

        self.Widget.WMessage_Box(Parent, 'Incorrect Username or Password', 'Financial Manager', QMessageBox.Information)
    
    def Registration_User(self, User, Email, Password, Parent):
        self.Di.Cur.execute('''
        SELECT * FROM Login
        ''')

        for self.Linha in self.Di.Cur.fetchall():
            if self.Linha[1] == User:
                self.Widget.WMessage_Box(Parent, 'User Already Registered', 'Financial Manager', QMessageBox.Information)
            
            else:
                self.Di.Insert('Login (ID, User, Password, Email, Logged)', f"NULL, '{User}', '{Password}', '{Email}', 1")
                return True

    def Password_Recovery(self, User, Parent):
        self.Di.Cur.execute('''
        SELECT * FROM Login
        ''')

        for self.Linha in self.Di.Cur.fetchall():
            self.Code = random.randint(1000, 9999)
            if self.Linha[1] == User:
                Send_Email(self.Linha[3], User, self.Code)

                return True

            else:
                continue

        self.Widget.WMessage_Box(Parent, 'Incorrect Username', 'Financial Manager', QMessageBox.Information)

    def Code_Validation(self, Code, Password, Parent):
        if self.Code == Code:
            self.Di.Update('Login', 'Password', Password, self.Linha[0])
            return True
        else: 
            self.Widget.WMessage_Box(Parent, 'Invalid Code', 'Financial Manager', QMessageBox.Information)

def Send_Email(Email, User, Code):
    message = Mail(
        from_email='hellou.world.py@gmail.com',
        to_emails= Email,
        subject='Password Recovery Code - Financial Manager',
        html_content= f'''
        <h1>Password Recovery</h1>
        <p>Hi!! {User}</p>
        <p>You informed that you forgot your Financial Manager password,\nuse the code below to reset your password.</p>
        <strong>{Code}</strong>
        '''
    )

    sg = SendGridAPIClient('API')
    sg.send(message)