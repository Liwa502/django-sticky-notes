from django import forms
from .models import StickyNote


# ModelForm for creating and updating StickyNote instances
class StickyNoteForm(forms.ModelForm):
    class Meta:
        # Specify the model this form is for
        model = StickyNote

        # Specify fields to include in the form
        fields = ['title', 'content', 'due_date']

        # Customize form field widgets for better UI
        widgets = {
            # Title input styled with Bootstrap and placeholder text
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note Title'
            }),
            # Content textarea styled with Bootstrap, fixed rows, and placeholder
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your note here...'
            }),
            # Due date input as a date picker with Bootstrap styling
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
