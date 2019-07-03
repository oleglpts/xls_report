from setuptools import setup

setup(name='xls_report',
      version='0.0.1',
      packages=['xls_report'],
      url='https://github.com/oleglpts/xls_report',
      license='MIT',
      platforms='any',
      author='Oleg Lupats',
      author_email='oleglupats@gmail.com',
      description='Database report generation in .xls format according to the xml description',
      long_description=open('README.md').read(),
      zip_safe=False,
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5'
      ],
      setup_requires=['bottle>=0.12.17', 'lxml>=4.3.4', 'pyodbc>=4.0.26', 'xlwt>=1.3.0'])
