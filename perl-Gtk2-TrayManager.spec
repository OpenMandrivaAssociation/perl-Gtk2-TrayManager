%define upstream_name    Gtk2-TrayManager
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl bindings for EggTrayManager
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
URL:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: glitz-devel
BuildRequires: gtkspell-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2
BuildRequires: perl-Glib > 1.00 
BuildRequires: perl-ExtUtils-PkgConfig 
Buildrequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: gtk+2

%description
The EggTrayManager library is used internally by GNOME to implement the
server-side of the Notification Area (or system tray) protocol.

Gtk2::TrayManager allows you to create notification area applications using
Gtk2-Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/Gtk2/*
