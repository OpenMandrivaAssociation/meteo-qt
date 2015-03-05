Summary:	Weather status system tray application
Name:		meteo-qt
Version:	0.5.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
URL:		http://qt-apps.org/content/show.php/meteo-qt?content=167733
Source0:	https://github.com/dglent/meteo-qt/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(python3)
BuildRequires:	imagemagick
Requires:	python-qt5
Requires:	python3-sip
Requires:	python3egg(urllib3)
Requires:	python3egg(lxml)
Requires:	qt5-qttranslations

%description
A Qt system tray application for the weather status.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
convert -scale 16x16 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/meteo-qt.png
convert -scale 32x32 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/meteo-qt.png

%files
%doc TODO CHANGELOG README.md
%{_datadir}/meteo_qt/images/
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{python_sitelib}/meteo_qt-%{version}-py%py3ver.egg-info
%{python_sitelib}/meteo_qt/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/meteo-qt.png
%{_datadir}/meteo_qt/translations/
