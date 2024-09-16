from setuptools import find_packages, setup

def get_requirements(filepath):
    '''
    this function will return the list of requirements.
    '''
    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements


setup(
    name='MLproject',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)