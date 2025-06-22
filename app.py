import os
import signal
import subprocess
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from wasteDetection.pipeline.training_pipeline import TrainPipeline
from wasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from wasteDetection.constant.application import APP_HOST, APP_PORT
import platform

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

clApp = ClientApp()

# Global variable for detection process
detection_process = None

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful!!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system(
            "cd yolov5 && python detect.py --weights best.onnx --img 640 --conf 0.5 "
            "--source ../data/inputImage.jpg --project runs/detect --name results --exist-ok"
        )
        result_image_path = "yolov5/runs/detect/results/inputImage.jpg"
        opencodedbase64 = encodeImageIntoBase64(result_image_path)

        result = {"image": opencodedbase64.decode("utf-8")}

    except ValueError as val:
        return Response("Value not found inside JSON data", status=400)
    except KeyError:
        return Response("Key value error, incorrect key passed", status=400)
    except Exception as e:
        print(f"Exception: {e}")
        return Response(f"Invalid input or internal error: {e}", status=500)

    return jsonify(result)

@app.route("/live", methods=['POST'])
@cross_origin()
def liveRoute():
    global detection_process
    try:
        if detection_process is not None:
            return jsonify({"status": False, "error": "Detection is already running"}), 400

        if platform.system() == "Windows":
            detection_process = subprocess.Popen(
                ["python", "yolov5/detect.py", "--weights", "best.onnx", "--img", "640", "--conf", "0.5", "--source", "0"]
            )
        else:
            detection_process = subprocess.Popen(
                "cd yolov5 && python detect.py --weights best.onnx --img 640 --conf 0.5 --source 0",
                shell=True,
                preexec_fn=os.setsid
            )
        return jsonify({"status": True, "message": "Detection started successfully"})

    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500

@app.route("/stop", methods=['POST'])
@cross_origin()
def stopDetection():
    global detection_process
    try:
        if detection_process is None:
            return jsonify({"status": False, "error": "No detection process running"}), 400

        if platform.system() == "Windows":
            detection_process.terminate()
            detection_process.wait()
        else:
            os.killpg(os.getpgid(detection_process.pid), signal.SIGTERM)

        detection_process = None
        return jsonify({"status": True, "message": "Detection stopped successfully"})

    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT, debug=True, use_reloader=False)
