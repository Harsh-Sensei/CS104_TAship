BEGIN {
    FS=","
    total=0
}
{
    if(NR == 1)
    {
        print $0
        next
    }
    total+=$4
    indiv[$3]+=$4
    print $0
}
END {
    print "====="
    print "Net :", total
    for (i in indiv) {
        print i " : " indiv[i] | "sort"
    }
}