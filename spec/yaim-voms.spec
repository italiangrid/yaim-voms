%define prefix /opt/glite

Name: yaim-voms
Version: 1.1.0
Release: 1%{?dist}
Summary: The Virtual Organisation Membership Service YAIM configuration module

Group: System Environment/Libraries
License: ASL 2.0
URL: https://wiki.italiangrid.it/twiki/bin/view/VOMS
Source: %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
Requires: glite-yaim-core

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the YAIM configuration module for the VOMS server.

%prep
%setup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/functions
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/node-info.d
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/examples
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/examples/siteinfo
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/examples/siteinfo/services
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/defaults
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/etc
mkdir -p $RPM_BUILD_ROOT%{prefix}/yaim/etc/versions

echo "%{name} %{version}-%{release}" > $RPM_BUILD_ROOT%{prefix}/yaim/etc/versions/%{name}

install -m 0644 config/functions/config* $RPM_BUILD_ROOT%{prefix}/yaim/functions
install -m 0644 config/node-info.d/glite* $RPM_BUILD_ROOT%{prefix}/yaim/node-info.d
install -m 0644 config/services/glite* $RPM_BUILD_ROOT%{prefix}/yaim/examples/siteinfo/services/.
install -m 0644 config/defaults/*.pre $RPM_BUILD_ROOT%{prefix}/yaim/defaults
install -m 0644 config/defaults/*.post $RPM_BUILD_ROOT%{prefix}/yaim/defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/yaim/functions/config_*
%config(noreplace) %{prefix}/yaim/node-info.d/glite-*
%{prefix}/yaim/examples/siteinfo/services/glite-*
%{prefix}/yaim/defaults/*
%{prefix}/yaim/etc/versions/%{name}
%doc LICENSE

%changelog
* Fri Feb 24 2011 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.11-1
- Self-managed packaging
