Summary:	Weather status system tray application
Name:		meteo-qt
Version:	2.3
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
URL:		http://qt-apps.org/content/show.php/meteo-qt?content=167733
Source0:	https://github.com/dglent/meteo-qt/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	qtchooser
BuildRequires:	pkgconfig(python3)
BuildRequires:	imagemagick
Requires:	python-qt5
Requires:	python-sip
Requires:	python3dist(urllib3)
Requires:	python3dist(lxml)
Requires:	qt5-qttranslations

%description
A Qt system tray application for the weather status.

%prep
%setup -q

%build
# (tpg) needed for lrelease
export PATH=%{_libdir}/qt5/bin:$PATH

%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

#mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
#convert -scale 16x16 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/meteo-qt.png
#convert -scale 32x32 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/meteo-qt.png

rm -rf %{buildroot}%{_docdir}/meteo-qt

%files
%doc TODO CHANGELOG README.md
#{_datadir}/meteo_qt/images/
%{_bindir}/%{name}
#{_iconsdir}/%{name}.png
%{python_sitelib}/meteo_qt-%{version}-py*.egg-info
%{python_sitelib}/meteo_qt/
%{_datadir}/applications/%{name}.desktop
#{_iconsdir}/hicolor/*/apps/meteo-qt.png
%{_datadir}/meteo_qt/translations/
%{_datadir}/icons/weather-few-clouds.png
