# Generated by Django 3.2 on 2021-05-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Логин')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CasePc',
            fields=[
                ('id_case', models.AutoField(db_column='Id_case', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('max_height_cooler', models.IntegerField(db_column='Max_height_cooler', verbose_name='Максимальная высота кулера')),
                ('integrated_power_supply', models.IntegerField(blank=True, db_column='Integrated_power_supply', default='', null=True, verbose_name='Встроенный блок питания,Вт')),
                ('max_length_video', models.IntegerField(db_column='Max_length_video', verbose_name='Максимальная длинна видеокарты')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('form_factor_2_5', models.IntegerField(blank=True, db_column='Form_factor_2_5', null=True, verbose_name='Число внутренних отсеков 2,5')),
                ('form_factor_3_5', models.IntegerField(blank=True, db_column='Form_factor_3_5', null=True, verbose_name='Число внутренних отсеков 3,5')),
                ('case_img', models.ImageField(db_column='Case_img', max_length=255, upload_to='case/', verbose_name='Изображение')),
            ],
            options={
                'db_table': 'case_pc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id_cooler', models.AutoField(db_column='Id_ cooler', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('cooler_height', models.IntegerField(db_column='Cooler_height', verbose_name='Высота кулера')),
                ('cooler_max_tdp', models.IntegerField(db_column='Cooler_Max_TDP', verbose_name='Максимальная рассеиваемая мощность')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('cooler_img', models.ImageField(db_column='Cooler_img', max_length=255, upload_to='cooler/', verbose_name='Изображение')),
            ],
            options={
                'db_table': 'cooler',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id_manuf', models.AutoField(db_column='Id_manuf', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Производитель')),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mboard_size',
            fields=[
                ('id_mboard_size', models.AutoField(db_column='Id_mboard_size', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
            ],
            options={
                'db_table': 'mboard_size',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id_mboard', models.AutoField(db_column='Id_mboard', primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='utf8_general_ci', db_column='Name', max_length=100, verbose_name='Наименование')),
                ('mboard_max_ddr', models.IntegerField(db_column='Mboard_max_DDR', verbose_name='Количество слотов памяти')),
                ('mboard_max_frenquency_ddr', models.IntegerField(db_column='Mboard_max_frenquency_DDR', verbose_name='Максимальная частота памяти, поддерживаемая мат. платой')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('mboard_m2', models.IntegerField(blank=True, db_column='Mboard_M2', null=True, verbose_name='Количество слотов M2')),
                ('mboard_sata_iii', models.IntegerField(db_column='Mboard_Sata_III', verbose_name='Количество слотов Sata III')),
                ('mboard_img', models.ImageField(db_column='Mboard_img', max_length=255, upload_to='mboard/', verbose_name='Изображение')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель')),
                ('id_mboard_size', models.ForeignKey(db_column='Id_mboard_size', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.mboard_size', verbose_name='Размер мат. платы')),
            ],
            options={
                'db_table': 'motherboard',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PcAssembly',
            fields=[
                ('id_pc_assembly', models.AutoField(db_column='Id_Pc_assembly', primary_key=True, serialize=False)),
                ('pc_assembly_date', models.DateTimeField(db_column='Pc_assembly_date')),
                ('pc_assembly_price_end', models.IntegerField(db_column='Pc_assembly_price_end')),
                ('id_case', models.ForeignKey(db_column='Id_case', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.casepc')),
                ('id_cooler', models.ForeignKey(db_column='Id_cooler', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.cooler')),
                ('id_motherboard', models.ForeignKey(db_column='Id_Motherboard', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.motherboard')),
            ],
            options={
                'db_table': 'pc_assembly',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id_socket', models.AutoField(db_column='Id_socket', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Сокет')),
            ],
            options={
                'db_table': 'socket',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Storage_form_factor',
            fields=[
                ('id_form_factor', models.AutoField(db_column='Id_form_factor', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Форм-фактор накопителя')),
            ],
            options={
                'db_table': 'storage_form_factor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Storage_type',
            fields=[
                ('id_storage_type', models.AutoField(db_column='Id_storage_type', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Тип накопителя')),
            ],
            options={
                'db_table': 'storage_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id_test', models.AutoField(db_column='Id_test', primary_key=True, serialize=False)),
                ('test_title', models.CharField(db_column='Test_title', max_length=250, verbose_name='Наименование')),
                ('test_desc', models.CharField(db_column='Test_desc', max_length=250)),
                ('test_active', models.IntegerField(db_column='Test_active')),
            ],
            options={
                'db_table': 'test',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypeMemory',
            fields=[
                ('id_type_mem', models.AutoField(db_column='Id_type_mem', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Тип памяти')),
            ],
            options={
                'db_table': 'typeMemory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Videocard',
            fields=[
                ('id_vga', models.AutoField(db_column='Id_vga', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('video_frequency', models.IntegerField(db_column='Video_frequency', verbose_name='Частота видеокарты')),
                ('memory_frequency', models.IntegerField(db_column='Memory_frequency', verbose_name='Частота памяти')),
                ('video_memory', models.IntegerField(db_column='Video_memory', verbose_name='Объем видеопамяти')),
                ('video_benchmark', models.IntegerField(db_column='Video_benchmark', verbose_name='Число баллов в тестах')),
                ('power_supply_unit', models.IntegerField(db_column='Power_supply_unit', verbose_name='Рекомендуемая мощность блока питания')),
                ('video_length', models.IntegerField(db_column='Video_length', verbose_name='Длинна видеокарты')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('video_pci_e', models.IntegerField(blank=True, db_column='Video_PCI_e', null=True, verbose_name='Дополнительное питание')),
                ('video_img', models.ImageField(db_column='Video_img', max_length=255, upload_to='video/', verbose_name='Изображение')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель')),
                ('id_type_mem', models.ForeignKey(db_column='Id_type_mem_', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.typememory', verbose_name='Тип памяти')),
            ],
            options={
                'db_table': 'videocard',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id_storage', models.AutoField(db_column='Id_Storage', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('storage_volume', models.IntegerField(db_column='Storage_volume', verbose_name='Объем памяти')),
                ('storage_read_speed', models.IntegerField(db_column='Storage_read_speed', verbose_name='Скорость чтения')),
                ('storage_write_speed', models.IntegerField(db_column='Storage_write_speed', verbose_name='Скорость записи')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('storage_img', models.ImageField(db_column='Storage_img', max_length=255, upload_to='storage/', verbose_name='Изображение')),
                ('id_form_factor', models.ForeignKey(db_column='Id_form_factor', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.storage_form_factor', verbose_name='Форм-фактор')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель')),
                ('id_storage_type', models.ForeignKey(db_column='Id_storage_type', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.storage_type', verbose_name='Тип накопителя')),
            ],
            options={
                'db_table': 'storage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id_result', models.AutoField(db_column='Id_result', primary_key=True, serialize=False)),
                ('result_date', models.DateTimeField(db_column='Result_date')),
                ('result_title', models.CharField(db_column='Result_title', max_length=255, verbose_name='Наименование')),
                ('power_supply', models.CharField(db_column='Power_supply', max_length=255)),
                ('storage', models.CharField(db_column='Storage', max_length=255)),
                ('mboard', models.CharField(db_column='Mboard', max_length=255)),
                ('proc', models.CharField(db_column='Proc', max_length=255)),
                ('video', models.CharField(db_column='Video', max_length=255)),
                ('ddr', models.CharField(db_column='DDR', max_length=255)),
                ('cooler', models.CharField(db_column='Cooler', max_length=255)),
                ('result_price_end', models.IntegerField(db_column='Result_price_end')),
                ('id_pc_assembly', models.ForeignKey(db_column='Id_Pc_assembly', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.pcassembly')),
                ('id_test', models.ForeignKey(db_column='Id_test', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.test')),
            ],
            options={
                'db_table': 'result',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id_question', models.AutoField(db_column='Id_question', primary_key=True, serialize=False)),
                ('question_title', models.CharField(db_column='Question_title', max_length=255, verbose_name='Наименование')),
                ('question_type', models.IntegerField(db_column='Question_type')),
                ('id_test', models.ForeignKey(db_column='Id_test', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.test')),
            ],
            options={
                'db_table': 'question',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id_proc', models.AutoField(db_column='Id_proc', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('number_cores', models.IntegerField(db_column='Number_cores', verbose_name='Количество ядер')),
                ('proc_frequency', models.IntegerField(db_column='Proc_Frequency', verbose_name='Частота процессора')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('tdp', models.IntegerField(db_column='TDP', verbose_name='Тепловыделение')),
                ('proc_benchmark', models.IntegerField(db_column='Proc_benchmark', verbose_name='Число баллов в тестах')),
                ('proc_max_frenquency_ddr', models.IntegerField(db_column='Proc_max_frenquency_DDR', verbose_name='Максимальная частота опер. памяти, поддерживаемая процессором')),
                ('proc_max_syze_ddr', models.IntegerField(db_column='Proc_max_syze_DDR', verbose_name='Максимальный объем опер. памяти, поддерживаемый процессором')),
                ('proc_img', models.ImageField(db_column='Proc_img', max_length=255, upload_to='proc/', verbose_name='Изображение')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель')),
                ('id_socket', models.ForeignKey(db_column='Id_socket', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.socket', verbose_name='Разъем процессора')),
                ('id_type_mem_ddr', models.ForeignKey(db_column='Id_type_mem', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.typememory', verbose_name='Тип опер. памяти, поддерживаемая процессором')),
            ],
            options={
                'db_table': 'processor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id_power_supply', models.AutoField(db_column='Id_ power_supply', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('power_supply_power', models.IntegerField(db_column='Power_supply_ power')),
                ('power_supply_pci_e', models.IntegerField(db_column='Power_supply_PCI-E', verbose_name='Количество разъемов 6+2-pin PCI-E')),
                ('price_rub', models.IntegerField(db_column='Price_rub', verbose_name='Стоимость')),
                ('power_supply_img', models.ImageField(db_column='Power_supply_img', max_length=255, upload_to='power_supply/', verbose_name='Изображение')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer')),
            ],
            options={
                'db_table': 'power_supply',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pcassembly',
            name='id_power_supply',
            field=models.ForeignKey(db_column='Id_power_supply', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.powersupply'),
        ),
        migrations.AddField(
            model_name='pcassembly',
            name='id_proc',
            field=models.ForeignKey(db_column='Id_proc', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.processor'),
        ),
        migrations.AddField(
            model_name='pcassembly',
            name='id_storage',
            field=models.ManyToManyField(db_column='Id_storage', related_name='PcAssemblyies', to='assembly.Storage'),
        ),
        migrations.AddField(
            model_name='pcassembly',
            name='id_user',
            field=models.ForeignKey(db_column='Id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.authuser'),
        ),
        migrations.AddField(
            model_name='pcassembly',
            name='id_vga',
            field=models.ForeignKey(db_column='Id_vga', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.videocard'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='id_mboard_type_ddr',
            field=models.ForeignKey(db_column='Id_type_mem', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.typememory', verbose_name='Поколение памяти, которая поддерживает мат. плата'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='mboard_socket',
            field=models.ForeignKey(db_column='Id_socket', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.socket', verbose_name='Сокет'),
        ),
        migrations.CreateModel(
            name='Ddr',
            fields=[
                ('id_ddr', models.AutoField(db_column='Id_DDR', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, verbose_name='Наименование')),
                ('ddr_frenquency', models.IntegerField(db_column='DDR_frenquency', verbose_name='Частота памяти')),
                ('ddr_quantity', models.IntegerField(db_column='DDR_quantity', verbose_name='Модулей памяти в комплекте')),
                ('ddr_size', models.IntegerField(db_column='DDR_size', verbose_name='Объем одного модуля')),
                ('ddr_rub', models.IntegerField(db_column='DDR_rub', verbose_name='Стоимость')),
                ('ddr_img', models.ImageField(db_column='DDR_img', max_length=255, upload_to='ddr/', verbose_name='Изображение')),
                ('ddr_type', models.ForeignKey(db_column='Id_type_mem', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.typememory', verbose_name='Тип памяти')),
                ('id_manuf', models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'db_table': 'ddr',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cooler',
            name='cooler_socket',
            field=models.ManyToManyField(db_column='Id_soket', related_name='Coolers', to='assembly.Socket'),
        ),
        migrations.AddField(
            model_name='cooler',
            name='id_manuf',
            field=models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='casepc',
            name='id_manuf',
            field=models.ForeignKey(db_column='Id_manuf', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='casepc',
            name='id_mboard_size',
            field=models.ForeignKey(db_column='Id_mboard_size', on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.mboard_size', verbose_name='Размер мат. платы'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id_answer', models.AutoField(db_column='Id_answer', primary_key=True, serialize=False)),
                ('answer_title', models.CharField(db_column='Answer_title', max_length=255, verbose_name='Ответ')),
                ('answer_param_proc', models.CharField(db_column='Answer_param_proc', max_length=255, verbose_name='Параметр процессора')),
                ('answer_param_video', models.CharField(db_column='Answer_param_video', max_length=255, verbose_name='Параметр видеокарты')),
                ('answer_img', models.ImageField(db_column='Answer_img', max_length=255, upload_to='answer/', verbose_name='Изображение')),
                ('id_question', models.ForeignKey(db_column='Id_question', default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.question')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'db_table': 'answer',
                'managed': True,
            },
        ),
    ]
