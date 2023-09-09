from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from axes.utils import reset
from .models import Cliente


class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = "clientes"


class UserAdmin(BaseUserAdmin):
    inlines = [ClienteInline]
    actions = ["desbloquear_cuentas"]

    @admin.action(description="Desbloquear cuentas seleccionadas")
    def desbloquear_cuentas(modeladmin, request, queryset):
        for obj in queryset:
            reset(username=obj.username)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)