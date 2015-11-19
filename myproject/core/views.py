import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Person
from django.db.models import Count


def index(request):
    return render(request, "index.html")


def download(request):
    return render(request, "download.html")


def about(request):
    return render(request, "about.html")


def morris(request):
    return render(request, "core/morris.html")


def morris_dataview(request):
    return render(request, "core/morris_data.html")


def uf_json(request):
    data = Person.objects.values('uf').annotate(
        quant=Count('uf')).order_by('uf').values('uf', 'quant')
    s = json.dumps(list(data), cls=DjangoJSONEncoder)
    # s = serializers.serialize('json', data, fields=('uf', 'quant'))
    return HttpResponse(s)


class PersonsUFView(TemplateView):
    template_name = 'core/persons_by_uf.html'
    model = Person

    def get_context_data(self, **kwargs):
        ''' pessoas por uf '''
        q = Person.objects.values('uf').annotate(
            quant=Count('uf')).order_by('uf').values('uf', 'quant')

        ''' porcentagem de gender '''
        genders = Person.objects.values('gender').annotate(
            quant=Count('gender')).order_by('gender')
        total_items = Person.objects.count()
        genders = [
            {'gender': g['gender'], 'value': int(g['quant'] * 100 / total_items)} for g in genders]

        context = super(PersonsUFView, self).get_context_data(**kwargs)
        context['itens'] = q
        context['genders'] = genders
        return context

# porcentagem de active
# por faixa etária 10 em 10
