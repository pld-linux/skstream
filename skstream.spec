Summary:	Portable C++ classes for IP(sockets) applications
Summary(pl):	Przeno¶ne klasy C++ implementuj±ce gniazda IP
Name:		skstream
Version:	0.3.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.worldforge.org/pub/worldforge/libs/skstream/%{name}-%{version}.tar.bz2
# Source0-md5:	5364e1dc9b5016fd0d8a118be53ef2a5
# Source0-size:	192780
URL:		http://www.worldforge.org/dev/eng/libraries/skstream/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skstream library.

%description -l pl
Biblioteka skstream.

%package devel
Summary:	Header files for skstream development
Summary(pl):	Pliki nag³ówkowe do biblioteki skstream
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
This package contains the header files needed to develop programs that
use these skstream.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych bibliotek skstream.

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
