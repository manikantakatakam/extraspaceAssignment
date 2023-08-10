#!/bin/bash

# Find the largest log file named x.log
largest_log=$(find / -name "x.log" -type f -exec du -h {} + | sort -rh | head -n 1 | cut -f2)

# Truncate the file to 100 lines
tail -n 100 "$largest_log" > "$largest_log.tmp"
mv "$largest_log.tmp" "$largest_log"
