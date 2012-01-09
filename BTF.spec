Summary:	BTF: permutation to block triangular form
Summary(pl.UTF-8):	BTF - permutacja do postaci blokowo trójkątnej
Name:		BTF
Version:	1.1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/btf/%{name}-%{version}.tar.gz
# Source0-md5:	cd8f2e52a3618da471fbb60342a96915
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/btf/
BuildRequires:	UFconfig >= 3.7.0
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BTF permutes an unsymmetric matrix (square or rectangular) into its
block upper triangular form (more precisely, it computes a
Dulmage-Mendelsohn decomposition). BTF is required by the KLU package.

%description -l pl.UTF-8
BTF permutuje macierz niesymetryczną (kwadratową lub prostokątną) do
postaci górnej blokowo trójkątnej (ściślej mówiąc, oblicza rozkład
Dulmage'a-Mendelsohna). Pakiet BTF jest wymagany przez pakiet KLU.

%package devel
Summary:	Header files for BTF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BTF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig >= 3.7.0

%description devel
Header files for BTF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BTF.

%package static
Summary:	Static BTF library
Summary(pl.UTF-8):	Statyczna biblioteka BTF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static BTF library.

%description static -l pl.UTF-8
Statyczna biblioteka BTF.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/btf

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/btf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libbtf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbtf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbtf.so
%{_libdir}/libbtf.la
%{_includedir}/btf

%files static
%defattr(644,root,root,755)
%{_libdir}/libbtf.a
