PKG_NAME := clr-rpm-config
VERSION := 1

include ../common/Makefile.common

tar:
	rm -f `find -name "*~"` || 1
	tar -zcf clr-rpm-config-1.tar.gz clr-rpm-config-1
