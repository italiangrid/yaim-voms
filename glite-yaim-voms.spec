%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-voms module configures the VOMS server. 
Name: glite-yaim-voms
Version: 1.0.0
Vendor: EGEE
Release: 3
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt/glite
Requires: glite-yaim-core
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the yaim functions necessary to configure a mysql or oracle VOMS server.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(-,root,root)
%{prefix}/yaim/functions/config_*
%config(noreplace) %{prefix}/yaim/node-info.d/glite-*
%{prefix}/yaim/examples/siteinfo/services/glite-*
%{prefix}/yaim/defaults/*
%{prefix}/yaim/etc/versions/%{name}
%doc LICENSE


%clean
rm -rf %{buildroot}


