from myproject.core.models import Person
from django.db.models import Count

''' pessoas por uf '''
p = Person.objects.values('uf').annotate(
    quant=Count('uf')).order_by('uf').values('uf', 'quant')
[print(i) for i in p]

''' porcentagem de gender '''
genders = Person.objects.values('gender').annotate(
    quant=Count('gender')).order_by('gender')
total_items = Person.objects.count()
items = [{'gender': g['gender'], 'value': g['quant'] * 100 / total_items}
         for g in genders]
[print(i) for i in items]
