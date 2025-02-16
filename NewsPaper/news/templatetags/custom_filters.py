from django import template


register = template.Library()

ban_list = set(['Редиска', 'Какашка'])

@register.filter()
def ban_words(value):
    for i in value.split():
        if i.strip('!@#$%^&*?') in ban_list:
            i = '*' * len(value)
    return ''.join(value)
