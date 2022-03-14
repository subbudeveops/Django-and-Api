from testapp.mixins import HttpResponseMixin
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.


def emp_data_json(request):
    emp_data = {
        'eno': 100,
        'ename': 'subbu',
        'esal': 1000,
        'eaddr': 'saravapalli',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')


def emp_data_json2(request):
    emp_data = {
        'eno': 100,
        'ename': 'subbu',
        'esal': 1000,
        'eaddr': 'saravapalli',
    }

    return JsonResponse(emp_data)


class jsonCBView(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is json get method'})
        return self.return_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is json post method'})
        return self.return_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is json put method'})
        return self.return_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is json delete method'})
        return self.return_to_http_response(json_data)
