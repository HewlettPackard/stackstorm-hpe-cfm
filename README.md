# stackstorm-hpe-cfm
Current status: Alpha
Version : 0.1.2


HPE Composable Fabric stackstorm pack

To install this pack on a stackstorm server: `st2 pack install https://www.github.com/HewlettPackard/stackstorm-hpe-cfm.git`

For scripts that use the pyhpecfm python library for HPE Composable Fabric, they will need the IP address username and password for the CFM controller.

In order to do this the StackStorm datastore offers a perfect place to hold this data.

In the `/opt/stackstorm/packs/hpecfm/etc` directory there is a file called `system-settings.json`
```
[
  {
    "name" : "ipaddress",
    "value": "172.25.192.138"
  },
  {
    "name" : "username",
    "value": "admin"
  },
  {
    "name" : "password",
    "value": "siesta3"
  }
]
```
Edit this file to have the appropriate data for the CFM you need to access.

Save the file and issue: `st2 key load system-settings.json`

Now these variable can be accessed in actions by using "{{ st2kv.system.ipaddress }}"
