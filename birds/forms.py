import re

from django import forms

from birds.models import Species


class BirdSearchForm(forms.Form):
    query = forms.CharField(required=False, label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'e.g. chickadee'}))

    def clean(self):
        cleaned_data = super(BirdSearchForm, self).clean()
        terms = re.split('\W+', cleaned_data['query'])

        all_birds = Species.objects.filter(is_visible=True)
        search_birds = []

        for b in all_birds:
            for term in terms:
                if (term.lower() not in b.scientific_name.lower() and
                        term.lower() not in b.common_name.lower()):
                    break
            else:
                search_birds.append(b)

        cleaned_data['search_birds'] = search_birds
