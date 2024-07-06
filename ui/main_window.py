# ui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt
from ui.vehicle_window import VehicleWindow
from ui.person_window import PersonWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("校园监控系统")
        self.setFixedSize(1200, 900)  # 固定窗口大小

        # 设置背景图片
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1200, 900)
        self.background_label.setPixmap(QPixmap('data/bg.jpg').scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.background_label.lower()

        # 添加logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('data/logo.png')
        logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setGeometry(10, 10, 100, 100)  # 左上角，大小100x100

        # 创建堆栈窗口部件
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setGeometry(0, 0, 1200, 900)
        self.setCentralWidget(self.stacked_widget)

        # 创建主界面
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)

        # 调整按钮位置
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignTop)
        button_layout.setSpacing(20)  # 设置按钮之间的间距

        self.vehicle_button = QPushButton("车辆检测")
        self.person_button = QPushButton("行人检测")
        button_layout.addWidget(self.vehicle_button)
        button_layout.addWidget(self.person_button)
        # 设置样式表
        self.setStyleSheet("""
                  QLabel {
                      font-size: 30px;
                      color: #333;
                  }
                  QPushButton {
                      font-size: 30px;
                      padding: 15px;
                      background-color: #0078d7;
                      color: white;
                      border: none;
                      border-radius: 10px;
                  }
                  QPushButton:hover {
                      background-color: #0053a0;
                  }
              """)

        button_widget = QWidget(self)
        button_widget.setLayout(button_layout)
        button_widget.setGeometry(10, 120, 200, 100)  # logo下方，大小200x100

        self.main_layout.addWidget(button_widget)
        self.main_widget.setLayout(self.main_layout)
        self.stacked_widget.addWidget(self.main_widget)

        # 创建车辆检测界面
        self.vehicle_window = VehicleWindow(self)
        self.stacked_widget.addWidget(self.vehicle_window)

        # 创建行人检测界面
        self.person_window = PersonWindow(self)
        self.stacked_widget.addWidget(self.person_window)

        # 绑定按钮事件
        self.vehicle_button.clicked.connect(self.show_vehicle_window)
        self.person_button.clicked.connect(self.show_person_window)

    def show_vehicle_window(self):
        self.stacked_widget.setCurrentWidget(self.vehicle_window)

    def show_person_window(self):
        self.stacked_widget.setCurrentWidget(self.person_window)

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)
