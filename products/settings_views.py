from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from .models import CompanySettings


def staff_required(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(staff_required, login_url="/admin/login/")
def company_settings(request):
    settings = CompanySettings.load()

    if request.method == "POST":
        company_name = request.POST.get("company_name", "").strip()
        address = request.POST.get("address", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        currency = request.POST.get("currency", "BDT").strip().upper()

        errors = []

        if not company_name:
            errors.append("Company name is required.")

        if email:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Enter a valid email address.")

        if not currency or len(currency) > 10:
            errors.append("Enter a valid currency code.")

        if errors:
            return render(request, "products/company_settings.html", {
                "settings": settings,
                "errors": errors,
            })

        settings.company_name = company_name
        settings.address = address
        settings.phone = phone
        settings.email = email
        settings.currency = currency
        settings.save()

        messages.success(request, "Company settings saved successfully.")
        return redirect("products:company_settings")

    return render(request, "products/company_settings.html", {
        "settings": settings,
        "errors": [],
    })
