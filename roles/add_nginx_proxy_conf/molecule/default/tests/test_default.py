import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_proxy_config_file(host):
    f = host.file('/etc/nginx/sites-available/anarres.local.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_proxy_config_symlink(host):
    f = host.file('/etc/nginx/sites-enabled/anarres.local.conf')
    assert f.is_symlink


# The following tests fail because of
# https://github.com/ansible/ansible/issues/30192 but if you manually start
# the service they work properly.
def test_nginx_service(host):
    nginx = host.service("nginx")
    assert nginx.is_running


def test_dummy_server_socket(host):
    socket = host.socket("tcp://0.0.0.0:8000")
    assert socket.is_listening


def test_nginx_proxy(host):
    command = "curl -kH 'Host: anarres.local' https://127.0.0.1/"
    web = host.check_output(command)
    assert "Hello World!" in web
