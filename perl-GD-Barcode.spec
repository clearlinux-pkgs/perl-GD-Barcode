#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-GD-Barcode
Version  : 1.15
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/K/KW/KWITKNR/GD-Barcode-1.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KW/KWITKNR/GD-Barcode-1.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgd-barcode-perl/libgd-barcode-perl_1.15-7.debian.tar.xz
Summary  : Create barcode image with GD
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-GD-Barcode-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
GD::Barcode - Create barcode image with GD
DESCRIPTION
GD::Barcode is a subclass of GD and allows you to create barcode image with GD.

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


%prep
%setup -q -n GD-Barcode-1.15
cd ..
%setup -q -T -D -n GD-Barcode-1.15 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/GD-Barcode-1.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-GD-Barcode
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-GD-Barcode/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/COOP2of5.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/Code39.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/EAN13.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/EAN8.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/IATA2of5.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/ITF.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/Industrial2of5.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/Matrix2of5.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/NW7.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv01H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv01L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv01M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv01Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv02H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv02L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv02M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv02Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv03H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv03L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv03M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv03Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv04H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv04L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv04M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv04Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv05H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv05L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv05M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv05Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv06H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv06L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv06M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv06Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv07H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv07L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv07M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv07Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv08H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv08L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv08M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv08Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv09H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv09L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv09M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv09Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv10H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv10L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv10M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv10Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv11H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv11L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv11M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv11Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv12H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv12L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv12M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv12Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv13H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv13L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv13M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv13Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv14H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv14L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv14M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv14Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv15H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv15L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv15M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv15Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv16H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv16L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv16M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv16Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv17H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv17L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv17M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv17Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv18H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv18L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv18M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv18Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv19H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv19L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv19M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv19Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv20H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv20L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv20M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv20Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv21H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv21L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv21M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv21Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv22H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv22L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv22M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv22Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv23H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv23L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv23M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv23Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv24H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv24L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv24M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv24Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv25H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv25L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv25M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv25Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv26H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv26L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv26M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv26Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv27H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv27L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv27M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv27Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv28H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv28L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv28M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv28Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv29H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv29L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv29M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv29Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv30H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv30L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv30M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv30Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv31H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv31L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv31M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv31Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv32H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv32L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv32M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv32Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv33H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv33L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv33M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv33Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv34H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv34L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv34M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv34Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv35H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv35L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv35M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv35Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv36H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv36L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv36M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv36Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv37H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv37L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv37M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv37Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv38H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv38L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv38M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv38Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv39H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv39L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv39M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv39Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv40H.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv40L.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv40M.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/qrv40Q.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc07.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc10.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc13.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc15.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc16.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc17.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc18.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc20.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc22.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc24.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc26.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc28.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/QRcode/rsc30.dat
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/UPCA.pm
/usr/lib/perl5/vendor_perl/5.28.2/GD/Barcode/UPCE.pm

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
/usr/share/package-licenses/perl-GD-Barcode/deblicense_copyright
