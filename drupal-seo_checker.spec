%define modname		seo_checker
%define drupal_version	7
%define module_version	1.5
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	SEO Compliance Checker module for Drupal
Version:	%{version}
Release:	2
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
The SEO Compliance Checker checks node content on search engine optimization
upon its creation or modification. Whenever a publisher saves or previews
a node, the module performs a set of checks and gives the user a feedback
on the compliance of the rules.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/{*.txt,.gitignore}

%files
%{_var}/www/drupal/modules/%{modname}
%doc README_FOR_DEVELOPERS.txt


%changelog
* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.5-1
+ Revision: 798451
- imported package drupal-seo_checker

