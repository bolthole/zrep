


ZSOURCE=zrep_top zrep_vars zrep_status zrep_snap zrep_sync zrep_failover

zrep:	$(ZSOURCE)
	nawk '$$1 == "AWKinclude" {system ("cat "$$2);next;} \
	      {print}' zrep_top > $@
	chmod 0755 $@

save:
	cp -p $(ZSOURCE) Makefile SAVE

diffs:
	for f in `ls SAVE` ; do echo '###' $$f;  diff -r SAVE/$$f $$f ||true ; done |less

# To find list of zrep: key properties, use the following:
# sed -n 's/.*\(zrep:.*\)=.*/\1/p' zrep_*|sort -u

listfuncs:
	grep '^[_a-z].*[(]' $(ZSOURCE)
