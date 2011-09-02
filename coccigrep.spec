%define	oname	coccigrep

Name:		%{oname}
Version:	1.0rc1
Release:	1
Summary:	Semantic grep for C based on coccinelle
Source0:	http://pypi.python.org/packages/source/c/%{oname}/%{oname}-%{version}.tar.gz
License:	GNU General Public License (GPL)
Group:		Development/Libraries
Url:		http://home.regit.org/software/coccigrep/
BuildArch:	noarch
Requires:	coccinelle
Requires:	%{name}-data = %{version}-%{release}
BuildRequires:  python-devel
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
Coccigrep is a semantic grep for the C language based on coccinelle. It
can be used to find where a given structure is used in code files.
coccigrep depends on the spatch program which comes with coccinelle.

%files
%{_bindir}/%{name}
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/%{name}*.egg-info

%package data
Summary:	Data for %{name}

%description data
This package provides the data for %{name}, i.e. the coccinelle semantic
patches.

%files data
%{py_puresitedir}/%{name}/%{name}.cfg
%{py_puresitedir}/%{name}/data/

%package doc
Summary:	Documentation for %{name}

%description doc
This package provides the documentation for %{name}.

%files doc

%package vim
Summary:	VIM support for %{name}

%description vim
This package provides Vim integration for %{name}.

%files vim

%package emacs
Summary:	Emacs for %{name}

%description emacs
This package provides Emacs integration for %{name}.

%files emacs

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}