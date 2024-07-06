# detection/vehicle_detection.py
import requests
import base64
import cv2 as cv

# opencv 图片
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = "24.6f6f52ecd764be14ecb800435ff4b45e.2592000.1722737086.282335-89935081"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    vehicle_num = {
        'car': 0,
        'truck': 0,
        'bus': 0,
        'motorbike': 0,
        'tricycle': 0
    }
    if response:
        data = response.json()
        vehicle_num = data['vehicle_num']
        num = vehicle_num['car'] + vehicle_num['truck'] + vehicle_num['bus'] + vehicle_num['motorbike'] + vehicle_num['tricycle']
        for item in data['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            # 定义要绘制的文字
            text = item['type']
            position = (x1, y1 - 2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # 红色
            thickness = 2
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)

    return img, num, vehicle_num
