# -*- coding: utf-8 -*-
"""

NUVRS
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

from ..fetchers import NUJobsFetcher
from ..fetchers import NUHSCsFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUPortStatussFetcher
from ..fetchers import NUVSCsFetcher
from ..fetchers import NUMultiNICVPortsFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUAlarmsFetcher


class NUVRS(NURESTObject):
    """ Represents a VRS object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUVRS instance """

        super(NUVRS, self).__init__()

        # Read/Write Attributes
        self.parent_i_ds = None  #  Holds VRS controllers ids - int
        self.cluster_node_role = None  #  Indicate that the controller associated is primary, secondary or unknown. - int
        self.messages = None  #  An array of degraded messages. - int
        self.dynamic = None  #  Flag to indicate it is dynamically configured or not. - int
        self.hypervisor_connection_state = None  #  The VRS connection state with the hypervisor. - int
        self.hypervisor_identifier = None  #  The hypervisor IP (or name) associated with the VRS. - int
        self.hypervisor_name = None  #  The hypervisor name associated with the VRS. - int
        self.hypervisor_type = None  #  The hypervisor type associated with the VRS. - int
        self.address = None  #  The IP of the VRS entity - int
        self.jsonrpc_connection_state = None  #  The current JSON RPC connection status. - int
        self.last_event_name = None  #  The last event name from the hypervisor. - int
        self.last_event_object = None  #  The last event object (including metadata) from the hypervisor. - int
        self.last_event_timestamp = None  #  The last event timestamp from the hypervisor. - long
        self.management_ip = None  #  The management IP of the VRS entity - int
        self.multi_nicv_port_enabled = None  #  VRS is in Multi-NIC VPORT Mode - int
        self.number_of_bridge_interfaces = None  #  Number of bridge interfaces defined in this VRS. - int
        self.number_of_host_interfaces = None  #  Number of host interfaces defined in this VRS. - int
        self.number_of_virtual_machines = None  #  Number of VMs defined in this VRS. - int
        self.peer = None  #  The redundant peer id for the current VRS. - int
        self.personality = None  #  VRS personality. - int
        self.role = None  #  Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways. - int
        self.uptime = None  #  How long the VRS was up. - long
        self.average_cpu_usage = None  #  Average CPU usage percentage. - float
        self.average_memory_usage = None  #  Average memory usage percentage. - float
        self.current_cpu_usage = None  #  Current CPU usage percentage. - float
        self.current_memory_usage = None  #  Current memory usage percentage. - float
        self.description = None  #  Description of the entity. - int
        self.disks = None  #  Set of disk usage details. - int
        self.last_state_change = None  #  Last state change timestamp (in millis). - long
        self.location = None  #  Identifies the entity to be associated with a location. - int
        self.name = None  #  Identifies the entity with a name. - int
        self.peak_cpu_usage = None  #  Peek CPU usage percentage. - float
        self.peak_memory_usage = None  #  Peek memory usage percentage. - float
        self.product_version = None  #  Product version supported by this entity. - int
        self.status = None  #  Computed status of the entity. - int
        
        self.expose_attribute(local_name=u"parent_i_ds", remote_name=u"parentIDs", attribute_type=int)
        self.expose_attribute(local_name=u"cluster_node_role", remote_name=u"clusterNodeRole", attribute_type=int)
        self.expose_attribute(local_name=u"messages", remote_name=u"messages", attribute_type=int)
        self.expose_attribute(local_name=u"dynamic", remote_name=u"dynamic", attribute_type=int)
        self.expose_attribute(local_name=u"hypervisor_connection_state", remote_name=u"hypervisorConnectionState", attribute_type=int)
        self.expose_attribute(local_name=u"hypervisor_identifier", remote_name=u"hypervisorIdentifier", attribute_type=int)
        self.expose_attribute(local_name=u"hypervisor_name", remote_name=u"hypervisorName", attribute_type=int)
        self.expose_attribute(local_name=u"hypervisor_type", remote_name=u"hypervisorType", attribute_type=int)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=int)
        self.expose_attribute(local_name=u"jsonrpc_connection_state", remote_name=u"JSONRPCConnectionState", attribute_type=int)
        self.expose_attribute(local_name=u"last_event_name", remote_name=u"lastEventName", attribute_type=int)
        self.expose_attribute(local_name=u"last_event_object", remote_name=u"lastEventObject", attribute_type=int)
        self.expose_attribute(local_name=u"last_event_timestamp", remote_name=u"lastEventTimestamp", attribute_type=long)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=int)
        self.expose_attribute(local_name=u"multi_nicv_port_enabled", remote_name=u"multiNICVPortEnabled", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_bridge_interfaces", remote_name=u"numberOfBridgeInterfaces", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_host_interfaces", remote_name=u"numberOfHostInterfaces", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_virtual_machines", remote_name=u"numberOfVirtualMachines", attribute_type=int)
        self.expose_attribute(local_name=u"peer", remote_name=u"peer", attribute_type=int)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=int)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=int)
        self.expose_attribute(local_name=u"uptime", remote_name=u"uptime", attribute_type=long)
        self.expose_attribute(local_name=u"average_cpu_usage", remote_name=u"averageCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"average_memory_usage", remote_name=u"averageMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"current_cpu_usage", remote_name=u"currentCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"current_memory_usage", remote_name=u"currentMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"disks", remote_name=u"disks", attribute_type=int)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=long)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"peak_cpu_usage", remote_name=u"peakCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"peak_memory_usage", remote_name=u"peakMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=int)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=int)
        
        # Fetchers
        self.jobs = []
        self.jobs_fetcher = NUJobsFetcher.fetcher_with_object(nurest_object=self, local_name=u"jobs")
        self.hscs = []
        self.hscs_fetcher = NUHSCsFetcher.fetcher_with_object(nurest_object=self, local_name=u"hscs")
        self.v_ports = []
        self.v_ports_fetcher = NUVPortsFetcher.fetcher_with_object(nurest_object=self, local_name=u"v_ports")
        self.port_statuss = []
        self.port_statuss_fetcher = NUPortStatussFetcher.fetcher_with_object(nurest_object=self, local_name=u"port_statuss")
        self.vscs = []
        self.vscs_fetcher = NUVSCsFetcher.fetcher_with_object(nurest_object=self, local_name=u"vscs")
        self.multi_nicv_ports = []
        self.multi_nicv_ports_fetcher = NUMultiNICVPortsFetcher.fetcher_with_object(nurest_object=self, local_name=u"multi_nicv_ports")
        self.virtual_machines = []
        self.virtual_machines_fetcher = NUVirtualMachinesFetcher.fetcher_with_object(nurest_object=self, local_name=u"virtual_machines")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.alarms = []
        self.alarms_fetcher = NUAlarmsFetcher.fetcher_with_object(nurest_object=self, local_name=u"alarms")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vrs"

