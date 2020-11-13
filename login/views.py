from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.
class LoginIndexView(View):
   def get(self, request):
       return render(request, 'login/index.html')
   def post(self, request):
     return JsonResponse(request.POST, json_dumps_params = {'indent': 4})