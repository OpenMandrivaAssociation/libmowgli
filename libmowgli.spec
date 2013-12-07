%define major	2
%define libname	%mklibname mowgli %{major}
%define devname	%mklibname -d mowgli

Summary:	Development framework with high performance algorithms
Name:		libmowgli
Version:	1.0.0
Release:	5
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/project/mowgli
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib list manipulation
functions), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%package -n %{libname}
Group:		System/Libraries
Summary:	Development framework library

%description -n %{libname}
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib list manipulation
functions), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%package -n %{devname}
Group:		Development/C
Summary:	Development framework header files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmowgli.so.%{major}*

%files -n %{devname}
%doc AUTHORS
%{_libdir}/libmowgli.so
%{_libdir}/pkgconfig/libmowgli.pc
%{_includedir}/%{name}/

