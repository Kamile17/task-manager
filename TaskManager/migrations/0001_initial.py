# Generated by Django 3.0.7 on 2020-07-21 17:21

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User
import django.db.models.deletion


def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name=u'Admin'),
    ])
    User.objects.create_superuser('admin', os.getenv('ADMIN_PASSWORD'))


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(apply_migration),
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='not_completed', max_length=50, null=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200, null=True)),
                ('task_description', models.TextField(max_length=3000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ManyToManyField(through='TaskManager.AssignedTask', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignedtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskManager.Task'),
        ),
        migrations.AddField(
            model_name='assignedtask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='assignedtask',
            unique_together={('user', 'task')},
        ),
    ]
