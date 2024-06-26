# Generated by Django 4.2 on 2024-04-04 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multitenancy', '0006_alter_tenantmembership_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantmembership',
            name='creator',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='created_tenant_memberships',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
