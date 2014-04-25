Name:		coccigrep
Version:	1.13
Release:	1
Summary:	Semantic grep for C based on coccinelle

Source0:	http://pypi.python.org/packages/source/c/coccigrep/%{name}-%{version}.tar.gz
License:	GNU General Public License (GPL)
Group:		Development/C
Url:		http://home.regit.org/software/coccigrep/
BuildArch:	noarch
Requires:	coccinelle
Requires:	%{name}-data = %{version}-%{release}
Suggests:	%{name}-doc = %{version}-%{release}
Suggests:	%{name}-vim = %{version}-%{release}
Suggests:	%{name}-emacs = %{version}-%{release}
BuildRequires:	python-sphinx
BuildRequires:	python-setuptools
BuildRequires:	texlive
BuildRequires:  python-devel

%description
Coccigrep is a semantic grep for the C language based on coccinelle. It
can be used to find where a given structure is used in code files.
coccigrep depends on the spatch program which comes with coccinelle.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
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
%{_docdir}/%{name}-doc/%{name}.pdf

%package vim
Summary:	VIM support for %{name}

Requires:	%{name} = %{version}-%{release}

%description vim
This package provides Vim integration for %{name}.

%files vim
%{_datadir}/vim/plugin/cocci-grep.vim

%package emacs
Summary:	Emacs for %{name}

Requires:	%{name} = %{version}-%{release}

%description emacs
This package provides Emacs integration for %{name}.

%files emacs
%{_datadir}/emacs/site-lisp/cocci-grep.el

%prep
%setup -q

%build
python setup.py build

pushd doc
make man latexpdf
popd

%install
python setup.py install --root=%{buildroot}

pushd doc
%{__install} -m0644 -D _build/latex/%{name}.pdf %{buildroot}%{_docdir}/%{name}-doc/%{name}.pdf
%{__install} -m0644 -D _build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
popd

pushd editors
%{__install} -m0644 -D cocci-grep.vim %{buildroot}%{_datadir}/vim/plugin/cocci-grep.vim
%{__install} -m0644 -D cocci-grep.el %{buildroot}%{_datadir}/emacs/site-lisp/cocci-grep.el
popd



