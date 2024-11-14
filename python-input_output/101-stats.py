#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""


import sys

total_size = 0
status_counts = {}
valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()

        if len(data) >= 7:
            try:
                file_size = int(data[-1])
                total_size += file_size

                status_code = data[-2]
                if status_code in valid_statuses:
                    if status_code not in status_counts:
                        status_counts[status_code] = 0
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts.keys()):
                print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    print("\nFile size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))
    raise

print("File size: {}".format(total_size))
for code in sorted(status_counts.keys()):
    print("{}: {}".format(code, status_counts[code]))
