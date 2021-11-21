#!/bin/bash

SRC=scratch/src
NEWSRC=scratch/newsrc

failmsg(){
    echo $*
    exit 1
}   

test -x "$ZREP_PATH" || failmsg ZREP_PATH is not set

echo Running basic syn test
$ZREP_PATH -S $SRC

echo Running changed syn test

test -f /$NEWSRC/testfile && echo WARNING:  /$NEWSRC/testfile exists already

echo "this is a test" > /$SRC/testfile
$ZREP_PATH -S $SRC

echo validating sync
cmp /$SRC/testfile /$NEWSRC/testfile || failmsg FAILED 1
echo 'PASSED #1'; echo ""

echo Testing refresh
echo "this is the second test" > /$SRC/testfile
$ZREP_PATH refresh $NEWSRC
cmp /$SRC/testfile /$NEWSRC/testfile || failmsg FAILED 2
echo 'PASSED #2' ; echo ""
