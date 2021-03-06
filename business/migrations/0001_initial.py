# Generated by Django 2.2.4 on 2019-08-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BecomeAnAffiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=50)),
                ('contact_phone_number', models.CharField(max_length=15)),
                ('tell_us_about_you', models.CharField(choices=[('', 'select'), ('Manufacturer', 'Manufacturer'), ('Wholesaler', 'Wholesaler')], default='select', max_length=50)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('contact_address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=70)),
                ('state', models.CharField(blank=True, max_length=70)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
    ]
