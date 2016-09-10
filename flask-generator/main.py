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
    def __init__(self, name, template_name='base'):
        self.template_path = os.path.join(
            'flask-generator/templates/', template_name)

    def handle(self):
        skeleton = self.load_skeleton()

        self.parse(skeleton)

    def parse(self, skeleton):
        for key in skeleton:
            print(key)
            if key['type'] == 'file':
                pass  # create file and put template inside
            elif key['type'] == 'dir':
                pass  # create dir and call parse again
            else:
                raise Exception('Erro boladao')

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
