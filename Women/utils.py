menu = ['home', 'women', 'add page', 'about']

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs): #Form the necessary context by default
        context = kwargs #Create a dictionary from passed parametrs
        menu_cop = menu.copy()
        if  not self.request.user.is_authenticated:
            menu_cop.pop(2)
        context['menu'] = menu_cop
        context['page_selected'] = int(self.request.GET.get('page', 1))
        return context
