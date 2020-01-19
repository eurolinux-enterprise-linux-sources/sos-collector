Summary: Capture sosreports from multiple nodes simultaneously
Name: sos-collector
Version: 1.4
Release: 3%{?dist}
Source0: http://people.redhat.com/jhunsake/sos-collector/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Url: https://github.com/sosreport/sos-collector
Requires: sos >= 3.0
Obsoletes: clustersos < 1.2.2-2
Provides: clustersos = %{version}-%{release}


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
* Wed Aug 01 2018 Jake Hunsaker <jhunsake@redhat.com> 1.4-3
- Initial RHEL 7 release
