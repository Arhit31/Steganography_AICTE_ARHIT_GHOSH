import cv2
import os

def decryption(img, msg, password, c, input_password):
    message = ""
    n = 0
    m = 0
    z = 0
    if password == input_password:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        return message
    else:
        return "YOU ARE NOT auth"