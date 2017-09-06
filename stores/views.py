from django.shortcuts import render
from stores.models import Stores, Brand, municipality
from django.db.models import Count


def stores_list(request):
  seznam = Stores.objects.all()
  return render(request, 'seznam.html', {'seznam':seznam})

  