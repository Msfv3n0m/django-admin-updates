from django.contrib.contenttypes.admin import GenericTabularInline
from admin_updates.models import Update
from admin_updates.helpers import get_class_from_str
from django.conf import settings


class UpdateInline(GenericTabularInline):

    model = Update

    readonly_fields = ('user',)

    classes = ['collapse']

    def __init__(self, *args, **kwargs):
        form_klass = getattr(
            settings,
            'ADMIN_COMMENTS_FORM_CLASS',
            'admin_updates.forms.UpdateInlineForm')

        formset_klass = getattr(
            settings,
            'ADMIN_COMMENTS_FORMSET_CLASS',
            'admin_updates.forms.UpdateInlineFormset')

        SHOW_EMPTY = getattr(settings, 'ADMIN_COMMENTS_SHOW_EMPTY', False)

        UpdateForm = get_class_from_str(form_klass)
        UpdateFormSet = get_class_from_str(formset_klass)

        self.form = UpdateForm
        self.formset = UpdateFormSet
        self.extra = 1 if SHOW_EMPTY else 0
        super(UpdateInline, self).__init__(*args, **kwargs)

    def get_queryset(self, request):
        return super(UpdateInline, self).get_queryset(request).order_by('-time')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(UpdateInline, self).get_formset(
            request, obj, **kwargs)
        formset.current_user = request.user
        return formset


__all__ = ['UpdateInline']
