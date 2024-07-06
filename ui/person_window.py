# ui/person_window.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
from Preprocessing.video_capture import Video
import cv2 as cv
import numpy as np

class PersonWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(1200, 900)  # 固定窗口大小
        self.setWindowTitle("行人检测")

        # 设置样式表
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #333;
            }
            QPushButton {
                font-size: 18px;
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

        # 布局
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # 标签显示检测结果
        self.result_label = QLabel("行人数: 0", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.result_label)
        layout.addWidget(self.video_label)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(20)

        self.detect_button = QPushButton("行人检测")
        self.back_button = QPushButton("返回主界面")
        self.detect_button.clicked.connect(self.toggle_detection)
        self.back_button.clicked.connect(self.back_to_main)

        button_layout.addWidget(self.detect_button)
        button_layout.addWidget(self.back_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # 启动视频捕捉线程
        self.video_thread = Video('data/vd4.mp4', mode='person')
        self.video_thread.send.connect(self.update_frame)
        self.video_thread.start()

    def toggle_detection(self):
        self.video_thread.toggle_detection()

    def back_to_main(self):
        self.main_window.show_main_window()

    @pyqtSlot(int, int, int, bytes, str, int, dict)
    def update_frame(self, h, w, c, img_bytes, mode, num, response_data):
        # 将图像数据转换为numpy数组
        img_np = np.frombuffer(img_bytes, dtype=np.uint8).reshape((h, w, c))
        # 转换颜色通道从BGR到RGB
        img_rgb = cv.cvtColor(img_np, cv.COLOR_BGR2RGB)
        # 创建QImage
        img_qt = QImage(img_rgb.data, w, h, QImage.Format_RGB888)
        # 更新视频帧和检测结果
        self.video_label.setPixmap(QPixmap.fromImage(img_qt))
        self.result_label.setText(f"行人数: {num}")
