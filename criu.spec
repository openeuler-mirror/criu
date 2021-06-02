Name:          criu
Version:       3.15
Release:       3
Provides:      crtools = %{version}-%{release}
Obsoletes:     crtools <= 1.0-2
Summary:       A tool of Checkpoint/Restore in User-space
License:       GPL-2.0-or-later or LGPL-2.1-only
URL:           http://criu.org/
Source0:       http://download.openvz.org/criu/criu-%{version}.tar.bz2
BuildRequires: systemd libnet-devel asciidoc xmlto perl-interpreter libselinux-devel gcc
BuildRequires: protobuf-devel protobuf-c-devel python3-devel libnl3-devel libcap-devel
Recommends:    tar
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x
Requires:      %{name} = %{version}-%{release}
Provides:      %{name}-libs = %{version}-%{release}
Obsoletes:     %{name}-libs < %{version}-%{release}

Patch0001:     0001-Fix-crit-encode-TypeError.patch
Patch0002:     0002-Fix-crit-info-struct-unpack-error.patch
Patch0003:     0003-Fix-crit-x-UnicodeDecodeError.patch
Patch0004:     0004-criu-dump-and-restore-cpu-affinity-of-each-thread.patch
Patch0005:     0005-vdso-fix-segmentation-fault-caused-by-char-pointer-a.patch
Patch0006:     0006-criu-add-pin-memory-method.patch

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
* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 3.15-3
- Add gcc in BuildRequires

* Thu Apr 08 2021 fu.lin <fulin10@huawei.com> - 3.15-1
- bump the criu version to v3.15

* Tue Sep 22 2020 lingsheng <lingsheng@huawei.com> - 3.13-7
- Fix crit errors

* Fri Apr 24 2020 wutao <wutao61@huawei.com> - 3.13-6
- Package init
