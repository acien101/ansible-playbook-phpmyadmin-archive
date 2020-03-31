Add nginx proxy configuration
=============================

This role adds and enables a reverse proxy configuration to an existing nginx
instance.

Requirements
------------

* nginx
* An SSL cert for the domain.

Role Variables
--------------

* `domain`: domain (or subdomain) for the reverse proxy to bind to.
* `binded_port`: Internal binded port of the service we want the proxy to reach
.
* `external_port`: External binded port through which the proxy will be
  accessible (with SSL/TLS).
* `ssl_certificate`: Path to the SSL cert file.
* `ssl_certificate_key`: Path to the SSL private key file.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- name: Add nginx proxy configuration
  hosts: all
  vars:
    binded_port: 8000
    domain: anarres.local
  roles:
    - role: add_nginx_proxy_conf
```

**Note**: by default this role will use the SSL cert files found in */etc/letsencrypt/live/{{ domain }}/*.

Testing
-------

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
and **docker**.


```bash
molecule test
```

License
-------

GPLv3

Author Information
------------------

m0wer [ at ] autistici.org
