# Ansible Playbook RadioClub Archive DB

## How to deploy

You must have ansible installed.

```
$ ansible-playbook --ask-vault-pass -i custom/ea4rct/hosts.yml --limit "zulu" --tags "archive_db" full.yml
```