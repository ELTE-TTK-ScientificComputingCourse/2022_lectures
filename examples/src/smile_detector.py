import cv2
import numpy as np
import pathlib
import PySimpleGUI as sg
import tensorflow as tf

from collections import deque

WIDTH = 640
HEIGHT = 480

FOLDER = pathlib.Path(__file__).parent.parent / "data"

SMILEY_FACE = FOLDER / "smiley_face.png"
NEUTRAL_FACE = FOLDER / "neutral_face.png"


def create_window():
    layout = [
        [
            sg.Image(key="-IMAGE-", size=(WIDTH, HEIGHT)),
            sg.Image(source=NEUTRAL_FACE.as_posix(), key="-PREDICTION-", subsample=2)
        ]
    ]

    return sg.Window("Smile detector", layout, finalize=True)


def main():
    window = create_window()
    xml_path = FOLDER / "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(xml_path.as_posix())
    recent_predictions = deque(maxlen=10)
    model = tf.keras.models.load_model(FOLDER / "smiles.h5")
    cap = cv2.VideoCapture(0)

    while True:
        event, _ = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break

        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7, minSize=(30, 30))
        if len(faces) == 1:
            x, y, w, h = faces[0]
            cropped = gray[y:y+h, x:x+w]
            model_input = np.expand_dims(cv2.resize(cropped, (64, 64)), axis=0) / 255.0
            p = float(np.squeeze(model.predict(model_input, verbose=0)))
            verdict = int(p >= 0.5)
            recent_predictions.append(verdict)

            if sum(recent_predictions) >= 7:
                window["-PREDICTION-"].update(source=SMILEY_FACE.as_posix(), subsample=2)
            else:
                window["-PREDICTION-"].update(source=NEUTRAL_FACE.as_posix(), subsample=2)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    cap.release()
    window.close()


if __name__ == "__main__":
    main()
