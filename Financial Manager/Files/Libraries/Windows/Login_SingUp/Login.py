#Importação de bibliotecas
from Files.Libraries.Qt_Core.Qt_Core import *
from Files.Libraries.Database.Database import *
from Files.Libraries.Windows.Login_SingUp.UI_Pages import Ui_Login_SingUp_Pages

#Login Window
class UI_Login_Window(object):
    def Setup(self, Parent):
        #Verificação padrão do Qt
        if not Parent.objectName():
            Parent.setObjectName(u"Parent")

        #Definindo parametros iniciais: Tamanho e Nome
        Parent.setWindowTitle('Financial Manager')
        Parent.setMinimumSize(720, 480)
        Parent.setWindowIcon(QIcon('Python/Projetos/Financial Manager/Files/Images/Icon.png'))
        #Importação de fonte Itim
        QFontDatabase.addApplicationFont('Python/Projetos/Financial Manager/Files/Sources/Itim.ttf')
        
        # ----------------------> Main <----------------------
        self.Main_Frame = QFrame()
        self.Main_Frame.setStyleSheet('background-color: #eef0f2;')

        self.Main_Layout = QHBoxLayout(self.Main_Frame)
        self.Main_Layout.setContentsMargins(0, 0, 0, 0)
        self.Main_Layout.setSpacing(0)

        # ----------------------> Logo <----------------------
        self.Left_Frame = QFrame()
        self.Left_Frame.setMinimumWidth(260)
        self.Left_Frame.setMaximumWidth(260)
        self.Left_Frame.setStyleSheet('background-color: #242333;')

        self.Left_Layout = QVBoxLayout(self.Left_Frame)
        self.Left_Layout.setContentsMargins(0, 0, 0, 0)
        self.Left_Layout.setSpacing(0)
        self.Left_Layout.setAlignment(Qt.AlignCenter)

        self.Logo_Frame = QFrame()
        self.Logo_Frame.setMinimumSize(130, 109)

        self.Img = QPixmap('Python/Projetos/Financial Manager/Files/Images/Logo.png')

        self.Logo_Background = QLabel(self.Logo_Frame)
        self.Logo_Background.setPixmap(self.Img)

        self.Left_Layout.addWidget(self.Logo_Frame)
        
        # ---------------------> Content <--------------------
        self.Content_Frame = QFrame()
        self.Content_Frame.setStyleSheet('background-color: #eef0f2;')

        self.Content_Layout = QVBoxLayout(self.Content_Frame)
        self.Content_Layout.setContentsMargins(0, 0, 0, 0)
        self.Content_Layout.setSpacing(0)
        self.Content_Layout.setAlignment(Qt.AlignHCenter)

        # ----------------------> Pages <---------------------
        self.Pages = QStackedWidget()
        self.Pages.setStyleSheet('background-color: #eef0f2;')
        self.Ui_Pages = Ui_Login_SingUp_Pages()
        self.Ui_Pages.setupUi(self.Pages)

        self.Content_Layout.addWidget(self.Pages)

        # --------------------> Bottom bar <------------------
        self.Bottom_Bar = QFrame()
        self.Bottom_Bar.setMinimumHeight(20)
        self.Bottom_Bar.setMaximumHeight(20)
        self.Bottom_Bar_Layout = QHBoxLayout(self.Bottom_Bar)
        self.Bottom_Bar_Layout.setContentsMargins(20, 0, 20, 0)

        self.Left_Label = QLabel('Created By: Tonny Francis')
        self.Left_Label.setStyleSheet('font-size: 8pt; font-family: Arial; color: #242333;')

        self.Spacing = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Right_Label = QLabel('© 2022 | V1.0.1')
        self.Right_Label.setStyleSheet('font-size: 8pt; font-family: Arial; color: #242333;')

        self.Bottom_Bar_Layout.addWidget(self.Left_Label)
        self.Bottom_Bar_Layout.addItem(self.Spacing)
        self.Bottom_Bar_Layout.addWidget(self.Right_Label)

        self.Content_Layout.addWidget(self.Bottom_Bar)

        # --------------------> Add App <---------------------
        self.Main_Layout.addWidget(self.Left_Frame)
        self.Main_Layout.addWidget(self.Content_Frame)

        #Definindo widget central/primary
        Parent.setCentralWidget(self.Main_Frame)