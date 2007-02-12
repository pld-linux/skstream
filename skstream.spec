Summary:	Portable C++ classes for IP(sockets) applications
Summary(pl.UTF-8):   Przenośne klasy C++ implementujące gniazda IP
Name:		skstream
Version:	0.3.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	4fd3505755e6bad18d5ec1b269afe756
URL:		http://www.worldforge.org/dev/eng/libraries/skstream/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skstream library.

%description -l pl.UTF-8
Biblioteka skstream.

%package devel
Summary:	Header files for skstream development
Summary(pl.UTF-8):   Pliki nagłówkowe do biblioteki skstream
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files needed to develop programs that
use these skstream.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających bibliotek skstream.

%package static
Summary:	Static libraries for skstream development
Summary(pl.UTF-8):   Statyczne biblioteki skstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static skstream libraries.

%description static -l pl.UTF-8
Pakiet zawiera statyczne biblioteki skstream.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/skstream-*
%{_includedir}/skstream-*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
