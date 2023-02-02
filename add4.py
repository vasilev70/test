from typing import Callable

def output_stock(start_msg: str,
                data_list: list,
                action: Callable = None):
    assert type(start_msg) is str
    assert type(data_list) is list
    for data in data_list:
        assert type(data) is str
    if action is not None:
        assert isinstance(action, Callable)
        
    print(start_msg)
    index = 1
    for data in data_list:
        print(f' {index}. {data.capitalize()}')
        if action is not None:
            action(data_list[data])
        index += 1
    print(f' {index}. Exit')
               
def get_article_menu(start_msg: str,
                     data_list: list,
                     index_exit: int):
    from utils.console_input import get_number_range
    return get_number_range(msg='choose article menu',
                            left_edge=1,
                            right_edge=index_exit,
                            action = lambda: output_stock(start_msg = start_msg,
                                                     data_list = data_list))