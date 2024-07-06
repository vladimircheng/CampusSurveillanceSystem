# Preprocessing/person_detection.py
import requests
import base64
import cv2 as cv

def person_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = "24.edc532d99d4a314365a0c746473facb0.2592000.1722735145.282335-90885151"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        num = data.get('person_num', 0)
    return num, response.json()  # 返回检测到的行人数和完整的响应
