from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_housing_bathrooms_alter_housing_bedrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='submitted_by',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='landlord',
            name='submitted_by',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
