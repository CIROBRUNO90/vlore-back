# constants.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExpenseTypeChoices(models.TextChoices):
    """Tipos de gastos permitidos en el sistema"""
    # Gastos operativos
    SALARIES = 'SAL', _('Salarios')
    UTILITIES = 'UTL', _('Servicios')

    # Gastos comerciales
    MARKETING = 'MKT', _('Marketing')
    SHIPPING = 'SHI', _('Envíos')

    # Gastos administrativos
    TAXES = 'TAX', _('Impuestos')
    PLATFORM = 'PLT', _('Plataforma')

    # Gastos de inventario
    SUPPLIES = 'SUP', _('Insumos')
    LOGISTICS = 'LOG', _('Logística')

    # Otros
    OTHER = 'OTH', _('Otros')
