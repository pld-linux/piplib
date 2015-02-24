#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Parametric Integer Programming library
Summary(pl.UTF-8):	Biblioteka do parametrycznego programowania całkowitoliczbowego
Name:		piplib
Version:	1.4.0
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.bastoul.net/cloog/pages/download/%{name}-%{version}.tar.gz
# Source0-md5:	f5d1c7d45c5c40c0d64fa7d6bb143740
Patch0:		format-security.patch
URL:		http://www.piplib.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PIP/PipLib is the well known Paul Feautrier's parametric integer
programming solver. PIP is a software which finds the lexicographic
minimum of the set of integer points which lie inside a convex
polyhedron. This polyhedron can depend linearly on one or more
integral parameters. If user ask for a non integral solution, PIP can
give the exact solution as an integral quotient. The heart of PIP is
the parametrized Gomory's cuts algorithm followed by parametrized dual
simplex method. The PIP Library (PipLib for short) was implemented to
allow the user to call PIP directly from his programs, without file
accesses or system calls. The user only needs to link his programs
with C libraries.

%description -l pl.UTF-8
PIP/PipLib to biblioteka implementująca dobrze znany algorytm Paula
Featriera rozwiązywania problemów parametrycznego programowania
całkowitoliczbowego. PIP znajduje leksykograficzne minimum zbioru
punktów całkowitych leżących wewnątrz wielościanu wypukłego.
Wielościan może zależeć liniowo od jednego lub większej liczby
parametrów całkowitych. W przypadku zapytania o rozwiązanie
niecałkowite, PIP potrafi wyznaczyć dokładne rozwiązanie jako iloraz
liczb całkowitych. Sercem PIP jest parametryzowany algorytm cięć
Gomory'ego, po którym stosowana jest parametryzowana dualna metoda
simpleks. Biblioteka PIP (w skrócie PipLib) została zaimplementowana
tak, aby użytkownik mógł wywołać PIP bezpośrednio z programów, bez
dostępu do plików czy wywołań systemowych; wymagane są tylko
biblioteki C.

%package devel
Summary:	Header files for PIP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PIP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel

%description devel
Header files for PIP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PIP.

%package static
Summary:	Static PIP library
Summary(pl.UTF-8):	Statyczna biblioteka PIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PIP library.

%description static -l pl.UTF-8
Statyczna biblioteka PIP.

%package apidocs
Summary:	PIP API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki PIP
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for PIP library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki PIP.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
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
%doc README
%attr(755,root,root) %{_bindir}/pip32
%attr(755,root,root) %{_bindir}/pip64
%attr(755,root,root) %{_bindir}/pipMP
%attr(755,root,root) %{_libdir}/libpiplib32.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpiplib32.so.2
%attr(755,root,root) %{_libdir}/libpiplib64.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpiplib64.so.2
%attr(755,root,root) %{_libdir}/libpiplibMP.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpiplibMP.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpiplib32.so
%attr(755,root,root) %{_libdir}/libpiplib64.so
%attr(755,root,root) %{_libdir}/libpiplibMP.so
%{_libdir}/libpiplib32.la
%{_libdir}/libpiplib64.la
%{_libdir}/libpiplibMP.la
%{_includedir}/piplib

%files static
%defattr(644,root,root,755)
%{_libdir}/libpiplib32.a
%{_libdir}/libpiplib64.a
%{_libdir}/libpiplibMP.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/piplib.pdf
%endif
