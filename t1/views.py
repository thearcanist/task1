from django.shortcuts import render
from rest_framework import generics
from serializers import TupleSerializer
from models import Tuple

from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("First Proper Django app")

class TupleList(generics.ListCreateAPIView):
      queryset = Tuple.objects.all()
      serializer_class = TupleSerializer
class TupleDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Tuple.objects.all()
      serializer_class=TupleSerializer
