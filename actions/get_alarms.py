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

class alarmLookup(Action):
    def run(self, ipaddress=None, username=None, password=None):

        # Create client connection
        client = CFMClient(ipaddress, username, password)


        try:
            cfm_audits = system.get_audit_logs(client)
        except:
            error = "ERR-GET - Failed to GET audits from CFM controller"
            return error

        # Create a empty list for alarms
        alarm_data = []

        # Loop through cfm_audits and process ALARMS

        for a in cfm_audits:
            typex = a['record_type']
            if typex == 'ALARM':
                # Build dictionary to add to list
                out = {
                      'u_eventType': a['data']['event_type'],
                      'u_typex': a['record_type'],
                      'u_sev': a['severity'],
                      'u_desc': a['description']
                      }
                alarm_data.append(out)

        return (True, alarm_data)
