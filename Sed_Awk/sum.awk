#!/bin/bash
awk -F, -v name="$1" '
BEGIN {
    total=0
}
{
    total+=$4
    indiv[$3]+=$4
    print $0
}
END {
    print "====="
    print "Net :", total
    for(i in indiv)
    {
        print i, ":", indiv[i] 
    }
    print "Created by :", name
}
' < employment.csv