from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Supplier, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "country", "city", "debt")
    list_filter = ("country", "city")
    search_fields = ("name", "email")
    ordering = ("name",)
    fields = ("name", "email", ("country", "city"), "address", "debt")
    inlines = [ProductInline]
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = (
        "Очистить задолженность перед поставщиком у выбранных объектов"
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date", "supplier_link")
    list_filter = ("release_date",)
    search_fields = ("name", "model")
    ordering = ("-release_date",)

    def supplier_link(self, obj):
        # Получение URL для редактирования объекта Supplier
        link = reverse("admin:app_supplier_change", args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier.name)

    supplier_link.short_description = "Поставщик"
