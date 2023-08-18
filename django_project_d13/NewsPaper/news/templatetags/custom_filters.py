from django import template

register = template.Library()

INCORRECT_WORDS = ['тег', 'теги', 'тегов', 'фильтр', 'фильтры', 'фильтров.', 'django.']


@register.filter()
def correct(text):
    s = ''
    for i in text.split():
        if i.lower() in INCORRECT_WORDS:
            i = i[0] + (len(i)-1)*'*'
        s += ' ' + i

    return s

