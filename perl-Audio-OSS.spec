#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	OSS
Summary:	Audio::OSS Perl module - interface to Open Sound System
Summary(pl):	Modu³ Perla Audio::OSS - interfejs do Open Sound System
Name:		perl-Audio-OSS
Version:	0.0501
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Provides:	perl(Audio::OSS::Constants)
# it uses C code only at build time - built package doesn't contain any binaries
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a pure-Perl, no-nonsense, filehandle-based
interface to the Open Sound System. Audio::DSP is fine for simple,
blocking audio I/O, but it doesn't hold up when you want to do
something more complicated. That is, it doesn't expose the features of
the audio device interface that are required to do things like
non-blocking audio, real-time control of playback, querying the
capabilities of the audio device, finding the supported sampling
rates, etc. Audio::OSS provides a procedural interface based around
filehandles opened on the audio device (usually /dev/dsp* for PCM
audio). It also defines constants for various ioctl calls and other
things based on the OSS system header files, so you don't have to rely
on .ph files that may or may be correct or even present on your
system.

%description -l pl
Ten modu³ udostêpnia czysto perlowy, logiczny, oparty na uchwytach
plików interfejs do systemu d¼wiêku Open Sound. Audio::DSP jest dobry
do prostego, blokuj±cego odtwarzania/nagrywania d¼wiêku, ale nie
wystarcza, je¶li trzeba zrobiæ co¶ bardziej skomplikowanego. To znaczy
nie udostêpnia mo¿liwo¶ci interfejsu OSS potrzebnych do rzeczy takich
jak nie blokuj±cy d¼wiêk, kontrola odtwarzania w czasie rzeczywistym,
odczytywanie mo¿liwo¶ci urz±dzenia d¼wiêkowego, sprawdzanie
obs³ugiwanych czêstotliwo¶ci próbkowania itp. Modu³ Audio::OSS
udostêpnia proceduralny interfejs oparty na uchwytach plików
zwi±zanych z urz±dzeniem d¼wiêkowym (zazwyczaj /dev/dsp* dla d¼wiêku
PCM). Modu³ tak¿e definiuje sta³ê dla ró¿nych wywo³añ ioctl oraz
innych rzeczy zwi±zanych z plikami nag³ówkowymi OSS, wiêc nie trzeba
polegaæ na plikach .ph.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Audio/OSS.pm
%{perl_sitelib}/Audio/OSS
%{_mandir}/man3/*
