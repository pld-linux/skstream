Summary:	Portable C++ classes for IP(sockets) applications
Summary(pl):	Przenośne klasy C++ implementujące sokety IP
Name:		skstream
Version:	0.2.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	39f42e1294ec35fa581df56c1291621f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildREquires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skstream library.

%description -l pl
Biblioteka skstream.

%package devel
Summary:	Header files for skstream development
Summary(pl):	Pliki nagłówkowe do biblioteki skstream
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
This package contains the header files needed to develop programs that
use these skstream.

%description devel -l pl
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających bibliotek skstream.

%package static
Summary:	Static libraries for skstream development
Summary(pl):	Statyczne biblioteki skstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the static skstream libraries.

%description static -l pl
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
