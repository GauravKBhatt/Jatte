from django import template

register = template.library()

@register.filter(name='initials')
def initials(value):
        initials = ''

        for name in value.split(''):
            if name and len(initials) < 3:
                initials += name[0].upper
        
        return initials