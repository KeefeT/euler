CC ?= cc
CFLAGS ?= -std=c11 -O2 -Wall -Wextra

LIBKEEFE := ../libkeefe/build/libkeefe.a
CPPFLAGS += -I../libkeefe

SOURCES := $(wildcard problems/p*/*.c)
TARGETS := $(patsubst %.c,build/%,$(SOURCES))

.PHONY: all clean
all: build/main $(TARGETS)

.PHONY: run
run: build/main
	./build/main

build/main: main.c Makefile
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(CPPFLAGS) -DEULER_DIR='"$(CURDIR)"' $< $(LDFLAGS) $(LDLIBS) -o $@

$(LIBKEEFE): FORCE
	$(MAKE) -C ../libkeefe CC="$(CC)" CFLAGS="$(CFLAGS)"

.PHONY: FORCE
FORCE:

build/%: %.c $(LIBKEEFE)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(CPPFLAGS) -MMD -MP $< $(LDFLAGS) $(LIBKEEFE) $(LDLIBS) -o $@

-include $(TARGETS:=.d)

clean:
	rm -rf build
