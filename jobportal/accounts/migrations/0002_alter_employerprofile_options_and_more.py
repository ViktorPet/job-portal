# Generated by Django 5.1 on 2025-05-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employerprofile',
            options={'verbose_name': 'Employer Profile', 'verbose_name_plural': 'Employer Profiles'},
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_address_postcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_address_street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_address_town',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_eik',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_picture',
            field=models.ImageField(blank=True, upload_to='company_pictures/'),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='type_of_business',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_employee_photos/'),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='company_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='logo',
            field=models.ImageField(blank=True, upload_to='company_logos/'),
        ),
    ]
