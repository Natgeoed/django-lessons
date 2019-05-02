# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-02 17:24
from __future__ import unicode_literals

import bitfield.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('curricula', '0007_delete_cascade_fix'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='skill',
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tipcategory',
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None, help_text=b'Select the audience(s) for which this content is\n        appropriate. Selecting audiences means that a separate audience view of\n        the page will exist for those audiences.\n\n        Note that the text you input in this form serves as the default text.\n        If you indicate this activity is appropriate for multiple audiences,\n        you either need to add text variations or the default text must be\n        appropriate for those audiences.'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None, help_text=b'Select the audience(s) for which this content is\n        appropriate.'),
        ),
        migrations.AlterField(
            model_name='ideacategory',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None, help_text=b'Select the audience(s) for which this content is\n        appropriate.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None, help_text=b'Select the audience(s) for which this content is\n        appropriate. Selecting audiences means that a separate audience view of\n        the page will exist for those audiences. For a lesson, the only possible\n        choices are Teachers and Informal Educators.\n\n        Note that the text you input in this form serves as the default text.\n        If you indicate this activity is appropriate for both T/IE audiences,\n        you either need to add text variations or the default text must be\n        appropriate for for both audiences.'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None),
        ),
        migrations.AlterField(
            model_name='tip',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None),
        ),
        migrations.AlterField(
            model_name='unit',
            name='appropriate_for',
            field=bitfield.models.BitField([b'Educator', b'Informal Educator', b'Family', b'Student', b'PreK', b'Kindergarten', b'1st Grade', b'2nd Grade', b'3rd Grade', b'4th Grade', b'5th Grade', b'6th Grade', b'7th Grade', b'8th Grade', b'9th Grade', b'10th Grade', b'11th Grade', b'12th Grade', b'Higher Education'], default=None, help_text=b'Select the audience(s) for which this content is\n        appropriate. Selecting audiences means that a separate audience view of\n        the page will exist for those audiences.\n\n        Note that the text you input in this form serves as the default text.\n        If you indicate this unit is appropriate for multiple audiences,\n        you either need to add text variations or the default text must be\n        appropriate for those audiences.'),
        ),
    ]
