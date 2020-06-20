Name:          criu
Version:       3.13
Release:       6
Provides:      crtools = %{version}-%{release}
Obsoletes:     crtools <= 1.0-2
Summary:       A tool of Checkpoint/Restore in User-space
License:       GPLv2
URL:           http://criu.org/
Source0:       http://download.openvz.org/criu/criu-%{version}.tar.bz2
BuildRequires: systemd libnet-devel asciidoc xmlto perl-interpreter libselinux-devel
BuildRequires: protobuf-devel protobuf-c-devel python3-devel libnl3-devel libcap-devel
Recommends:    tar
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x
Requires:      %{name} = %{version}-%{release}
Provides:      %{name}-libs = %{version}-%{release}
Obsoletes:     %{name}-libs < %{version}-%{release}

%description
Checkpoint/Restore in Userspace(CRIU),is a software tool for the linux operating system.
Using this tool,it is possible to freeze a running application (or part of it) and
checkpoint it to persistent storage as a collection of files.

%package devel
Summary:  Static files and header files of libraries for criu
Requires: %{name} = %{version}-%{release}

%description devel
Static files and header files of libraries for criu.

%package -n python3-criu
%{?python_provide:%python_provide python3-criu}
Summary:   Bindings of python for criu
Requires:  python3-protobuf
Obsoletes: python2-criu < 3.10-1

%description -n python3-criu
Bindings of python for criu.

%package -n crit
Summary:  A tool for CRIU image
Requires: python3-criu = %{version}-%{release}

%description -n crit
A tool for CRIU image.

%package help
Summary:  Help documents for criu

%description help
Help documents for criu.

%prep
%autosetup -n %{name}-%{version} -p1

%build
CFLAGS+=`echo %{optflags} | sed -e 's,-fstack-protector\S*,,g'` make V=1 WERROR=0 PREFIX=%{_prefix} RUNDIR=/run/criu PYTHON=python3

%install
make install-criu DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}
make install-lib DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} PYTHON=python3
make install-man DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}

install -d %{buildroot}/run/%{name}/
chmod 0755 %{buildroot}/run/%{name}/

%files
%{_sbindir}/%{name}
%{_libexecdir}/%{name}
%dir /run/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/criu
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/libcriu.a

%files -n python3-criu
%{python3_sitelib}/{pycriu/*,*egg-info}

%files -n crit
%{_bindir}/crit

%files help
%doc README.md COPYING
%doc %{_mandir}/man8/criu.8*
%doc %{_mandir}/man1/{compel.1*,crit.1*}

%changelog
* Fri Apr 24 2020 wutao <wutao61@huawei.com> - 3.13-6
- Package init
