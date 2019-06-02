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
            error = "ERR-LOGIN - Failed to log into CFM controller"
            return error

        # Create a empty list for alarms
        event_data = []

        # Set some counters
        c = 0
        x = 0

        # Loop through cfm_audits and process EVENTS
        for i in cfm_audits:

            try:
                typex = cfm_audits[c]['record_type']
            except:
                typex = '-'

            if typex == 'EVENT':

                try:
                    eventType = cfm_audits[c]['data']['event_type']
                except:
                    eventType = '-'

                try:
                    objectName = cfm_audits[c]['data']['object_name']
                except:
                    objectName = '-'

                try:
                    objectType = cfm_audits[c]['data']['object_type']
                except:
                    objectType = '-'

                try:
                    sev = cfm_audits[c]['severity']
                except:
                    sev = '-'

                try:
                    desc = cfm_audits[c]['description']
                except:
                    desc = '-'

                # Build dictionary to add to list
                out = {
                      'u_eventType': eventType,
                      'u_typex': typex,
                      'u_sev': sev,
                      'u_desc': desc,
                      'u_name' : objectName,
                      'u_typeo' : objectType
                      }
                event_data.append(out)

            c = c + 1
        return (True, event_data)
