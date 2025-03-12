import json
import google.cloud.dialogflow_v2 as dialogflow
from google.oauth2 import service_account
from django.conf import settings
import os
from google.oauth2 import service_account

# Load Dialogflow credentials
DIALOGFLOW_PROJECT_ID = "shopbot-sqtp"
DIALOGFLOW_LANGUAGE_CODE = "en"


# Get the base directory dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construct the full path to agent.json
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "ShopBot", "agent.json")

# Debug: Check if the file exists
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    raise FileNotFoundError(f"Service account file not found: {SERVICE_ACCOUNT_FILE}")

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)
session_client = dialogflow.SessionsClient(credentials=credentials)


def get_dialogflow_response(session_id, text):
    """Sends a message to Dialogflow and returns the response."""
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)

    text_input = dialogflow.types.TextInput(
        text=text, language_code=DIALOGFLOW_LANGUAGE_CODE
    )
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text  # Get chatbot response
