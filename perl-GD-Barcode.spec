#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-GD-Barcode
Version  : 2.00
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/GD-Barcode-2.00.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/GD-Barcode-2.00.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgd-barcode-perl/libgd-barcode-perl_1.15-7.debian.tar.xz
Summary  : 'Create barcode image with GD'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-GD-Barcode-license = %{version}-%{release}
Requires: perl-GD-Barcode-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Importer)
BuildRequires : perl(Test2::V0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
GD::Barcode - Create barcode images with GD
SYNOPSIS
*ex. CGI*
use GD::Barcode::UPCE;
binmode(STDOUT);
print "Content-Type: image/png\n\n";
print GD::Barcode->new('EAN13', '123456789012')->plot->png;

%package dev
Summary: dev components for the perl-GD-Barcode package.
Group: Development
Provides: perl-GD-Barcode-devel = %{version}-%{release}
Requires: perl-GD-Barcode = %{version}-%{release}

%description dev
dev components for the perl-GD-Barcode package.


%package license
Summary: license components for the perl-GD-Barcode package.
Group: Default

%description license
license components for the perl-GD-Barcode package.


%package perl
Summary: perl components for the perl-GD-Barcode package.
Group: Default
Requires: perl-GD-Barcode = %{version}-%{release}

%description perl
perl components for the perl-GD-Barcode package.


%prep
%setup -q -n GD-Barcode-2.00
cd %{_builddir}
tar xf %{_sourcedir}/libgd-barcode-perl_1.15-7.debian.tar.xz
cd %{_builddir}/GD-Barcode-2.00
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/GD-Barcode-2.00/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-GD-Barcode
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-GD-Barcode/0855cf88e764a7df6acca787c89f3e2568895474 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/GD::Barcode.3
/usr/share/man/man3/GD::Barcode::COOP2of5.3
/usr/share/man/man3/GD::Barcode::Code39.3
/usr/share/man/man3/GD::Barcode::EAN13.3
/usr/share/man/man3/GD::Barcode::EAN8.3
/usr/share/man/man3/GD::Barcode::IATA2of5.3
/usr/share/man/man3/GD::Barcode::ITF.3
/usr/share/man/man3/GD::Barcode::Industrial2of5.3
/usr/share/man/man3/GD::Barcode::Matrix2of5.3
/usr/share/man/man3/GD::Barcode::NW7.3
/usr/share/man/man3/GD::Barcode::QRcode.3
/usr/share/man/man3/GD::Barcode::UPCA.3
/usr/share/man/man3/GD::Barcode::UPCE.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-GD-Barcode/0855cf88e764a7df6acca787c89f3e2568895474

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
