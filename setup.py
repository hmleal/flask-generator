try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def load_from(filename):
    with open(filename) as requirements:
        return requirements.read().splitlines()


setup(
    name='Flask Generator',
    version='0.1',
    description='Generator tool to quickly create flask application skeleton.',
    long_description='Generator tool to quickly create flask application skeleton.',
    author='Henrique Leal',
    author_email='hm.leal@hotmail.com',
    packages=[
        'flask-generator'
    ],
    package_dir={
        'flask-generator': 'flask-generator'
    },
    install_requires=load_from('requirements.txt')
)
