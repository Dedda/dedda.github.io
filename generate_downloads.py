__author__ = 'dedda'

import json
import jinja2

TEMPLATES_FOLDER = 'template/'

JSON_FILE = 'json/projects.json'
TEMPLATE_FILE = 'download.html'
RENDERED_FILE = 'download.html'

def generate(debug):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
    template_env = jinja2.Environment(loader=template_loader)
    print('generating projects page...')
    json_data = open(JSON_FILE).read()
    data = json.loads(json_data)
    template_data = {'debug' : debug}
    template_data['projects'] = {}
    for (name, project) in data.items():
        project_data = {}
        if 'downloads' in project:
            print('download in project ' + name)
            downloads = {}
            for downloadName in project['downloads']:
                downloads[downloadName] = 'download/' + project['downloads'][downloadName]
            project_data['downloads'] = downloads
            project_data['url'] = project['url']
            if 'logo' in project:
                if project['logo']:
                    project_data['logo'] = 'img/' + project['logo']
            template_data['projects'][name] = project_data
    template = template_env.get_template(TEMPLATE_FILE)
    rendered = open(RENDERED_FILE, 'w')
    rendered.write(template.render(template_data))
    print('download page generated!')
    pass