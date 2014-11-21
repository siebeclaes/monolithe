# -*- coding: utf-8 -*-
"""

NUEgressACLTemplate
This file has been autogenerated by Swagger  and should not be modified.

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from bambou import NURESTObject

from ..fetchers import NUEgressACLTemplateEntriesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUVirtualMachinesFetcher


class NUEgressACLTemplate(NURESTObject):
    """ Represents a EgressACLTemplate object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUEgressACLTemplate instance """

        super(NUEgressACLTemplate, self).__init__()

        # Read/Write Attributes
        self.default_install_acl_implicit_rules = None  #  If enabled, implicit rule will allow intra domain traffic by default - int
        self.default_allow_ip = None  #  If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries - int
        self.default_allow_non_ip = None  #  If enabled, non ip traffic will be dropped - int
        self.description = None  #  A description of the entity - int
        self.name = None  #  The name of the entity - int
        self.active = None  #  If enabled, it means that this ACL or QOS entry is active - int
        
        self.expose_attribute(local_name=u"default_install_acl_implicit_rules", remote_name=u"defaultInstallACLImplicitRules", attribute_type=int)
        self.expose_attribute(local_name=u"default_allow_ip", remote_name=u"defaultAllowIP", attribute_type=int)
        self.expose_attribute(local_name=u"default_allow_non_ip", remote_name=u"defaultAllowNonIP", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=int)
        
        # Fetchers
        self.egress_acl_template_entries = []
        self.egress_acl_template_entries_fetcher = NUEgressACLTemplateEntriesFetcher.fetcher_with_object(nurest_object=self, local_name=u"egress_acl_template_entries")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.virtual_machines = []
        self.virtual_machines_fetcher = NUVirtualMachinesFetcher.fetcher_with_object(nurest_object=self, local_name=u"virtual_machines")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"egressacltemplate"

