Summary:	An extra iconset for PSI Jabber client
Summary(pl):	Zestaw ikonek do klienta Jabbera PSI
Name:		psi-icons
Version:	1
Release:	1
License:	GPL
Packager:	Michal Cieslicki <yoshi@aip.pl>
Group:		X11/Networking/Communications
Source0:	%{name}-%{version}-%{release}.tar.gz
URL:		http://psi.affinix.com/iconset.php
BuildRequires:	unzip
Requires:	psi 
BuildArch:	noarch
Obsoletes:	psi-icons-beos
Obsoletes:	psi-icons-cosmic
Obsoletes:	psi-icons-crystal
Obsoletes:	psi-icons-gabber
Obsoletes:	psi-icons-icq2
Obsoletes:	psi-icons-jilly
Obsoletes:	psi-icons-licq
Obsoletes:	psi-icons-mike
Obsoletes:	psi-icons-smiley
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

%define		_iconsdir	%{_prefix}/X11R6/share/psi/iconsets

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
- BeOS Style (icon conversion by Gossip)
- Cosmic
- Crystal (KDE 3, Crystal IconSet)
- Gabber
- Licq - icq2 Style
- Jilly's icons
- Licq - Computer Style
- Mike's icons
- Smiley - Fun Style

%package -n psi-icons-beos
Summary:	Beos icons
Summary(pl): 	Ikonki Beos
Group:		X11/Networking/Communications
Obsoletes:	psi-icons
Requires:       psi

%description -n psi-icons-beos
"beos" - icon set for PSI Jabber client.

%description -n psi-icons-beos -l pl
"beos" - zestaw ikonek dla klienta Jabbera PSI.


%package -n psi-icons-cosmic
Summary:        cosmic icons
Summary(pl):    Ikonki cosmic
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-cosmic
"cosmic" - icon set for PSI Jabber client.

%description -n psi-icons-cosmic -l pl
"cosmic" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-crystal
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-crystal
"crystal" - icon set for PSI Jabber client.

%description -n psi-icons-crystal -l pl
"crystal" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-gabber
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-gabber
"gabber" - icon set for PSI Jabber client.

%description -n psi-icons-gabber -l pl
"gabber" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-icq2
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-icq2
"icq2" - icon set for PSI Jabber client.

%description -n psi-icons-icq2 -l pl
"icq2" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-jilly
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-jilly
"jilly" - icon set for PSI Jabber client.

%description -n psi-icons-jilly -l pl
"jilly" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-licq
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-licq
"licq" - icon set for PSI Jabber client.

%description -n psi-icons-licq -l pl
"licq" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-mike
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-mike
"mike" - icon set for PSI Jabber client.

%description -n psi-icons-mike -l pl
"mike" - zestaw ikonek dla klienta Jabbera PSI.

%package -n psi-icons-smiley
Summary:        Beos icons
Summary(pl):    Ikonki Beos
Group:          X11/Networking/Communications
Obsoletes:      psi-icons
Requires:       psi

%description -n psi-icons-smiley
"smiley" - icon set for PSI Jabber client.

%description -n psi-icons-smiley -l pl
"smiley" - zestaw ikonek dla klienta Jabbera PSI.

%prep
%setup -q -n %{name}-%{version}-%{release} 

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
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr
install -d $RPM_BUILD_ROOT/usr/X11R6
install -d $RPM_BUILD_ROOT/usr/X11R6/share
install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi
install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/beos
install beos/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/beos

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/cosmic
install cosmic/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/cosmic

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/crystal
install crystal/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/crystal

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/gabber
install gabber/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/gabber

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/icq2
install icq2/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/icq2

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/jilly
install jilly/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/jilly

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/licq
install licq/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/licq

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/mike
install mike/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/mike

install -d $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/smiley
install smiley/* $RPM_BUILD_ROOT/usr/X11R6/share/psi/iconsets/smiley

#%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*/*


%files -n psi-icons-beos
%defattr(644,root,root,755)
%{_iconsdir}/beos/*

%files -n psi-icons-cosmic
%defattr(644,root,root,755)
%{_iconsdir}/cosmic/*

%files -n psi-icons-crystal
%defattr(644,root,root,755)
%{_iconsdir}/crystal/*

%files -n psi-icons-gabber
%defattr(644,root,root,755)
%{_iconsdir}/gabber/*

%files -n psi-icons-icq2
%defattr(644,root,root,755)
%{_iconsdir}/icq2/*

%files -n psi-icons-jilly
%defattr(644,root,root,755)
%{_iconsdir}/jilly/*

%files -n psi-icons-licq
%defattr(644,root,root,755)
%{_iconsdir}/licq/*

%files -n psi-icons-mike
%defattr(644,root,root,755)
%{_iconsdir}/mike/*

%files -n psi-icons-smiley
%defattr(644,root,root,755)
%{_iconsdir}/smiley/*
