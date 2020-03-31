# NGINX

Ansible role to install, configure and launch Nginx.

It is part of [anarres](https://git.hdg.sh/anarres/anarres), a playbook that
uses a collection of roles to deploy a full-featured server. But it can be used
and tested independently.

It deploys a "Hello world!" default page and a *robots.txt* file disallowing
all bots from */*.

## Compatibility

These are the tested GNU/Linux distributions. Maybe it works on some other
distributions too or just requieres a few changes.

* [debian](https://www.debian.org/)
	* stretch

## Requirements

`sudo` and `python`.

## Role Variables

* `domain`: Domain name for the server.
* `nginx_processes`: Defines the number of `nginx` worker processes.
* `web_ports_http`: Web port for `nginx` to bind to for HTTP connections.
* `web_ports_https`: Web port for `nginx` to bind to for HTTPS connections.
* `web_path`: Base webs path.
* `web_path_letsencrypt`: Web path for letsencrypt, used to store ACME
verification files.
* `web_path_default`: Default web path.


## Dependencies

You can manually clone the repos in your **roles_path** or with:

`ansible-galaxy install -r requierements.yml`.

* [anarres/anarres-common](https://git.hdg.sh/anarres/anarres-common)
* [anarres/anarres-sec](https://git.hdg.sh/anarres/anarres-sec)
* [anarres/anarres-letsencrypt](https://git.hdg.sh/anarres/anarres-letsencrypt)

## Example playbook

```yaml
- hosts: all
  roles:
    - anarres-common
    - anarres-sec
    - anarres-letsencrypt
    - anarres-nginx
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
