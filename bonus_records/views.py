from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView

from braces.views import SelectRelatedMixin

from .forms import RecordForm
from . models import Record


class CreateRecord(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    form_class = RecordForm
    select_related = ('user', 'company')
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteRecordView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        user_id = self.request.user
        return self.model.objects.filter(user_id=user_id)


