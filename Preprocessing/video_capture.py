# Preprocessing/video_capture.py
from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
from detection.vehicle_detection import vehicle_detect
from detection.person_detection import person_detect

class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, str, int, dict)  # emit

    def __init__(self, video_id, mode='vehicle'):
        super().__init__()
        self.video_id = video_id
        self.mode = mode
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)
        self.detect_mode = False

    def toggle_detection(self):
        self.detect_mode = not self.detect_mode

    def run(self):
        while True:
            ret, frame = self.dev.read()
            num = 0
            response_data = {}
            if not ret:
                print('no')
            if self.detect_mode:
                if self.mode == 'vehicle':
                    frame, num, response_data = vehicle_detect(frame)
                elif self.mode == 'person':
                    num, response_data = person_detect(frame)
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.mode, num, response_data)
            QThread.usleep(100000)  # 每100ms截取一次
