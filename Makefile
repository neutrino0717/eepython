#
# Makefile for eepython
#
# target        description
# ----------------------------------------------------------------------
# all           use 'pip install' to build all required python libraries
# dist          build the IDP
# clean         remove files built by make
########################################################################
SHELL := /bin/bash

.PHONY: test
test: 
	@echo Running unit tests
	@(cd test; \
	for d in *.py; do \
	logfile=$${d%%.*}.log;\
	result=$$(diff <(./$$d) $$logfile);\
	echo "$$d: -->$$result<--";\
	if [ "$$result" ]; then echo error with $$d output; exit 1 ; fi;\
	done)
	@echo
