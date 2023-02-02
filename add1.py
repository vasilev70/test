class Бистро:
    __название: str
    __разновидность: str
    __цена: float

    # ............ название
    @property
    def название(self):
        return self.__название

    @название.setter
    def название(self, value: str):
        assert type(value) == str, 'Неверный тип данных'
        self.__название = value

    # .............разновидность
    @property
    def разновидность(self):
        return self.__разновидность

    @разновидность.setter
    def разновидность(self, value: str):
        assert type(value) == str, 'Неверный тип данных'
        self.__разновидность = value

    # .............цена
    @property
    def цена(self):
        return self.__цена

    @цена.setter
    def цена(self, value: float):
        assert type(value) == float, 'Неверный тип данных'
        self.__цена = value

    def __init__(self,
                 название: str,
                 разновидность: str,
                 цена: float) -> None:
        self.название = название
        self.разновидность = разновидность
        self.цена = цена

    def __str__(self) -> str:
        return f'{self.__название} {self.__разновидность} {self.__цена}'
