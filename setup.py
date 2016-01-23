from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'guajiro/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
        name='Scrapy',
        version=version,
        url='http://scrapy.org',
        description='Insanely fast high-productivity web services framework built fo enterprise.',
        long_description=open('README.rst').read(),
        author='Dairon Medina',
        maintainer='Dairon Medina',
        maintainer_email='dairon.medina@gmail.com',
        license='BSD',
        packages=find_packages(exclude=('tests', 'tests.*')),
        include_package_data=True,
        zip_safe=False,
        entry_points={
            'console_scripts': ['guajiro = guajiro.cmdline:execute']
        },
        classifiers=[
            'Framework :: Guajiro',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        install_requires=[
            'Twisted>=10.0.0',
        ],
)
