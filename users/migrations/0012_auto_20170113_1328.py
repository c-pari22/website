# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20160702_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewSlot',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('availability', models.BooleanField(default=True)),
                ('officer_username', models.CharField(help_text='Please enter a valid officer username as this is used for website queries.', max_length=30)),
                ('student', models.CharField(verbose_name='Student', max_length=50, blank=True)),
                ('student_email', models.EmailField(verbose_name='Student Email', max_length=255, blank=True)),
                ('day_of_week', models.IntegerField(default=1, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], max_length=1)),
                ('hour', models.IntegerField(default=9, choices=[(9, '9am - 10am'), (10, '10am - 11am'), (11, '11am - 12pm'), (12, '12pm - 1pm'), (13, '1pm - 2pm'), (14, '2pm - 3pm'), (15, '3pm - 4pm'), (16, '4pm - 5pm')], max_length=2)),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='term',
            field=models.CharField(default='S15', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017')], max_length=5, verbose_name='Officer term'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='grad_year',
            field=models.CharField(default='15', choices=[('95', '1995'), ('96', '1996'), ('97', '1997'), ('98', '1998'), ('99', '1999'), ('00', '2000'), ('01', '2001'), ('02', '2002'), ('03', '2003'), ('04', '2004'), ('05', '2005'), ('06', '2006'), ('07', '2007'), ('08', '2008'), ('09', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020')], max_length=4, verbose_name='When are you graduating | When did you graduate?'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_joined',
            field=models.CharField(default='F14', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017')], max_length=11, verbose_name='When did you join UPE?'),
        ),
    ]