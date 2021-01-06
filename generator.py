#!/usr/bin/python
__author__ = 'dedda'

import jinja2
import json

TEMPLATE_FOLDER = 'template'
TEMPLATE_LOADER = jinja2.FileSystemLoader(searchpath=TEMPLATE_FOLDER)
TEMPLATE_ENV = jinja2.Environment(loader=TEMPLATE_LOADER)


def nav_template() -> jinja2.Template:
    return TEMPLATE_ENV.get_template('navigation.html')


def nav_bar(current_page) -> str:
    template = nav_template()
    with open('json/navigation.json') as file:
        data = json.loads(file.read())
    data = {
        'navigation': data,
        'current_page': current_page,
    }
    return template.render(data)


class Page(object):
    def __init__(self, template, rendered):
        self.template = template
        self.rendered = rendered

    def render(self, data):
        template = TEMPLATE_ENV.get_template(self.template)
        data['nav'] = nav_bar(self.rendered)
        rendered = template.render(data)
        with open(self.rendered, 'w') as rendered_file:
            rendered_file.write(rendered)


if __name__ == '__main__':
    Page('index.html', 'index.html').render({})
    Page('regal.html', 'regal.html').render({})
