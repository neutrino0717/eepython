#
# Makefile for eepython
#
# target        description
# ----------------------------------------------------------------------
# test          system test
# buildlog      build all the log files for the py files
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
buildlog:
	@echo rebuild the log
	@(cd test; \
	for d in *.py; do \
	logfile=$${d%%.*}.log;\
	./$$d |tee $$logfile;\
	done)
	@echo

