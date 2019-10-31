import cv2
import vlc
from time import sleep
import keyboard


class Controller:
    def __init__(self):
        self.face_detected = False
        self.player = None
        self.cascPath = "haarcascade_frontalface_default.xml"
        self.faceCascade = None
        self.video_capture = None

    def initiate_player(self, filePath):
        self.player = vlc.MediaPlayer(filePath)
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.video_capture = cv2.VideoCapture(0)

    def face_detector(self):
        global count
        count = 1
        if not self.video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass
        ret, frame = self.video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        if len(faces) == 0:
            print("No face detected")
            self.face_detected = False
        else:
            print("Face detected")
            self.face_detected = True
            if count == 0:
                    keyboard.press_and_release('space')
                    count = 1
        if cv2.waitKey(1) & 0xff == ord('q'):
            cv2.destroyAllWindows()
        return self.face_detected

    def player_start(self):
        while True:
            if self.face_detector():
                self.player.play()
            else:
                if self.player.is_playing():
                    self.player.pause()
                else:
                    pass

    def player_close(self):
        self.player.stop()
        self.video_capture.release()