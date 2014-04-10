%define module pymtp
%define debug_package %{nil}

Summary:	A python binding to libmtp

Name:		python-%{module}
Version:	0.0.6
Release:	1
License:	GPLv3
Group:		Development/Python
Url:		http://nick125.com/projects/pymtp
Source0:	https://pypi.python.org/packages/source/P/PyMTP/PyMTP-%{version}.tar.gz
BuildRequires:	python-devel
Requires:	libmtp-utils

%description
PyMTP is a Python binding to libmtp, the defacto open source
library for communicating with MTP-enabled devices.
These devices include the Creative Zen, Microsoft Zune, 
Normsoft Pocket Tunes and many more.

%prep
%setup -qn PyMTP-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc examples README
%{py_puresitedir}/*

