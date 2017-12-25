import os


ENCODING = 'UTF-8'
CHAT_DELIMITER = ' :--://:--: '
COUNT_DELIMITER = ': '
readpath = 'data/'
writepath = 'data/'

master_count = 'master_count'

period = 5000 # If verbose, how often an example (of e.g. message) should be displayed

"""
Read nicknames: replace nicknames with name identifiers
"""
with open(os.path.join(readpath, 'names.txt'), encoding=ENCODING, mode='r') as f:
    namelist = f.readlines()

nickname_replace_list = []
for i, line in enumerate(namelist):
    items = line.split(':')
    if len(items) == 1:
        namelist[i] = items[0].strip('\n')
    else:
        name, nicknames = items
        namelist[i] = name
        nicknames = nicknames.strip().split(',')
        for nickname in nicknames:
            nickname = nickname.strip()
            nickname_replace_list.append([name, nickname])

numerate = range(len(namelist))
namedict = dict(zip(namelist, numerate))


"""
Read aliases: replace identifiers with aliases if
aliasing is enabled
"""
with open(os.path.join(readpath, 'aliases.txt'), encoding=ENCODING, mode='r') as f:
    aliaslist = f.readlines()

name_to_alias_dict = {}
name_to_alias_dict[master_count] = master_count
for i, line in enumerate(aliaslist):
    line = line.strip('\ufeff').strip()
    # Ignore comments
    if not line: continue
    if line[0] == '#': continue

    items = line.split(':')
    if len(items) == 1:
        aliaslist[i] = items[0].strip('\n')
    else:
        alias, names = items
        aliaslist[i] = alias
        names = names.strip().split(',')
        for name_ in names:
            name_ = name_.strip()
            name_to_alias_dict[name_] = alias
            if name_ != name_.capitalize():
                name_to_alias_dict[name_.capitalize()] = alias
            if name_ != name_.lower():
                name_to_alias_dict[name_.lower()] = alias

