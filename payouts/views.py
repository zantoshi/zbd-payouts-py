from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import json

from .util import *
import environ

env = environ.Env()
callback_url = env('ZEBEDEE_API_KEY')



def index(request):

    return render(request, "payouts/index.html")

def pay(request):
    if request.POST:
        payload = request.POST.dict()
        
        ln_addresses = []
        payout = []
        for key, value in payload.items():
            if 'csrf' not in key:
                if int(key[-1]): 
                    payout.append(value)
                    if 'amount' in key:
                        ln_addresses.append(payout)
                        payout = []

        for payout in ln_addresses:
            pay_to_ln_address(apikey, payout[0], payout[1])

        ctx = {
            "ln_addresses" : ln_addresses
        }

        return render(request, "payouts/success.html", ctx)
    else:
        return render(redirect('home'))

def withdraw(request):
    withdrawal = get_withdrawal(apikey)
    ctx = { "w" : withdrawal }
    return render(request, "payouts/withdrawal.html", ctx)


def callback(request):
    data = json.loads(request.body)
    print (data)
    return HttpResponse(True)