%define major 2
%define libname %mklibname mowgli %{major}
%define libnamedev %mklibname -d mowgli

Summary:	Development framework with high performance algorithms
Name:		libmowgli
Version:	1.0.0
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/project/mowgli
Source0:	http://distfiles.atheme.org/libmowgli-%{version}.tar.bz2

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

%package -n %{libnamedev}
Group:		Development/C
Summary:	Development framework header files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmowgli.so.%{major}*

%files -n %{libnamedev}
%doc AUTHORS
%{_libdir}/libmowgli.so
%{_libdir}/pkgconfig/libmowgli.pc
%{_includedir}/%{name}/


%changelog
* Tue Nov 29 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2012.0
+ Revision: 735333
- update to new version 1.0.0

* Tue Sep 27 2011 Götz Waschk <waschk@mandriva.org> 0.9.95-1
+ Revision: 701416
- update to new version 0.9.95

* Thu May 05 2011 Götz Waschk <waschk@mandriva.org> 0.9.50-1
+ Revision: 669174
- new version
- fix source URL
- update URL

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 570282
- new version

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2009.0
+ Revision: 239309
- new version
- new major

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 170663
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jan 01 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 140063
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.1
+ Revision: 98443
- new version

* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 96174
- new version

* Mon Jul 23 2007 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 54554
- Import libmowgli



* Mon Jul 23 2007 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2008.0
- initial package
