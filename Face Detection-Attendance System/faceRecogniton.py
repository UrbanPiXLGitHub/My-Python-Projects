import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Detector:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1366x768")
        # self.root.title("Face Recognition System")



        # root = Tk()
        # root.geometry("1366x768")
        # root.title("Face Recognition System")

        video_capture = cv2.VideoCapture(0)

        myimage1_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\myimage1.jpg")
        myimage1_encoding = face_recognition.face_encodings(myimage1_image)[0]

        einstein_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\albert einstein.jpg")
        einstein_encoding = face_recognition.face_encodings(einstein_image)[0]

        elon_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\elon musk.jpg")
        elon_encoding = face_recognition.face_encodings(elon_image)[0]

        nikola_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\nikola tesla.jpg")
        nikola_encoding = face_recognition.face_encodings(nikola_image)[0]

        sundar_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\sundar pichai.jpg")
        sundar_encoding = face_recognition.face_encodings(sundar_image)[0]
        
        magnus_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\magnus carlsen.jpg")
        magnus_encoding = face_recognition.face_encodings(magnus_image)[0]
        
        chris_image = face_recognition.load_image_file("D:\\VScodes\\Python\\attendanceface\\chris hemsworth.jpg")
        chris_encoding = face_recognition.face_encodings(chris_image)[0]

        known_face_encoding = [
        myimage1_encoding,
        einstein_encoding,
        elon_encoding,
        sundar_encoding,      
        nikola_encoding,
        magnus_encoding,
        chris_encoding
        ]

        known_faces_names = [
        "Jayesh",
        "Einstein",
        "Elon Musk",
        "Sundar",
        "Nikola",
        "Magnus",
        "Chris"
        ]

        students = known_faces_names.copy()
        print(students)

        face_locations = []
        face_encodings = []
        face_names = []
        s=True

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")

        f = open(current_date+'.csv','w+',newline='')
        lnwriter = csv.writer(f)

        while True:
            _,frame = video_capture.read()
            small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = small_frame[:,:,::-1]
            if s:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                    name = ""
                    face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = known_faces_names[best_match_index]

                    face_names.append(name)
                    if name in known_faces_names:
                        if name in students:
                            students.remove(name)
                            print(students)
                            current_time = now.strftime("%H-%M-%S")
                            lnwriter.writerow([name,current_time])
            cv2.imshow("attendance system",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        video_capture.release()
        cv2.destroyAllWindows()
        f.close()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Detector(root)
    root.mainloop()

# root.mainloop() 