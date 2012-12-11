%define module pymtp

Summary:	A python binding to libmtp
Name:		python-%{module}
Version:	0.0.4
Release:	%mkrel 6
License:	GPLv3
Group:		Development/Python
Url:		http://nick125.com/projects/pymtp
Source0:	http://downloads.nick125.com/projects/pymtp/%{module}-%{version}.tar.bz2
BuildRequires:	python-devel
Requires:	libmtp-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PyMTP is a Python binding to libmtp, the defacto open source
library for communicating with MTP-enabled devices.
These devices include the Creative Zen, Microsoft Zune, 
Normsoft Pocket Tunes and many more.

%prep
%setup -qn %{module}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples README
%{py_puresitedir}/*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.0.4-6mdv2010.0
+ Revision: 442443
- rebuild

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.0.4-5mdv2009.1
+ Revision: 320645
- rebuild for new python

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.0.4-4mdv2009.0
+ Revision: 269039
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.4-3mdv2009.0
+ Revision: 195632
- fix buildrequires
- package is no more noarch

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.4-2mdv2009.0
+ Revision: 195483
- fix requires

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.4-1mdv2009.0
+ Revision: 195275
- add source and spec file
- Created package structure for python-pymtp.

