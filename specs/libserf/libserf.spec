# $Id$
# Authority: cmr
# Upstream: <serf-dev@googlegroups.com>

%define real_name serf

Summary: HTTP client library written in C using apr
Name: libserf
Version: 1.1.1
Release: 0.1%{?dist}
License: Apache License 2.0
Group: Development/Libraries
URL: http://code.google.com/p/serf/

Source: http://serf.googlecode.com/files/serf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: openssl-devel
Requires: apr
Requires: apr-util
Requires: openssl

%description
HTTP client library written in C using apr.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/libserf-1.so.*
%{_libdir}/pkgconfig/serf-1.pc

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/libserf-1.so
%exclude %{_libdir}/libserf-1.a
%exclude %{_libdir}/libserf-1.la

%changelog
* Sun Feb 17 2013 Nico Kadel-Garcia <nkadel@gmail.com> - 1.1.1-0.1
- Update to 1.1.1.

* Mon Sep 12 2011 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.0-0.1
- Update to 1.0.0.

* Fri May 08 2009 Christoph Maser <cmr@financial.com> - 0.3.0-1
- Initial package.
