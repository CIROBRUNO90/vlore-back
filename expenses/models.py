from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import ExpenseTypeChoices
from vlore_back.models import TimestampsMixin


class Expenses(TimestampsMixin):

    date = models.DateField(
        verbose_name=_('Fecha del gasto'),
        help_text=_('Fecha en que se realizó el gasto')
    )

    expense_type = models.CharField(
        max_length=3,
        choices=ExpenseTypeChoices.choices,
        default=ExpenseTypeChoices.OTHER,
        verbose_name=_('Tipo de gasto'),
        help_text=_('Categoría o tipo de gasto realizado')
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Monto'),
        help_text=_('Monto total del gasto')
    )

    observations = models.TextField(
        blank=True,
        verbose_name=_('Observaciones'),
        help_text=_('Observaciones o notas adicionales sobre el gasto')
    )

    class Meta:
        verbose_name = _('Gasto')
        verbose_name_plural = _('Gastos')
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_expense_type_display()} - {self.date} - ${self.amount}"
