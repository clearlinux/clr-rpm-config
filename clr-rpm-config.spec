Name:       clr-rpm-config
Summary:    Clear Linux specific rpm configuration files
Version:    1
Release:    28
Group:      Development/System
License:    GPLv2+
URL:        http://www.clearlinux.org
Source0:    clr-rpm-config-%{version}.tar.gz
AutoReqProv: No

%description
Clear Linux specific rpm configuration files.



%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install
mkdir -p  $RPM_BUILD_ROOT/usr/lib/rpm
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/unknown
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/generic
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/redhat
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/koji
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/pc

%files
%defattr(-,root,root,-)
/usr/lib/rpm/*
