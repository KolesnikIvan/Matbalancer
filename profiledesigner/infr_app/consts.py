from enum import Enum

class InfraObjKind(str, Enum):
    """Допустимые объекты инфраструктуры"""
    SEPARATION_OBJECT = "SEPARATION_OBJECT"
    FLOODING_OBJECT = "FLOODING_OBJECT"
    TRANSFORMER_SUBSTATION = "TRANSFORMER_SUBSTATION"
    WELL_PAD = "WELL_PAD"
    WELL = "WELL"
    # @classmethod
    # def get_translation(self):
    #     if self.value == self.SEPARATION_OBJECT:
    #         return "Объект подготовки (разделения) продукции скважин"
    #     elif self.value == self.FLOODING_OBJECT:
    #         return "Объект закачки пластовой воды"
    #     elif self.value == self.TRANSFORMER_SUBSTATION:
    #         return "Трансформаторная подстанция"
    #     elif self.value == self.WELL_PAD:
    #         return "Кустовая площадка скважин"
    #     elif self.value == self.WELL:
    #         return "Скважина"
    @property
    # @classmethod
    def get_translation(cls):
        if cls.value == cls.SEPARATION_OBJECT:
            return "Объект подготовки (разделения) продукции скважин"
        elif cls.value == cls.FLOODING_OBJECT:
            return "Объект закачки пластовой воды"
        elif cls.value == cls.TRANSFORMER_SUBSTATION:
            return "Трансформаторная подстанция"
        elif cls.value == cls.WELL_PAD:
            return "Кустовая площадка скважин"
        elif cls.value == cls.WELL:
            return "Скважина"
    @classmethod
    def get_translation2(cls):
        if cls.value == cls.SEPARATION_OBJECT:
            return "Объект подготовки (разделения) продукции скважин"
        elif cls.value == cls.FLOODING_OBJECT:
            return "Объект закачки пластовой воды"
        elif cls.value == cls.TRANSFORMER_SUBSTATION:
            return "Трансформаторная подстанция"
        elif cls.value == cls.WELL_PAD:
            return "Кустовая площадка скважин"
        elif cls.value == cls.WELL:
            return "Скважина"