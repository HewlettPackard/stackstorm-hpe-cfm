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

# A python script for adding vlans to the cfm controller

from pyhpecfm import fabric
from lib.actions import HpecfmBaseAction

class AddVlans(HpecfmBaseAction):
    def run(self, name=None, description=None, vlans=None):
        # Send fit request to the plexxi controller
        result = fabric.add_vlan_groups(self.client, name, description, vlans)
        if result.status_code == 200:
            return(True, result.status_code)
        return (False, result.status_code)
