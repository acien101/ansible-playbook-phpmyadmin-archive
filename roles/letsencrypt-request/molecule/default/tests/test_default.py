import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_letsencrypt_dir(host):
    data_dir = host.file("/etc/letsencrypt/live")
    assert data_dir.exists
    assert data_dir.is_directory


@pytest.mark.parametrize("name", [
                        "/etc/letsencrypt/live/anarres.local/fullchain.pem",
                        "/etc/letsencrypt/live/anarres.local/privkey.pem",
                        "/etc/letsencrypt/live/anarres.local/cert.pem"])
def test_letsecnrypt_cert(host, name):
    letsencrypt_cert = host.file(name)
    assert letsencrypt_cert.exists
