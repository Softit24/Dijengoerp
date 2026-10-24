from django.contrib import admin
from .models import Category, Product, StockTransaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "cost_price",
        "selling_price",
        "stock_quantity",
        "is_active",
    )
    search_fields = ("sku", "name")
    list_filter = ("category", "is_active")
    list_editable = ("selling_price", "is_active")


@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "transaction_type",
        "quantity",
        "reason",
        "created_at",
    )
    search_fields = ("product__sku", "product__name", "reason")
    list_filter = ("transaction_type", "created_at")
from .models import CompanySettings

from .models import CompanySettings

@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    list_display = ("company_name", "phone", "email", "currency")
