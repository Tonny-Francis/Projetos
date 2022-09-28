from  Files.Libraries.Qt_Core.Qt_Core import *
from  Files.Libraries.Qt_Core.Widgets import*

class Ui_Login_SingUp_Pages(object):
    def setupUi(self, Login):
        Login.resize(720, 480)

        #Instanciando Widgets
        self.Widget = Widgets()

        ''' ----> Abreviações <----
        Lt - Layout
        Fr - Frame
        Lb - Label
        Bt - Button
        Ld - Lineedit
        '''
        # ----> Sing in <----
        self.Page_Sing_In = QWidget()

        self.Page_Sing_In_Lt = QVBoxLayout(self.Page_Sing_In)
        self.Page_Sing_In_Lt.setAlignment(Qt.AlignCenter)

        self.Sing_In_Fr = self.Widget.WFrame(self.Page_Sing_In, 160, 237, 160, 237)
        self.Sing_In_Fr.setStyleSheet('background-color: #eef0f2;')

        # ----> Sing up <----
        self.Page_Sing_Up = QWidget()

        self.Page_Sing_Up_Lt = QVBoxLayout(self.Page_Sing_Up)
        self.Page_Sing_Up_Lt.setAlignment(Qt.AlignCenter)

        self.Sing_Up_Fr = self.Widget.WFrame(self.Page_Sing_Up, 160, 284, 160, 284)
        self.Sing_Up_Fr.setStyleSheet('background-color: #eef0f2;')

        # ---> Send Email <----
        self.Page_Send_Email = QWidget()

        self.Page_Send_Email_Lt = QVBoxLayout(self.Page_Send_Email)
        self.Page_Send_Email_Lt.setAlignment(Qt.AlignCenter)

        self.Send_Email_Fr = self.Widget.WFrame(self.Page_Send_Email, 210, 196, 210, 196)
        self.Send_Email_Fr.setStyleSheet('background-color: #eef0f2;')

        # ---> Forgot Password <----
        self.Page_Forgot = QWidget()

        self.Page_Forgot_Lt = QVBoxLayout(self.Page_Forgot)
        self.Page_Forgot_Lt.setAlignment(Qt.AlignCenter)

        self.Forgot_Fr = self.Widget.WFrame(self.Page_Forgot, 160, 163, 160, 163)
        self.Forgot_Fr.setStyleSheet('background-color: #eef0f2;')

        # -------------> Itens da pagina Sing in <-------------
        self.Bt_Sing_Up_1 = self.Widget.WButton('Sing up', self.Sing_In_Fr, 80, 0, 80, 30, 
        '#eef0f2', '15px', '#242333', 'Itim', '12pt', 'normal', '0px') 

        self.Bt_Sing_In_Top_1 = self.Widget.WButton('Sing in', self.Sing_In_Fr, 0, 0, 80, 30,
        '#242333', '15px', '#eef0f2', 'Itim', '12pt', 'normal','0px') 

        self.Bt_Sing_In_Bottom_1 = self.Widget.WButton('SING IN', self.Sing_In_Fr, 0, 207, 160, 
        30, '#242333', '15px', '#eef0f2', 'Itim', '12pt', 'normal','1px solid #eef0f2')

        self.Bt_Forgot_1 = self.Widget.WButton('Forgot password?', self.Sing_In_Fr, 0, 177, 
        118, 19, '#eef0f2', '15px', '#242333', 'Itim', '12pt', 'underline','0px') 

        self.Lb_User_1 = self.Widget.WLabel('User', self.Sing_In_Fr, 0, 61, 35, 14, '#242333',
        'Itim', '12pt')  

        self.Lb_Password_1 = self.Widget.WLabel('Password', self.Sing_In_Fr, 0, 118, 65, 16, '#242333',
        'Itim', '12pt') 

        self.Ld_User_1 = self.Widget.WLineedit(self.Sing_In_Fr, 0, 77, 160, 30, 15, '#242333', 
        'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333') 

        self.Ld_Password_1 = self.Widget.WLineedit_Password(self.Sing_In_Fr, 0, 134, 160, 30, 15, 
        '#242333', 'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333')

        self.Page_Sing_In_Lt.addWidget(self.Sing_In_Fr)

        # -------------> Itens da pagina Sing up <-------------
        self.Bt_Sing_Up_2 = self.Widget.WButton('Sing up', self.Sing_Up_Fr, 80, 0, 80, 30,
        '#242333', '15px', '#eef0f2', 'Itim', '12pt', 'normal', '0px') 

        self.Bt_Sing_In_Top_2 = self.Widget.WButton('Sing in', self.Sing_Up_Fr, 0, 0, 80, 30,
        '#eef0f2', '15px', '#242333', 'Itim', '12pt', 'normal', '0px') 

        self.Bt_Sing_Up_Bottom_2 = self.Widget.WButton('SING UP', self.Sing_Up_Fr, 0, 254, 160, 30,
        '#212333', '15px', '#eef0f2', 'Itim', '12pt', 'normal', '1px solid #eef0f2') 

        self.Lb_Email_2 = self.Widget.WLabel('E-mail Address', self.Sing_Up_Fr, 0, 62, 105, 14,
        '#242333', 'Itim', '12pt')

        self.Lb_User_2 = self.Widget.WLabel('User', self.Sing_Up_Fr, 0, 119, 35, 14, '#242333', 
        'Itim', '12pt')

        self.Lb_User_2 = self.Widget.WLabel('Password', self.Sing_Up_Fr, 0, 175, 64, 16, '#242333', 
        'Itim', '12pt')

        self.Ld_Email_2 = self.Widget.WLineedit(self.Sing_Up_Fr, 0, 77, 160, 30, 50, '#242333', 
        'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333') 

        self.Ld_User_2 = self.Widget.WLineedit(self.Sing_Up_Fr, 0, 134, 160, 30, 15, '#242333', 
        'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333') 

        self.Ld_Password_2 = self.Widget.WLineedit_Password(self.Sing_Up_Fr, 0, 191, 160, 30, 15, 
        '#242333', 'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333')  

        self.Page_Sing_Up_Lt.addWidget(self.Sing_Up_Fr)

        # -------------> Itens da pagina Send email <--------------
        self.Lb_text_3 = self.Widget.WLabel('Enter the username\nassociated with the account to\nrecover the password.',
        self.Send_Email_Fr, 0, 0, 210, 60, '#242333', 'Itim', '12pt')
        self.Lb_text_3.setAlignment(Qt.AlignHCenter)

        self.Lb_User_3 = self.Widget.WLabel('Username', self.Send_Email_Fr, 0, 105, 105, 14, '#242333', 
        'Itim', '12pt')

        self.Ld_User_3 = self.Widget.WLineedit(self.Send_Email_Fr, 0, 120, 210, 30, 15, '#242333', 
        'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333')

        self.Bt_Send_3 = self.Widget.WButton('SEND', self.Send_Email_Fr, 0, 166, 210, 30, '#212333',
        '15px', '#eef0f2', 'Itim', '12pt', 'normal', '1px solid #eef0f2') 

        self.Page_Send_Email_Lt.addWidget(self.Send_Email_Fr)

        # -------------> Itens da pagina Forgot Password <--------------
        self.Lb_code_4 = self.Widget.WLabel('What code did you get?', self.Forgot_Fr, 0, 0, 160, 19, 
        '#242333', 'Itim', '12pt')
        self.Lb_code_4.setAlignment(Qt.AlignCenter)

        self.Ld_Digit_1_4 = self.Widget.WLineedit(self.Forgot_Fr, 0, 30, 32.5, 30, 1, '#242333', 
        'Itim', '12pt', '2px solid #888890', '10px', '2px solid #242333', '2px solid #242333')

        self.Ld_Digit_2_4 = self.Widget.WLineedit(self.Forgot_Fr, 43, 30, 32.5, 30, 1, '#242333', 
        'Itim', '12pt', '2px solid #888890', '10px', '2px solid #242333', '2px solid #242333')

        self.Ld_Digit_3_4 = self.Widget.WLineedit(self.Forgot_Fr, 86, 30, 32.5, 30, 1, '#242333', 
        'Itim', '12pt', '2px solid #888890', '10px', '2px solid #242333', '2px solid #242333') 

        self.Ld_Digit_4_4 = self.Widget.WLineedit(self.Forgot_Fr, 128, 30, 32.5, 30, 1, '#242333', 
        'Itim', '12pt', '2px solid #888890', '10px', '2px solid #242333', '2px solid #242333')

        self.Lb_New_Password_4 = self.Widget.WLabel('New Password', self.Forgot_Fr, 0, 72, 100, 19, 
        '#242333', 'Itim', '12pt')

        self.Ld_New_Passord_4 = self.Widget.WLineedit_Password(self.Forgot_Fr, 0, 89, 160, 30, 15, '#242333', 
        'Itim', '12pt', '2px solid #888890', '15px', '2px solid #242333', '2px solid #242333')

        self.Bt_Chage_Password_4 = self.Widget.WButton('CHANGE', self.Forgot_Fr, 0, 133, 160, 30, 
        '#212333', '15px', '#eef0f2', 'Itim', '12pt', 'normal', '1px solid #eef0f2') 

        self.Page_Forgot_Lt.addWidget(self.Forgot_Fr)

        #Adiciona as paginas
        Login.addWidget(self.Page_Sing_In)
        Login.addWidget(self.Page_Sing_Up)
        Login.addWidget(self.Page_Send_Email)
        Login.addWidget(self.Page_Forgot)