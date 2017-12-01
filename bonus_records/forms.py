from django import forms

from . import models


class RecordForm(forms.ModelForm):
    class Meta:
        fields = ('amount', 'notes', 'company')
        model = models.Record

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["company"].queryset = (
                models.Company.objects.filter(
                    pk__in=user.companies.values_list("company__pk")
                )
            )


class DeleteForm(forms.ModelForm):
    pass
