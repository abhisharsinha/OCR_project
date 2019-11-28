# REFERENCES:
# 1. https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# 2. https://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string
# 3. https://medium.com/@jsflo.dev/saving-and-loading-a-tensorflow-model-using-the-savedmodel-api-17645576527



from flask import Flask, request, redirect, jsonify
import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
export_path = "./exported-model"

app = Flask(__name__)

sess = tf.Session(graph=tf.Graph())
tf.saved_model.loader.load(sess, ["serve"], export_path)

@app.route("/", methods=["POST", "GET"])
def detect_text():
    if request.method == "POST":
        if "image" not in request.files:
            print("NO files")
        else:
            print("File got")
        files = request.files.getlist("image")
        send_res = {"response":[]}
        for img in files:
            print("Image:", img.filename)
            image = img.read()
            out = sess.run(['prediction:0', 'probability:0'], feed_dict={'input_image_as_bytes:0': image})
            print(out)
            temp = {"filename":img.filename, "prediction":out[0].decode("utf-8"), "probability":out[1]}
            send_res["response"].append(temp)
        sess.close()
        return jsonify(send_res)
    if request.method == "GET":
        return redirect("file:///home/abhishar/Desktop/Abhishar_Sinha-IITB-Assignment/client.html")

if __name__ == "__main__":
    app.run(host="localhost")
    # close the session properly
