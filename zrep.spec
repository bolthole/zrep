Name:        zrep
Version:     1.7.3
Release:     1%{?dist}
License:     free non redistributable
Group:       External packages
URL:         http://www.bolthole.com/solaris/zrep/
# https://github.com/bolthole/zrep/archive/v%{version}.tar.gz
Source:      %{name}-%{version}.tar.gz
#Source1:	http://www.bolthole.com/solaris/zrep/index.html
BuildRoot:   %{_tmppath}/%{pkg}-%{version}
Requires: ksh zfs
Summary:    a robust yet easy to use ZFS based replication and failover solution. It can also serve as the conduit to create a simple backup hub.
BuildArch:	noarch
%description
Zrep is an enterprise-grade, single-program solution for handling asynchronous,
continuous replication of a zfs filesystem, to another filesystem. That
filesystem can be on another machine, or on the same machine.

It also handles 'failover', as simply as "zrep failover datapool/yourfs". This
will conveniently handle all the details of

    Making 'yourfs' be a data destination, rather than a source
    Making 'yourfs' be read-only
    Making the destination fs be "live", and ready to transfer data to yourfs 

%prep
%setup -q

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir} ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -m0644 00-README CHANGELOG LICENSE.txt notes.locks PORTABILITY TODO workflow.txt ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
cp -pr usage ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version} 
install -m0644 index.html ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
#install -m0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -m0755 zrep ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%{_bindir}/zrep

%doc
%{_docdir}/%{name}-%{version}/index.html
%{_docdir}/%{name}-%{version}/00-README
%{_docdir}/%{name}-%{version}/CHANGELOG
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_docdir}/%{name}-%{version}/notes.locks
%{_docdir}/%{name}-%{version}/PORTABILITY
%{_docdir}/%{name}-%{version}/TODO
%{_docdir}/%{name}-%{version}/workflow.txt
%{_docdir}/%{name}-%{version}/usage/*

%changelog
* Sat Jul 8 2017 Tru Huynh <tru@pasteur.fr> - 1.6.7-2
- add http://www.bolthole.com/solaris/zrep/index.html in the tree
- fix spec file doc section
* Thu Jul 6 2017 Tru Huynh <tru@pasteur.fr> - 1.6.7-1
- initial version
