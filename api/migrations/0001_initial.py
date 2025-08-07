from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('nacion', models.CharField(blank=True, max_length=30, null=True)),
                ('biogra', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
