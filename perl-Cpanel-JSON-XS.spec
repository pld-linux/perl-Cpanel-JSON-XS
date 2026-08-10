#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Cpanel
%define	pnam	JSON-XS
Summary:	Cpanel::JSON::XS - cPanel fork of JSON::XS, fast and correct serializing
Summary(pl.UTF-8):	Cpanel::JSON::XS - fork cPanel modulu JSON::XS, szybka i poprawna serializacja
Name:		perl-Cpanel-JSON-XS
Version:	4.40
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/R/RU/RURBAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cc1af777e25e61d134568fb22ef9efe9
URL:		https://metacpan.org/release/Cpanel-JSON-XS
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Encode
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast.
This is the cPanel fork of JSON::XS with additional fixes and
enhancements.

%description -l pl.UTF-8
Ten modul konwertuje struktury danych Perla do formatu JSON i
odwrotnie. Jego podstawowym celem jest poprawne dzialanie, a drugim -
szybkosc. Jest to fork cPanel modulu JSON::XS z dodatkowymi poprawkami
i ulepszeniami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/cpanel_json_xs
%dir %{perl_vendorarch}/Cpanel
%dir %{perl_vendorarch}/Cpanel/JSON
%{perl_vendorarch}/Cpanel/JSON/XS
%{perl_vendorarch}/Cpanel/JSON/XS.pm
%dir %{perl_vendorarch}/auto/Cpanel
%dir %{perl_vendorarch}/auto/Cpanel/JSON
%dir %{perl_vendorarch}/auto/Cpanel/JSON/XS
%{perl_vendorarch}/auto/Cpanel/JSON/XS/*.so
%{_mandir}/man1/cpanel_json_xs.1p*
%{_mandir}/man3/Cpanel::JSON::XS.3pm*
%{_mandir}/man3/Cpanel::JSON::XS::Boolean.3pm*
%{_mandir}/man3/Cpanel::JSON::XS::Type.3pm*
