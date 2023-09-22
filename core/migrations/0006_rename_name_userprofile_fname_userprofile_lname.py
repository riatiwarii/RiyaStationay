# Generated by Django 4.2.3 on 2023-07-31 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userprofile_delete_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
