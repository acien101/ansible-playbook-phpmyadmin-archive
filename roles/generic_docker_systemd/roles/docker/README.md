# Docker

Install docker. Not available for arm7, as it still doesn't support
repositories, follow [this link](https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script)

## Requirements

To run this role you must have installed:

* pip

## Role Variables

* `install_docker_pip`: Set if you want to install the `docker` pip package
  [Default: `True`]

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: docker }
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/).

And vagrant installed with libvirt

```bash
molecule test
```

## License

GPL3

## Author Information

drymer [ EN ] autistici.org
lyz [EN] riseup.net
