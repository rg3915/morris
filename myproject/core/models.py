from django.db import models
from django.utils.translation import ugettext_lazy as _

gender_list = [('M', 'masculino'), ('F', 'feminino')]

uf_list = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', 'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Brasília'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', 'Tocantins'),
)


class Person(models.Model):
    gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    first_name = models.CharField(_('nome'), max_length=30)
    last_name = models.CharField(_('sobrenome'), max_length=30)
    birthday = models.DateTimeField(_('nascimento'), null=True, blank=True)
    email = models.EmailField(_('e-mail'), blank=True)
    uf = models.CharField(_('UF'), max_length=2, choices=uf_list)
    active = models.BooleanField(_('ativo'), default=True)
    blocked = models.BooleanField(_('bloqueado'), default=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.first_name + " " + self.last_name

    full_name = property(__str__)
