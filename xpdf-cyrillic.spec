Summary:	KOI8-R encoding support for xpdf
Summary(pl):	Wsparcie kodowania KOI8-R dla xpdf
Name:		xpdf-cyrillic
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Cyrillic PDF files.

%description -l pl
Pakiety wspieraj±ce jêzyki Xpdf zawieraj± pliki CMap, kodowania oraz
ró¿ne inne informacje konfiguracyjne niezbêdne b±d¼ przydatne przy
okre¶lonych zestawach znaków. (Nie zawieraj± ¿adnych fontów).
Ten pakiet zawiera pliki potrzebne do u¿ywania narzêdzi Xpdf z plikami
PDF w cyrylicy.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	KOI8-R	/usr/X11R6/share/xpdf/KOI8-R.unicodeMap' >> /etc/xpdfrc
else
 if ! grep -q 'KOI8-R\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	KOI8-R	/usr/X11R6/share/xpdf/KOI8-R.unicodeMap' >> /etc/xpdfrc
 fi
fi

%preun
umask 022
grep -v 'KOI8-R\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
mv -f /etc/xpdfrc.new /etc/xpdfrc

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
