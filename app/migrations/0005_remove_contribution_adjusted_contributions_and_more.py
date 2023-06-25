# Generated by Django 4.2.2 on 2023-06-21 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_contribution_newsmodel_personaldata_retirementvalue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribution',
            name='adjusted_contributions',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='workedtime',
            name='employment_period',
        ),
        migrations.RemoveField(
            model_name='workedtime',
            name='salary',
        ),
        migrations.AddField(
            model_name='contribution',
            name='current_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='contribution',
            name='indexed_contributions',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='statistic',
            name='salary_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='workedtime',
            name='employment_period_months',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workedtime',
            name='gross_salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='initial_capital',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='retirementvalue',
            name='contribution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contribution'),
        ),
        migrations.AlterField(
            model_name='retirementvalue',
            name='retirement_payment',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='retirementvalue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='months_worked',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workedtime',
            name='contribution_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
