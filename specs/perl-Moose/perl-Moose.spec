# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Moose

Summary: Perl module that implements a complete modern object system
Name: perl-Moose
Version: 0.29
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Moose/

Source: http://www.cpan.org/authors/id/G/GR/GRODITI/Moose-%{version}.tar.gz
#Source: http://www.cpan.org/authors/id/S/ST/STEVAN/Moose-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::LongString)
#BuildRequires: perl(Test::More) >= 0.62

%description
Moose is a Perl module that implements a complete modern object system.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Moose.3pm*
%doc %{_mandir}/man3/Moose::*.3pm*
%doc %{_mandir}/man3/Test::Moose.3pm*
%{perl_vendorlib}/Moose/
%{perl_vendorlib}/Moose.pm
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Moose.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
