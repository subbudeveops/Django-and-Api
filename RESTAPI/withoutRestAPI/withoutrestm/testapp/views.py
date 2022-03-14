from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from dataclasses import fields
from django.shortcuts import render
from django.views.generic import View
import json
from testapp.models import Student
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin, HttpResponseMixins
from testapp.utils import is_json
from .forms import Studentform
# Create your views here.


class StudentDetailCBV(HttpResponseMixins, SerializeMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            st = Student.objects.get(id=id)
        except Student.DoesNotExist:
            json_data = json.dumps({'msg': 'This site cant reached'})
            return self.render_to_http_response(json_data, status=400)
        else:
            json_data = self.Mymethod([st, ])
        return self.render_to_http_response(json_data)


@method_decorator(csrf_exempt, name='dispatch')
class StudentListCBV(HttpResponseMixins, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        st = Student.objects.all()
        json_data = self.Mymethod(st)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data'})
            return self.render_to_http_response(json_data, status=400)

        empdata = json.loads(data)
        form = Studentform(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
