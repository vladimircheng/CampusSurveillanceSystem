# 校园监控系统

本项目是一个基于Python和Qt的校园监控系统，能够实时检测车辆和行人。系统使用百度AI接口进行车辆和行人的识别，并在Qt界面中显示检测结果。

## 功能说明

- **车辆检测**：通过调用百度AI接口检测视频中的车辆，包括小汽车、卡车、巴士、摩托车和三轮车，并在界面中显示检测到的车辆数量和类型。
- **行人检测**：通过调用百度AI接口检测视频中的行人，并在界面中显示检测到的行人数。

## 项目结构

CampusSurveillanceSystem/
│
├── data/
│ ├── bg.jpg # 背景图片
│ ├── logo.png # Logo图片
│ ├── vd1.mp4 # 车辆检测视频
│ ├── vd4.mp4 # 行人检测视频
│
├── detection/
│ ├── vehicle_detection.py # 车辆检测模块
│ ├── person_detection.py # 行人检测模块
│
├── Preprocessing/
│ ├── video_capture.py # 视频捕获模块
│
├── ui/
│ ├── main_window.py # 主界面
│ ├── vehicle_window.py # 车辆检测界面
│ ├── person_window.py # 行人检测界面
│
├── main.py # 主程序入口
├── README.md # 项目说明文件
│
└── requirements.txt # 依赖包列表
