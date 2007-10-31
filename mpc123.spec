#
# Conditional build:
%bcond_without	alsa		# build without default alsa
#
Summary:	Musepack Console audio player
Summary(pl.UTF-8):	Konsolowy odtwarzacz plików Musepack
Name:		mpc123
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mpc123/%{name}-%{version}.tar.gz
# Source0-md5:	430cf1ada67177d2ca802ce8e1b59916
Patch0:		%{name}-defaults-alsa.patch
URL:		http://mpc123.sourceforge.net/
BuildRequires:	libao-devel
BuildRequires:	libmpcdec-devel
Suggests:	libao-alsa
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
%setup -q -n %{name}
%{?with_alsa:%patch0 -p1}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="-lao -lmpcdec %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mpc123 $RPM_BUILD_ROOT%{_bindir}
install mpc123.1  $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with alsa}
%post
cat <<EOF
NOTE:
Please make sure you have "libao-alsa" package installed, as ALSA driver is
used as output by default.
EOF
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
