import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", ['curl', 'tree', 'htop', 'less',
                                  'speedtest-cli', 'nload', 'git',
                                  'vim', 'tmux', 'sendxmpp', 'mlocate',
                                  'python-pip', 'lsof', 'python-mysqldb',
                                  'python-pexpect', 'net-tools'])
def test_install_dependencies(host, name):
    package = host.package(name)
    assert package.is_installed


def test_sendxmpp_conf(host):
    sendxmpp_conf = host.file("/root/.sendxmpprc")
    assert sendxmpp_conf.exists
    assert sendxmpp_conf.contains("server@domain.com")
    assert sendxmpp_conf.user == "root"
    assert sendxmpp_conf.group == "root"
    assert sendxmpp_conf.mode == 0o644


def test_data_dir(host):
    data_dir = host.file("/data")
    assert data_dir.exists
    assert data_dir.is_directory
    assert data_dir.user == "root"
    assert data_dir.group == "root"
    assert data_dir.mode == 0o700


def test_ntp_dependencies(host):
    ntp_package = host.package("ntp")
    assert ntp_package.is_installed


def test_ntp_conf(host):
    ntp_conf = host.file("/etc/ntp.conf")
    assert ntp_conf.exists
    assert ntp_conf.contains("server pool.ntp.org")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644


def test_ntp_service(host):
    ntp_service = host.service("ntp.service")
    assert ntp_service.is_enabled
    assert ntp_service.is_running


def test_sytemd_conf(host):
    ntp_conf = host.file("/etc/systemd/network/99-default.link")
    assert ntp_conf.exists
    assert ntp_conf.contains("MACAddressPolicy=none")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o600


@pytest.mark.parametrize("name", ['apt-transport-https', 'ca-certificates',
                                  'curl', 'gnupg2',
                                  'software-properties-common'])
def test_docker_dependencies(host, name):
    docker_package = host.package(name)
    assert docker_package.is_installed


@pytest.mark.parametrize("path", ['/var/lib/docker', '/root/dockerfiles'])
def test_docker_directories(host, path):
    docker_directory = host.file(path)
    assert docker_directory.exists
    assert docker_directory.user == "root"
    assert docker_directory.group == "root"
    assert docker_directory.mode == 0o711


def test_sytemd_docker_conf(host):
    systemd_docker_conf = host.file("/lib/systemd/system/docker.service")
    assert systemd_docker_conf.contains(
                    "ExecStart=/usr/bin/dockerd --data-root /var/lib/docker")
