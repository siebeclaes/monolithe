# -*- coding: utf-8 -*-

from monolithe.tests.functional import FunctionalTest
from monolithe.lib.parsers import SwaggerParser, SpecificationParser
from monolithe.lib.transformers import SwaggerTransformer, SpecificationTransformer

from monolithe.lib.utils.printer import Printer


class SpecificationTransformerTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerParser(path=cls.get_swagger_files_path(), vsdurl=None, apiversion=None)
        swagger_resources = parser.run()

        cls.specifications = SwaggerTransformer.get_specifications(resources=swagger_resources, version=None)

    @classmethod
    def tearDownClass(cls):
        """ Clean up context

        """
        cls.specifications = None

    def test_transformer_returns_all_objects_rest_names(self):
        """ SpecificationTransformer returns all objects with correct rest names

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        self.assertEqual(objects.keys(), [u'addressrange',
                                          u'alarm',
                                          u'app',
                                          u'application',
                                          u'applicationservice',
                                          u'autodiscoveredgateway',
                                          u'bgppeer',
                                          u'bootstrap',
                                          u'bootstrapactivation',
                                          u'bridgeinterface',
                                          u'component',
                                          u'dhcpoption',
                                          u'domain',
                                          u'domaintemplate',
                                          u'dscpforwardingclassmapping',
                                          u'dscpforwardingclasstable',
                                          u'egressaclentrytemplate',
                                          u'egressacltemplate',
                                          u'egressqospolicy',
                                          u'enterprise',
                                          u'enterprisenetwork',
                                          u'enterprisepermission',
                                          u'enterpriseprofile',
                                          u'eventlog',
                                          u'floatingip',
                                          u'flow',
                                          u'flowforwardingpolicy',
                                          u'flowsecuritypolicy',
                                          u'gateway',
                                          u'gatewaytemplate',
                                          u'globalmetadata',
                                          u'group',
                                          u'hostinterface',
                                          u'hsc',
                                          u'infraconfig',
                                          u'infrastructuregatewayprofile',
                                          u'infrastructureportprofile',
                                          u'ingressaclentrytemplate',
                                          u'ingressacltemplate',
                                          u'ingressadvfwdentrytemplate',
                                          u'ingressadvfwdtemplate',
                                          u'ipreservation',
                                          u'job',
                                          u'l2domain',
                                          u'l2domaintemplate',
                                          u'ldapconfiguration',
                                          u'license',
                                          u'location',
                                          u'me',
                                          u'metadata',
                                          u'mirrordestination',
                                          u'monitoringport',
                                          u'multicastchannelmap',
                                          u'multicastrange',
                                          u'multinicvport',
                                          u'natmapentry',
                                          u'networklayout',
                                          u'nsgateway',
                                          u'nsgatewaytemplate',
                                          u'patnatpool',
                                          u'permission',
                                          u'policydecision',
                                          u'policygroup',
                                          u'policygrouptemplate',
                                          u'port',
                                          u'porttemplate',
                                          u'publicnetwork',
                                          u'qos',
                                          u'ratelimiter',
                                          u'redirectiontarget',
                                          u'redirectiontargettemplate',
                                          u'redundancygroup',
                                          u'resync',
                                          u'service',
                                          u'sharednetworkresource',
                                          u'staticroute',
                                          u'statistics',
                                          u'statisticscollector',
                                          u'statisticspolicy',
                                          u'subnet',
                                          u'subnettemplate',
                                          u'systemconfig',
                                          u'tca',
                                          u'tier',
                                          u'user',
                                          u'virtualip',
                                          u'vlan',
                                          u'vlantemplate',
                                          u'vm',
                                          u'vminterface',
                                          u'vpnconnection',
                                          u'vport',
                                          u'vportmirror',
                                          u'vrs',
                                          u'vsc',
                                          u'vsd',
                                          u'vsp',
                                          u'zone',
                                          u'zonetemplate'])

    def test_transformer_returns_valid_rest_user(self):
        """ SpecificationTransformer returns REST User with correct rest names

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        obj = objects['me']

        self.assertEqual(obj.name, 'RESTUser')
        self.assertEqual(obj.remote_name, 'me')
        self.assertEqual(obj.plural_name, u'RESTUsers')
        self.assertEqual(obj.package, u'/usermgmt')
        self.assertEqual(obj.description, u'Object that identifies the user functions')

        # Attributes

        local_names = [attribute.local_name for attribute in obj.attributes]
        remote_names = [attribute.remote_name for attribute in obj.attributes]
        local_types = [attribute.local_type for attribute in obj.attributes]

        self.assertEqual(local_names, [u'avatar_data',
                                       u'avatar_type',
                                       u'email', 'enterprise_id', 'enterprise_name',
                                       u'first_name',
                                       u'last_name',
                                       u'mobile_number',
                                       u'password', 'role',
                                       u'user_name'])

        self.assertEqual(remote_names, [u'avatarData',
                                        u'avatarType',
                                        u'email', 'enterpriseID', 'enterpriseName',
                                        u'firstName',
                                        u'lastName',
                                        u'mobileNumber',
                                        u'password', 'role',
                                        u'userName'])

        self.assertEqual(local_types, [u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str'])

        # Parents apis
        parents = obj.apis['parents']
        paths = parents.keys()

        self.assertEqual(paths, [])

        # Self apis
        self_apis = obj.apis['self']

        paths = self_apis.keys()
        self.assertEqual(paths, [])

        # Children apis
        children = obj.apis['children']

        paths = children.keys()

        self.assertEqual(paths, [u'/applicationservices',
                                 u'/autodiscoveredgateways',
                                 u'/domains',
                                 u'/egressaclentrytemplates',
                                 u'/egressacltemplates',
                                 u'/egressqospolicies',
                                 u'/enterpriseprofiles',
                                 u'/enterprises',
                                 u'/floatingips',
                                 u'/gateways',
                                 u'/gatewaytemplates',
                                 u'/globalmetadatas',
                                 u'/infrastructuregatewayprofiles',
                                 u'/infrastructureportprofiles',
                                 u'/ingressaclentrytemplates',
                                 u'/ingressacltemplates',
                                 u'/l2domains',
                                 u'/licenses',
                                 u'/mirrordestinations',
                                 u'/multicastchannelmaps',
                                 u'/networklayout',
                                 u'/nsgateways',
                                 u'/nsgatewaytemplates',
                                 u'/patnatpools',
                                 u'/policygroups',
                                 u'/ratelimiters',
                                 u'/redirectiontargets',
                                 u'/redundancygroups',
                                 u'/sharednetworkresources',
                                 u'/staticroutes',
                                 u'/statisticscollector',
                                 u'/subnets',
                                 u'/systemconfigs',
                                 u'/tcas',
                                 u'/vminterfaces',
                                 u'/vms',
                                 u'/vsps',
                                 u'/zones'])

        child_info = children.values()
        resource_names = [info.resource_name for info in child_info]
        remote_names = [info.remote_name for info in child_info]
        plural_names = [info.plural_name for info in child_info]
        instance_plural_names = [info.instance_plural_name for info in child_info]

        self.assertEqual(resource_names, [u'applicationservices',
                                          u'autodiscoveredgateways',
                                          u'domains',
                                          u'egressaclentrytemplates',
                                          u'egressacltemplates',
                                          u'egressqospolicies',
                                          u'enterpriseprofiles',
                                          u'enterprises',
                                          u'floatingips',
                                          u'gateways',
                                          u'gatewaytemplates',
                                          u'globalmetadatas',
                                          u'infrastructuregatewayprofiles',
                                          u'infrastructureportprofiles',
                                          u'ingressaclentrytemplates',
                                          u'ingressacltemplates',
                                          u'l2domains',
                                          u'licenses',
                                          u'mirrordestinations',
                                          u'multicastchannelmaps',
                                          u'networklayout',
                                          u'nsgateways',
                                          u'nsgatewaytemplates',
                                          u'patnatpools',
                                          u'policygroups',
                                          u'ratelimiters',
                                          u'redirectiontargets',
                                          u'redundancygroups',
                                          u'sharednetworkresources',
                                          u'staticroutes',
                                          u'statisticscollector',
                                          u'subnets',
                                          u'systemconfigs',
                                          u'tcas',
                                          u'vminterfaces',
                                          u'vms',
                                          u'vsps',
                                          u'zones'])

        self.assertEqual(remote_names, [u'applicationservice',
                                        u'autodiscoveredgateway',
                                        u'domain',
                                        u'egressaclentrytemplate',
                                        u'egressacltemplate',
                                        u'egressqospolicy',
                                        u'enterpriseprofile',
                                        u'enterprise',
                                        u'floatingip',
                                        u'gateway',
                                        u'gatewaytemplate',
                                        u'globalmetadata',
                                        u'infrastructuregatewayprofile',
                                        u'infrastructureportprofile',
                                        u'ingressaclentrytemplate',
                                        u'ingressacltemplate',
                                        u'l2domain',
                                        u'license',
                                        u'mirrordestination',
                                        u'multicastchannelmap',
                                        u'networklayout',
                                        u'nsgateway',
                                        u'nsgatewaytemplate',
                                        u'patnatpool',
                                        u'policygroup',
                                        u'ratelimiter',
                                        u'redirectiontarget',
                                        u'redundancygroup',
                                        u'sharednetworkresource',
                                        u'staticroute',
                                        u'statisticscollector',
                                        u'subnet',
                                        u'systemconfig',
                                        u'tca',
                                        u'vminterface',
                                        u'vm',
                                        u'vsp',
                                        u'zone'])

        self.assertEqual(plural_names, [u'ApplicationServices',
                                        u'AutoDiscoveredGateways',
                                        u'Domains',
                                        u'EgressACLEntryTemplates',
                                        u'EgressACLTemplates',
                                        u'EgressQOSPolicies',
                                        u'EnterpriseProfiles',
                                        u'Enterprises',
                                        u'FloatingIps',
                                        u'Gateways',
                                        u'GatewayTemplates',
                                        u'GlobalMetadatas',
                                        u'InfrastructureGatewayProfiles',
                                        u'InfrastructurePortProfiles',
                                        u'IngressACLEntryTemplates',
                                        u'IngressACLTemplates',
                                        u'L2Domains',
                                        u'Licenses',
                                        u'MirrorDestinations',
                                        u'MultiCastChannelMaps',
                                        u'NetworkLayouts',
                                        u'NSGateways',
                                        u'NSGatewayTemplates',
                                        u'PATNATPools',
                                        u'PolicyGroups',
                                        u'RateLimiters',
                                        u'RedirectionTargets',
                                        u'RedundancyGroups',
                                        u'SharedNetworkResources',
                                        u'StaticRoutes',
                                        u'StatsCollectorInfos',
                                        u'Subnets',
                                        u'SystemConfigs',
                                        u'TCAs',
                                        u'VMInterfaces',
                                        u'VMs',
                                        u'VSPs',
                                        u'Zones'])

        self.assertEqual(instance_plural_names, [u'application_services',
                                                 u'auto_discovered_gateways',
                                                 u'domains',
                                                 u'egress_acl_entry_templates',
                                                 u'egress_acl_templates',
                                                 u'egress_qos_policies',
                                                 u'enterprise_profiles',
                                                 u'enterprises',
                                                 u'floating_ips',
                                                 u'gateways',
                                                 u'gateway_templates',
                                                 u'global_metadatas',
                                                 u'infrastructure_gateway_profiles',
                                                 u'infrastructure_port_profiles',
                                                 u'ingress_acl_entry_templates',
                                                 u'ingress_acl_templates',
                                                 u'l2_domains',
                                                 u'licenses',
                                                 u'mirror_destinations',
                                                 u'multi_cast_channel_maps',
                                                 u'network_layouts',
                                                 u'ns_gateways',
                                                 u'ns_gateway_templates',
                                                 u'patnat_pools',
                                                 u'policy_groups',
                                                 u'rate_limiters',
                                                 u'redirection_targets',
                                                 u'redundancy_groups',
                                                 u'shared_network_resources',
                                                 u'static_routes',
                                                 u'stats_collector_infos',
                                                 u'subnets',
                                                 u'system_configs',
                                                 u'tcas',
                                                 u'vm_interfaces',
                                                 u'vms',
                                                 u'vsps',
                                                 u'zones'])

    def test_transformer_returns_valid_enterprise(self):
        """ SpecificationTransformer returns Enterprise with all correct information

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        obj = objects['enterprise']

        self.assertEqual(obj.name, 'Enterprise')
        self.assertEqual(obj.remote_name, 'enterprise')
        self.assertEqual(obj.plural_name, u'Enterprises')
        self.assertEqual(obj.package, u'/usermgmt')
        self.assertEqual(obj.description, u'Definition of the enterprise object. This is the top level object that represents an enterprise or organization.')


        # Attributes
        local_names = [attribute.local_name for attribute in obj.attributes]
        remote_names = [attribute.remote_name for attribute in obj.attributes]
        local_types = [attribute.local_type for attribute in obj.attributes]

        self.assertEqual(local_names, [u'allow_advanced_qos_configuration',
                                       u'allow_gateway_management',
                                       u'allow_trusted_forwarding_class',
                                       u'allowed_forwarding_classes',
                                       u'avatar_data',
                                       u'avatar_type',
                                       u'customer_id',
                                       u'description',
                                       u'dhcp_lease_interval',
                                       u'enterprise_profile_id',
                                       u'floating_ips_quota',
                                       u'floating_ips_used',
                                       u'name'])

        self.assertEqual(remote_names, [u'allowAdvancedQOSConfiguration',
                                        u'allowGatewayManagement',
                                        u'allowTrustedForwardingClass',
                                        u'allowedForwardingClasses',
                                        u'avatarData',
                                        u'avatarType',
                                        u'customerID',
                                        u'description',
                                        u'DHCPLeaseInterval',
                                        u'enterpriseProfileID',
                                        u'floatingIPsQuota',
                                        u'floatingIPsUsed',
                                        u'name'])

        self.assertEqual(local_types, ['bool',
                                       'bool',
                                       'bool',
                                       'str',
                                       'str',
                                       'str',
                                       'long',
                                       'str',
                                       'int',
                                       'str',
                                       'int',
                                       'int',
                                       'str'])


        # Parents apis
        parents = obj.apis['parents']
        paths = parents.keys()
        self.assertEqual(paths, [u'/enterpriseprofiles/{id}/enterprises', u'/enterprises'])

        # Self apis
        self_apis = obj.apis['self']
        paths = self_apis.keys()
        self.assertEqual(paths, [u'/enterprises/{id}'])

        # Children apis
        children = obj.apis['children']
        paths = children.keys()

        self.assertEqual(paths, [u'/enterprises/{id}/alarms',
                                 u'/enterprises/{id}/allalarms',
                                 u'/enterprises/{id}/applications',
                                 u'/enterprises/{id}/applicationservices',
                                 u'/enterprises/{id}/domains',
                                 u'/enterprises/{id}/domaintemplates',
                                 u'/enterprises/{id}/dscpforwardingclasstables',
                                 u'/enterprises/{id}/egressqospolicies',
                                 u'/enterprises/{id}/enterprisenetworks',
                                 u'/enterprises/{id}/eventlogs',
                                 u'/enterprises/{id}/gateways',
                                 u'/enterprises/{id}/gatewaytemplates',
                                 u'/enterprises/{id}/groups',
                                 u'/enterprises/{id}/infrastructureportprofiles',
                                 u'/enterprises/{id}/jobs',
                                 u'/enterprises/{id}/l2domains',
                                 u'/enterprises/{id}/l2domaintemplates',
                                 u'/enterprises/{id}/ldapconfigurations',
                                 u'/enterprises/{id}/multicastchannelmaps',
                                 u'/enterprises/{id}/nsgateways',
                                 u'/enterprises/{id}/nsgatewaytemplates',
                                 u'/enterprises/{id}/patnatpools',
                                 u'/enterprises/{id}/publicnetworks',
                                 u'/enterprises/{id}/ratelimiters',
                                 u'/enterprises/{id}/redundancygroups',
                                 u'/enterprises/{id}/users',
                                 u'/enterprises/{id}/vms'])

        child_info = children.values()
        resource_names = [info.resource_name for info in child_info]
        remote_names = [info.remote_name for info in child_info]
        plural_names = [info.plural_name for info in child_info]
        instance_plural_names = [info.instance_plural_name for info in child_info]

        self.assertEqual(resource_names, [u'alarms',
                                          u'allalarms',
                                          u'applications',
                                          u'applicationservices',
                                          u'domains',
                                          u'domaintemplates',
                                          u'dscpforwardingclasstables',
                                          u'egressqospolicies',
                                          u'enterprisenetworks',
                                          u'eventlogs',
                                          u'gateways',
                                          u'gatewaytemplates',
                                          u'groups',
                                          u'infrastructureportprofiles',
                                          u'jobs',
                                          u'l2domains',
                                          u'l2domaintemplates',
                                          u'ldapconfigurations',
                                          u'multicastchannelmaps',
                                          u'nsgateways',
                                          u'nsgatewaytemplates',
                                          u'patnatpools',
                                          u'publicnetworks',
                                          u'ratelimiters',
                                          u'redundancygroups',
                                          u'users',
                                          u'vms'])

        self.assertEqual(remote_names, [u'alarm',
                                        u'allalarm',
                                        u'application',
                                        u'applicationservice',
                                        u'domain',
                                        u'domaintemplate',
                                        u'dscpforwardingclasstable',
                                        u'egressqospolicy',
                                        u'enterprisenetwork',
                                        u'eventlog',
                                        u'gateway',
                                        u'gatewaytemplate',
                                        u'group',
                                        u'infrastructureportprofile',
                                        u'job',
                                        u'l2domain',
                                        u'l2domaintemplate',
                                        u'ldapconfiguration',
                                        u'multicastchannelmap',
                                        u'nsgateway',
                                        u'nsgatewaytemplate',
                                        u'patnatpool',
                                        u'publicnetwork',
                                        u'ratelimiter',
                                        u'redundancygroup',
                                        u'user',
                                        u'vm'])

        self.assertEqual(plural_names, [u'Alarms',
                                        u'Alarms',
                                        u'Apps',
                                        u'ApplicationServices',
                                        u'Domains',
                                        u'DomainTemplates',
                                        u'DSCPForwardingClassTables',
                                        u'EgressQOSPolicies',
                                        u'EnterpriseNetworks',
                                        u'EventLogs',
                                        u'Gateways',
                                        u'GatewayTemplates',
                                        u'Groups',
                                        u'InfrastructurePortProfiles',
                                        u'Jobs',
                                        u'L2Domains',
                                        u'L2DomainTemplates',
                                        u'LDAPConfigurations',
                                        u'MultiCastChannelMaps',
                                        u'NSGateways',
                                        u'NSGatewayTemplates',
                                        u'PATNATPools',
                                        u'PublicNetworkMacros',
                                        u'RateLimiters',
                                        u'RedundancyGroups',
                                        u'Users',
                                        u'VMs'])

        self.assertEqual(instance_plural_names, [u'alarms',
                                                 u'all_alarms',
                                                 u'apps',
                                                 u'application_services',
                                                 u'domains',
                                                 u'domain_templates',
                                                 u'dscp_forwarding_class_tables',
                                                 u'egress_qos_policies',
                                                 u'enterprise_networks',
                                                 u'event_logs',
                                                 u'gateways',
                                                 u'gateway_templates',
                                                 u'groups',
                                                 u'infrastructure_port_profiles',
                                                 u'jobs',
                                                 u'l2_domains',
                                                 u'l2_domain_templates',
                                                 u'ldap_configurations',
                                                 u'multi_cast_channel_maps',
                                                 u'ns_gateways',
                                                 u'ns_gateway_templates',
                                                 u'patnat_pools',
                                                 u'public_network_macros',
                                                 u'rate_limiters',
                                                 u'redundancy_groups',
                                                 u'users',
                                                 u'vms'])


class ManualSpecificationTransformerTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        path = cls.get_specificication_files_path()

        cls.specifications = SpecificationParser.run(path)

    @classmethod
    def tearDownClass(cls):
        """ Clean up context

        """
        cls.specifications = None

    def test_transformer_returns_valid_vcenter(self):
        """ SpecificationTransformer from manual specification returns a VCenter with all valid information

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        vcenter = objects['vcenter']

        self.assertEqual(vcenter.name, 'VCenter')
        self.assertEqual(vcenter.remote_name, 'vcenter')
        self.assertEqual(vcenter.plural_name, u'VCenters')

        # Attributes
        local_names = [attribute.local_name for attribute in vcenter.attributes]
        remote_names = [attribute.remote_name for attribute in vcenter.attributes]
        local_types = [attribute.local_type for attribute in vcenter.attributes]

        self.assertEqual(local_names, [u'allow_data_dhcp',
                                       u'allow_mgmt_dhcp',
                                       u'customized_script_url',
                                       u'data_dns1',
                                       u'data_dns2',
                                       u'data_gateway',
                                       u'data_network_portgroup',
                                       u'datapath_sync_timeout',
                                       u'description',
                                       u'dhcp_relay_server',
                                       u'flow_eviction_threshold',
                                       u'http_port',
                                       u'https_port',
                                       u'ip_address',
                                       u'mgmt_dns1',
                                       u'mgmt_dns2',
                                       u'mgmt_gateway',
                                       u'mgmt_network_portgroup',
                                       u'mtu',
                                       u'multi_vmssupport',
                                       u'multicast_interface_ip',
                                       u'multicast_interface_netmask',
                                       u'multicast_range',
                                       u'multicast_source_portgroup',
                                       u'name',
                                       u'nfs_log_server',
                                       u'nfs_mount_path',
                                       u'ntp_server1',
                                       u'ntp_server2',
                                       u'password',
                                       u'personality',
                                       u'portgroup_metadata',
                                       u'primary_nuage_controller',
                                       u'secondary_nuage_controller',
                                       u'separate_data_network',
                                       u'static_route',
                                       u'static_route_gateway',
                                       u'user_name',
                                       u'v_require_nuage_metadata',
                                       u'vm_network_portgroup',
                                       u'vrs_config_id'])

        self.assertEqual(remote_names, [u'allowDataDHCP',
                                        u'allowMgmtDHCP',
                                        u'customizedScriptURL',
                                        u'dataDNS1',
                                        u'dataDNS2',
                                        u'dataGateway',
                                        u'dataNetworkPortgroup',
                                        u'datapathSyncTimeout',
                                        u'description',
                                        u'dhcpRelayServer',
                                        u'flowEvictionThreshold',
                                        u'httpPort',
                                        u'httpsPort',
                                        u'ipAddress',
                                        u'mgmtDNS1',
                                        u'mgmtDNS2',
                                        u'mgmtGateway',
                                        u'mgmtNetworkPortgroup',
                                        u'mtu',
                                        u'multiVMSsupport',
                                        u'multicastInterfaceIP',
                                        u'multicastInterfaceNetmask',
                                        u'multicastRange',
                                        u'multicastSourcePortgroup',
                                        u'name',
                                        u'nfsLogServer',
                                        u'nfsMountPath',
                                        u'ntpServer1',
                                        u'ntpServer2',
                                        u'password',
                                        u'personality',
                                        u'portgroupMetadata',
                                        u'primaryNuageController',
                                        u'secondaryNuageController',
                                        u'separateDataNetwork',
                                        u'staticRoute',
                                        u'staticRouteGateway',
                                        u'userName',
                                        u'vRequireNuageMetadata',
                                        u'vmNetworkPortgroup',
                                        u'vrsConfigID'])

        self.assertEqual(local_types, [u'bool',
                                       u'bool',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'int',
                                       u'str',
                                       u'str',
                                       u'int',
                                       u'int',
                                       u'int',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'int',
                                       u'bool',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'bool',
                                       u'str',
                                       u'str',
                                       u'bool',
                                       u'str',
                                       u'str',
                                       u'str',
                                       u'bool',
                                       u'str',
                                       u'str'])

        # Parents apis
        parents = vcenter.apis['parents']
        paths = parents.keys()

        self.assertEqual(paths, ['/vcenters'])

        # Self apis
        self_apis = vcenter.apis['self']

        paths = self_apis.keys()
        self.assertEqual(paths, [u'/vcenters/{id}'])

        # Children apis
        children = vcenter.apis['children']
        paths = children.keys()

        self.assertEqual(paths, [])

        child_info = children.values()
        resource_names = [info.resource_name for info in child_info]
        remote_names = [info.remote_name for info in child_info]
        plural_names = [info.plural_name for info in child_info]
        instance_plural_names = [info.instance_plural_name for info in child_info]

        self.assertEqual(resource_names, [])

        self.assertEqual(remote_names, [])

        self.assertEqual(plural_names, [])

        self.assertEqual(instance_plural_names, [])