Summary:	C++ class library for symbolic calculations
Name:		GiNaC
Version:	1.1.0
Release:	1
License:	GPL
Group:		Sciences/Mathematics
# Source0-md5:	30c86d96a9d9d689ff0981409b038906
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/GiNaC/%{name}-%{version}.tar.bz2
Source1:	ginac.png
URL:		http://www.ginac.de/
BuildRequires:	cln-devel >= 1.1
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the C++
programming language.

%package devel
Summary:	Libraries, includes and more to develop GiNaC applications
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the C++
programming language.

This is the libraries, include files and other resources you can use
to develop GiNaC applications.

%package utils
Summary:	GiNaC-related utilities
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}-%{release}

%description utils
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the C++
programming language.

This package includes the ginsh ("GiNaC interactive shell") which
provides a simple and easy-to-use CAS-like interface to GiNaC for
non-programmers, and the tool "viewgar" which displays the contents of
GiNaC archives.

%prep
%setup -q

%build
%configure
%{__make}

%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
%_install_info ginac.info

%preun devel
%_remove_install_info ginac.info

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/ginac/*.h
%{_infodir}/*.info*
%{_mandir}/man1/ginac-config.1*
%attr(755,root,root) %{_bindir}/ginac-config
%{_aclocaldir}/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ginsh
%attr(755,root,root) %{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*
%_menudir/%name-utils
%_iconsdir/ginac.png
