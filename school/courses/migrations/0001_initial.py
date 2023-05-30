# Generated by Django 4.0 on 2021-12-28 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("slug", models.CharField(max_length=64, unique=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("short_description", models.CharField(blank=True, max_length=200)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "kurz",
                "verbose_name_plural": "kurzy",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("slug", models.CharField(max_length=64)),
                ("layer", models.IntegerField()),
                ("order", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
            ],
            options={
                "verbose_name": "lekcia",
                "verbose_name_plural": "lekcie",
            },
        ),
        migrations.CreateModel(
            name="CourseGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("order", models.IntegerField()),
                ("courses", models.ManyToManyField(blank=True, to="courses.Course")),
            ],
            options={
                "verbose_name": "skupina kurzov",
                "verbose_name_plural": "skupiny kurzov",
            },
        ),
        migrations.AddConstraint(
            model_name="lesson",
            constraint=models.UniqueConstraint(
                fields=("course", "slug"), name="unique_course_slug"
            ),
        ),
    ]
