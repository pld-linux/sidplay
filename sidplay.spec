Summary:	Spartanic console sid-music player
Summary(pl):	Spartañski odtwarzacz muzyki sid dla konsoli
Name:		sidplay
Version:	1.0.9
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-base-%{version}.tgz
# Source0-md5:	633506d1225ce9713106fc8d851b0750
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
BuildRequires:	libsidplay-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spartanic console sid-music player

%description -l pl
Spartañski odtwarzacz muzyki sid dla konsoli

%prep
%setup -q -n %{name}-base-%{version}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog POINTER
%attr(755,root,root) %{_bindir}/*
