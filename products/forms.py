from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        labels = {
            "cost_price": "Cost price (Tk)",
            "selling_price": "Sell price (Tk)",
        }
        model = Product
        fields = [
            "sku",
            "name",
            "category",
            "unit",
            "cost_price",
            "selling_price",
            "stock_quantity",
            "reorder_level",
            "is_active",
        ]


from .models import StockTransaction


class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = [
            "product",
            "transaction_type",
            "quantity",
            "reason",
        ]


from .models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["product", "quantity", "unit_price", "notes"]
        labels = {
            "unit_price": "Unit price (Tk)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"].queryset = Product.objects.filter(
            is_active=True
        ).order_by("name")
        self.fields["quantity"].min_value = 1
        self.fields["unit_price"].min_value = 0.01
