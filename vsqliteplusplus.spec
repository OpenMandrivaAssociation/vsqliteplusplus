%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:       vsqlite++
Version:    0.3.13
Release:    1
Summary:    Well designed C++ sqlite 3.x wrapper library

Group:      Development/C++
License:    BSD
URL:        https://github.com/vinzenz/vsqlite--
Source0:    http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/vsqlite---%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  sqlite3-devel
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
VSQLite++ is a C++ wrapper for sqlite3 using 
the C++ standard library and boost.
VSQLite++ is designed to be easy to 
use and focuses on simplicity.

%package -n     %{libname}
Summary:        Development files for %{name}
Group:          Development/C++

%description -n     %{libname}
This package contains development files for %{name}.

%package -n     %{develname}
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n     %{develname}
This package contains development files for %{name}.


%prep
%setup -q -n vsqlite---%{version}
./autogen.sh

%build
%configure2_5x --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make
doxygen Doxyfile

%install
# devel & base
install -p -m 755 -d %{buildroot}%{_libdir}
# devel only
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite/ext
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/ext/*.hpp %{buildroot}%{_includedir}/sqlite/ext
# docs
install -p -m 755 -d %{buildroot}%{_docdir}

# build for all
make DESTDIR=%{buildroot} install



%files 
%doc ChangeLog README COPYING examples/sqlite_wrapper.cpp html/*

%files -n     %{develname}
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite

%files -n %{libname}
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.*



