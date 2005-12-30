Summary:	C++ class library for symbolic calculations
Summary(pl):	Biblioteka klas C++ do obliczeñ symbolicznych
Name:		GiNaC
Version:	1.3.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/GiNaC/%{name}-%{version}.tar.bz2
# Source0-md5:	40c160ad313977293e5fea2acab09518
Patch0:		%{name}-info.patch
URL:		http://www.ginac.de/
BuildRequires:	automake
BuildRequires:	cln-devel >= 1.1
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	cln >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the C++
programming language.

%description -l pl
GiNaC (co oznacza "GiNaC is Not a CAS (Computer Algebra System)") to
otwarty szkielet do obliczeñ symbolicznych w jêzyku programowania C++.

%package devel
Summary:	Header files and more to develop GiNaC applications
Summary(pl):	Pliki nag³ówkowe i inne do tworzenia aplikacji GiNaC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cln-devel >= 1.1
Requires:	pkgconfig

%description devel
This package contains include files and other resources you can use to
develop GiNaC applications.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i inne zasoby, których mo¿na
u¿ywaæ do rozwiajania aplikacji opartych na GiNaC.

%package static
Summary:	Static GiNaC library
Summary(pl):	Statyczna biblioteka GiNaC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GiNaC library.

%description static -l pl
Statyczna biblioteka GiNaC.

%package utils
Summary:	GiNaC-related utilities
Summary(pl):	Narzêdzia zwi±zane z GiNaC
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description utils
This package includes the ginsh ("GiNaC interactive shell") which
provides a simple and easy-to-use CAS-like interface to GiNaC for
non-programmers, and the tool "viewgar" which displays the contents of
GiNaC archives.

%description utils -l pl
Ten pakiet zawiera ginsh (interaktywn± pow³okê GiNaC, ktora udostêpnia
prosty i ³atwy w u¿yciu, podobny do CAS interfejs do GiNaC dla osób
nie bêd±cych programistami) oraz narzêdzie viewgar, wy¶wietlaj±ce
zawarto¶æ archiwów GiNaC.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%preun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ginac-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/ginac
%{_infodir}/*.info*
%{_mandir}/man1/ginac-config.1*
%{_aclocaldir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ginsh
%attr(755,root,root) %{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*
