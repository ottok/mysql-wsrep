#
# spec file for package mysql-wsrep-cluster
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Codership Oy
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


# Few definitions which will alter build
%define prefered   1
%define use_cmake  1
%define cluster    0
%define builtin_plugins partition,csv,heap,myisam,innobase
%define use_extra_provides 1
%define extra_provides mysql-wsrep_56

%if %{?rel:0}%{!?rel:1}
%define rel 1
%endif
#Distribution:   %dist
#Packager:       %packager
#Vendor:         %vendor

Name:           mysql-wsrep
Summary:        Server part of MySQL WSREP (Galera) Server
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Productivity/Databases/Servers
Version:        5.6.21
Release:        0
%define srv_vers 5.6.21
Url:            http://www.mysql.com
Source:         mysql-wsrep-%{version}.tar.gz
Source2:        baselibs.conf
Source3:        suse-test-run
Source4:        mysql.SuSEfirewall2
Source5:        rc.mysql-multi
Source6:        build.inc
Source7:        install.inc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
PreReq:         pwdutils
PreReq:         %install_info_prereq %insserv_prereq
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  procps
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version}
BuildRequires:  pwdutils
BuildRequires:  tcpd-devel
%endif
%if 0%{?suse_version} > 1030 || 0%{?fedora_version} > 8
BuildRequires:  fdupes
%endif
%if 0%{?fedora_version} > 11
BuildRequires:  sqlite
%endif
%if 0%{?suse_version} > 1030
Recommends:     logrotate
%else
Requires:       logrotate
%endif
# required by rcmysql
Requires:       %{name}-client
Requires:       %{name}-errormessages = %version
Requires:       galera
Requires:       perl-base
Provides:       mysql = %{srv_vers}
Provides:       mysql-Max = %{srv_vers}
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides} = %{version}
Obsoletes:      %{extra_provides} < %{version}
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql < %{srv_vers}
Obsoletes:      mysql-Max < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql)

%description
SQL is the most popular database language in the world. MySQL is a
client/server implementation that consists of a server daemon (mysqld)
and many different client programs and libraries.

The main goals of MySQL are speed, robustness, and ease of use. MySQL
was originally developed because the developers at TcX needed an SQL
server that could handle very large databases an order of magnitude
faster than what any database vendor could offer them. They have now
been using MySQL since 1996 in an environment with more than 40
databases containing 10,000 tables, of which more than 500 have more
than 7 million rows. This is about 100 gigabytes of mission-critical
data.

The base upon which MySQL is built is a set of routines that have been
used in a highly demanding production environment for many years. While
MySQL is still in development, it already offers a rich and highly
useful function set.

The official way to pronounce MySQL is &quot;My Ess Que Ell&quot; (Not
MY-SEQUEL). 

This package only contains the server-side programs.

%if 0%{?prefered} > 0

%package -n libmysqlclient-devel
# mysql-devel was last used in openSUSE 10.2
Provides:       mysql-devel = %srv_vers-%release
Obsoletes:      mysql-devel < %srv_vers
Requires:       glibc-devel
Requires:       libmysqlclient18 = %version
Requires:       libmysqlclient_r18 = %version
Requires:       openssl-devel
Requires:       zlib-devel
Summary:        MySQL Community Server development header files and libraries
Group:          Development/Libraries/C and C++

%description -n libmysqlclient-devel
This package contains the development header files and libraries
necessary to develop client applications for MySQL Community Server.

%endif

%package -n libmysqlclient18
Summary:        Shared Libraries for MySQL Community Server
Group:          Development/Libraries/Other

%description -n libmysqlclient18
This package contains the shared libraries (.so) which certain
languages and applications need to dynamically load and use MySQL Community Server.

%package -n libmysqlclient_r18
Summary:        Shared Libraries for MySQL Community Server
Group:          Development/Libraries/Other

%description -n libmysqlclient_r18
This package contains the shared libraries (.so) which certain
languages and applications need to dynamically load and use MySQL Community Server.

%package client
Summary:        Client for MySQL Community Server
Group:          Productivity/Databases/Clients
Provides:       mysql-client = %{srv_vers}
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides}-client = %{version}
Obsoletes:      %{extra_provides}-client < %{version}
Requires:       %{name}-errormessages = %version
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql-client < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql-client)

%description client
This package contains the standard clients for MySQL Community Server.

%package errormessages
Summary:        MySQL Community Server development header files and libraries
Group:          Development/Libraries/C and C++

%description errormessages
This package provides the translated error messages for the standalone
server daemon as well as the embedded server

%package bench
Requires:       %{name}-client
Requires:       perl-DBD-mysql
Summary:        Benchmarks for MySQL Community Server
Group:          Productivity/Databases/Tools
Provides:       mysql-bench = %{srv_vers}
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides}-bench = %{version}
Obsoletes:      %{extra_provides}-bench < %{version}
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql-bench < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql-bench)

%description bench
This package contains benchmark scripts and data for MySQL Community Server.

To run these database benchmarks, start the script "run-all-tests" in
the directory /usr/share/sql-bench after starting MySQL Community Server.


%package debug-version
Summary:        MySQL Community Server with debug options turned on
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
Provides:       %{name}-debug = %{srv_vers}
Provides:       mysql-debug = %{srv_vers}
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides}-debug-verion = %{version}
Obsoletes:      %{extra_provides}-debug-version < %{version}
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql-debug < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql-debug)

%description debug-version
A version of the MySQL Community Server that has some debug code turned on.
It should be only used to track down problems with the standard
servers. Note that merely installing this package will bot replace the
standard server.

%package test
Summary:        Testsuite for MySQL Community Server
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-bench = %{version}
Requires:       %{name}-client = %{version}
Requires:       %{name}-tools = %{version}
Requires:       perl-DBD-mysql
Provides:       mysql-test = %{srv_vers}
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides}-test = %{version}
Obsoletes:      %{extra_provides}-test < %{version}
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql-test < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql-test)

%description test
This package contains the test scripts and data for MySQL Community Server.

To run the testsuite, run /usr/share/mysql-test/suse-test-run.

%package tools
Summary:        MySQL Community Server tools
Group:          Productivity/Databases/Servers
Requires:       perl-DBD-mysql
# make sure this package is installed when updating from 10.2 and older
Provides:       mysql-client:/usr/bin/perror
Provides:       mysql-tools = %{srv_vers}
Provides:       mysql:/usr/bin/mysqlhotcopy
%if 0%{?use_extra_provides} > 0
Provides:       %{extra_provides}-tools = %{version}
Obsoletes:      %{extra_provides}-tools < %{version}
%endif
%if 0%{?prefered} > 0
Obsoletes:      mysql-tools < %{srv_vers}
%endif
Conflicts:      otherproviders(mysql-tools)

%description tools
A set of scripts for administering a MySQL Community Server or developing
applications with MySQL Community Server.

%if 0%{?cluster} > 0

%if 0%{?cluster} > 1

%package -n libndbclient6
Summary:        Shared Libraries for cluster client
Group:          Development/Libraries/Other

%description -n libndbclient6
This package contains the shared libraries (.so) which certain
languages and applications need to dynamically load and use MySQL Community Server
cluster.

%endif

%package ndb-storage
Summary:        MySQL Community Server - ndbcluster storage engine
Group:          Productivity/Databases/Servers
Provides:       mysql-ndb-storage = %{srv_vers}
Obsoletes:      mysql-ndb-storage < %{srv_vers}
Conflicts:      otherproviders(mysql-ndb-storage)

%description ndb-storage
This package contains the ndbcluster storage engine. 
It is necessary to have this package installed on all 
computers that should store ndbcluster table data.


%package ndb-management
Summary:        MySQL Community Server - ndbcluster storage engine management
Group:          Productivity/Databases/Servers
Provides:       mysql-ndb-management = %{srv_vers}
Obsoletes:      mysql-ndb-management < %{srv_vers}
Conflicts:      otherproviders(mysql-ndb-management)

%description ndb-management
This package contains ndbcluster storage engine management.
It is necessary to have this package installed on at least 
one computer in the cluster.

%package ndb-tools
Summary:        MySQL Community Server - ndbcluster storage engine basic tools
Group:          Productivity/Databases/Servers
Provides:       mysql-ndb-tools = %{srv_vers}
Obsoletes:      mysql-ndb-tools < %{srv_vers}
Conflicts:      otherproviders(mysql-ndb-tools)

%description ndb-tools
This package contains ndbcluster storage engine basic tools.

%package ndb-extra
Summary:        MySQL Community Server - ndbcluster storage engine extra tools
Group:          Productivity/Databases/Servers
Provides:       mysql-ndb-extra = %{srv_vers}
Obsoletes:      mysql-ndb-extra < %{srv_vers}
Conflicts:      otherproviders(mysql-ndb-extra)

%description ndb-extra
This package contains some extra ndbcluster storage engine tools for the
advanced user.  They should be used with caution.
%endif

%prep
%setup -q
cp %_sourcedir/suse-test-run .
# remove unneeded manpages ('make install' basically installs everything under
# man/*)
rm -f man/mysqlman.1        # dummy fallback manpage
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysqlman.1||'     man/CMakeLists.txt
rm -f man/mysql.server.1    # init script, not installed in our rpm
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysql.server.1||' man/CMakeLists.txt
rm -f man/make_win_*.1      # windows build scripts
rm -f man/comp_err.1        # built-time utility
# 5.1 Carrier Grade Edition only / still under development as of 5.1.22
rm -f man/ndbd_redo_log_reader.1
# breaks VPATH builds when in sourcedir, is generated in the builddirs
rm -f sql/sql_builtin.cc
sed -i 's|@localstatedir@|/var/log|' support-files/mysql-log-rotate.sh
%if 0%{prefered} < 1
for i in `grep -Rl mysqlclient .`; do
	sed -i 's|mysqlclient|mysqlclient|g' $i
done
%endif

%build
%{expand:%(cat %_sourcedir/build.inc)}

%install
%{expand:%(cat %_sourcedir/install.inc)}

%pre
/usr/sbin/groupadd -r mysql >/dev/null 2>/dev/null || :
/usr/sbin/useradd -r -o -g mysql -u 60 -c "MySQL database admin" \
                  -s /bin/false -d /var/lib/mysql mysql 2> /dev/null || :
/usr/sbin/usermod -g mysql -s /bin/false mysql || :

#######################################################################
# preun and posttran takes care of restart                            #
#######################################################################

%preun
[ $1 = 1 ] || /usr/sbin/rcmysql stop

%pretrans -p <lua>
if posix.access("/usr/sbin/rcmysql", "x") then
  restart = os.execute("/usr/sbin/rcmysql status > /dev/null")
  os.execute("/usr/sbin/rcmysql stop")

  if restart == 0 then
    os.execute("/bin/mkdir -p /var/run/mysql/restart")
  end
end

dbfile="var/mysql/mysql/db.ISM"
olddir="var/mysql"
newdir="var/lib/mysql"
-- Do the database files still belong to root (very old installation)?
-- Change ownerships
if posix.stat(dbfile, "uid") == 0 then
  os.execute("/bin/chown -Rv mysql:mysql var/mysql/")
end

%posttrans
%install_info --info-dir=%{_infodir} %{_infodir}/mysql.info.*
if [ -d /var/lib/mysql ]; then
	touch /var/lib/mysql/.run-mysql_upgrade
	chown -R mysql:mysql /var/lib/mysql
fi
for i in /var/lib/mysql/{.protected,.tmp}; do
	( [ -d "$i" ] && rmdir "$i" ) || :
done
# start mysql again if it should run
if [ "`ls /etc/rc.d/rc*.d/S*mysql 2> /dev/null`" ] || [ -d /var/run/mysql/restart ]; then
	[ -x /usr/sbin/rcmysql ] && /usr/sbin/rcmysql start
	rmdir /var/run/mysql/restart || :
fi

#######################################################################
# Various ldconfig post scripts                                       #
#######################################################################

%post -n libmysqlclient18 -p /sbin/ldconfig

%postun -n libmysqlclient18 -p /sbin/ldconfig

%post -n libmysqlclient_r18 -p /sbin/ldconfig

%postun -n libmysqlclient_r18 -p /sbin/ldconfig

%if 0%{cluster} > 1

%post -n libndbclient6 -p /sbin/ldconfig

%postun -n libndbclient6 -p /sbin/ldconfig
%endif

%postun
if [ $1 = 0 ]; then
	%install_info_delete --info-dir=%{_infodir} %{_infodir}/mysql.info.*
	%{insserv_cleanup}
fi

#######################################################################
# Files section                                                       #
#######################################################################

%files -f mysql.files
%defattr(-, root, root)
%config(noreplace) %attr(0640, root, mysql) /etc/my.cnf
%dir %attr(0750, root, mysql) /etc/mysql
# /etc/mysql/ empty, skip this for now
#%config(noreplace) %attr(0640, root, mysql) /etc/mysql/*
%config /etc/logrotate.d/mysql
%doc %{_defaultdocdir}/%{name}
%doc %{_infodir}/mysql.info.*
/etc/init.d/mysql
/usr/bin/wsrep_*
/usr/sbin/rcmysql
%dir /usr/share/%{name}
%dir /usr/share/mysql
/usr/share/%{name}/charsets/
/usr/share/mysql/*.cnf
# Below is perhaps different from mysql-5.5?
#/usr/share/mysql/*.ini
/usr/share/mysql/wsrep_*
/usr/share/%{name}/*.sql
%ghost %dir %attr(755,mysql,mysql)/var/run/mysql
%dir %{_libdir}/mysql
%{_libdir}/mysql/mysqld.sym
%config /etc/sysconfig/SuSEfirewall2.d/services/mysql
%dir %_libdir/mysql/plugin
%_libdir/mysql/plugin/[!d]*.so

%files errormessages -f errormessages.files
%defattr(-, root, root)
/usr/share/%{name}/*/errmsg.sys

%files client -f mysql-client.files
%defattr(-, root, root)
%config(noreplace) %attr(0640, root, mysql) /etc/mysqlaccess.conf

%if 0%{prefered} > 0

%files -n libmysqlclient-devel -f libmysqlclient-devel.files
%defattr(-, root, root)
/usr/include/mysql
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so
%dir /usr/share/aclocal
/usr/share/aclocal/mysql.m4

%endif

%files -n libmysqlclient18
%defattr(-, root, root)
%{_libdir}/libmysqlclient.so.*

%if 0%{cluster} > 1

%files -n libndbclient6
%defattr(-, root, root)
%{_libdir}/libndbclient.so.*
%endif

%files -n libmysqlclient_r18
%defattr(-, root, root)
%{_libdir}/libmysqlclient_r.so.*

%files bench -f mysql-bench.files
%defattr(-, root, root)
/usr/share/sql-bench

%files debug-version
%defattr(-, root, root)
/usr/sbin/mysqld-debug
%{_libdir}/mysql/mysqld-debug.sym

%files test -f mysql-test.files
%defattr(-, root, root)
%{_bindir}/my_safe_process
# Not available in mysql-wsrep-5.6.20
#%_mandir/man1/mysql-test-run.pl.1*
#%_mandir/man1/mysql-stress-test.pl.1*
/usr/share/mysql-test/valgrind.supp
%dir %attr(755, root, root)/usr/share/mysql-test
/usr/share/mysql-test/[^v]*
%dir %attr(755, mysql, mysql) /usr/share/mysql-test/var

%files tools -f mysql-tools.files
%defattr(-, root, root)
%_bindir/mysqlrepair
%_bindir/mysqlanalyze
%_bindir/mysqloptimize

%if 0%{cluster} > 0

%files ndb-storage -f mysql-ndb-storage.files

%files ndb-management -f mysql-ndb-management.files

%files ndb-tools -f mysql-ndb-tools.files

%files ndb-extra -f mysql-ndb-extra.files

%endif

%changelog
