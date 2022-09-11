import pathlib
import PySimpleGUI as sg
import cv2

SCALE_FACTOR = 1.5

WIDTH = int(640 * SCALE_FACTOR)
HEIGHT = int(480 * SCALE_FACTOR)


def create_window():
    layout = [
        [sg.Image(key="-IMAGE-", size=(WIDTH, HEIGHT))],
        [sg.Text("Number of people found in the classroom: 0", key="-TEXT-", expand_x=True)]
    ]

    return sg.Window("Face detector", layout, finalize=True)


def main():
    current_path = pathlib.Path(__file__)
    xml_path = current_path.parent.parent / "data/haarcascade_frontalface_default.xml"
    window = create_window()
    face_cascade = cv2.CascadeClassifier(xml_path.as_posix())
    cap = cv2.VideoCapture(0)

    while True:
        event, _ = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break

        _, frame = cap.read()
        fw, fh, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7, minSize=(30, 30))

        frame = cv2.resize(frame, (int(SCALE_FACTOR*fh), int(SCALE_FACTOR*fw)))
        for x, y, w, h in faces:
            cv2.rectangle(
                frame,
                (int(SCALE_FACTOR*x), int(SCALE_FACTOR*y)),
                (int(SCALE_FACTOR*(x + w)), int(SCALE_FACTOR*(y + h))),
                (0, 255, 0),
                thickness=2)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
        window["-TEXT-"].update(f"People in the image: {len(faces)}")

    cap.release()
    window.close()


if __name__ == "__main__":
    main()
