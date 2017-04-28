#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 16.3.8
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: avi_sslkeyandcertificate
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of SSLKeyAndCertificate Avi RESTful Object
description:
    - This module is used to configure SSLKeyAndCertificate object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    ca_certs:
        description:
            - Ca certificates in certificate chain.
    certificate:
        description:
            - Sslcertificate settings for sslkeyandcertificate.
        required: true
    certificate_management_profile_ref:
        description:
            - It is a reference to an object of type certificatemanagementprofile.
    created_by:
        description:
            - Creator name.
    dynamic_params:
        description:
            - Dynamic parameters needed for certificate management profile.
    enckey_base64:
        description:
            - Encrypted private key corresponding to the private key (e.g.
            - Those generated by an hsm such as thales nshield).
    enckey_name:
        description:
            - Name of the encrypted private key (e.g.
            - Those generated by an hsm such as thales nshield).
    hardwaresecuritymodulegroup_ref:
        description:
            - It is a reference to an object of type hardwaresecuritymodulegroup.
    key:
        description:
            - Private key.
    key_params:
        description:
            - Sslkeyparams settings for sslkeyandcertificate.
    name:
        description:
            - Name of the object.
        required: true
    status:
        description:
            - Status of sslkeyandcertificate.
            - Default value when not specified in API or module is interpreted by Avi Controller as SSL_CERTIFICATE_FINISHED.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    type:
        description:
            - Type of sslkeyandcertificate.
            - Default value when not specified in API or module is interpreted by Avi Controller as SSL_CERTIFICATE_TYPE_VIRTUALSERVICE.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
extends_documentation_fragment:
    - avi
'''


EXAMPLES = '''
- name: Create a SSL Key and Certificate
  avi_sslkeyandcertificate:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    key: |
        -----BEGIN PRIVATE KEY-----
        ....
        -----END PRIVATE KEY-----
    certificate:
        self_signed: true
        certificate: |
          -----BEGIN CERTIFICATE-----
          ....
          -----END CERTIFICATE-----
    type: SSL_CERTIFICATE_TYPE_VIRTUALSERVICE
    name: MyTestCert
'''
RETURN = '''
obj:
    description: SSLKeyAndCertificate (api/sslkeyandcertificate) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule

try:
    from ansible.module_utils.avi import (
        avi_common_argument_spec, HAS_AVI, avi_ansible_api)
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        ca_certs=dict(type='list',),
        certificate=dict(type='dict', required=True),
        certificate_management_profile_ref=dict(type='str',),
        created_by=dict(type='str',),
        dynamic_params=dict(type='list',),
        enckey_base64=dict(type='str',),
        enckey_name=dict(type='str',),
        hardwaresecuritymodulegroup_ref=dict(type='str',),
        key=dict(type='str',),
        key_params=dict(type='dict',),
        name=dict(type='str', required=True),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=16.3.5.post1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'sslkeyandcertificate',
                           set(['key']))


if __name__ == '__main__':
    main()