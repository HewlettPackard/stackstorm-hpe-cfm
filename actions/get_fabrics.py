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

# A python script for getting a dictionary of composable fabrics

from pyhpecfm.auth import CFMClient
from pyhpecfm import fabric


from st2common.runners.base_action import Action


class fabricLookup(Action):
    def run(self, ipaddress=None, username=None, password=None):

        # Create client connection
        client = CFMClient(ipaddress, username, password)

        # Get fabrics from plexxi controller
        try:
            cfm_fabrics = fabric.get_fabrics(client)
        except:
            error = "ERR-GET - Failed to GET fabric from CFM controller"
            return error

        fabric_data = []

        # Loop through cfm_fabrics and process fabrics
        # Use try because variable may be empty
        for fab in cfm_fabrics:
            desc = fab['description']
            if desc == '':
                desc = 'HPE Composable Fabric'
            out ={
                    'u_desc':fab['description'],
                    'u_uuid':fab['uuid'],
                    'u_name':fab['name'],
                    'u_stable':fab['is_stable'],
                    'u_fms':fab['foreign_fabric_state']
                  }
            fabric_data.append(out)

        return (True, fabric_data)
