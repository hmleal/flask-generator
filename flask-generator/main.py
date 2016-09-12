"""
Usage:
    flask-generator start_project <name>
    flask-generator start_blueprint <name>

Options:
    -v --version    Show version.
    -h --help       Show this screen.
"""
import os
import yaml

from docopt import docopt


class GenerateSkeleton:
    def __init__(self, name, output='.', template_name='base'):
        self.app_name = name
        self.template_path = os.path.join(
            'flask-generator/templates/', template_name)

    def handle(self):
        print('\n\tcreate: {0}'.format(self.app_name))

        base_path = '/tmp/'
        os.mkdir(base_path + self.app_name)

        skeleton = self.load_skeleton()
        self.parse(skeleton, parent=self.app_name)

    def parse(self, skeleton, parent):
        for key in skeleton:
            print('\tcreate: {0}/{1}'.format(parent, key['name']))

            if key['type'] == 'dir' and 'children' in key:
                os.mkdir(os.path.join('/tmp', parent) + '/' + key['name'])
                if 'children' in key:
                    new_parent = os.path.join(parent, key['name'])
                    self.parse(key['children'], parent=new_parent)

            if key['type'] == 'file':
                filepath = os.path.join(self.template_path, key['name'])
                with open(filepath, 'r') as f:
                    content = f.read()

                with open(os.path.join('/tmp', parent) + '/' + key['name'], 'w+') as f:
                    f.write(content)

    def load_skeleton(self):
        schema = os.path.join(self.template_path, 'schema.yml')
        with open(schema) as f:
            content = yaml.load(f.read())
        return content['project']

    def load_template(self, filename):
        template = os.path.join(self.template_path, filename)
        with open(template) as f:
            return f.read()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')

    if arguments['start_project']:
        skeleton = GenerateSkeleton(name=arguments['<name>'])
        skeleton.handle()
