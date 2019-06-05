# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of fabric ip addresses

from pyhpecfm import fabric
from lib.actions import HpecfmBaseAction

class fabricIpLookup(HpecfmBaseAction):
    def run(self):
        cfm_fabrics = fabric.get_fabric_ip_networks(self.client)
        if isinstance(cfm_fabrics, list):
            fabric_data = []
            # Loop through cfm_fabrics and process IPZ
            for fabip in cfm_fabrics:
                desc = fabip['description']
                if desc == '':
                    desc = 'HPE Composable Fabric'
                out ={
                        'u_desc':fabip['description'],
                        'u_fabu_uid':fabip['fabric_uuid'],
                        'u_name':fabip['name'],
                        'u_mode':fabip['mode'],
                        'u_sub_address':fabip['subnet']['address'],
                        'u_mask_prefix':fabip['subnet']['prefix_length']
                      }
                fabric_data.append(out)

            return (True, fabric_data)
        return (False, switches)
