Summary:	Portable C++ classes for IP(sockets) applications
Summary(pl):	Przeno¶ne klasy C++ implementuj±ce sokety IP
Name:		skstream
Version:	0.2.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildREquires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skstream library.

%description
Biblioteka skstream.

%package devel
Summary:	Header files for skstream development
Summary(pl):	Pliki nag³ówkowe do biblioteki skstream
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
skstream library.

This package contains the header files needed to develop programs that
use these skstream.

%description devel -l pl
Biblioteka skstream.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych bibliotek skstream.

%package static
Summary:	Static libraries for skstream development
Summary(pl):	Statyczne biblioteki skstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
skstream library.

This package contains the static skstream libraries.

%description static -l pl
Biblioteka skstream.

Pakiet zawiera statyczne biblioteki skstream.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skstream-config
%{_includedir}/skstream
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
