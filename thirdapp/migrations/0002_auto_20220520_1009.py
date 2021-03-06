# Generated by Django 3.2.5 on 2022-05-20 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sido', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('medical', models.IntegerField(default=0)),
                ('room', models.IntegerField(default=0)),
                ('tel', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JejuOlle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=10, null=True)),
                ('course_name', models.CharField(max_length=20, null=True)),
                ('distance', models.FloatField()),
                ('time_info', models.CharField(max_length=10, null=True)),
                ('start_end_info', models.CharField(max_length=30, null=True)),
                ('cre_date', models.DateField()),
            ],
            options={
                'db_table': 'jeju_olle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'animal',
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=14)),
                ('loc', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'owner',
            },
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_nm', models.CharField(max_length=50, null=True)),
                ('period', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'warranty',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirdapp.animal')),
                ('warranty', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirdapp.warranty')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Playground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('animals', models.ManyToManyField(null=True, to='thirdapp.Animal')),
            ],
            options={
                'db_table': 'playground',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=9)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateTimeField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('dept', models.ForeignKey(db_column='deptno', null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirdapp.dept')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirdapp.owner'),
        ),
    ]
