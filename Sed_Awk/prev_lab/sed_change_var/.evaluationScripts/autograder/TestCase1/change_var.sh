#!/bin/bash
while read line
do
	echo $line | sed "s/\b/\!@#/g;
	s/\!@#$1\!@#/$2/g;
	s/\!@#//g"
done< $3