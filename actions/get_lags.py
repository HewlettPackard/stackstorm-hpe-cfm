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


from pyhpecfm import fabric
from lib.actions import HpecfmBaseAction

class lagLookup(HpecfmBaseAction):
    def run(self,count_only=None, mac_attachments=None,mac_learning=None,ports=None,port_type=None,tag=None,type=None,vlan_groups=None):
        params={'count_only': count_only,
                 'mac_attachemnts': mac_attachments,
                 'mac_learning': mac_learning,
                 'ports': ports,
                 'port_type': port_type,
                 'tag': tag,
                 'type': type,
                 'vlan_groups': vlan_groups
                 }
        cfm_lags=fabric.get_lags(self.client,params)
        return (True, cfm_lags)
