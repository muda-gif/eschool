# Generated by Django 3.1.6 on 2021-02-16 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('details', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=64)),
                ('xclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xclass', to='authentification.class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('xclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='authentification.class')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('students', models.ManyToManyField(blank=True, related_name='parents', to='authentification.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='authentification.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='authentification.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='eschool')),
                ('date', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='authentification.subject')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='classes', to='authentification.Teacher'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('details', models.CharField(max_length=200)),
                ('doc', models.FileField(blank=True, upload_to='eschool')),
                ('classn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='authentification.class')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absences', to='authentification.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absences', to='authentification.subject')),
            ],
        ),
    ]
