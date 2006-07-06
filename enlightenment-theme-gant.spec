%define	_theme	gant
Summary:	E17 theme based on the G.A.N.T. icons
Name:		enlightenment-theme-%{_theme}
Version:	0.0.2
Release:	1
License:	distributable
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}.edj
# Source0-md5:	c6366a421149afb79058b6e4e32e7e3b
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenmentDR17
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
E17 theme based on the G.A.N.T. icons.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj
