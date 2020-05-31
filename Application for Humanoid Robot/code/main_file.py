from dialogflow_modules import get_response_from_dialogflow
from nltk_modules import output_nltk_text
from speech_api import SpeakText , listen
import cv2
from recognise_face import pre_process_image, face_detection, face_recognition_fn, display_cam , show_video
import threading
import time
import sys
from multiprocessing import Process
from threading import Thread
from queue import Queue


queue1 = Queue()
queue2 = Queue()
queue3 = Queue()
queue4 = Queue()

def face_recognition_background():

    naam = ''  
    
    while True:
        
        fram, rg_small_frame = pre_process_image()

                
        queue2.put(fram)


        
        detected_face = face_detection(rg_small_frame)

        if not queue4.empty():
            naam = queue4.get()

        queue1.put(detected_face)
        
        queue3.put(rg_small_frame)

        
        
        display_cam(naam, detected_face, fram)


        

        

def my_background_function():
    # do some stuff
    download_thread = threading.Thread(target=face_recognition_background())
    download_thread.start()



def my_forward_function():
    # do some stuff
    front_thread = threading.Thread(target=state_1())
    front_thread.start()

    

def state_1():

    

    time.sleep(1)    
    
    while True:




        

        
        time.sleep(1)
        detected_face = []

        while True:
            if queue1.empty():
                break
            detected_face = queue1.get()

        

        if len(detected_face) != 0:
            
            time.sleep(1)
            state_2()




        

def state_2():

    name_of_person = ""



    


    while True:

        
        while True:

            

            if queue1.empty() and queue2.empty() and queue3.empty():
                break


            if not queue1.empty():
                detected_face = queue1.get()


            if not queue2.empty():
                fram = queue2.get()
 

            if not queue3.empty():
                rg_small_frame = queue3.get()

    
        
        if len(detected_face) == 0:

            time.sleep(3)
            print("Bot: Goodbye " + name_of_person)
            SpeakText("Goodbye " + name_of_person)

            queue4.put("")
            state_1()

        else:

                
            if name_of_person == "":


                name_of_person = face_recognition_fn(rg_small_frame, detected_face, fram)

                queue4.put(name_of_person)


            #display_cam(name_of_person, detected_face , frame)
                #cv2.imshow('Video', frame)



            

            try:
            
                captured_text = listen()

                

                if captured_text =="terminate":

                    sys.exit()
                    

                dialog_response = get_response_from_dialogflow(captured_text)

                if dialog_response == "nltk":

                    nltk_response = output_nltk_text(name_of_person ,captured_text )

                    print("Bot: "+ nltk_response)
                    SpeakText(nltk_response)



                elif dialog_response == "clsprg":

                    print("Bot: Goodbye "+ name_of_person)
                    SpeakText("Goodbye " + name_of_person)
                    queue4.put("")
                    time.sleep(5)
                    state_1()

                else:
                    
                    print("Bot: "+ dialog_response)
                    SpeakText(dialog_response)


            except Exception:
                
                print("Bot: Could you please repeat?")
                SpeakText("Could you please repeat?")








class Example():
    def __init__(self):
        self.method_1()

    def method_1(self):

        def run(self):
            threading.Thread(target = function_a, args = (self,)).start()
            time.sleep(1)
            threading.Thread(target = function_b, args = (self,)).start()

        def function_a(self):
            face_recognition_background()


        def function_b(self):
            state_1()


        run(self)





print("Bot: Hello World!")
SpeakText("Hello World!")




Example()

while True:
    pass

# Release handle to the webcam

