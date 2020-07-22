from django.contrib import admin
from .models import *
# Register models


admin.site.site_header = "Task Manager Administration"

# TaskAdmin is used to owerwrite default admin view for tasks
# if user is not superuser, return only those tasks that where created by that particular user
class TaskAdmin(admin.ModelAdmin):

    def get_exclude(self, request, obj=None):
        excluded = []
        # if user is not a superuser, don't show created_by option
        if not request.user.is_superuser:
            return excluded + ['created_by']

        return excluded

    def get_queryset(self, request):
        exclude = ('created_by')
        qs = super(TaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()


# AssignedTaskAdmin is used to owerwrite default admin view for assigned tasks
# if user is not superuser, return only those assigned tasks that where assigned by that particular user
class AssignedTaskAdmin(admin.ModelAdmin):
    def get_exclude(self, request, obj=None):
        excluded = []
        # if user is not a superuser, don't show assigned_by option
        if not request.user.is_superuser:
            return excluded + ['assigned_by']

        return excluded

    # only show assigned tasks that where assigned by that admin
    def get_queryset(self, request):
        qs = super(AssignedTaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(assigned_by=request.user)

    # automatically assign task to its creator
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'assigned_by', None) is None:
            obj.assigned_by = request.user
        obj.save()

    # make sure admin can assign tasks only he created
    def formfield_for_foreignkey(self, field, request, **kwargs):
        if field.name == "task":
            if not request.user.is_superuser:
                kwargs["queryset"] = Task.objects.filter(created_by=request.user.id)
        return super(AssignedTaskAdmin, self).formfield_for_foreignkey(field, request, **kwargs)


admin.site.register(Task, TaskAdmin)
admin.site.register(AssignedTask, AssignedTaskAdmin)
