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

import json
from pyhpecfm.auth import CFMClient
from pyhpecfm import system
from st2common.runners.base_action import Action

class eventLookup(Action):
    def run(self, ipaddress=None, username=None, password=None):

        # Create client connection
        client = CFMClient(ipaddress, username, password)


        try:
            cfm_audits = system.get_audit_logs(client)
        except:
            error = "ERR-GET - Failed to GET audits from CFM controller"
            return error

        # Create a empty list for events
        event_data = []

        # Loop through cfm_audits and process EVENTS
        for e in cfm_audits:
            typex = e['record_type']
            if typex == 'EVENT':
                # Build dictionary to add to list
                out = {
                      'u_eventType': e['data']['event_type'],
                      'u_typex': e['record_type'],
                      'u_sev': e['severity'],
                      'u_desc': e['description'],
                      'u_name' : e['data']['object_name'],
                      'u_typeo' : e['data']['object_type']
                      }
                event_data.append(out)

        return (True, event_data)
