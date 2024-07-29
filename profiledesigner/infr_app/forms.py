from django.forms import ModelForm
from infr_app.models import SeparationObject, FloodingObject, Pad, Well, Prognose

class SeparationObjectCreateForm(ModelForm):
    class Meta:
        model = SeparationObject
        # fields = ('name', 'obj_type', 'liq_sep_pwr')
        fields = '__all__'
        # fields = [\
        #     "name",
        #     "obj_type",
        #     "liq_sep_pwr",
        #     "oil_sep_pwr",
        #     "wat_sep_pwr",
        #     "liq_pmp_pwr",
        #     "oil_pmp_pwr",
        #     "wat_pmp_pwr",
        #     "wcut",
        # ]
        # help_texts = {
        #     "name": "наименование создаваемого объекта подготовки",
        #     "obj_type": "тип создаваемого объекта подготовки", 
        #     "liq_sep_pwr": "мощность по подготовке жидкости создаваемого объекта подготовки", 
        #     "oil_sep_pwr": "мощность по подготовке нефти создаваемого объекта подготовки", 
        #     "wat_sep_pwr": "мощность по подготовке пластовой воды создаваемого объекта подготовки", 
        #     "liq_pmp_pwr": "мощность по перекачке жидкости создаваемого объекта подготовки", 
        #     "oil_pmp_pwr": "мощность по перекачке нефти создаваемого объекта подготовки", 
        #     "wat_pmp_pwr": "мощность по перекачке воды создаваемого объекта подготовки", 
        #     "wcut": "остаточная обводненность продукции объекта подготовки", 
        # }
