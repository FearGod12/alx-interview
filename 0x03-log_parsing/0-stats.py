#!/usr/bin/python3
"""log parsing"""

import re
import sys

count = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0

for line in sys.stdin:
    data = line.rstrip()
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
    match = re.match(pattern, data)
    if match:
        ip, date, status, file_size = match.group(1, 2, 3, 4)
        total_file_size += int(file_size)
        status_codes[status] += 1
        count += 1
        if count == 10 or KeyboardInterrupt:
            print("File size: {}".format(total_file_size))
            for code in status_codes:
                print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import random
    from time import sleep
    import datetime

    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
        sys.stdout.flush()