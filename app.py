# REFERENCES:
# 1. https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# 2. https://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string
# 3. https://medium.com/@jsflo.dev/saving-and-loading-a-tensorflow-model-using-the-savedmodel-api-17645576527

# Runs flask webapp on http://localhost:5000
# Takes SavedModel path as argument
# python app.py ./exported-model/default-model

from flask import Flask, request, redirect, jsonify
import tensorflow as tf
import sys
import numpy as np

# Allow only image files
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

if not len(sys.argv) == 2:
    raise Exception("Provide path of savedmodel")

# path of saved model
# eg: ./exported-model
export_path = sys.argv[1]

app = Flask(__name__)

# Starting tf Session and loading saved model
sess = tf.Session(graph=tf.Graph())
tf.saved_model.loader.load(sess, ["serve"], export_path)

@app.route("/", methods=["POST", "GET"])
def detect_text():
    if request.method == "GET":
        return app.send_static_file('./index.html')
    if request.method == "POST":
        files = request.files.getlist("image")
        
        # if no file is selected
        if files[0].filename == "":
            print("No files uploaded!")
            return redirect(request.url)
        send_res = {"response":[]}
        images = []
        filenames = []
        # Creating a list of images as bytes to feed to the model
        for img in files:
            # Checking if all uploaded files are images
            if img.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
                continue
            image = img.read()
            images.append(image)
            filenames.append(img.filename)
        
        # If not image files then redirect
        if not filenames:
            print("No images uploaded!")
            return redirect(request.url)

        # out is a list of two lists for pred and prob
        out = sess.run(['prediction:0', 'probability:0'], feed_dict={'input_image_as_bytes:0': images}) 
        
        # Cannot zip non-lists so making list of single value when out[1] is not a list
        if not type(out[1]) == np.ndarray:
            out[0] = [out[0]]
            out[1] = [out[1]]
        for img_name, pred, prob in zip(filenames, out[0], out[1]):
            temp = {"filename":img_name, "prediction":pred.decode("utf-8"), "probability":prob}
            send_res["response"].append(temp)
        
        return jsonify(send_res)

def main():
    app.run(host="localhost")

if __name__ == "__main__":
    # Free gpu memory by calling sess.close on keyboard interrupt

    try:
        main()
    except KeyboardInterrupt:
        sess.close()
