from django.shortcuts import render
import stripe,json
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from Product.models import Product
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_PRIVATE_KEY

''' Landing Page '''
def product_Landing_View(request):
    productList = Product.objects.all().values()
    key = settings.STRIPE_PUBLIC_KEY
    # print(key)
    # print(list(productList))
    # print(len(productList))
    return render(request,'landing.html',{'dict_Data':list(productList),'count':range(1,len(productList)+1),"key":key})

class success(TemplateView):
    template_name = 'success.html'

class cancel(TemplateView):
    template_name = 'cancel.html'

@csrf_exempt
def check_Out(request):
    a = request.body.decode('utf-8')
    body = json.loads(a)
    productId = body['productId']
    getProductDetails = Product.objects.get(productId=productId)
    dis_price = int(getProductDetails.productPrice)*100
    # print(dis_price)
    # print(getProductDetails.get_display_price)
    # print(getProductDetails.get_display_price.__self__)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [
            {
                'price_data': {
                    'currency': 'INR',
                    'unit_amount': dis_price,
                    'product_data': {
                        'name': getProductDetails.productName,
                    },
                },
                'quantity': 1,
            },
        ],
        mode = 'payment',
        success_url = settings.YOUR_DOMAIN + '/success/',
        cancel_url = settings.YOUR_DOMAIN + '/cancel/',
    )

    return JsonResponse({'id':checkout_session.id})
