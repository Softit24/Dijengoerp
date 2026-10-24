from django.urls import path
from . import views, settings_views

app_name = "products"

urlpatterns = [
    path("settings/", settings_views.company_settings, name="company_settings"),

    path("sales/dashboard/", views.sales_dashboard, name="sales_dashboard"),
    path("sales/export/pdf/", views.sales_export_pdf, name="sales_export_pdf"),
    path("sales/export/excel/", views.sales_export_excel, name="sales_export_excel"),
    path("sales/report/", views.sales_report, name="sales_report"),
    path("sales/", views.sale_create, name="sale_create"),
    path("inventory/transactions/", views.stock_transaction_create, name="stock_transaction_create"),

    path("", views.dashboard, name="dashboard"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/add/", views.category_create, name="category_create"),
    path("categories/<int:pk>/edit/", views.category_edit, name="category_edit"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),
]
