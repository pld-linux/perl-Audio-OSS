#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	OSS
Summary:	Audio::OSS Perl module - interface to Open Sound System
Summary(pl.UTF-8):	Moduł Perla Audio::OSS - interfejs do Open Sound System
Name:		perl-Audio-OSS
Version:	0.0501
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c77167acea908501c243be198149efb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Ten moduł udostępnia czysto perlowy, logiczny, oparty na uchwytach
plików interfejs do systemu dźwięku Open Sound. Audio::DSP jest dobry
do prostego, blokującego odtwarzania/nagrywania dźwięku, ale nie
wystarcza, jeśli trzeba zrobić coś bardziej skomplikowanego. To znaczy
nie udostępnia możliwości interfejsu OSS potrzebnych do rzeczy takich
jak nie blokujący dźwięk, kontrola odtwarzania w czasie rzeczywistym,
odczytywanie możliwości urządzenia dźwiękowego, sprawdzanie
obsługiwanych częstotliwości próbkowania itp. Moduł Audio::OSS
udostępnia proceduralny interfejs oparty na uchwytach plików
związanych z urządzeniem dźwiękowym (zazwyczaj /dev/dsp* dla dźwięku
PCM). Moduł także definiuje stałe dla różnych wywołań ioctl oraz
innych rzeczy związanych z plikami nagłówkowymi OSS, więc nie trzeba
polegać na plikach .ph.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
%{perl_vendorlib}/Audio/OSS.pm
%{perl_vendorlib}/Audio/OSS
%{_mandir}/man3/*
