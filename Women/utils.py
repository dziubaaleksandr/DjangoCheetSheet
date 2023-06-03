menu = ['home', 'women', 'add page', 'about']

class DataMixin:
    def get_user_context(self, **kwargs): #Form the necessary context by default
        context = kwargs #Create a dictionary from passed parametrs
        context['menu'] = menu
        return context
