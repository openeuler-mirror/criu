Name:          criu
Version:       3.16.1
Release:       6
Provides:      crtools = %{version}-%{release}
Obsoletes:     crtools <= 1.0-2
Summary:       A tool of Checkpoint/Restore in User-space
License:       GPL-2.0-or-later or LGPL-2.1-only
URL:           http://criu.org/
Source0:       http://github.com/chechpoint-restore/criu/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: systemd libnet-devel asciidoc xmlto perl-interpreter libselinux-devel gcc
BuildRequires: protobuf-devel protobuf-c-devel python3-devel libnl3-devel libcap-devel
BuildRequires: libmnl-devel libnftnl-devel
Recommends:    tar
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x
Requires:      %{name} = %{version}-%{release}
Provides:      %{name}-libs = %{version}-%{release}
Obsoletes:     %{name}-libs < %{version}-%{release}

Patch:      0001-criu-dump-and-restore-cpu-affinity-of-each-thread.patch
Patch:      0002-compel-add-rseq-syscall-into-compel-std-plugin-sysca.patch
Patch:      0003-kerndat-check-for-rseq-syscall-support-Signed-off-by.patch
Patch:      0004-util-move-fork_and_ptrace_attach-helper-from-cr-chec.patch
Patch:      0005-cr-check-Add-ptrace-rseq-conf-dump-feature-Add-get_r.patch
Patch:      0006-rseq-initial-support-TODO-1.-properly-handle-case-wh.patch
Patch:      0007-zdtm-add-simple-test-for-rseq-C-R-Signed-off-by-Alex.patch
Patch:      0008-ci-add-Fedora-Rawhide-based-test-on-Cirrus-We-have-a.patch
Patch:      0009-include-add-thread_pointer.h-from-Glibc-Implementati.patch
Patch:      0010-clone-noasan-unregister-rseq-at-the-thread-start-for.patch
Patch:      0011-zdtm-static-rseq00-fix-rseq-test-when-linking-with-a.patch
Patch:      0012-compel-add-helpers-to-get-set-instruction-pointer-Si.patch
Patch:      0013-cr-dump-fixup-thread-IP-when-inside-rseq-cs-Signed-o.patch
Patch:      0014-zdtm-add-rseq-transition-test-for-amd64-Signed-off-b.patch
Patch:      0015-cr-dump-handle-rseq-flags-field-Userspace-may-config.patch
Patch:      0016-zdtm-add-rseq02-transition-test-with-NO_RESTART-CS-f.patch
Patch:      0017-zdtm-fix-zdtm-static-maps00-case-in-arm64.patch
Patch:      0018-test-flush-ipt-rules-after-program-exits.patch
Patch:      0019-zdtm-fix-cleaning-step-of-zdtm_netns.patch
%ifarch aarch64
Patch:      0020-mm-add-pin-memory-method-for-criu.patch
Patch:      0021-pid-add-pid-recover-method-for-criu.patch
Patch:      0022-notifier-add-notifier-calling-method-for-checkpoint-.patch
Patch:      0023-block-device-dump-block-device-as-reguler-file.patch
Patch:      0024-anon-inode-add-support-for-anon-inode-fd.patch
Patch:      0025-char_dev-add-support-for-char-device-dump-and-restor.patch
Patch:      0026-improve-char-dev-fd-check-and-repair-method.patch
Patch:      0027-mmap-restore-dev-hisi_sec2-deivce-vma.patch
Patch:      0028-infiniband-fix-the-infiniband-fd-conflict.patch
Patch:      0029-cred-provide-cred-checkpoint-restore-method.patch
Patch:      0030-socket-fix-connect-error-of-invalid-param.patch
Patch:      0031-criu-eventpollfd-fix-for-improper-usage-in-appdata.patch
Patch:      0032-task_exit_notify-add-task-exit-notify-mask-method-fo.patch
Patch:      0033-unix-socket-add-support-for-unix-stream-socket.patch
Patch:      0034-netlink-add-repair-modes-and-clear-resource-when-fai.patch
Patch:      0035-sysvshm-add-dump-restore-sysv-shm-in-host-ipc-ns.patch
Patch:      0036-add-O_REPAIR-flag-to-vma-fd.patch
Patch:      0037-looser-file-mode-and-size-check.patch
Patch:      0038-file-lock-add-repair-mode-to-dump-file-locks.patch
Patch:      0039-unlock-network-when-restore-fails.patch
Patch:      0040-net-add-shared-socket-recover-method-for-criu.patch
Patch:      0041-tcp-save-src-ports-to-ip_local_reserved_ports-when-d.patch
Patch:      0042-reg-file-fix-dump-fail-problem-with-null-seek-op.patch
Patch:      0043-fix-dump-fail-problem-with-no-access-to-get-socket-f.patch
Patch:      0044-proc-parse-fix-vma-offset-value-for-the-sysfs-file-o.patch
Patch:      0045-add-reuse-file-method-for-recover-deleted-file-state.patch
Patch:      0046-sk-fix-share-sockets-repair-problem.patch
Patch:      0047-mm-add-clear-pin-mem-and-init-page-map-option.patch
Patch:      0048-fds-fix-fds-list-restore.patch
Patch:      0049-log-print-error-log-to-dev-kmsg.patch
Patch:      0050-unix-sk-improve-dgram-robustness.patch
Patch:      0051-sk-ignore-the-bind-error-for-icmp-socket.patch
Patch:      0052-optimization-parallel-collecting-vmas.patch
Patch:      0053-mm-add-exec-file-mapping-pin-method.patch
Patch:      0054-ptrace-trace-specific-syscall.patch
Patch:      0055-notifier-rollback-when-open-img-failed.patch
Patch:      0056-detach-don-t-kill-task-when-ptrace-PTRACE_DETACH-ret.patch
Patch:      0057-build-add-secure-compilation-options.patch
Patch:      0058-nftables-add-mnl-api.patch
Patch:      0059-nftables-implement-nft-api-for-tcp.patch
Patch:      0060-net-switch-to-nftables-API.patch
Patch:      0061-zdtm-unlink-kdat-before-testing.patch
Patch:      0062-zdtm-add-host-ns-sysvshm-ipc-case.patch
Patch:      0063-zdtm-add-pinmem-testcase.patch
Patch:      0064-zdtm-init-notifier-testcase.patch
Patch:      0065-zdtm-print-errno-info-when-accessing-.out-failure.patch
Patch:      0066-zdtm-print-more-info-for-fs.c.patch
Patch:      0067-zdtm-add-chardev-testcase.patch
Patch:      0068-zdtm-add-infiniband-testcase.patch
Patch:      0069-zdtm-add-share-port-testcase.patch
Patch:      0070-zdtm-tmp-test-script.patch
Patch:      0071-mod-add-criu-indepent-test.patch
Patch:      0072-kabichk-add-KABI-check-code.patch
%endif
Patch:      0073-criu-fix-conflicting-headers.patch
Patch:      0074-mount-add-definition-for-FSOPEN_CLOEXEC.patch
%if "%toolchain" == "clang"
Patch:      0075-fix-clang.patch
%endif

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
%if "%toolchain" == "clang"
	export LDFLAGS=`echo $LDFLAGS | sed 's/-fno-openmp-implicit-rpath//g'`
%endif
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
%{python3_sitelib}/crit-0.0.1-py%{python3_version}.egg

%files -n crit
%{_bindir}/crit

%files -n criu-ns
%{_sbindir}/criu-ns

%files help
%doc COPYING
%doc %{_mandir}/man8/criu.8*
%doc %{_mandir}/man1/{compel.1*,crit.1*,criu-ns.1*}

%changelog
* Fri Jul 14 2023 yoo <sunyuechi@iscas.ac.cn> - 3.16.1-6
- fix clang build error

* Wed Jan 4 2023 zhoujie <zhoujie133@huawei.com> - 3.16.1-5
- Fix compilation problems caused by glibc upgrade

* Fri Jul 22 2022 tenglei <tenglei@kylinos.cn> - 3.16.1-4
- Remove non-compliant README files
- fix files not found egg-info
- move changelog into spec file

* Wed Apr 13 2022 fu.lin <fulin10@huawei.com> - 3.16.1-3
- backport kinds of feature/bugfix
- spec: split changelog

* Fri Mar 4 2022 ningyu <ningyu9@huawei.com> - 3.16.1-2
- rseq c/r support

* Thu Dec 2 2021 zhouwenpei <zhouwenpei11@huawei.com> - 3.16.1-1
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
