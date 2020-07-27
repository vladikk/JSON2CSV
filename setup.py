from setuptools import setup

setup(name='json2csv',
      version='2.0.0',
      author='Vladik Khononov',
      packages=['json2csv'],
      install_requires=['six==1.10.0'],
      entry_points={
          'console_scripts': [
              'json2csv = json2csv.__main__:main'
          ]
      })
      
