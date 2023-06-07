from django import forms
from .models import *


class AddPostForm(forms.Form): #Not related with db
    title = forms.CharField(max_length=255, label = "TITLE")
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(required = False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Category not selected")


class AddPostFormRelatedWithDB(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category not selected"

    class Meta:
        model = Women
        #fields = '__all__' #Takes all fields except optional
        fields = ['title', 'slug', 'content', 'is_published', 'cat']

        widgets = {
                'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
            }

    def clean_title(self): #Validation fnct for title. Prefix clean_ is necessary
        title = self.cleaned_data['title']
        if len(title)>20:
            raise forms.ValidationError('Longer than 200 characters')
        return title