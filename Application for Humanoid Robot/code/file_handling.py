from nltk.tokenize import sent_tokenize, word_tokenize

def read_file (entity, query):

    
    f=open("known_people_data/" + entity +".txt", 'r')
    file_data = f.readlines()
    text=""
    found = 0


    
    for i in file_data:

        
        line = word_tokenize(i)
        
        if line[0] == query:
            for j in range (2, len(line) ):
                text = text + " " + line[j]
                found = 1

    f.close()

    if found ==0:

        text = "i don't know"

    return(text)

        




def write_file(name, query, entity ) :
    
    
    f= open("known_people_data/" +name+".txt","a+")
    f.write(query + " " + ":" + " " + entity + "\n")

    f.close()




