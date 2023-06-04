menu = ['home', 'women', 'add page', 'about']

class DataMixin:
    def get_user_context(self, **kwargs): #Form the necessary context by default
        context = kwargs #Create a dictionary from passed parametrs
        menu_cop = menu.copy()
        if  not self.request.user.is_authenticated:
            menu_cop.pop(2)
        context['menu'] = menu_cop
        return context
