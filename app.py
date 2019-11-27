# REFERENCES:
# 1. https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# 2. https://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string

# 'input_image_as_bytes:0'

from flask import Flask, request, redirect
import matplotlib.pyplot as plt
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def detect_text():
    if request.method == "POST":
        if "image" not in request.files:
            print("NO files")
        else:
            print("File got")
        img = request.files["image"]
        print("Image:", img.filename)
        image = img.read()
        # print(type(img.read()))
        nparr = np.frombuffer(image, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # plt.imshow(img_np)
        # plt.show()
        return redirect("file:///home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/client.html")
    if request.method == "GET":
        return redirect("file:///home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/client.html")

if __name__ == "__main__":
    app.run(host="localhost")
