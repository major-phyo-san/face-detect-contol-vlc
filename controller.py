import cv2
import vlc
from time import sleep


class Controller:
    def __init__(self):
        self.player = None
        self.face_present = True

    def initiate_player(self, filePath):
        self.player = vlc.MediaPlayer(filePath)

    def player_start(self):
        self.player.play()
        sleep(3)
        while True:
            self.face_detect()

    def player_close(self):
        self.player.stop()

    def face_detect(self):
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        video_capture = cv2.VideoCapture(0)
        global count
        count = 1
        while True:
            if not video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('Video', frame)

            if len(faces) == 0:
                print("No face detected")
                face_detected = False

                if count == 1:
                    count = 0
            else:
                print("Face detected")
                face_detected = True

                if count == 0:
                    count = 1
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
        print('end')
