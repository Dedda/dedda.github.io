__author__ = 'dedda'

import json
import jinja2

TEMPLATES_FOLDER = 'template/'

JSON_FILE = 'json/index.json'
TEMPLATE_FILE = 'index.html'
RENDERED_FILE = 'index.html'

def generate(debug):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
    template_env = jinja2.Environment(loader=template_loader)
    print('generating index page...')
    json_data = open(JSON_FILE).read()
    template_data = json.loads(json_data)
    template_data['debug'] = debug
    if 'desc' in template_data:
        template_data['desc'] = "".join(template_data['desc'])
    template = template_env.get_template(TEMPLATE_FILE)
    rendered = open(RENDERED_FILE, 'w')
    rendered.write(template.render(template_data))
    print('index page generated!')
    pass
