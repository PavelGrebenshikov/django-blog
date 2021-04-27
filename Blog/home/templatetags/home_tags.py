from django import template
from home.models import Category

register = template.Library()

@register.inclusion_tag('home/list_category.html')
def show_category():
    return {"Category": Category.objects.all()}