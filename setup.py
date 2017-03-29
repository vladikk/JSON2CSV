from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(name='json2csv',
      version='2.0.0',
      author='Vladik Khononov',
      packages=['json2csv'],
      install_requires=reqs,
      entry_points={
          'console_scripts': [
              'json2csv = json2csv.__main__:main'
          ]
      })
      
