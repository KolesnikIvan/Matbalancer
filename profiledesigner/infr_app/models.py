from django.db import models

# Create your models here.
SEP_OBJ_TYPES = [
    ("dns", "ДНС"),
    ("upsv", "УПСВ"),
    ("ptvo", "ПТВО"),
    ("upn", "УПН"),
    ("cppn", "ЦППН"),
]

FLOOD_OBJ_TYPES = [
    ("kns", "КНС"),
]

WELL_TYPES = [
    ("prod", "добывающая"),
    ("inj", "нагнетательная"),
]

class DO(models.Model):
    name = models.CharField(max_length=70, verbose_name="Наименование добывающего общества")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Добывающее общество'
        verbose_name_plural = 'Добывающие общества'

class Field(models.Model):
    name = models.CharField(max_length=70, verbose_name="Наименование месторождения")
    do = models.ForeignKey(DO, null=True, on_delete=models.CASCADE, verbose_name="Добывающее общество")
    
    def __str__(self):
        return f'{self.name}, {self.do}'
    
    class Meta:
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Мусторождения'

class SeparationObject(models.Model):
    name = models.CharField(max_length=70)
    obj_type = models.CharField(max_length=15, choices=SEP_OBJ_TYPES)
    liq_sep_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по подготовке жидкости, м3/сут')
    oil_sep_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по подготовке нефти, м3/сут')
    wat_sep_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по подготовке воды, м3/сут')
    liq_pmp_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по перекачке жидкости, м3/сут')
    oil_pmp_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по перекачке нефти, м3/сут')
    wat_pmp_pwr = models.FloatField(null=True, blank=True, verbose_name='Мощность по перекачке воды, м3/сут')
    wcut = models.FloatField(null=True, verbose_name="Остаточная обводненность продукции")
    # regime = models.BooleanField(null=True, verbose_name="Если ноль, то выход нефти считается по обводненности; иначе задается пропускная способность по жидкости")
    # do = models.ForeignKey(DO, null=True, on_delete=models.CASCADE, verbose_name="Добывающее общество")
    field = models.ForeignKey(Field, null=True, on_delete=models.CASCADE, verbose_name="Месторождение")
    

    class Meta:
        verbose_name = "Дожимная насосная станция"
        verbose_name_plural = "Дожимные насосные станции"

    def __repr__(self) -> str:
        return ','.join((self.name, 
                         str(self.liq_sep_pwr),
                         str(self.oil_sep_pwr),
                         str(self.wat_sep_pwr),
                         str(self.liq_pmp_pwr),
                         str(self.oil_pmp_pwr),
                         str(self.wat_pmp_pwr)))

class FloodingObject(models.Model):
    """KNSs"""
    name = models.CharField(max_length=70)
    obj_type = models.CharField(max_length=15, choices=FLOOD_OBJ_TYPES, verbose_name="Тип объекта закачки")
    wat_pmp_pwr = models.FloatField(null=True, blank=True, verbose_name="Мощность по закачке воды, м3/сут")
    wat_src_dbt = models.FloatField(null=True, blank=True, verbose_name="Мощность водозаборов, м3/сут")
    # do = models.ForeignKey(DO, null=True, on_delete=models.CASCADE, verbose_name="Добывающее общество")
    field = models.ForeignKey(Field, null=True, on_delete=models.CASCADE, verbose_name="Месторождение")
    
    class Meta:
        verbose_name = "Кустовая насосная станция"
        verbose_name_plural = "Кустовые насосные станции"

class Pad(models.Model):
    # TODO: deside, wether to calc distribution by wells or by pads
    name = models.CharField(max_length=70, verbose_name="Наименование кустовой площадки")
    # do = models.ForeignKey(DO, null=True, on_delete=models.CASCADE, verbose_name="Добывающее общество")
    field = models.ForeignKey(Field, null=True, on_delete=models.CASCADE, verbose_name="Месторождение")
    oil_fact = models.FloatField(null=True,verbose_name="Фактическая добыча нефти")
    liq_fact = models.FloatField(null=True,verbose_name="Фактическая добыча жидкости")
    gas_fact = models.FloatField(null=True,verbose_name="Фактическая добыча попутного газа")
    fld_fact = models.FloatField(null=True,verbose_name="Фактическая закачка воды")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Кустовая площадка'
        verbose_name_plural = 'Кустовые площадки'
        
class PadDNSConnection(models.Model):
    id_pad = models.ForeignKey(Pad, on_delete=models.CASCADE, verbose_name="Идентификатор кустовой площадки")
    id_dns = models.ForeignKey(SeparationObject, null=True, on_delete=models.PROTECT, verbose_name="Объект сбора, к которому подключена кустовая площадка")
    date_pt = models.DateField(verbose_name="Дата, когда выполняется указанное соответствие куста объекту")

class Well(models.Model):
    name = models.CharField(max_length=70, verbose_name="Наименование скважины")
    dest = models.CharField(max_length=25, choices=WELL_TYPES, verbose_name="Назначение скважины")
    oil_fact = models.FloatField(null=True, blank=True, verbose_name="Фактическая добыча нефти, м3/сут")
    liq_fact = models.FloatField(null=True, blank=True, verbose_name="Фактическая добыча жидкости, м3/сут")
    gas_fact = models.FloatField(null=True, verbose_name="Фактическая добыча попутного газа")
    fld_fact = models.FloatField(null=True, blank=True, verbose_name="Фактическая закачка воды, м3/сут")
    pad = models.ForeignKey(Pad, null=True, on_delete=models.CASCADE, verbose_name="Кустовая площадка")
    # do = models.ForeignKey(DO, null=True, on_delete=models.CASCADE, verbose_name="Добывающее общество")
    # field = models.ForeignKey(Field, null=True, on_delete=models.CASCADE, verbose_name="Месторождение")
    
    class Meta:
        verbose_name = "Скважина и фактические уровни добычи или закачки на ней"
        verbose_name_plural = "Скважины и фактические уровни добычи или закачки на них"

class PadKNSConnection(models.Model):
    id_pad = models.ForeignKey("Pad", on_delete=models.CASCADE, verbose_name="Идентификатор кустовой площадки")
    id_kns = models.ForeignKey("FloodingObject", null=True, on_delete=models.PROTECT, verbose_name="Объект ппд (закачки), к которому подключена кустовая площадка")
    date_pt = models.DateField(verbose_name="Дата, когда выполняется указанное соответствие куста объекту")

class WellPadConnection(models.Model):
    id_well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name="Идентификатор скважины")
    id_pad= models.ForeignKey(Pad, on_delete=models.CASCADE, verbose_name="Идентификатор куста")

class PadFieldConnection(models.Model):
    id_pad = models.ForeignKey(Pad, on_delete=models.CASCADE, verbose_name="Идентификатор куста")
    id_field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")

# class FieldDOConnection(models.Model):
#     id_field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")
#     id_do = models.ForeignKey(DO, on_delete=models.CASCADE, verbose_name="Идентификатор ДО")

class DNSFieldConnection(models.Model):
    id_dns = models.ForeignKey(SeparationObject, on_delete=models.CASCADE, verbose_name="Идентификатор ДНС")
    id_field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")

class KNSFieldConnection(models.Model):
    id_kns = models.ForeignKey(FloodingObject, on_delete=models.CASCADE, verbose_name="Идентификатор КНС")
    id_field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")

class DNSKNSConnection(models.Model):
    id_dns = models.ForeignKey(FloodingObject, on_delete=models.CASCADE, verbose_name="Идентификатор КНС")
    id_kns = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")
    priority = models.IntegerField(verbose_name="Приоритет потребителя воды для данного источника")
    date_pt = models.DateField(verbose_name="Дата, когда выполняется указанное соответствие объектов")

class KNSDNSConnection(models.Model):
    id_kns = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Идентификатор м-я")
    id_dns = models.ForeignKey(SeparationObject, on_delete=models.CASCADE, verbose_name="Идентификатор КНС")
    priority = models.IntegerField(verbose_name="Приоритет источника воды для данного потребителя")
    date_pt = models.DateField(verbose_name="Дата, когда выполняется указанное соответствие объектов")

class Prognose(models.Model):
    liquid = models.FloatField(null=True, blank=True, verbose_name="Добыча жидкости")
    oil = models.FloatField(null=True, blank=True, verbose_name="Добыча нефти")
    gas = models.FloatField(null=True, blank=True, verbose_name="Добыча газа")
    flood = models.FloatField(null=True, blank=True, verbose_name="Закачка воды")
    date_pt = models.DateField(verbose_name="Дата")
    id_field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Прогноз добычи/закачки на месторождении"
        verbose_name_plural = "Прогнозы добычи/закачки на месторождениях"
