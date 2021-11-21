SRC=scratch/src
NEWSRC=scratch/newsrc

if [ -z "$ZREP_PATH" ] ; then
	echo ERROR: ZREP_PATH var must be set with full path to zrep
	exit 1
fi

echo doing $ZREP_PATH init $SRC localhost $NEWSRC now

$ZREP_PATH init $SRC localhost $NEWSRC 

# this is normally not neccessary, but because we will be doing someting
# "weird", with a zrep refresh, we have to force this

zfs set  zrep:src-host=localhost $NEWSRC
