BEGIN {
    FS=","
    OFS="";
}
{
    if (NR==1){
        print $0,",Email-ID";
    }
    if (NR>1){
        print $0,",",$2$4,"@surveycorps.com";
    }
}
END {
}
