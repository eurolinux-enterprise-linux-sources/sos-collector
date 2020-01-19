Summary: Capture sosreports from multiple nodes simultaneously
Name: sos-collector
Version: 1.5
Release: 3%{?dist}
Source0: http://people.redhat.com/jhunsake/sos-collector/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Url: https://github.com/sosreport/sos-collector
Requires: sos >= 3.0
Obsoletes: clustersos < 1.2.2-2
Provides: clustersos = %{version}-%{release}

Patch0:	sos-collector-bytes-conversion.patch
Patch1:	sos-collector-fix-non-root-local.patch
Patch2:	sos-collector-deb-support.patch
Patch3:	sos-collector-case-id-prompt.patch
Patch4: sos-collector-fix-options-reporting.patch
Patch5: sos-collector-race-condition-cluster-loading.patch
Patch6: sos-collector-quote-all-options.patch

%if 0%{?rhel}
BuildRequires: python-devel
BuildRequires: python-paramiko
Requires: python-paramiko >= 2.0
Requires: python2-futures
Requires: python-six
%else
BuildRequires: python3-devel
BuildRequires: python3-paramiko
Requires: python3-paramiko >= 2.0
Requires: python3-six
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
%patch6 -p1

%build
%if 0%{?rhel}
%py2_build
%else
%py3_build
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/sos-collector.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%if 0%{?rhel}
%py2_install
%else
%py3_install
%endif



%check
%if 0%{?rhel}
%{__python2} setup.py test
%else
%{__python3} setup.py test
%endif

%files
%{_bindir}/sos-collector
%if 0%{?rhel}
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_mandir}/man1/*

%doc LICENSE

%changelog
* Tue Nov 13 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-3
- Resolve race condition in cluster profile loading
- Quote all options globally
- RHBZ#1633515
- RHBZ#1647955

* Wed Nov 07 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-2
- Fix cluster option reporting

* Mon Oct 22 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-1
- Update to version 1.5
- Resolves CVE-2018-14650

* Wed Aug 01 2018 Jake Hunsaker <jhunsake@redhat.com> 1.4-3
- Initial RHEL 7 release
