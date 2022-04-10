
Name:        zrep

# change version AND nversion to "master" to get latest raw git commits
%define nversion    2.0.1

#this would need to be updated for every version as well, if it actualy worked
%global commit e02f8ba5475c8d45ebfb09d8c53021a3d2dab537
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:     v%{nversion}
Release:     1%{?dist}
License:     free non redistributable
Group:       External packages
URL:         http://www.bolthole.com/solaris/zrep/

Source0:      https://github.com/bolthole/zrep/archive/%{version}.tar.gz
# this should work, but doesnt for me...
#Source0:      https://github.com/bolthole/zrep/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Source1:      http://www.bolthole.com/solaris/zrep/zrep.documentation.html

Summary:    a robust yet easy to use ZFS based replication and failover solution. It can also support a simple backup hub.
BuildArch:	noarch
%description
Zrep is an enterprise-grade, single-program solution for handling asynchronous,
continuous replication of a zfs filesystem, to another filesystem. That
filesystem can be on another machine, or on the same machine.

It also handles 'failover', as simply as "zrep failover datapool/yourfs".
It has many other related subcommands.

%prep
%setup -q -n %{name}-%{nversion}

# no build section is needed. zrep comes prebuilt. 
# however, if you change the source, you can run "make"

%install
mkdir -p  ${RPM_BUILD_ROOT}%{_bindir} ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}

install -m 0755 zrep ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 LICENSE.txt ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -m 0644 %{_sourcedir}/zrep.documentation.html ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}


%files
%{_bindir}/zrep

%doc
%{_docdir}/%{name}-%{version}/zrep.documentation.html
%{_docdir}/%{name}-%{version}/LICENSE.txt

