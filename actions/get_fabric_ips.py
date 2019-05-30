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
# __version__ = "1.0.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

from pyhpecfm.auth import CFMClient
from pyhpecfm import fabric


from st2common.runners.base_action import Action


class switchLookup(Action):
    def run(self, ipaddress=None, username=None, password=None):

        # Create client connection
        client = CFMClient(ipaddress, username, password)

        # Get switches from plexxi controller
        try:
            cfm_fabrics = fabric.get_fabric_ip_networks(client)
        except:
            error = "ERR-LOGIN - Failed to log into CFM controller"
            return error

        fabric_data = []
        c = 0
        # Loop through cfm_fabrics and process IPZ
        for i in cfm_fabrics:

            try:
                desc = cfm_fabrics[c]['description']
                if desc == '':
                    desc = 'HPE Composable Fabric'

            except:
                desc = 'HPE Composable Fabric'

            try:
                fab_uuid = cfm_fabrics[c]['fabric_uuid']
            except:
                fab_uuid = '-unknown'

            try:
                name = cfm_fabrics[c]['name']
            except:
                name = '-unknown'

            try:
                mode = cfm_fabrics[c]['mode']
            except:
                mode = '-unknown'

            try:
                sub_address = cfm_fabrics[c]['subnet']['address']
            except:
                sub_address = '-unknown'

            try:
                sub_prefix = cfm_fabrics[c]['subnet']['address']
            except:
                sub_prefix = '-unknown'


            out ={
                    'u_desc':desc,
                    'u_fabu_uid':fab_uuid,
                    'u_name':name,
                    'u_mode':mode,
                    'u_sub_address':sub_address,
                    'u_sub_prefix':sub_prefix
                  }
            fabric_data.append(out)

            c = c + 1
        return (True, switch_data)
