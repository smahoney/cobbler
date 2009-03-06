%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Network provisioning tool for Xen and Bare Metal Machines 
Name: koan
Version: 1.4.3
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GPLv2+
Group: Applications/System
Requires: mkinitrd
Requires: python >= 1.5
BuildRequires: python-devel
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]" || echo 0)}
Requires: python(abi) = %{pyver}
%endif
%if 0%{?fedora} >= 8
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/cobbler/

%description

Koan is a helper tool for use with 'cobbler'.  It allows for 
network installation of new virtualized guests and reinstallation 
of an existing system.

%prep
%setup -q

%build
%{__python} setup.py build

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --optimize=1 --root=$RPM_BUILD_ROOT

%clean
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%if 0%{?fedora} > 8
%{python_sitelib}/koan*.egg-info
%endif
%dir /var/spool/koan
%{_bindir}/koan
%dir %{python_sitelib}/koan
%{python_sitelib}/koan/*.py*
%{_mandir}/man1/koan.1.gz
%dir /var/log/koan

%doc AUTHORS COPYING CHANGELOG README

%changelog

* Tue Feb 17 2009 Michael DeHaan <mdehaan@redhat.com> - 1.4.333-1
- Upstream changes (see CHANGELOG)
- Reduce python version requirements

* Fri Feb 12 2009 Michael DeHaan <mdehaan@redhat.com> - 1.4.2-1
- Upstream changes (see CHANGELOG)

* Fri Jan 09 2009 Michael DeHaan <mdehaan@redhat.com> - 1.4.1-1
- Upstream changes (see CHANGELOG)

* Mon Dec 22 2008 Michael DeHaan <mdehaan@redhat.com> - 1.4.0-4
- Fix python(abi) requirement some more

* Mon Dec 22 2008 Michael DeHaan <mdehaan@redhat.com> - 1.4.0-3
- Fix python(abi) requirement

* Fri Dec 19 2008 Michael DeHaan <mdehaan@redhat.com> - 1.4.0-2
- Upstream changes (see CHANGELOG)

* Wed Dec 10 2008 Michael DeHaan <mdehaan@redhat.com> - 1.3.4-1
- New test release

* Mon Dec 08 2008 Michael DeHaan <mdehaan@redhat.com> - 1.3.3-1
- Upstream changes (see CHANGELOG)
- specfile changes for python 2.6 support

* Fri Nov 14 2008 Michael DeHaan <mdehaan@redhat.com> - 1.3.1-1
- Upstream changes (see CHANGELOG)

* Fri Sep 26 2008 Michael DeHaan <mdehaan@redhat.com> - 1.2.5-1
- Upstream changes (see CHANGELOG)

* Wed Aug 29 2008 Michael DeHaan <mdehaan@redhat.com> - 1.2.0-1
- Upstream changes (see CHANGELOG)

* Mon Jun 16 2008 Michael DeHaan <mdehaan@redhat.com> - 1.0.2-1
- Upstream changes (see CHANGELOG)

* Fri Jun 06 2008 Michael DeHaan <mdehaan@redhat.com> - 1.0.1-1
- Upstream changes (see CHANGELOG)

