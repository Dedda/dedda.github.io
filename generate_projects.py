from pprint import pprint

__author__ = 'dedda'

import json
import jinja2
import sys

TEMPLATES_FOLDER = 'template/'

JSON_FILE = 'projects.json'
TEMPLATE_FILE = 'projects.html'
RENDERED_FILE = 'projects.html'

debug = 'debug' in sys.argv

print('debug: ' + str(debug))

templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
templateEnv = jinja2.Environment(loader=templateLoader)

print('generating projects page...')

json_data = open(JSON_FILE).read()
data = json.loads(json_data)
template_data = {'debug' : debug}
template_data['projects'] = {}
for (name, project) in data.items():
    print("found project '" + name + "'")
    project_data = project
    project_data['name'] = name
    template_data['projects'][name] = project_data
##pprint(projects_template_data)
template = templateEnv.get_template(TEMPLATE_FILE)
rendered = open(RENDERED_FILE, 'w')
rendered.write(template.render(template_data))
print('projcets page generated!')