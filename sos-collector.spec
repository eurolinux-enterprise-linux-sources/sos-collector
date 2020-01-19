Summary: Capture sosreports from multiple nodes simultaneously
Name: sos-collector
Version: 1.7
Release: 5%{?dist}
Source0: http://people.redhat.com/jhunsake/sos-collector/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Url: https://github.com/sosreport/sos-collector
Requires: sos >= 3.0
Obsoletes: clustersos < 1.2.2-2
Provides: clustersos = %{version}-%{release}

Patch0: sos-collector-setuptools.patch
Patch1: sos-collector-old-pexpect.patch
Patch2: sos-collector-none-cluster-fix.patch
Patch3: sos-collector-nested-container-fix.patch
Patch4: sos-collector-rhcos-image.patch
Patch5: sos-collector-rhhiv-profile.patch

%if 0%{?rhel} == 7
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python2-futures
Requires: python-six
Requires: pexpect
%else
BuildRequires: python3-devel
Requires: python3-six
Requires: python3-pexpect
%endif


%description
sos-collector is a utility designed to capture sosreports from multiple nodes
at once and collect them into a single archive. If the nodes are part of
a cluster, profiles can be used to configure how the sosreport command
is run on the nodes.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%if 0%{?rhel} == 7
%py2_build
%else
%py3_build
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/sos-collector.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%if 0%{?rhel} == 7
%py2_install
%else
%py3_install
%endif



%check
%if 0%{?rhel} == 7
%{__python2} setup.py test
%else
%{__python3} setup.py test
%endif

%files
%{_bindir}/sos-collector
%if 0%{?rhel} == 7
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_mandir}/man1/*

%doc LICENSE

%changelog
* Wed May 15 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-5
- Add missing local fixes for older pexpect versions

* Wed May 15 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-4
- Correct handling of older pexpect versions

* Tue Apr 23 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-3
- Added RHHI-V cluster profile

* Thu Apr 11 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-2
- Fix 'none' cluster type enablement
- Update RHCOS image to use RHEL 8 support-tools
- Fix execution from within a container

* Mon Apr 01 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-1
- New upstream release
- Enhance container execution

* Thu Mar 07 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.6-3
- Fix local command execution
- Fix quoting for non-root commands
- Backport Satellite support
- Backport RHCOS support

* Tue Dec 11 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.6-2
- Handle older pexpect installations on RHEL 7

* Tue Dec 11 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.6-1
- New upstream release
- Drop paramiko dependency, use OpenSSH ControlPersist instead.

* Wed Nov 07 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-2
- Fix cluster option reporting

* Mon Oct 22 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-1
- Update to version 1.5
- Resolves CVE-2018-14650

* Wed Aug 01 2018 Jake Hunsaker <jhunsake@redhat.com> 1.4-3
- Initial RHEL 7 release
