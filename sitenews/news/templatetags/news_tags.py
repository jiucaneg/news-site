from django import template
from django.db.models import Count

from news.models import Category, Tag

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {'categories': categories}


@register.inclusion_tag('news/tags_tpl.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}