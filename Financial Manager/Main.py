"""
----------------------------- Informações ----------------------------
Projeto: Financial Manager      Autor: Tonny Francis
Data de Inicio: 03/06/2022      Ultima Modificação: 03/06/2022

Objetivo da Aplicação: Criar uma aplicação onde o usuário possa 
fazer o gerenciamento de suas finanças mensais e obter um extrato.

Objetivo Pessoal: Obter conhecimento e praticar sobre desenvolvimento 
de interfaces gráficas e banco de dados.

Horas gastas nesse projeto: 48hrs
----------------------------------------------------------------------
"""

#Importação de bibliotecas

from pydoc import text
from random import random
from Files.Libraries.Qt_Core.Qt_Core import *
from Files.Libraries.Qt_Core.Widgets import *
from Files.Libraries.Windows.Login_SingUp import Login, UI_Pages
from Files.Libraries.Database import Database
import sys

#Login Window
class Login_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Setup Login Window
        self.Ui = Login.UI_Login_Window()
        self.Ui.Setup(self)

        #Iniciando Database
        self.Dm = Database.Database_Manipulation()

        #Iniciando Widget
        self.Widget = Widgets()

        #Funções dos Botões Sing In Pagina 1
        self.Ui.Ui_Pages.Bt_Sing_In_Top_1.clicked.connect(self.Show_Page_Sing_In)
        self.Ui.Ui_Pages.Bt_Sing_Up_1.clicked.connect(self.Show_Page_Sing_Up)
        self.Ui.Ui_Pages.Bt_Forgot_1.clicked.connect(self.Show_Page_Send_Email)
        self.Ui.Ui_Pages.Bt_Sing_In_Bottom_1.clicked.connect(self.Sing_In)

        #Funções dos Botões Sing Up Pagina 2
        self.Ui.Ui_Pages.Bt_Sing_In_Top_2.clicked.connect(self.Show_Page_Sing_In)
        self.Ui.Ui_Pages.Bt_Sing_Up_2.clicked.connect(self.Show_Page_Sing_Up)
        self.Ui.Ui_Pages.Bt_Sing_Up_Bottom_2.clicked.connect(self.Sing_Up)
        #Funções dos Botões Send Email Pagina 3
        self.Ui.Ui_Pages.Bt_Send_3.clicked.connect(self.Send_Email)


        #Funções dos Botoes Forgot Password Pagina 4
        self.Ui.Ui_Pages.Bt_Chage_Password_4.clicked.connect(self.Forgot_Password)

        #Exibe as alterações
        self.show()

    def Show_Page_Sing_In(self):
        self.Ui.Pages.setCurrentWidget(self.Ui.Ui_Pages.Page_Sing_In)

    def Show_Page_Sing_Up(self):
        self.Ui.Pages.setCurrentWidget(self.Ui.Ui_Pages.Page_Sing_Up)

    def Show_Page_Send_Email(self):
        self.Ui.Pages.setCurrentWidget(self.Ui.Ui_Pages.Page_Send_Email)
    
    def Show_Page_Forgot_Password(self):
        #Deve ter uma condição de verificação para realizar essa troca de tela
        self.Ui.Pages.setCurrentWidget(self.Ui.Ui_Pages.Page_Forgot)

    def Sing_In(self):
        User = self.Ui.Ui_Pages.Ld_User_1.text().title()
        Password = self.Ui.Ui_Pages.Ld_Password_1.text()

        Answer = self.Dm.User_Validation(User, Password, self)

        if Answer == True:
            self.close()
    
    def Sing_Up(self):
        User = self.Ui.Ui_Pages.Ld_User_2.text().title()
        Email = self.Ui.Ui_Pages.Ld_Email_2.text()
        Password = self.Ui.Ui_Pages.Ld_Password_2.text()

        Answer = self.Dm.Registration_User(User, Email, Password, self)

        if Answer == True:
            self.close()
        
    def Send_Email(self):
        User = self.Ui.Ui_Pages.Ld_User_3.text().title()

        Answer = self.Dm.Password_Recovery(User, self)

        if Answer == True:
            self.Ui.Pages.setCurrentWidget(self.Ui.Ui_Pages.Page_Forgot)
    
    def Forgot_Password(self):
        Digito_1 = self.Ui.Ui_Pages.Ld_Digit_1_4.text()
        Digito_2 = self.Ui.Ui_Pages.Ld_Digit_2_4.text()
        Digito_3 = self.Ui.Ui_Pages.Ld_Digit_3_4.text()
        Digito_4 = self.Ui.Ui_Pages.Ld_Digit_4_4.text()
        Password = self.Ui.Ui_Pages.Ld_New_Passord_4.text()

        Code = Digito_1 + Digito_2 + Digito_3 + Digito_4
        
        Answer = self.Dm.Code_Validation(int(Code), Password, self)
        
        if Answer == True:
            self.close()

#Inicio do Loop
MyApp = QApplication(sys.argv)

# ----> Conteúdo do Loop <----

#Inicia a Tela de Login
Login_Window_ = Login_Window()

#Fim do Loop
sys.exit(MyApp.exec())