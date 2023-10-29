#!/usr/bin/bash

echo "Input first number"
read fn
echo "first number you entered is $fn"
echo "Input second number"
read sn
echo "second number you entered is $sn"
echo "Input third number"
read tn
echo "third number you entered is $tn"
c=`expr $fn + $sn + $tn`
echo "Sum of all number is $c "
echo "total is $((fn + sn + tn))"
echo "also gives total as $(($fn + $sn + $tn))"
if [ $fn -gt $sn -a $fn -gt $tn ]
    then
	echo "$fn is greatest number"
	#printf "$fn is greatest number"
    elif
	[ $sn -gt $tn ]
    then
	echo "$sn is greatest"
    else
	echo "$tn is greatest"
	#printf 'either of two is greatest\n'
fi

