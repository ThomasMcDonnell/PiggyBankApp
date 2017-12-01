from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from companies.models import Company


class Record(models.Model):
    company = models.ForeignKey(Company, related_name='bonus_records', null=True, blank=True)
    user = models.ForeignKey(User, related_name='bonus_records', null=True, blank=True)
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    amount = models.IntegerField()
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}: £{}: {}'.format(self.recorded_at.strftime('%Y-%M-%D'), self.amount, self.notes)

    class Meta:
        ordering = ['-recorded_at']

