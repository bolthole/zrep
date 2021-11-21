SRC=scratch/src
NEWSRC=scratch/newsrc

if [ -z "$ZREP_PATH" ] ; then
	echo ERROR: ZREP_PATH var must be set with full path to zrep
	exit 1
fi

echo doing $ZREP_PATH init $SRC localhost $NEWSRC now

$ZREP_PATH init $SRC localhost $NEWSRC 
