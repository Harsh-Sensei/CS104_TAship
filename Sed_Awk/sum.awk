#!/bin/bash
awk -F, -v name="$1" '
BEGIN {
    total=0
}
{
    total+=$4
    print $0
}
END {
    print "Total :", total
    print "Created by :", name
}
' < employment.csv