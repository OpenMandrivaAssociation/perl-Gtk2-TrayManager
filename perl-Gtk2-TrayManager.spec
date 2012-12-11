%define upstream_name    Gtk2-TrayManager
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl bindings for EggTrayManager
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
URL:		http://gtk2-perl.sf.net/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}
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


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.50.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 403232
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2009.0
+ Revision: 257187
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2008.1
+ Revision: 152117
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2008.1
+ Revision: 122674
- kill re-definition of %%buildroot on Pixel's request


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-3mdk
- fix mistake

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Fix BuildRequires

* Thu May 19 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-1mdk
- initial release

