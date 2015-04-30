Name:           packer
Version:        0.7.5
Release:        1%{?dist}
Summary:        Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
Group:          Applications/System
License:        MPLv2.0
URL:            https://packer.io/
Source0:        https://dl.bintray.com/mitchellh/%{name}/%{name}_%{version}_linux_amd64.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%endif

%description
Packer is a tool for creating identical machine images for multiple platforms
from a single source configuration.
Out of the box Packer comes with support to build images for Amazon EC2,
DigitalOcean, Google Compute Engine, QEMU, VirtualBox, VMware, and more.
Support for more platforms is on the way, and anyone can add new platforms via
plugins. 

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name}* %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}*

%doc

%changelog
* Wed Apr 29 2015 dan phrawzty <phrawzty@mozilla.com>
- init v0.7.5
