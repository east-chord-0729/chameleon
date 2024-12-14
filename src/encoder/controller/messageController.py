from datetime import datetime
import hashlib
import base64
import hmac

MAX_LEN = 44


def padding(str):
    new_str = str

    # Cut
    if len(new_str) > MAX_LEN:
        new_str = new_str[0:MAX_LEN]

    # Pad
    while len(new_str) != MAX_LEN:
        new_str += '_'

    return new_str


def hashing_and_output_base64(message, key):
    '''
    메시지를 HMAC으로 해싱하여 base64로 인코딩하는 함수. sha256을 사용한다.

    param str message: 해싱할 메시지
    param str key: 해시에 사용할 키
    '''
    # 해시값 생성
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    hmac_value = hmac_obj.hexdigest()

    # print("hash.....", hmac_value)

    # 해시값을 base64로 인코딩
    byte_array = bytes.fromhex(hmac_value)
    base64_encoded = base64.b64encode(byte_array)
    base64_string = base64_encoded.decode('utf-8')

    # print("base64...", base64_string)

    return base64_string


def generate(info):
    host_name, audience_name, host_key = info
    time = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    message = host_name + "-" + audience_name + "-" + time
    message = padding(message)
    mac = hashing_and_output_base64(message, host_key)
    return message, mac
