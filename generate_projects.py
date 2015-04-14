__author__ = 'dedda'

import json
import jinja2

TEMPLATES_FOLDER = 'template/'

JSON_FILE = 'json/projects.json'
TEMPLATE_FILE = 'projects.html'
RENDERED_FILE = 'projects.html'

def generate(debug):
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
        project_data['desc'] = "".join(project['desc'])
        template_data['projects'][name] = project_data
    template = templateEnv.get_template(TEMPLATE_FILE)
    rendered = open(RENDERED_FILE, 'w')
    rendered.write(template.render(template_data))
    print('projcets page generated!')
    pass
