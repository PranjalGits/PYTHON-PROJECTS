from keras.models import load_model
from time import sleep
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('C:/Users/hp/Desktop/PYTHON PROJECTS/emotion project/haarcascade_frontalface_default.xml')
classifier = load_model('/Emotion_detection.h5')

class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2, COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1, 3, 5)
    for (X, Y, W, H) in faces:
        cv2.rectangle(frame < (X, Y), (X + W, Y + H), (255, 0, 0), 2)
        roi_gray = gray[Y:Y + H, X:X + H]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = classifier.predict(roi)[0]
            print("\nprediction = ", preds)
            labels = class_labels[preds.argmax()]
            print("\nprediction max = ", preds.argmax())
            print("\nlabel = ", label)
            label_position = (X, Y)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0))

        else:
            cv2.putText(frame, 'no face found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0))


        print("\n\n")
    cv2.imshow('emotion detector', frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





