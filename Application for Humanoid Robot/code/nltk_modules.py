
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import wikipedia
from nltk.corpus import stopwords
from file_handling import read_file, write_file



stop_words = set(stopwords.words('english'))

#############################################################################

def get_from_wikipedia(tokenised_word):

    try:

        filtered_sentence = []

        text = ""
        for w in tokenised_word:
            if w not in stop_words:
                filtered_sentence.append(w)
        
        for i in range(len(filtered_sentence)):
            text = text + " " + filtered_sentence[i]
        
        final_text = wikipedia.summary(text, sentences=2)

    except:

        final_text = "Can you be more specific? "
    
    return(final_text)


########################################################################

def decide_intent(token):
    
    key = 0
    
    ques = 0

    for i in token:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        

        k=tagged[0]
        decide = k[-1]

        if decide =="WP":
            ques = 1

        if decide == "PRP$" or decide == "PRP":
            

            if k[0] == "my":

                

                if ques == 1:
                    
                    key = 1    # user question

                else:
                    
                    key = 2    # use statement

            else:
                
                key = 3        # bot question

            
    return (key)


    
####################################################################################


def ask_personal_question(name,token):
    
    for i in token:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        
        

        k=tagged[0]
        decide = k[-1]

        if decide == "NN" or decide == "NNS":

            query = k[0]
            
    output_text = read_file (name, query)
    

    return (output_text)


############################################################################################

def note_user_info(name,token):
    
    count = 0
    entity = ""
    for i in token:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)



        k=tagged[0]
        decide = k[-1]

        if decide == "VBZ" or decide == "VBP":

            query = token[ count - 1]

            for j in range (count +1 , len(token)):

                entity = entity + " " + token[j]

            
        count = count +1
                


    write_file(name, query, entity )



#################################################################################################

def output_nltk_text( name, sentence):

    text_op = ""

    token = word_tokenize(sentence)

    key = decide_intent(token)
    
    if (key == 1):

        print("User asked Question on himself ")

        
        text_op = ask_personal_question(name,token)
        



        
    elif (key == 2):
        

        note_user_info(name,token)

        text_op = "I have saved your information"
        

        

    elif (key == 3 ):
        
        

        text_op = ask_personal_question("bot",token)
        


        
    else:
        print(" ")
        print("Searching wikipedia for answer")
        print(" ")
        text_op = get_from_wikipedia(token)



    return (text_op)
    

###############################################################################################



def get_name(input_text):


    tokenized_word = word_tokenize(input_text)

    filtered_sentence = []

    text = ""
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sentence.append(w)
    
    for i in range(len(filtered_sentence)):

        if (filtered_sentence[i] != "name"):
            text = text + " " + filtered_sentence[i]


    text = text[1: ]

    return (text)



