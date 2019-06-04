# HPECFM Integration Pack
This pack allows you to integrate with
[HPE COmposable Fabric](https://www.hpe.com/us/en/integrated-systems/composable-fabric.html).

## Configuration
Copy the example configuration in [hpecfm.yaml.example](./hpecfm.yaml.example) to
`/opt/stackstorm/configs/hpecfm.yaml` and edit as required.

It must contain:

```
ipaddress - Your CFM appliance IP address
username - CFM Username
password - CFM Password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "admin"
  password: "admin"
```

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_alarms``
* ``get_switches``
* ``get_events``
* ``get_fabrics``

### Orquestra Workflows: will not
* ``sendsnow``
* ``performfit``
* ``getswitches``
* ``getfabric_for_fit``
