#!/bin/sh


check=$(zfs help 2>&1)

if [ -z "$check" ] ; then
	echo ERROR: zfs does not seem to be installed
	exit 1
fi

zfs list scratch || exit 1

SRC=scratch/src
NEWSRC=scratch/newsrc

echo ensuring that $SRC and $NEWSRC exist

zfs list $SRC || zfs create $SRC
if [ $? -ne 0 ] ; then
	echo ERROR: could not create zfs filesystem $SRC; exit 1
else
	echo $SRC now exists
fi

zfs list $NEWSRC || zfs create $NEWSRC
if [ $? -ne 0 ] ; then
	echo ERROR: could not create zfs filesystem $NEWSRC; exit 1
else
	echo $NEWSRC now exists
fi
