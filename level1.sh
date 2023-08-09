#!/bin/bash

# Find the largest x.log file
largest_log=$(find /workspaces/extraspaceAssignment -name "x.log" -exec du -h {} + | sort -rh | head -n 1 | cut -f 2)

# Truncate the largest log file to 100 lines
tail -n 100 "$largest_log" > "$largest_log.tmp"
mv "$largest_log.tmp" "$largest_log"
