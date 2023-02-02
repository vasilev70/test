from models.bistro import Бистро

def order(бистро_list: list):
    from utils.menu import get_article_menu
    
    def get_название() -> str:
        бистро_list = list(бистро_dict.keys())
        index_exit = len(бистро_list)+1
        
        choose = get_article_menu(start_msg='Наше меню:',
                                    data_list=бистро_list,
                                    index_exit=index_exit)
        
        if choose == index_exit:
            raise SystemExit
        
        return бистро_list[choose-1]
        
    def get_бистро() -> Бистро:
        разновидность_list:list = []
        for бистро in бистро_разновидность_list:
            разновидность_list.append(бистро.разновидность)
            
        index_exit = len(разновидность_list)+1
        choose = get_article_menu(start_msg=f'Ваше меню: {название_бистро}',
                                data_list=разновидность_list,
                                index_exit=index_exit)
        
        if choose == index_exit:
            raise SystemExit
        
        return бистро_разновидность_list[choose-1]
        
    def get_menu() -> None :
        for бистро in бистро_list:
            название = бистро.название
            if название in бистро_dict:
                бистро_dict[название].append(бистро)
                
            else:
                бистро_dict[название] = [бистро]
            
    бистро_dict: dict[str, list[Бистро]] = {}
    get_menu()
         
    название_бистро = get_название()
    бистро_разновидность_list = бистро_dict[название_бистро]
    
    бистро = get_бистро()
                    
    print(f'Ваш заказ:\n\
Бистро: {бистро.название}\n\
Разновидность: {бистро.разновидность}\n\
Цена: {бистро.цена}')
                 
