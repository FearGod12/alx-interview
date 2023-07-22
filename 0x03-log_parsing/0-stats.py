#!/usr/bin/python3
"""log parsing"""

import re
import sys

count = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}
total_file_size = 0


def print_statistics(total_file_size, status_codes):
    """prints the statistics"""
    print("File size: {}".format(total_file_size))
    for code in status_codes:
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        data = line.rstrip()
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ' \
                  r'- \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
        match = re.match(pattern, data)
        if match:
            try:
                ip, date, status, file_size = match.groups()
                total_file_size += int(file_size)
                if status not in status_codes or not status.isdigit():
                    continue
                status_codes[status] += 1
                count += 1
                if count == 10:
                    print_statistics(total_file_size, status_codes)
                    count = 0
            except KeyboardInterrupt:
                raise
except KeyboardInterrupt:
    print_statistics(total_file_size, status_codes)
