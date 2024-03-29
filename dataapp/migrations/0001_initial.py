# Generated by Django 2.2.6 on 2019-10-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=30)),
                ('mpg', models.DecimalField(decimal_places=1, max_digits=5)),
                ('cyl', models.IntegerField()),
                ('cyl_disp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('horsep', models.DecimalField(decimal_places=1, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=6)),
                ('accel', models.DecimalField(decimal_places=1, max_digits=4)),
                ('model', models.IntegerField()),
                ('origin', models.IntegerField(choices=[(0, 'US'), (1, 'Europe'), (2, 'Japan')])),
            ],
        ),
    ]
