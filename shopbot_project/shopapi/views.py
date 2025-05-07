import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product


@csrf_exempt
def dialogflow_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        parameters = data["queryResult"]["parameters"]
        product_name = parameters.get("product")

        try:
            product = Product.objects.get(name__iexact=product_name)
            response_text = f"The {product.name} is ₹{product.price}"
        except Product.DoesNotExist:
            response_text = f"Sorry, we couldn't find the product {product_name}."

        return JsonResponse({"fulfillmentText": response_text})
