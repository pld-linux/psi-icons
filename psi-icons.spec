Summary:	An extra iconset for PSI Jabber client
Summary(pl):	Zestaw ikonek do klienta Jabbera PSI
Name:		psi-icons
Version:	1.1
%define		tar_version	%(echo %{version} | sed 's,\\.,-,g')
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{tar_version}.tar.gz
URL:		http://psi.affinix.com/iconset.php
BuildRequires:	unzip
Requires:	psi
Obsoletes:	psi-icons-beos
Obsoletes:	psi-icons-cosmic
Obsoletes:	psi-icons-crystal
Obsoletes:	psi-icons-gabber
Obsoletes:	psi-icons-icq2
Obsoletes:	psi-icons-jilly
Obsoletes:	psi-icons-licq
Obsoletes:	psi-icons-mike
Obsoletes:	psi-icons-smiley
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_iconsdir	%{_datadir}/psi/iconsets

%description
An icon set for PSI Jabber client:
- BeOS Style (icon conversion by Gossip)
- Cosmic
- Crystal (KDE 3, Crystal IconSet)
- Gabber
- Licq - icq2 Style
- Jilly's icons
- Licq - Computer Style
- Mike's icons
- Smiley - Fun Style

%description -l pl
Zestaw ikonek dla klienta Jabbera PSI:
- BeOS Style (ikony przekonwertowane przez Gossip)
- Cosmic
- Crystal (KDE 3, Crystal IconSet)
- Gabber
- Licq - icq2 Style
- ikonki Jilly'ego
- Licq - Computer Style
- ikonki Mike'a
- Smiley - Fun Style

%package beos
Summary:	Beos icons
Summary(pl):	Ikonki Beos
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description beos
"beos" - icon set for PSI Jabber client.

%description beos -l pl
"beos" - zestaw ikonek dla klienta Jabbera PSI.

%package cosmic
Summary:	Cosmic icons
Summary(pl):	Ikonki kosmiczne
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description cosmic
"cosmic" - icon set for PSI Jabber client.

%description cosmic -l pl
"cosmic" - zestaw ikonek dla klienta Jabbera PSI.

%package crystal
Summary:	Crystal icons
Summary(pl):	Ikonki Crystal
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description crystal
"crystal" - icon set for PSI Jabber client.

%description crystal -l pl
"crystal" - zestaw ikonek dla klienta Jabbera PSI.

%package gabber
Summary:	Gabber icons
Summary(pl):	Ikonki Gabbera
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description gabber
"gabber" - icon set for PSI Jabber client.

%description gabber -l pl
"gabber" - zestaw ikonek dla klienta Jabbera PSI.

%package icq2
Summary:	ICQ2 icons
Summary(pl):	Ikonki ICQ2
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description icq2
"icq2" - icon set for PSI Jabber client.

%description icq2 -l pl
"icq2" - zestaw ikonek dla klienta Jabbera PSI.

%package jilly
Summary:	Jilly's icons
Summary(pl):	Ikonki Jilly'ego
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description jilly
"jilly" - icon set for PSI Jabber client.

%description jilly -l pl
"jilly" - zestaw ikonek dla klienta Jabbera PSI.

%package licq
Summary:	Licq icons
Summary(pl):	Ikonki Licq
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description licq
"licq" - icon set for PSI Jabber client.

%description licq -l pl
"licq" - zestaw ikonek dla klienta Jabbera PSI.

%package mike
Summary:	Mike's icons
Summary(pl):	Ikonki Mike'a
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description mike
"mike" - icon set for PSI Jabber client.

%description mike -l pl
"mike" - zestaw ikonek dla klienta Jabbera PSI.

%package smiley
Summary:	Smiley icons
Summary(pl):	Ikonki Smiley
Group:		X11/Applications/Networking
Obsoletes:	psi-icons
Requires:	psi

%description smiley
"smiley" - icon set for PSI Jabber client.

%description smiley -l pl
"smiley" - zestaw ikonek dla klienta Jabbera PSI.

%prep
%setup -q -n %{name}-%{tar_version}

%build
for file in `ls -1 *.zip`
do
	mkdir `basename $file .zip`
	cd `basename $file .zip`
	unzip ../$file
	rm ../$file
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/{beos,cosmic,crystal,gabber,icq2,jilly,licq,mike,smiley}

install beos/* $RPM_BUILD_ROOT%{_iconsdir}/beos
install cosmic/* $RPM_BUILD_ROOT%{_iconsdir}/cosmic
install crystal/* $RPM_BUILD_ROOT%{_iconsdir}/crystal
install gabber/* $RPM_BUILD_ROOT%{_iconsdir}/gabber
install icq2/* $RPM_BUILD_ROOT%{_iconsdir}/icq2
install jilly/* $RPM_BUILD_ROOT%{_iconsdir}/jilly
install licq/* $RPM_BUILD_ROOT%{_iconsdir}/licq
install mike/* $RPM_BUILD_ROOT%{_iconsdir}/mike
install smiley/* $RPM_BUILD_ROOT%{_iconsdir}/smiley

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*

%files beos
%defattr(644,root,root,755)
%{_iconsdir}/beos

%files cosmic
%defattr(644,root,root,755)
%{_iconsdir}/cosmic

%files crystal
%defattr(644,root,root,755)
%{_iconsdir}/crystal

%files gabber
%defattr(644,root,root,755)
%{_iconsdir}/gabber

%files icq2
%defattr(644,root,root,755)
%{_iconsdir}/icq2

%files jilly
%defattr(644,root,root,755)
%{_iconsdir}/jilly

%files licq
%defattr(644,root,root,755)
%{_iconsdir}/licq

%files mike
%defattr(644,root,root,755)
%{_iconsdir}/mike

%files smiley
%defattr(644,root,root,755)
%{_iconsdir}/smiley
