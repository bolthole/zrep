


ZSOURCE=zrep_top zrep_vars zrep_status zrep_snap zrep_sync zrep_failover

zrep:	$(ZSOURCE)
	nawk '$$1 == "AWKinclude" {system ("cat "$$2);next;} \
	      {print}' zrep_top > $@
	chmod 0755 $@


# detect is a test util to see if zfs feature detect works
detect:	detect_test zrep_vars
	nawk '$$1 == "AWKinclude" {system ("cat "$$2);next;} \
	      {print}' detect_test > $@
	chmod 0755 $@


save:
	cp -p $(ZSOURCE) Makefile SAVE

diffs:
	for f in `ls SAVE` ; do echo '###' $$f;  diff -r SAVE/$$f $$f ||true ; done |less

# To find list of zrep: key properties, use the following:
# sed -n 's/.*\(zrep:.*\)=.*/\1/p' zrep_*|sort -u

listfuncs:
	grep '^[_a-z].*[(].*[{]' $(ZSOURCE)
