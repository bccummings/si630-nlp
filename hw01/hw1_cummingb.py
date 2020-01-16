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

# Clean up HTML syntax
tx = [i.replace('<html><head></head><body><p>', '') for i in tx]
tx = [i.replace(' </p><br /></body></html>\n', '') for i in tx]

# Search regular expressions
possible_versions_of_at = ['@', '@@', ' @ ', ' @@ ',
                           '\[at\]', ' \[at\] ',
                           '\/at\/', ' \/at\/ ',
                           ' at ']

possible_versions_of_dot = ['\.', '\.\.', ' \. ', ' \.\. ',
                           '\[dot\]', ' \[dot\] ',
                           '\/dot\/', ' \/dot\/ ',
                           ' dot ']

regex = '(\S+)(%s)([\S]+)(%s)(\S+)' % (
                       '|'.join(possible_versions_of_at),
                       '|'.join(possible_versions_of_dot)
                       )

m = [re.search(regex, i) for i in tx]
m = [i.group(1) + '@' + i.group(3) + '.' + i.group(5) if i is not None else None for i in m]
m = [i.replace('@@', '@') if i is not None else None for i in m]

fn_out = './email-outputs.csv'
pd.DataFrame(m).to_csv(fn_out, header=False, na_rep='None')
