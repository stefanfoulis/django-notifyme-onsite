from setuptools import setup, find_packages
import os

version = __import__('notifyme_onsite').__version__

def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
]

setup(
    name="django-notifyme-onsite",
    version=version,
    url='http://github.com/stefanfoulis/django-notifyme-onsite',
    license='BSD',
    platforms=['OS Independent'],
    description="An on site delivery backend for django-notifyme",
    long_description=read('README.rst'),
    author='Stefan Foulis',
    author_email='stefan.foulis@gmail.com',
    maintainer='Stefan Foulis',
    maintainer_email='stefan.foulis@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
