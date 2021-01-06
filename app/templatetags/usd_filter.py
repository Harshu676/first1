from django import template

register=template.Library()

#example of filter without arguement
def lowerr(value):
    return value.lower()


#example of filter with value,arg
@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c

@register.filter()
def cut(value,arg):
    return value.replace(arg,'')


@register.filter()
def replace(value,arg):
    return value.replace(arg,'b')


register.filter('low',lowerr)
#register.filter('rep',replace)

'''

remove --->h
count----> character or substring is repeated


string--->remove h--->immutable-->replace
'''