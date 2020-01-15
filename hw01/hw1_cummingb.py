'''
SI 630: Natural Language Processing
Homework 1
Brandon Cummings
Wednesday, January 22, 2020
'''

import re
import pandas as pd

# File IO
fn = '/Users/cummingb/School/si630/hw/hw01/W20_webpages.txt'
fh = open(fn, 'r')
tx = fh.readlines()
fh.close()

# Search for regular expression and extract results
#regex = '([A-Za-z._+-]+)(@|@@| \[at\] | \/at\/ +)([A-Za-z_+-]+)(\.| dot | \[dot\] | \/dot\/ )([A-Za-z]+)'
#regex = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
regex= '(\S+)(@|@@| \[at\] | \/at\/ +)([\S]+)(\.| dot | \[dot\] | \/dot\/ )([\S]+)'
m = [re.search(regex, i) for i in tx]
m = [i.group() if i is not None else None for i in m]
# Format addresses to be consistent
d = {'[at]':'@',
     '@@':'@',
     '/at/':'@',
     '[dot]':'.',
     '/dot/':'.',
     ' ':''}

for k, v in d.items():
    m = [i.replace(k, v) if i is not None else None for i in m]

fn_out = '/Users/cummingb/School/si630/hw/hw01/email-outputs.csv'
pd.DataFrame(m).to_csv(fn_out, header=False, na_rep='None')
#with open(fn_out, 'w') as fh_out:
#    [fh_out.write('%s\n' % i) for i in m]
