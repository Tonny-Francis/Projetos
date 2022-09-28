from  Files.Libraries.Qt_Core.Qt_Core import *

class Widgets():
    def WFrame(self, Parent, Width_MinimumSize, Height_MinimumSize, Width_MaximumSize, Height_MaximumSize):
        Frame = QFrame(Parent)
        Frame.setMinimumSize(Width_MinimumSize, Height_MinimumSize)
        Frame.setMaximumSize(Width_MaximumSize, Height_MaximumSize)
        return Frame

    def WBackground(self, Path, Parent):
        Img = QPixmap(Path)
        Background = QLabel(Parent)
        Background.setPixmap(Img)

        return Background

    def WLabel(self, Text, Parent, X, Y, Width, Height, Color, Font_Family, Font_Size):
        Label = QLabel(Text, Parent)
        Label.setGeometry(X, Y, Width, Height)
        Label.setStyleSheet(
        f'''
            QLabel{{
                color: {Color};
                font-family: {Font_Family};
                font-size: {Font_Size};
            }}
        ''')

        return Label

    def WLineedit(self, Parent,  X, Y, Width, Height, MaxCaractere, Color, Font_Family,
                    Font_Size, Border, Border_Radius, Hover_Border, Focus_Border):
        Lineedit = QLineEdit(Parent)
        Lineedit.setGeometry(X, Y, Width, Height)
        Lineedit.setMaxLength(MaxCaractere)
        Lineedit.setAlignment(Qt.AlignCenter)
        Lineedit.setStyleSheet(
        f'''
            QLineEdit{{
                color: {Color};
                font-family: {Font_Family};
                font-size: {Font_Size};
                border: {Border};
                border-radius: {Border_Radius};
            }}
            QLineEdit:hover{{
                border: {Hover_Border};
            }}
            QLineEdit:focus{{
                border: {Focus_Border};
            }}
        ''')

        return Lineedit

    def WLineedit_Password(self, Parent,  X, Y, Width, Height, MaxCaractere, Color, Font_Family,
                            Font_Size, Border, Border_Radius, Hover_Border, Focus_Border):
        Lineedit = QLineEdit(Parent)
        Lineedit.setGeometry(X, Y, Width, Height)
        Lineedit.setMaxLength(MaxCaractere)
        Lineedit.setAlignment(Qt.AlignCenter)
        Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        Lineedit.setStyleSheet(
        f'''
            QLineEdit{{
                color: {Color};
                font-family: {Font_Family};
                font-size: {Font_Size};
                border: {Border};
                border-radius: {Border_Radius};
            }}
            QLineEdit:hover{{
                border: {Hover_Border};
            }}
            QLineEdit:focus{{
                border: {Focus_Border};
            }}
        ''')

        return Lineedit

    def WButton(self, Text, Parent, X, Y, Width, Height, Background_Color, Border_Radius,
                Color, Font_Family, Font_Size, Text_Decoration, Hover_Border):
        Button = QPushButton(Text, Parent)
        Button.setGeometry(X, Y, Width, Height)
        Button.setStyleSheet(        
        f'''
            QPushButton{{
                background-color: {Background_Color}; 
                border-radius: {Border_Radius}; 
                color: {Color};
                font-family: {Font_Family};
                font-size: {Font_Size};
                text-decoration: {Text_Decoration};
            }}
            QPushButton:hover{{
                border: {Hover_Border};
            }}
        ''')

        return Button
    
    def WMessage_Box(self, Parent, Message, Title, Icon):
        Message_Box = QMessageBox(Parent)
        Message_Box.setText(Message)
        Message_Box.setWindowTitle(Title)
        Message_Box.setIcon(Icon)
        Message_Box.exec_()
        return Message_Box