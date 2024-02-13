from django import forms
from django.contrib.contenttypes.admin import BaseGenericInlineFormSet
from admin_updates.models import Update


class UpdateInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateInlineForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['update'].widget.attrs['rows'] = 4
        if instance and instance.pk:
            self.fields['update'].widget.attrs['readonly'] = True
            self.fields['update'].widget.attrs['border'] = 0

    class Meta:
        model = Update
        exclude = []

    class Media:
        css = {
            'all': ('css/admin_updates.css',)
        }


class UpdateInlineFormset(BaseGenericInlineFormSet):
    def save_new(self, form, commit=True):
        setattr(form.instance, "user", self.current_user)
        return super(UpdateInlineFormset, self).save_new(
            form, commit=True)


__all__ = ['UpdateInlineForm', 'UpdateInlineFormset']
