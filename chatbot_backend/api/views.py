from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from google.cloud import dialogflow_v2 as dialogflow
from .models import Product  # Import your product model

# Get the base directory dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construct the full path to agent.json
SERVICE_ACCOUNT_FILE = "/home/manasmehta/gig/intern/module1/ShopBot/dialogflow-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE
#


@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("query", "")

            if not user_message:
                return JsonResponse({"error": "Empty query"}, status=400)

            # Query Dialogflow
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path("shopbot-sqtp", "unique-session-id")

            text_input = dialogflow.TextInput(text=user_message, language_code="en")
            query_input = dialogflow.QueryInput(text=text_input)

            response = session_client.detect_intent(
                session=session, query_input=query_input
            )

            intent = response.query_result.intent.display_name

            if intent == "GetPrice":
                product_name = response.query_result.parameters.fields[
                    "product"
                ].string_value
                try:
                    product = Product.objects.get(name__iexact=product_name)
                    price = product.price
                    return JsonResponse(
                        {"response": f"The price of {product_name} is ₹{price}"}
                    )
                except Product.DoesNotExist:
                    return JsonResponse(
                        {"response": f"Sorry, {product_name} is not available."}
                    )

            return JsonResponse({"response": response.query_result.fulfillment_text})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
