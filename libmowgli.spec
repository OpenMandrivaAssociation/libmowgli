%define name libmowgli
%define version 0.7.1
%define release %mkrel 1

%define major 2
%define libname %mklibname mowgli %major
%define libnamedev %mklibname -d mowgli

Summary: Development framework with high performance algorithms
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://distfiles.atheme.org/libmowgli-%version.tbz2
License: BSD
Group: System/Libraries
Url: http://www.atheme.org/project/mowgli
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib list manipulation
functions), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.


%package -n %libname
Group: System/Libraries
Summary: Development framework library

%description -n %libname
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib list manipulation
functions), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%package -n %libnamedev
Group: Development/C
Summary: Development framework header files
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %libnamedev
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib list manipulation
functions), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/libmowgli.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%doc AUTHORS
%_libdir/libmowgli.so
%_libdir/pkgconfig/libmowgli.pc
%_includedir/%name/
