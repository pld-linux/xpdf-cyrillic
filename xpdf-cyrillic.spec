Summary:	KOI8-R encoding support for xpdf
Summary(pl):	Wsparcie kodowania KOI8-R dla xpdf
Name:		xpdf-cyrillic
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
# Source0-md5:	7b22f31289ce0812d2ec77014e7b0cdf
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install *.nameToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	KOI8-R	/usr/share/xpdf/KOI8-R.unicodeMap' >> /etc/xpdfrc
	echo 'nameToUnicode		/usr/share/xpdf/Bulgarian.nameToUnicode' >> /etc/xpdfrc
else
 if ! grep -q 'KOI8-R\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	KOI8-R	/usr/share/xpdf/KOI8-R.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Bulgarian\.nameToUnicode' /etc/xpdfrc; then
	echo 'nameToUnicode		/usr/share/xpdf/Bulgarian.nameToUnicode' >> /etc/xpdfrc
 fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v 'KOI8-R\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'Bulgarian\.nameToUnicode' /etc/xpdfrc.new > /etc/xpdfrc
	rm -f /etc/xpdfrc.new
fi

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
