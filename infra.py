#
# Ansible hosts file creator for Rebrain small cources. Paste Rebrain provided resources into s multiline variable and run the script.
#
import configparser
import re

s = '''
es01: connect command: ssh user@165.227.170.14 password: nuyeblxveeuh
es02: connect command: ssh user@165.227.138.183 password: avdppmwvtakw
es03: connect command: ssh user@206.81.16.229 password: utvhpffdqhnj
logs: connect command: ssh user@206.81.24.46 password: hlcytstrzuog
app1: connect command: ssh user@46.101.248.154 password: srhxrakjvrnk
app2: connect command: ssh user@159.89.2.174 password: oivqnkbcvioa
app3: connect command: ssh user@165.22.65.75 password: ltaqiicqqfao
'''

config = configparser.ConfigParser()

for i in s.split('\n'):
    if i:
        m = re.match(r'(?P<name>\D+?)(?P<id>\d*):.+ (?P<user>.+)@(?P<host>.+) password: (?P<password>.+)$', i)
        if m.group('name') + '_all' not in config.sections():
            config.add_section(m.group('name') + '_all')
            print(f'[{m.group("name") + "_all"}]')
        config_line = f'{m.group("name") + m.group("id")} ansible_host={m.group("host")} ansible_user={m.group("user")} ansible_ssh_pass={m.group("password")}'
        config.set(m.group('name') + '_all', config_line, '')
        print(f'{config_line}')

with open(r'./hosts', 'w') as configfile:
    config.write(configfile)

print('Done!')
