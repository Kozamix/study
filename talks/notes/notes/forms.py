from django import forms
from ..logic.migrations import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','content']
