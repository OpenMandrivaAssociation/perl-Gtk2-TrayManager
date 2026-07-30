%define upstream_name    Gtk2-TrayManager
%define upstream_version 0.05
Name:		perl-%{upstream_name}
Version:	0.05
Release:	2

Summary:	Perl bindings for EggTrayManager
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
URL:		https://gtk2-perl.sf.net/
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BORUP/Gtk2-TrayManager-0.05.tar.gz

BuildRequires:	make
BuildRequires:	glitz-devel
BuildRequires:	gtkspell-devel 
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(Glib) > 1.00 
Requires:	gtk+2

%description
The EggTrayManager library is used internally by GNOME to implement the
server-side of the Notification Area (or system tray) protocol.

Gtk2::TrayManager allows you to create notification area applications using
Gtk2-Perl.

%prep
%setup -q -n Gtk2-TrayManager-0.05
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%{optflags} -Os -s"
#%make test || :

%install
%makeinstall_std

%files
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/Gtk2/*


