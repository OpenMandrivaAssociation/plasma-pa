%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: The new Plasma5 Volume Manager
Name: plasma-pa
Version: 5.27.12
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: https://www.kde.org
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
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: sound-theme-freedesktop
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libcanberra)
BuildConflicts: pkgconfig(gconf-2.0)
Requires: pulseaudio
Requires: sound-theme-freedesktop
Recommends: pulseaudio-module-gsettings

%description
A new Volume manager plasmoid.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_pulseaudio.so
%{_datadir}/applications/kcm_pulseaudio.desktop
%{_libdir}/qt5/qml/org/kde/plasma/private/volume
%{_datadir}/metainfo/org.kde.plasma.volume.appdata.xml
%{_datadir}/kpackage/kcms/kcm_pulseaudio
%{_datadir}/kservices5/*.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.volume
%{_datadir}/kconf_update/*
%{_datadir}/kde4/apps/kconf_update/*
