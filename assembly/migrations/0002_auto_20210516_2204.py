# Generated by Django 3.2 on 2021-05-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id_fb', models.AutoField(db_column='Id_fb', primary_key=True, serialize=False)),
                ('from_email', models.EmailField(db_column='From_email', max_length=100, verbose_name='От кого отправлен Email')),
                ('subject', models.CharField(db_column='Subject', max_length=100, verbose_name='Тема')),
                ('message', models.CharField(db_column='Message', max_length=100, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'обратная связь',
                'verbose_name_plural': 'обратные связи',
                'db_table': 'feedback',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='casepc',
            options={'managed': True, 'verbose_name': 'корпус', 'verbose_name_plural': 'корпуса'},
        ),
        migrations.AlterModelOptions(
            name='cooler',
            options={'managed': True, 'verbose_name': 'кулер', 'verbose_name_plural': 'кулеры'},
        ),
        migrations.AlterModelOptions(
            name='ddr',
            options={'managed': True, 'verbose_name': 'оперативная память', 'verbose_name_plural': 'оперативная память'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'managed': True, 'verbose_name': 'производитель', 'verbose_name_plural': 'производители'},
        ),
        migrations.AlterModelOptions(
            name='mboard_size',
            options={'managed': True, 'verbose_name': 'размер мат. платы', 'verbose_name_plural': 'размеры мат. плат'},
        ),
        migrations.AlterModelOptions(
            name='motherboard',
            options={'managed': True, 'verbose_name': 'материнская плата', 'verbose_name_plural': 'материнские платы'},
        ),
        migrations.AlterModelOptions(
            name='pcassembly',
            options={'managed': True, 'verbose_name': 'сборка', 'verbose_name_plural': 'сборки'},
        ),
        migrations.AlterModelOptions(
            name='powersupply',
            options={'managed': True, 'verbose_name': 'блок питания', 'verbose_name_plural': 'блоки питания'},
        ),
        migrations.AlterModelOptions(
            name='processor',
            options={'managed': True, 'verbose_name': 'процессор', 'verbose_name_plural': 'процессоры'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': True, 'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'managed': True, 'verbose_name': 'сохраненная сборка', 'verbose_name_plural': 'сохраненные сборки'},
        ),
        migrations.AlterModelOptions(
            name='socket',
            options={'managed': True, 'verbose_name': 'сокет', 'verbose_name_plural': 'сокеты'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'managed': True, 'verbose_name': 'накопитель', 'verbose_name_plural': 'накопители'},
        ),
        migrations.AlterModelOptions(
            name='storage_form_factor',
            options={'managed': True, 'verbose_name': 'форм-фактор накопителя', 'verbose_name_plural': 'форм-фактор накопителей'},
        ),
        migrations.AlterModelOptions(
            name='storage_type',
            options={'managed': True, 'verbose_name': 'тип накопителя', 'verbose_name_plural': 'типы накопителей'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'managed': True, 'verbose_name': 'тест', 'verbose_name_plural': 'тесты'},
        ),
        migrations.AlterModelOptions(
            name='typememory',
            options={'managed': True, 'verbose_name': 'тип памяти', 'verbose_name_plural': 'типы памяти'},
        ),
        migrations.AlterModelOptions(
            name='videocard',
            options={'managed': True, 'verbose_name': 'видеокарта', 'verbose_name_plural': 'видеокарты'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='id_question',
            field=models.ForeignKey(db_column='Id_question', default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='id_socket',
            field=models.ForeignKey(db_column='Id_socket', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.socket', verbose_name='Сокет'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(db_column='Question_type', verbose_name='Тип вопроса'),
        ),
    ]
