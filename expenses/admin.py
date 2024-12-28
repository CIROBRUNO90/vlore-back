from django.contrib import admin
from django.db.models import Sum
from django.utils.html import format_html

from .models import Expenses


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    # Configuramos qué campos se muestran en la lista principal
    list_display = [
        'date',
        'expense_type_display',  # Método personalizado para mostrar el tipo
        'amount_display',        # Método personalizado para el monto
        'observations'
    ]

    list_filter = [
        'date',
        'expense_type'
    ]

    search_fields = [
        'observations',
        'expense_type'
    ]

    fieldsets = (
        ('Información Principal', {
            'fields': ('date', 'expense_type', 'amount')
        }),
        ('Detalles Adicionales', {
            'fields': ('observations',),
            'classes': ('collapse',)  # Hace esta sección colapsable
        })
    )

    ordering = ['-date']
    list_per_page = 20

    def expense_type_display(self, obj):
        """
        Mejora la visualización del tipo de gasto con un código de colores,
        ajustando automáticamente el color del texto para máxima legibilidad.
        """
        colors = {
            'MKT': '#FF9999',  # Rojo claro para Marketing
            'LOG': '#99FF99',  # Verde claro para Logística
            'PLT': '#9999FF',  # Azul claro para Plataforma
            'SUP': '#FFFF99',  # Amarillo claro para Insumos
            'UTL': '#FF99FF',  # Rosa claro para Servicios
            'TAX': '#99FFFF',  # Cyan claro para Impuestos
            'SAL': '#FFB366',  # Naranja claro para Salarios
            'SHI': '#B366FF',  # Púrpura claro para Envíos
            'OTH': '#E6E6E6'   # Gris claro para Otros
        }

        def get_text_color(bg_color):
            """
            Determina si el texto debe ser negro o blanco basado en el color de fondo.
            Utiliza la fórmula de luminosidad relativa (percepción humana de brillo).
            """
            # Convierte el color hexadecimal a RGB
            bg_color = bg_color.lstrip('#')
            r = int(bg_color[0:2], 16)
            g = int(bg_color[2:4], 16)
            b = int(bg_color[4:6], 16)

            # Calcula la luminosidad usando la fórmula de luminosidad relativa
            # Los coeficientes representan cómo el ojo humano percibe cada color
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

            # Si la luminosidad es mayor a 0.5, el fondo es claro y necesitamos texto oscuro
            return '#000000' if luminance > 0.5 else '#FFFFFF'

        bg_color = colors.get(obj.expense_type, '#E6E6E6')
        text_color = get_text_color(bg_color)

        return format_html(
            '<div class="expense-type-container">'
            '<span style="background-color: {}; color: {}; padding: 4px 12px; '
            'border-radius: 4px; display: inline-block; min-width: 100px; '
            'text-align: center; font-weight: 500;">{}</span>'
            '</div>',
            bg_color,
            text_color,
            obj.get_expense_type_display()
        )
    expense_type_display.short_description = 'Tipo de Gasto'

    def amount_display(self, obj):
        """
        Formatea el monto con color según su valor y alineación correcta
        """
        formatted_amount = "${:,.2f}".format(float(obj.amount))
        return format_html(
            '<div class="amount-cell" style="color:{};">{}</div>',
            'red' if obj.amount > 1000 else 'green',
            formatted_amount
        )
    amount_display.short_description = 'Monto'

    def changelist_view(self, request, extra_context=None):
        """
        Añade estadísticas al pie de la lista de gastos
        """
        response = super().changelist_view(request, extra_context)

        # Solo modificamos la respuesta si no es un popup
        if hasattr(response, 'context_data') and not request.GET.get('_popup'):
            queryset = self.get_queryset(request)
            total_amount = queryset.aggregate(total=Sum('amount'))['total'] or 0

            # Agregamos el total al contexto
            response.context_data['total_amount'] = total_amount

        return response

    class Media:
        """
        Añadimos estilos personalizados para mejorar la visualización
        """
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
