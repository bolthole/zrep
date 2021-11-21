#!/bin/bash

SRC=scratch/src
NEWSRC=scratch/newsrc

failmsg(){
    echo $*
    exit 1
}   

echo Running basic syn test
$ZREP_PATH -S $SRC

echo Running changed syn test

test -f /$NEWSRC/testfile && rm /$NEWSRC/testfile

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
