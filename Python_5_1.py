if __name__ == '__main__':
    pass

import os
import re
route_n_result = os.popen("route -n").read()

route_gateway = re.match(r'[\S\s]+0\.0\.0\.0\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[\S\s]+UG[\S\s]+', route_n_result).groups()

print_gateway = '{0:<}:{1:<}'
print(print_gateway.format('网关为', route_gateway[0]))
