Summary:	Musepack Console audio player
Summary(pl.UTF-8):	Konsolowy odtwarzacz plików Musepack
Name:		mpc123
Version:	0.2.6
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
#Source0Download: https://github.com/bucciarati/mpc123/releases
Source0:	https://github.com/bucciarati/mpc123/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	420420fdfb977c276aa719e46884c1be
Patch0:		%{name}-defaults-alsa.patch
Patch1:		%{name}-pl.po.patch
Patch2:		%{name}-fixes.patch
Patch3:		%{name}-ao.patch
URL:		https://github.com/bucciarati/mpc123
BuildRequires:	gettext-tools
BuildRequires:	libao-devel
BuildRequires:	musepack-devel >= 0.0.1.r475
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpc123 is handy console Musepack audio player. Its features are:
- plain file playing (that's easy ;)
- playlists
- random, shuffle
- output to file (wav, cdr, au)
- and more...

%description -l pl.UTF-8
mpc123 jest poręcznym, konsolowym odtwarzaczem plików Musepack. Jego
funkcje to m.in:
- odtwarzanie plików (po prostu ;)
- listy odtwarzania
- odtwarzanie losowe
- możliwość zapisu do pliku (wav, cdr, au)
- i więcej...

%prep
# ' (fixes braindead Emacs syntax highlight)
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -lao -lmpcdecsv8"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/locale}

install mpc123 $RPM_BUILD_ROOT%{_bindir}
cp -p mpc123.1  $RPM_BUILD_ROOT%{_mandir}/man1

for sdir in LOCALES/* ; do
	ddir=$RPM_BUILD_ROOT%{_datadir}/locale/$(basename $sdir)/LC_MESSAGES
	install -d $ddir
	cp -p $sdir/LC_MESSAGES/mpc123.mo $ddir/mpc123.mo
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md TODO
%attr(755,root,root) %{_bindir}/mpc123
%{_mandir}/man1/mpc123.1*
