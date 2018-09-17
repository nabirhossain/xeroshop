from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id])))

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Invoice'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    pass

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ['id', order_pdf, 'first_name', 'last_name', 'email', 'mobile',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    pass

"""
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
"""
"""
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
"""
