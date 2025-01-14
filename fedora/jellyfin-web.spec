%global         debug_package %{nil}

Name:           jellyfin-web
Version:        10.8.0
Release:        2%{?dist}
Summary:        The Free Software Media System web client
License:        GPLv2
URL:            https://jellyfin.org
# Jellyfin Server tarball created by `make -f .copr/Makefile srpm`, real URL ends with `v%%{version}.tar.gz`
Source0:        jellyfin-web-%{version}.tar.gz

BuildArch:		noarch
%if 0%{?rhel} > 0 && 0%{?rhel} < 8
BuildRequires:	nodejs
%else
BuildRequires:	git
# Nodejs 20 is required and npm >= 10 should bring in NodeJS 20
# This requires the build environment to use the nodejs:20 module stream:
# dnf module {install|switch-to}:web nodejs:20
BuildRequires:	npm >= 10
%endif

%description
Jellyfin is a free software media system that puts you in control of managing and streaming your media.


%prep
%autosetup -n jellyfin-web-%{version} -b 0

%if 0%{?rhel} > 0 && 0%{?rhel} < 8
# Required for CentOS build
chown root:root -R .
%endif


%build
npm ci --no-audit --unsafe-perm
npm run build:production


%install
%{__mkdir} -p %{buildroot}%{_libdir}/jellyfin/jellyfin-web
%{__cp} -r dist/* %{buildroot}%{_libdir}/jellyfin/jellyfin-web


%files
%defattr(644,root,root,755)
%{_libdir}/jellyfin/jellyfin-web
%license LICENSE


%changelog
* Fri Dec 04 2020 Jellyfin Packaging Team <packaging@jellyfin.org>
- Forthcoming stable release
* Mon Jul 27 2020 Jellyfin Packaging Team <packaging@jellyfin.org>
- Forthcoming stable release
* Mon Mar 23 2020 Jellyfin Packaging Team <packaging@jellyfin.org>
- Forthcoming stable release
