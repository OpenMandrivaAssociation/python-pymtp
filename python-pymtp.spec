%define module pymtp

Summary:	A python binding to libmtp
Name:		python-%{module}
Version:	0.0.4
Release:	%mkrel 1
License:	GPLv3
Group:		Development/Python
Url:		http://nick125.com/projects/pymtp
Source0:	http://downloads.nick125.com/projects/pymtp/%{module}-%{version}.tar.bz2
BuildRequires:	python-devel
Requires:	%{_lib}mtp7
BuildArch:	noarch
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
