PKG_NAME := clr-rpm-config
VERSION := 1

include ../common/Makefile.common

tar:
	rm `find -name "*~"`
	tar -zcf clr-rpm-config-1.tar.gz clr-rpm-config-1