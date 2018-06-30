#! /usr/local/bin/python3
import jinja2 as jj

template = jj.Template('Hello {{where}}')

print(template.render(where = 'World'))
print (template)
