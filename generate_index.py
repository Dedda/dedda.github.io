__author__ = 'dedda'

import json
import jinja2

TEMPLATES_FOLDER = 'template/'

JSON_FILE = 'json/index.json'
TEMPLATE_FILE = 'index.html'
RENDERED_FILE = 'index.html'

def generate(debug):
    templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
    templateEnv = jinja2.Environment(loader=templateLoader)
    print('generating index page...')
    json_data = open(JSON_FILE).read()
    template_data = json.loads(json_data)
    template_data['debug'] = debug
    template = templateEnv.get_template(TEMPLATE_FILE)
    rendered = open(RENDERED_FILE, 'w')
    rendered.write(template.render(template_data))
    print('index page generated!')
    pass
