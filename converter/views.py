import requests, urllib.request, json
from bs4 import BeautifulSoup
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class CurrencyConverter(APIView):
    
    def get(self,request):
        """[converting currencies]

        Args:
            request ([GET]): [need to send from_currency, to_currency, amount]

        Returns:
            [Json]: [this api will return converted currency]
        """
        from_currency = request.GET.get('from_currency')
        to_currency = request.GET.get('to_currency')
        amount = request.GET.get('amount')
        
        if not from_currency or not to_currency or not amount:
            return Response({'message':'from_currency, to_currency, amount are required'},status=400)
        
        url = f'https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&callback=sampleCallback&apiKey=bc90e82d78f02e0aede1'
        
        response = json.loads(urllib.request.urlopen(url).read().decode("utf-8").split('(')[-1].replace(')','').replace(';',''))
        
        converted_amount = float(amount)*response[f'{from_currency}_{to_currency}']
        
        return Response({
            'from_currency':from_currency, 
            'to_currency':to_currency, 
            'amount':amount, 
            'converted_amount':converted_amount
            }, 
            status=200
        )