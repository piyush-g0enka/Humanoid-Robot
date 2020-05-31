
def show_video():
    while True:
        ret, frame = video_capture.read()
        frame = cv2.flip( frame , 1 )
        cv2.imshow('Video', frame)
        cv2.waitKey(100)



def display_cam(face_names, face_locations, frame):
    # Display the results
    frame_1 = frame
    for (top, right, bottom, left) in (face_locations):

        
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame_1, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame_1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame_1, face_names, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        
    # Display the resulting image
    cv2.imshow('Video', frame_1)
    cv2.waitKey(1)





    

    
def initialize_face_recognition():


 

              
    #make an array of all the saved jpg files' paths
    list_of_files = [f for f in glob.glob(path+'*.jpg')]
    #find number of known faces
    number_files = len(list_of_files)

    names = list_of_files.copy()

    
    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        known_face_encodings.append(globals()['image_encoding_{}'.format(i)])

        # Create array of known names
        names[i] = names[i].replace(dirname + "\known_people_images" , "")
        
        names[i] = names[i][1:-4]
        
        known_face_names.append(names[i])



    return ()




def pre_process_image():

    
        # Grab a single frame of video
    ret, frame = video_capture.read()
    frame = cv2.flip( frame , 1 )

        # Resize frame of video to 1/4 size for faster face recognition processing

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]


    return (frame, rgb_small_frame)





def face_detection(rgb_small_frame):
 
    face_locations = face_recognition.face_locations(rgb_small_frame)


    return(face_locations)


def face_recognition_fn(rgb_small_frame, detected_face_locations, frame):


    # Initialize some variables
    
    face_encodings = []
    face_names = []
    unknown_count = 0
    name_count = 0
    previous_name = ""
    name_reset = 0

    
    face_encodings = face_recognition.face_encodings(rgb_small_frame, detected_face_locations)

    face_names = []

    
    for face_encoding in face_encodings:
        
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        
        
        best_match_index = np.argmin(face_distances)
        

        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        
        if name != "Unknown":
            print("Bot: Hello " + name)
            SpeakText("Hello " + name)

            return(name)
            
            
    
        else: 
            print("Bot: Hey Stranger. What is your name?")
            SpeakText("Hey Stranger. What is your name?")
            MyText = listen()
            
            name_text = get_name(MyText)

            ret, fr = video_capture.read()
            fr = cv2.flip( fr , 1 )
            
            

            
            cv2.imwrite(path + name_text + ".jpg", fr)
            known_face_encodings.append(face_encoding)
            known_face_names.append(name_text)
            write_file(name_text, "name", name_text )
            print("Bot: Hello "  + name_text + ". Nice to meet you!")
            SpeakText("Hello "  + name_text + " Nice to meet you!")
            return(name_text)            
                     
##########################################################################################


import face_recognition
import cv2
import numpy as np
import os
import glob
import time
from speech_api import SpeakText, listen
from nltk_modules import get_name
from file_handling import write_file


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)




known_face_encodings = []
known_face_names = []
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'known_people_images/')

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

initialize_face_recognition()





