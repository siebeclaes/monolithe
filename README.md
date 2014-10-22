pymodel
=======

IMPORTANT: This will be used as the Nuage Netowork Python SDK.
It means the name will probably change within the next few weeks.


Nuage Network Python SDK is based on Bambou.

Dependancies
------------

Python dependencies:
* bambou (http://github.mv.usa.alcatel.com/chserafi/bambou)

WARNING: You will need to install `bambou` library first.

Setup your Python Virtual Environment
-------------------------------------

Install your virtualenv

    $ virtualenv --no-site-packages pymodel-env

Activate your environment

    $ cd pymodel-env
    $ source bin/activate
    (pymodel-env) $

Installation from package
-------------------------

Note: Before install, make sure you have activated your python environment

Download the `tar.gz` file that is distributed in `dist` directory and install it using pip:

    (pymodel-env) $ pip install git+ssh://github.mv.usa.alcatel.com/chserafi/bambou#egg=bambou
    (pymodel-env) $ pip install git+ssh://github.mv.usa.alcatel.com/chserafi/pymodel.git#egg=pymodel

Installation from package in development
----------------------------------------

Note: Before install, make sure you have activated your python environment

This enables you to install both packages and see sources in your python environment

    (pymodel-env) $ pip install -e git+ssh://github.mv.usa.alcatel.com/chserafi/bambou#egg=bambou
    (pymodel-env) $ pip install -e git+ssh://github.mv.usa.alcatel.com/chserafi/pymodel.git#egg=pymodel


Installation from sources
-------------------------

Get the sources

    (pymodel-env) $ git clone http://github.mv.usa.alcatel.com/cserafin/pymodel.git
    (pymodel-env) $ cd pymodel

Install dependencies

    (pymodel-env) $ pip install -r requirements.txt


Example
-------

Here is a quick example !

     from pymodel import NUVSDSession
     from pymodel import NUEnterprise, NUUser, NUDomainTemplate, NUDomain

     # 'Setting a log level to see what happens (Optionnal)'
     import logging
     bambou_log = logging.getLogger('bambou')
     bambou_log.setLevel(logging.DEBUG)
     bambou_log.addHandler(logging.StreamHandler())

     # 'Create a session for CSPRoot'
     session = NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://135.227.220.152:8443/nuage/api/v3_0')

     # 'Start using the CSPRoot session
     session.start()
     csproot = session.user

     # 'Create an enterprise with csproot user'
     enterprise = NUEnterprise()
     enterprise.name = u'Enterprise example'
     csproot.create_enterprise(enterprise)

     # 'Create a domain template and an instance'
     domain_template = NUDomainTemplate()
     domain_template.name = u'Domain Template example'
     enterprise.create_gatewaytemplate(domain_template)
     domain = NUDomain()
     domain.name = u'Instance Domain example'
     enterprise.instantiate_domain(domain, domain_template)

     # Stop using the CSPRoot session
     session.stop()


Check a complete example in `examples/scripts.py`. You can launch the example using the following command line:

    $ python example/script.py

Packaging
---------

Creating a tar.gz package is possible using the following command line :

    $ python setup.py sdist

