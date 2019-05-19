ansible-role-fail2ban
================================================================================

Role to setup fail2ban. It tries to not modify upstream configuration and
only extend it with `*.local` files where possible.

Variables
--------------------------------------------------------------------------------

fail2ban_package_release

   Package default release

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-fail2ban.1
