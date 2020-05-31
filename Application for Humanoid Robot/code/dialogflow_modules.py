

import dialogflow
from google.api_core.exceptions import InvalidArgument
import os


dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'dialogflow_key/')
key_name = os.listdir(path)

DIALOGFLOW_PROJECT_ID = 'diya-2-0-dewvwo'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = path + key_name[0]          

SESSION_ID = 'me2'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


def get_response_from_dialogflow(text_to_be_analyzed ):

    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    output_text = ""
    
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    #print("Query text:", response.query_result.query_text)
    #print("Detected intent:", response.query_result.intent.display_name)
    #print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    #print("Fulfillment text:", response.query_result.fulfillment_text)

    
    if response.query_result.intent.display_name == "Default Fallback Intent":
        
        
        output_text = "nltk"
        
    elif response.query_result.intent.display_name == "Goodbye":

        output_text = "clsprg"

    else:

        output_text = response.query_result.fulfillment_text
        

    return(output_text)
        

