import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
                             QFrame, QGridLayout, QSizePolicy, QPushButton)
from PyQt5.QtGui import QPalette, QColor, QFont, QBrush, QPixmap
from PyQt5.QtCore import Qt, QSize

class HardwareMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Definir tamanho da janela
        self.setFixedSize(600, 800)

        # Remover a barra de título padrão e tornar o fundo transparente
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Cria um layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Cria um QLabel para a imagem de fundo
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 800)  # Define o tamanho e a posição
        self.background_label.setScaledContents(True) # Scale the image to fit the label
        self.background_label.lower()

        # Carrega a imagem
        pixmap = QPixmap("gato.png")
        if pixmap.isNull():
            print("Erro: Imagem 'background.png' não encontrada ou corrompida.")
        else:
            self.background_label.setPixmap(pixmap)

        # Paleta de cores futurista
        self.setStyleSheet("""
            QWidget {
                color: #cad3f5;
                font-family: 'Times New Roman', serif;
                font-size: 19px;
                background-color: transparent; /* Tornando o fundo do QWidget transparente */
            }
            QLabel {
                font-size: 19px;
                padding: 3px;
                margin: 0;
                color: #cad3f5; /* Garante que o texto seja visível */
                background-color: transparent; /* Tornando o fundo do QLabel transparente */
            }
            QLineEdit {
                background-color: #313244;
                border: 1px solid #45475a;
                color: #cad3f5;
                padding: 3px;
                border-radius: 3px;
                margin: 0;
            }
            QFrame {
                border: 1px solid #45475a;
                border-radius: 5px;
            }
        """)

        # Título do programa (apenas altura das letras)
        title_label = QLabel("Hardware Status", self)
        title_label.setFont(QFont("Times New Roman", 22, QFont.Bold))  # Aumentado e alterado a fonte
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(10)

        # Layout vertical para os containers de hardware
        hardware_layout = QVBoxLayout()
        main_layout.addLayout(hardware_layout)
        hardware_layout.setSpacing(20)  # Espaço entre os containers

        # Função para criar container de hardware
        def create_hardware_container(name, has_details=True):
            container = QWidget(self)
            container_layout = QVBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setSpacing(2) # Remove espaçamento interno

            # Layout vertical para rótulo e campo de saída
            name_layout = QVBoxLayout()
            name_layout.setSpacing(0)  # Remove espaçamento
            hardware_label = QLabel(name, container)
            hardware_label.setAlignment(Qt.AlignCenter)
            hardware_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) # Altura do texto
            name_layout.addWidget(hardware_label)
            hardware_output = QLineEdit(container)
            hardware_output.setReadOnly(True)
            name_layout.addWidget(hardware_output)
            container_layout.addLayout(name_layout)

            if has_details:
                # Layout horizontal para capacidade e temperatura
                details_layout = QHBoxLayout()
                details_layout.setSpacing(0)  # REMOVE spacing between capacity and temperature
                container_layout.addLayout(details_layout)

                # Criação de layouts verticais para "Capacidade" e "Temperatura"
                def create_detail_layout(detail_name, parent):
                    detail_vlayout = QVBoxLayout()
                    detail_vlayout.setSpacing(0)
                    detail_label = QLabel(detail_name, parent)
                    detail_label.setAlignment(Qt.AlignCenter)
                    detail_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)  # Altura do texto
                    detail_vlayout.addWidget(detail_label)
                    detail_output = QLineEdit(parent)
                    detail_output.setReadOnly(True)
                    detail_vlayout.addWidget(detail_output)
                    return detail_vlayout

                capacity_vlayout = create_detail_layout("Capacidade", container)
                temperature_vlayout = create_detail_layout("Temperatura", container)

                details_layout.addLayout(capacity_vlayout)
                details_layout.addLayout(temperature_vlayout)
            return container

        processor_container = create_hardware_container("Processador")
        hardware_layout.addWidget(processor_container)

        ram_container = create_hardware_container("Memória RAM")
        hardware_layout.addWidget(ram_container)

        video_card_container = create_hardware_container("Placa de Vídeo")
        hardware_layout.addWidget(video_card_container)

        motherboard_container = create_hardware_container("Placa Mãe", False)  # Sem detalhes
        hardware_layout.addWidget(motherboard_container)

        # Botão de fechar no rodapé
        close_button = QPushButton("Fechar", self)
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #4c566a;
                color: #cad3f5;
                border: 1px solid #45475a;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #626e7f;
            }
        """)
        main_layout.addWidget(close_button)
        close_button.setFixedHeight(40)  # Define a altura do botão

        self.setWindowTitle("Hardware Status")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HardwareMonitorApp()
    sys.exit(app.exec_())
