from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pydbc',
    url='https://github.com/gbletsch/pydbc',
    author='Guilherme Boelhouwer Letsch',
    author_email='gbletsch@gmail.com',
    # Needed to actually package something
    packages=['pydbc'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'tempfile', 'os', 'dbfread'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Handle a .dbc file and return it as a pandas.DataFrame.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)