import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_configuration_files(host):
    assert not host.file('/etc/fail2ban/jail.d').exists
    assert not host.file('/etc/fail2ban/action.d/dummy.conf').exists
    local = host.file('/etc/fail2ban/fail2ban.local')
    jails = host.file('/etc/fail2ban/jail.local')
    new_filter = host.file('/etc/fail2ban/filter.d/test.local')
    action = host.file('/etc/fail2ban/action.d/dummy2.local')
    assert local.contains(r'^loglevel = ERROR$')
    assert jails.contains(r'^\[sshd\]$')
    assert jails.contains(r'^enabled = true$')
    assert jails.contains(r'^port = 12345$')
    assert new_filter.contains(r'\[Definition\]$')
    assert new_filter.contains(r'failregex = tst$')
    assert new_filter.contains(r'ignoreregex = $')
    assert action.contains(
        r'^actionstart = touch /var/run/fail2ban/fail2ban.dummy$')
    assert action.contains(r'^init = 123$')


def test_package(host):
    assert host.package('fail2ban').is_installed


def test_service(host):
    assert host.run('fail2ban-client ping').rc == 0
    fail2ban = host.service('fail2ban')
    assert fail2ban.is_running
    assert fail2ban.is_enabled
