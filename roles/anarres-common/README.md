# Common

Ansible role to install and configure some basic utilities for a GNU/Linux
server.

It is part of [anarres](https://git.hdg.sh/anarres/anarres), a playbook that
uses a collection of roles to deploy a full-featured server. But it can be used
and tested independently.

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requieres a few changes.

* [debian](https://www.debian.org/)
	* stretch

## Requirements

`sudo` and `python`.

## Role Variables

### Docker

* `docker_data_root`: Base directory for **docker**.
* `dockerfile_path`: Directory that stores the dockerfiles.
* `docker_registry_mirror`: URL to a **docker** registry mirror.
* `db_docker_image`: Database docker image name and tag.

### SendXMPP

* `sendxmpp_jid`: Jabber ID for sendxmpp to send notifications.
* `sendxmpp_pass`: Password for the JID.
* `sendxmpp_config`: Path to **sendxmpp** configuration file.

### NTP

* `ntp_servers`: List of NTP mirrors.

## Dependencies

None.

## Example playbook

```yaml
- hosts: all
  roles:
    - anarres-common
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
.

```bash
molecule test
```

There is more documentation about the installation and configuration of the
required tools at
[wiki-testing](https://git.hdg.sh/anarres/anarres/wiki/testing).

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici.org
