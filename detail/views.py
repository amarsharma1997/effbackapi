from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from detail.models import BankDetails
import json
from django.forms.models import model_to_dict
# Create your views here.

def simple_view(request):
    return render(request,'detail/front.html',{})

def Banklist(request):
    bank = request.GET['bank']
    city = request.GET['city']
    if(( bank == '' ) or (city == '')):
        return render(request, 'detail/front.html', {})
    else:
        list = BankDetails.objects.filter(bank_name__iexact=bank).filter(city__iexact=city)
        if not list:
            return HttpResponse('There is no Bank with these details')
        dct={}
        i=1
        for lst in list.values():
            dct[i]=lst
            i=i+1
        return JsonResponse(dct,safe=False)

def Bank(request):
    ifsc = request.GET['ifsc']
    if (ifsc== ''):
        return render(request, 'detail/front.html', {})
    else:
        list = BankDetails.objects.filter(ifsc__iexact=ifsc)
        if not list :
            return HttpResponse('There is no Bank with this IFSC code')
        return JsonResponse(list.values()[0],safe=False)