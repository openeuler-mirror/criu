Name:          criu
Version:       3.16.1
Release:       5
Provides:      crtools = %{version}-%{release}
Obsoletes:     crtools <= 1.0-2
Summary:       A tool of Checkpoint/Restore in User-space
License:       GPL-2.0-or-later or LGPL-2.1-only
URL:           http://criu.org/
Source0:       http://github.com/checkpoint-restore/criu/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: systemd libnet-devel asciidoc xmlto perl-interpreter libselinux-devel gcc
BuildRequires: protobuf-devel protobuf-c-devel python3-devel libnl3-devel libcap-devel
Recommends:    tar
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x
Requires:      %{name} = %{version}-%{release}
Provides:      %{name}-libs = %{version}-%{release}
Obsoletes:     %{name}-libs < %{version}-%{release}

Patch1:     0001-criu-dump-and-restore-cpu-affinity-of-each-thread.patch
Patch2:     0002-mm-add-pin-memory-method-for-criu.patch
Patch3:     0002-compel-add-rseq-syscall-into-compel-std-plugin-sysca.patch
Patch4:     0003-kerndat-check-for-rseq-syscall-support.patch
Patch5:     0004-util-move-fork_and_ptrace_attach-helper-from-cr-chec.patch
Patch6:     0005-cr-check-Add-ptrace-rseq-conf-dump-feature.patch
Patch7:     0006-rseq-initial-support.patch
Patch8:     0007-zdtm-add-simple-test-for-rseq-C-R.patch
Patch9:     0008-ci-add-Fedora-Rawhide-based-test-on-Cirrus.patch
Patch10:    0009-include-add-thread_pointer.h-from-Glibc.patch
Patch11:    0010-clone-noasan-unregister-rseq-at-the-thread-start-for.patch
Patch12:    0011-zdtm-static-rseq00-fix-rseq-test-when-linking-with-a.patch
Patch13:    0012-compel-add-helpers-to-get-set-instruction-pointer.patch
Patch14:    0013-cr-dump-fixup-thread-IP-when-inside-rseq-cs.patch
Patch15:    0014-zdtm-add-rseq-transition-test-for-amd64.patch
Patch16:    0015-cr-dump-handle-rseq-flags-field.patch
Patch17:    0016-zdtm-add-rseq02-transition-test-with-NO_RESTART-CS-f.patch

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

%package -n criu-ns
Summary: Tool to run CRIU in different namespaces
Requires: %{name} = %{version}-%{release}

%description -n criu-ns

%package help
Summary:  Help documents for criu

%description help
Help documents for criu.

%prep
%autosetup -n %{name}-%{version} -p1

%build
CFLAGS+=`echo %{optflags}` make V=1 WERROR=0 PREFIX=%{_prefix} RUNDIR=/run/criu PYTHON=python3

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

%files -n criu-ns
%{_sbindir}/criu-ns

%files help
%doc README.md COPYING
%doc %{_mandir}/man8/criu.8*
%doc %{_mandir}/man1/{compel.1*,crit.1*,criu-ns.1*}

%changelog
* Thu Nov 10 2022 caodongxia <caodongxia@h-partners.com> - 3.16.1-5
- Modify invalid source0

* Wed Oct 19 2022 fu.lin <fulin10@huawei.com> -3.16.1-4
- bump the version

* Fri Mar 4 2022 ningyu <ningyu9@huawei.com> - 3.16.1-3
- rseq c/r support

* Sat Feb 26 2022 luolongjun <luolongjuna@gmail.com> - 3.16.1-2
- add support for pin memory

* Fri Dec 24 2021 zhouwenpei <zhouwenpei11@huawei.com> - 3.16.1-1
- upgrade criu version to 3.16.1

* Tue Sep 07 2021 chenchen <chen_aka_jan@163.com> - 3.15-4
- add "-fstack-protector-strong" for libcriu.so.2.0

* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 3.15-3
- Add gcc in BuildRequires

* Thu Apr 08 2021 fu.lin <fulin10@huawei.com> - 3.15-1
- bump the criu version to v3.15

* Tue Sep 22 2020 lingsheng <lingsheng@huawei.com> - 3.13-7
- Fix crit errors

* Fri Apr 24 2020 wutao <wutao61@huawei.com> - 3.13-6
- Package init
