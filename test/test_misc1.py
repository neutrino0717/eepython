#!/usr/bin/env eepython
import json
from pprint import pprint

cmd="""cat > AAT.conf <<EOF
{
    "data"              : "/home/eenmliu/aat/data01",
    "backup"            : "/home/eenmliu/aat/backup",
    "log-dir"           : "/home/eenmliu/aat/logs"
}
EOF"""

os.system(cmd)
with open('AAT.conf') as f:    
    data = json.load(f)
print data
pprint(data)
print type(data)
print data[u'log-dir']
print data['log-dir']
