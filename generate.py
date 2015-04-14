from pprint import pprint

__author__ = 'dedda'

import json
import jinja2

TEMPLATES_FOLDER = 'template/'

PROJECTS_JSON_FILE = 'projects.json'
PROJECTS_TEMPLATE = 'projects.html'
PROJECTS_RENDERED = 'projects.html'

templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
templateEnv = jinja2.Environment(loader=templateLoader)

print('generating projects page...')

projects_json_data = open(PROJECTS_JSON_FILE).read()
projects_data = json.loads(projects_json_data)
projects_template_data = {}
projects_template_data['projects'] = {}
for (name, project) in projects_data.items():
    print("found project '" + name + "'")
    project_data = project
    project_data['name'] = name
    projects_template_data['projects'][name] = project_data
##pprint(projects_template_data)
projects_template = templateEnv.get_template(PROJECTS_TEMPLATE)
projects_rendered = open(PROJECTS_RENDERED, 'w')
projects_rendered.write(projects_template.render(projects_template_data))
print('projcets page generated!')