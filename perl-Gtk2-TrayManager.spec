%define module Gtk2-TrayManager
%define fmodule Gtk2/TrayManager

Summary: Perl bindings for EggTrayManager
Name:    perl-%module
Version: 0.05
Release: %mkrel 6
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkspell-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2
BuildRequires: perl-Glib > 1.00 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: glitz-devel
Buildrequires: perl-devel

Requires: gtk+2

%description
The EggTrayManager library is used internally by GNOME to implement the
server-side of the Notification Area (or system tray) protocol.

Gtk2::TrayManager allows you to create notification area applications using
Gtk2-Perl.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}*
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule

