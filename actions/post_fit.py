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

# A python script for sending a 'fit' to the cfm controller

from pyhpecfm import fabric
from lib.action import HpecfmBaseAction

class FabricFit(HpecfmBaseAction):
    def run(self, fab_uuid=None, name=None, description=None):
        # Send fit request to the plexxi controller
        status = fabric.perform_fit(self.client, fab_uuid, name, description)
        if status == 200:
            return(True, status)
        return (False, status)
