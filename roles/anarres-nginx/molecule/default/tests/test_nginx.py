import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_install_nginx(host):
    nginx_package = host.package("nginx-light")
    assert nginx_package.is_installed


@pytest.mark.parametrize("name", [
                        "/var/www/default"
                        ])
def test_web_dirs(host, name):
    web_dir = host.file(name)
    assert web_dir.exists
    assert web_dir.is_directory
    assert web_dir.user == "www-data"
    assert web_dir.group == "www-data"
    assert web_dir.mode == 0o740


def test_nginx_conf(host):
    nginx_conf = host.file("/etc/nginx/nginx.conf")
    assert nginx_conf.exists
    assert nginx_conf.contains("pid /run/nginx.pid;")


def test_nginx_default_page(host):
    nginx_conf = host.file("/var/www/default/index.html")
    assert nginx_conf.exists
    assert nginx_conf.contains("Hello world!")


def test_nginx_robots_txt(host):
    nginx_conf = host.file("/var/www/default/robots.txt")
    assert nginx_conf.exists
    assert nginx_conf.contains("Disallow: /")


def test_default_web_conf(host):
    default_web_conf = host.file("/etc/nginx/sites-available/default")
    assert default_web_conf.exists
    assert default_web_conf.contains("return 301 https://$host$request_uri;")


def test_default_web_file(host):
    default_web_file = host.file("/var/www/default/index.html")
    assert default_web_file.exists
    assert default_web_file.contains("Hello world!")
    assert default_web_file.user == "www-data"
    assert default_web_file.group == "www-data"
    assert default_web_file.mode == 0o440


def test_default_web_enabled(host):
    default_web_enabled = host.file("/etc/nginx/sites-enabled/default")
    assert default_web_enabled.exists
    assert default_web_enabled.is_symlink


def test_gitea_socket(host):
    command = "curl -kH 'Host: anarres.local' https://127.0.0.1/"
    web = host.check_output(command)
    assert "Hello world!" in web
