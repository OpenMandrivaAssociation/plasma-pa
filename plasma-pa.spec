%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: The new Plasma5 Volume Manager
Name: plasma-pa
Version: 5.4.1
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://www.kde.org
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Plasma)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse)

%description
A new Volume manager plasmoid.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm_pulseaudio
%find_lang plasma_applet_org.kde.plasma.volume

%files -f kcm_pulseaudio.lang,plasma_applet_org.kde.plasma.volume.lang
%{_libdir}/libQPulseAudioPrivate.so
%{_libdir}/qt5/plugins/kcms/kcm_pulseaudio.so
%{_libdir}/qt5/qml/org/kde/plasma/private/volume
%{_datadir}/kconf_update/disable_kmix.upd
%{_datadir}/kconf_update/plasmaVolumeDisableKMixAutostart.pl
%{_datadir}/kpackage/kcms/kcm_pulseaudio
%{_datadir}/kservices5/*.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.volume
