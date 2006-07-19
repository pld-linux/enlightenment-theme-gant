%define	_theme	gant
Summary:	E17 theme based on the G.A.N.T. icons
Summary(pl):	Motyw E17 oparty na ikonach G.A.N.T.
Name:		enlightenment-theme-%{_theme}
Version:	0.0.2
Release:	1
License:	distributable
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}.edj
# Source0-md5:	c6366a421149afb79058b6e4e32e7e3b
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
E17 theme based on the G.A.N.T. icons.

%description -l pl
Motyw E17 oparty na ikonach G.A.N.T.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
