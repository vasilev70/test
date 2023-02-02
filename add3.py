from typing import Callable

def get_number(msg: str,
            action: Callable = None,
            action_in_launch = True) -> int:
    """
    Функция, для получения числа из консоли
     Args:
        str: сообщение - сообщение для пользователя
        Callable: действие - действие перед вводом
        bool: действие_при_запуске - нужно ли запускать действие при старте функции
        str: сообщение_при_ошибке
     Returns:
        int: число, которое ввел пользователь
    """    
    assert type(msg) is str
    if action is not None:
        assert isinstance(action, Callable)
        assert type(action_in_launch) is bool
    
    while True:
        if action is not None:
            if action_in_launch:
                action()
        number = input(f'{msg}:  ')
        try:
            number = int(number)
        except ValueError:
            print('Вы ввели не число!')
            if action is not None:
                action()
        else:
            return number
            
            
def get_number_range(msg: str,
                  right_edge: int,
                  left_edge = 1,
                  action: Callable = None,
                  action_in_launch = True):
    """Функция, для получения числа в заданном диапазоне
     Args:
        str: сообщение
        int: правая_граница
        int: левая_граница
        Callable: действие - действие перед вводом
        bool: действие_при_запуске - нужно ли запускать действие при старте функции
        str: сообщение_при_ошибке
     Returns:
        int: число в заданном диапазоне
    """
    
    assert type(msg) is str
    assert type(right_edge) is int
    assert type(left_edge) is int
    if action is not None:
        assert isinstance(action, Callable)
    assert type(action_in_launch) is bool
    
    while True:
        if action is not None:
            if action_in_launch:
                action()
        number = get_number(msg, action,False)
        try:
            assert number in range(left_edge, right_edge+1)
        except AssertionError:
            print(f'Введите число в диапазоне [{left_edge},\
{right_edge}]')
        else:
            return number
        
