# Generated by Django 4.0.6 on 2022-08-04 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rma.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rma', '0004_primary'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', rma.models.Uppercase(max_length=200, verbose_name='Name of School')),
                ('year_from', rma.models.Uppercase(choices=[('N/A', 'N/A'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=4, verbose_name='From')),
                ('year_to', rma.models.Uppercase(choices=[('N/A', 'N/A'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=4, verbose_name='To')),
                ('highest_level', rma.models.Uppercase(choices=[('GRADUATED', 'GRADUATED'), ('GRADE 1', 'GRADE 1'), ('GRADE 2', 'GRADE 2'), ('GRADE 3', 'GRADE 3'), ('GRADE 4', 'GRADE 4'), ('GRADE 5', 'GRADE 5'), ('GRADE 6', 'GRADE 6')], max_length=50, verbose_name='Highest Level')),
                ('year_graduated', rma.models.Uppercase(choices=[('N/A', 'N/A'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=4, verbose_name='Year Graduated')),
                ('academic_honors', rma.models.Uppercase(blank=True, max_length=150, verbose_name='Academic Honors Received')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'High School',
            },
        ),
    ]
