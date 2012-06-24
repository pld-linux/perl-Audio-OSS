#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	OSS
Summary:	Audio::OSS Perl module - interface to Open Sound System
Summary(pl):	Modu� Perla Audio::OSS - interfejs do Open Sound System
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
Ten modu� udost�pnia czysto perlowy, logiczny, oparty na uchwytach
plik�w interfejs do systemu d�wi�ku Open Sound. Audio::DSP jest dobry
do prostego, blokuj�cego odtwarzania/nagrywania d�wi�ku, ale nie
wystarcza, je�li trzeba zrobi� co� bardziej skomplikowanego. To znaczy
nie udost�pnia mo�liwo�ci interfejsu OSS potrzebnych do rzeczy takich
jak nie blokuj�cy d�wi�k, kontrola odtwarzania w czasie rzeczywistym,
odczytywanie mo�liwo�ci urz�dzenia d�wi�kowego, sprawdzanie
obs�ugiwanych cz�stotliwo�ci pr�bkowania itp. Modu� Audio::OSS
udost�pnia proceduralny interfejs oparty na uchwytach plik�w
zwi�zanych z urz�dzeniem d�wi�kowym (zazwyczaj /dev/dsp* dla d�wi�ku
PCM). Modu� tak�e definiuje sta�� dla r�nych wywo�a� ioctl oraz
innych rzeczy zwi�zanych z plikami nag��wkowymi OSS, wi�c nie trzeba
polega� na plikach .ph.

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
