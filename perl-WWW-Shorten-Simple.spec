%define upstream_name    WWW-Shorten-Simple
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Factory wrapper around WWW::Shorten to avoid imports
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
WWW::Shorten::Simple is a wrapper (factory) around WWW::Shorten
so that you can create an object representing each URL shortening
service, instead of importing makeashorterlink function into your 
namespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 661375
- import perl-WWW-Shorten-Simple

