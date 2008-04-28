prefix=/opt/glite
package=glite-yaim-voms
name=$Name:  $
tag:=$(shell echo $(name) | sed 's/^[^:]*: //' )
version:=$(shell echo "$(tag)" | sed 's/^.*R_//' | sed 's/_/\./g')
release:=$(shell echo "$(version)" | sed 's/.*\.//')
version:=$(shell echo "$(version)" | sed 's/\(.*\)\.[0-9]*/\1/')

.PHONY: configure install clean rpm

all: configure

install: 
	@echo installing ...
	@mkdir -p $(prefix)/yaim/functions
	@mkdir -p $(prefix)/yaim/node-info.d
	@mkdir -p $(prefix)/yaim/examples
	@mkdir -p $(prefix)/yaim/examples/siteinfo
	@mkdir -p $(prefix)/yaim/examples/siteinfo/services
	@mkdir -p $(prefix)/yaim/defaults


	@install -m 0644 config/functions/config* $(prefix)/yaim/functions
	@install -m 0644 config/node-info.d/glite* $(prefix)/yaim/node-info.d
	@install -m 0644 config/services/glite* $(prefix)/yaim/examples/siteinfo/services/.
	@install -m 0644 config/defaults/* $(prefix)/yaim/defaults


clean::
	rm -f *~ test/*~ etc/*~ doc/*~ src/*~  
	rm -rf rpmbuild 

rpm:
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/

ifneq ("$(tag)","ame:")
	@sed -i 's/^Version:.*/Version: $(version)/' $(package).spec
	@sed -i 's/^Release:.*/Release: $(release)/' $(package).spec
endif
	@tar --gzip --exclude='*CVS*' -cf rpmbuild/SOURCES/${package}.src.tgz *
	@rpmbuild -ba ${package}.spec



