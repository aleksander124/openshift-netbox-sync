# README

## Overview

This documentation provides guidance on setting up and using two Ansible roles for managing virtual machines in NetBox based on OpenShift virtual machines. The roles are:

1. **openshift_vms_add**: This role creates virtual machines in NetBox based on OpenShift virtual machines.
2. **openshift_vms_update_info**: This role updates virtual machines in NetBox with additional information.

## Prerequisites

Before using the playbooks and roles, ensure the following prerequisites are met:

1. **Ansible**: Ensure Ansible is installed on your system. You can install Ansible using pip:
    ```sh
    pip install ansible
    ```

2. **Python Packages**: The following Python packages are required:
    - `requests`
    - `pynetbox`

   Install the packages using pip:
    ```sh
    pip install requests pynetbox
    ```

3. **NetBox Configuration**: Update the `shared_vars/netbox.yml` file with the appropriate NetBox URL and API key:
    ```yaml
    NETBOX_URL: 'https://<netbox_url>'
    NETBOX_API_KEY: '<netbox_api_key>'
    ```

## Ansible Configuration

Update your `ansible.cfg` file to include the following settings:

```ini
[defaults]
;change this user if you are using different one
remote_user = ansible

[inventory]
enable_plugins = netbox.netbox.nb_inventory
```
## Dynamic Inventory
Configure the dynamic inventory in the inventory/inventory.yml file with the following content:
```yaml
plugin: netbox.netbox.nb_inventory
api_endpoint: https://<netbox_url>
token: <netbox_api_key>
validate_certs: false
config_context: false
query_filters:
  - role: 'openshift'
  - tag: 'ansible_sync'
```