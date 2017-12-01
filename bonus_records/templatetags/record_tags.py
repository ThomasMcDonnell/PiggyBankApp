import datetime
import json

from django import template
from django.utils import timezone

from ..forms import RecordForm


register = template.Library()


@register.inclusion_tag('records/_form.html')
def record_form():
    form = RecordForm()
    return {'form': form}


@register.simple_tag(takes_context=True)
def chart_data(context):
    company = context['object']
    quarter = timezone.now() - datetime.timedelta(days=91)
    records = company.bonus_records.filter(recorded_at__gte=quarter)
    return json.dumps({
        'labels': [record.recorded_at.strftime('%Y-%M-%D') for record in records],
        'series': [[record.amount for record in records]]
            })

