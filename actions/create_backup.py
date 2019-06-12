# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netmanchris"
# __credits__ = ["Chris Young"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"


# A python script for launching a backup on HPE Composable Fabric Manager

from pyhpecfm import system
from lib.actions import HpecfmBaseAction


class CreateBackup(HpecfmBaseAction):
    def run(self, fab_uuid=None, name=None, description=None):
        # Send create backup request to the HPE CFM controller
        status = system.create_backup(self.client)
        if result.status_code == 200:
            return (True, result.status_code)
        return (False, result.status_code)