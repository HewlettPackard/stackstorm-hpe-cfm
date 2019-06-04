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

# A python script for getting a dictionary of switches

from pyhpecfm import fabric
from lib.actions import HpecfmBaseAction


class switchLookup(HpecfmBaseAction):
    def run(self):
        # Get switches from plexxi controller
        switches = fabric.get_switches(self.client)
        if isinstance(switches, list):
            # Setup a list for holding dictionaries
            switch_data = []
            # Iterate through switch data from CFM API
            for i in switches:
                # Build dictionary for return
                out = {
                      'u_health': i['health'],
                      'u_ip_address': i['ip_address'],
                      'u_mac_address': i['mac_address'],
                      'u_name': i['name'],
                      'u_sw_version': i['sw_version']
                      }
                switch_data.append(out)

            return (True, switch_data)
        return (False, switches)
