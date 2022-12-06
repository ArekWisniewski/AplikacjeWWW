# Generated by Django 4.1.4 on 2022-12-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.TextField(max_length=64)),
                ('kraj', models.TextField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=64)),
                ('nazwisko', models.CharField(max_length=64)),
                ('miesiac_urodzenia', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1, max_length=2)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
                ('druzyna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.druzyna')),
            ],
            options={
                'verbose_name_plural': 'Osoby',
                'ordering': ['nazwisko'],
            },
        ),
    ]
