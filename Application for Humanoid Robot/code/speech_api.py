# Python program to translate 
# speech to text and text to speech 


import speech_recognition as sr 
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 



# Function to convert text to speech 
def SpeakText(command): 
	
        # Initialize the engine 
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say(command) 
        engine.runAndWait() 
	
	
# Loop infinitely for user to 
# speak 


def listen():

        while True:	
                # Exception handling to handle 
                # exceptions at the runtime
                
                try: 
                        
                        # use the microphone as source for input. 
                        with sr.Microphone() as source2: 
                                
                                # wait for a second to let the recognizer 
                                # adjust the energy threshold based on 
                                # the surrounding noise level
                                
                                r.adjust_for_ambient_noise(source2, duration=0.5)

                                print(" ")
                                print("Speak Now ...")
                                
                                #listens for the user's input 
                                audio2 = r.listen(source2) 
                                
                                # Using ggogle to recognize audio
                                
                                MyText = r.recognize_google(audio2) 
                                MyText = MyText.lower() 

                                print("User: "+MyText) 
                                
                                break
                                
                except sr.RequestError as e: 
                        print("Check Internet Connection")
                        SpeakText("Check Internet Connection")
                        
                        
                except sr.UnknownValueError: 
                        print("Bot: Could you repeat?")
                        SpeakText("Could you repeat?")
                        
		
        return MyText
