#!/usr/bin/env python

from distutils.core import setup

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

setup(name='django-allauth-providers-ko',
      version='1.0',
      description='kakao/naver providers for django-allauth',
      author='AskDjango',
      author_email='me@nomade.kr',
      classifiers=CLASSIFIERS,
      url='https://facebook.com/groups/askdjango',
      packages=['askdjango_providers', 'askdjango_providers.kakao', 'askdjango_providers.naver'],
     )

