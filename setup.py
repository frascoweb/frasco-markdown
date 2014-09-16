from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-markdown',
    version='0.1',
    url='http://github.com/frascoweb/frasco-markdown',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Markdown integration for Frasco",
    long_description=desc(),
    py_modules=['frasco_markdown'],
    platforms='any',
    install_requires=[
        'frasco',
        'Markdown==2.4.1'
    ]
)