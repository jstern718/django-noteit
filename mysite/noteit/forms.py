from django import forms


class Note_form(forms.Form):

    form_title = forms.CharField(label="title", help_text="enter title",
                                 initial="")
    form_content = forms.Textarea()

    def clean_note_data(self):
        data = self.cleaned_data['form_title', 'form_content']
        return data

    def __init___(self):
        self.title = ""
        self.content = ""