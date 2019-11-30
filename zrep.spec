
Name:        zrep
# change version to "master" to get latest raw git commits
Version:     v1.8.0
Release:     1%{?dist}
License:     free non redistributable
Group:       External packages
URL:         http://www.bolthole.com/solaris/zrep/
Source0:      https://github.com/bolthole/zrep/archive/%{version}.tar.gz
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
%setup -q -n %{name}-%{version}

# no build section is needed. zrep comes prebuilt. 
# however, if you change the source, you can run "make"

%install
install -m 0755 zrep ${buildroot}%{_bindir}
install -m 0755 LICENSE.txt ${buildroot}%{_docdir}
install -m 0644 %{_sourcedir}/zrep.documentation.html %{buildroot}%{_docdir}/

%files
%{_bindir}/zrep

%doc
%{_docdir}/zrep.documentation.html
