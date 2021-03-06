# Generated by Django 2.1.7 on 2019-08-05 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandexecution',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adhocrunhistory',
            name='adhoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='ops.AdHoc'),
        ),
        migrations.AddField(
            model_name='adhocrunhistory',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='ops.Task'),
        ),
        migrations.AddField(
            model_name='adhoc',
            name='hosts',
            field=models.ManyToManyField(to='assets.Asset', verbose_name='Host'),
        ),
        migrations.AddField(
            model_name='adhoc',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adhoc', to='ops.Task'),
        ),
    ]
