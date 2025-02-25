# Generated by Django 5.0 on 2025-02-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=30, verbose_name='Número de orden')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('order_status', models.CharField(choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada'), ('cancelada', 'Cancelada')], default='abierta', max_length=20, verbose_name='Estado de la orden')),
                ('payment_status', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20, verbose_name='Estado del pago')),
                ('shipping_status', models.CharField(choices=[('no_empaquetado', 'No está empaquetado'), ('empaquetado', 'Empaquetado'), ('enviado', 'Enviado'), ('entregado', 'Entregado')], default='no_empaquetado', max_length=20, verbose_name='Estado del envío')),
                ('currency', models.CharField(max_length=3, verbose_name='Moneda')),
                ('product_subtotal', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Subtotal de productos')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Descuento')),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Costo de envío')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total')),
                ('buyer_name', models.CharField(max_length=255, verbose_name='Nombre del comprador')),
                ('tax_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='DNI / CUIT')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
                ('shipping_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre para el envío')),
                ('shipping_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono para el envío')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('address_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número')),
                ('floor_apt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Piso')),
                ('locality', models.CharField(blank=True, max_length=100, null=True, verbose_name='Localidad')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad')),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Código postal')),
                ('state_province', models.CharField(blank=True, max_length=100, null=True, verbose_name='Provincia o estado')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='País')),
                ('shipping_method', models.CharField(blank=True, max_length=255, null=True, verbose_name='Medio de envío')),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medio de pago')),
                ('discount_coupon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cupón de descuento')),
                ('buyer_notes', models.TextField(blank=True, null=True, verbose_name='Notas del comprador')),
                ('seller_notes', models.TextField(blank=True, null=True, verbose_name='Notas del vendedor')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Fecha de pago')),
                ('shipping_date', models.DateField(blank=True, null=True, verbose_name='Fecha de envío')),
                ('product_name', models.CharField(max_length=255, verbose_name='Nombre del producto')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Precio del producto')),
                ('product_quantity', models.PositiveIntegerField(verbose_name='Cantidad del producto')),
                ('sku', models.CharField(blank=True, max_length=50, null=True, verbose_name='SKU')),
                ('channel', models.CharField(blank=True, max_length=50, null=True, verbose_name='Canal')),
                ('tracking_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código de tracking del envío')),
                ('payment_transaction_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Identificador de la transacción en el medio de pago')),
                ('order_id', models.CharField(max_length=50, unique=True, verbose_name='Identificador de la orden')),
                ('is_physical_product', models.BooleanField(default=True, verbose_name='Producto Físico')),
                ('registered_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Persona que registró la venta')),
                ('sales_branch', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sucursal de venta')),
                ('seller', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vendedor')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'ordering': ['-date'],
                'indexes': [models.Index(fields=['order_number'], name='incomes_inc_order_n_88f5d6_idx'), models.Index(fields=['email'], name='incomes_inc_email_e6ccff_idx'), models.Index(fields=['date'], name='incomes_inc_date_e0bc36_idx'), models.Index(fields=['order_status'], name='incomes_inc_order_s_f883ab_idx'), models.Index(fields=['payment_status'], name='incomes_inc_payment_6ca58e_idx'), models.Index(fields=['shipping_status'], name='incomes_inc_shippin_a195d0_idx'), models.Index(fields=['buyer_name'], name='incomes_inc_buyer_n_f1e017_idx'), models.Index(fields=['order_id'], name='incomes_inc_order_i_f75942_idx')],
            },
        ),
    ]
