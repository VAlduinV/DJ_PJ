from django import template
from main.models import *

register = template.Library()


# Коллекция данных
@register.simple_tag(name='get_techs')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
# превращение функции в простой тег


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, tech_selected=0):
    if not sort:
        techs = Category.objects.all()
    else:
        techs = Category.objects.order_by(sort)

    return {"techs": techs, "tech_selected": tech_selected}


@register.inclusion_tag('main/menu.html')
def menu():
    menu = [{'title': "Про сайт", 'url_name': 'about'},
            {'title': "Додати статтю", 'url_name': 'add_page'},
            {'title': "Контакти", 'url_name': 'contact'}]

    posts = main.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка',
        'tech_selected': 0,
    }

    return {'menu': menu}
