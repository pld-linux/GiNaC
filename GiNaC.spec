Summary:	C++ class library for symbolic calculations
Summary(pl.UTF-8):	Biblioteka klas C++ do obliczeń symbolicznych
Name:		GiNaC
Version:	1.6.5
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.ginac.de/ginac-%{version}.tar.bz2
# Source0-md5:	5379a3ce17c30277513ef8ca9e0f53c2
Patch0:		%{name}-info.patch
URL:		http://www.ginac.de/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison >= 2.3
BuildRequires:	cln-devel >= 1.2.2
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	cln >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the C++
programming language.

%description -l pl.UTF-8
GiNaC (co oznacza "GiNaC is Not a CAS (Computer Algebra System)") to
otwarty szkielet do obliczeń symbolicznych w języku programowania C++.

%package devel
Summary:	Header files and more to develop GiNaC applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do tworzenia aplikacji GiNaC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cln-devel >= 1.2.2
Requires:	libstdc++-devel

%description devel
This package contains include files and other resources you can use to
develop GiNaC applications.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i inne zasoby, których można
używać do rozwiajania aplikacji opartych na GiNaC.

%package static
Summary:	Static GiNaC library
Summary(pl.UTF-8):	Statyczna biblioteka GiNaC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GiNaC library.

%description static -l pl.UTF-8
Statyczna biblioteka GiNaC.

%package utils
Summary:	GiNaC-related utilities
Summary(pl.UTF-8):	Narzędzia związane z GiNaC
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description utils
This package includes the ginsh ("GiNaC interactive shell") which
provides a simple and easy-to-use CAS-like interface to GiNaC for
non-programmers, and the tool "viewgar" which displays the contents of
GiNaC archives.

%description utils -l pl.UTF-8
Ten pakiet zawiera ginsh (interaktywną powłokę GiNaC, ktora udostępnia
prosty i łatwy w użyciu, podobny do CAS interfejs do GiNaC dla osób
nie będących programistami) oraz narzędzie viewgar, wyświetlające
zawartość archiwów GiNaC.

%prep
%setup -q -n ginac-%{version}
%patch0 -p1
%{__sed} -i -e 's/#include <iostream>/#include <cstdio>\n#include <iostream>/g' ginac/parser/lexer.cpp
# generated with wrong bison version, miscompiled by gcc 4.1+
#%{__rm} ginac/input_parser.{cc,h}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libginac.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libginac.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libginac.so
%{_libdir}/libginac.la
%{_includedir}/ginac
%{_infodir}/ginac.info*
%{_infodir}/ginac-examples.info*
%{_pkgconfigdir}/ginac.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libginac.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ginac-excompiler
%attr(755,root,root) %{_bindir}/ginsh
%attr(755,root,root) %{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*
