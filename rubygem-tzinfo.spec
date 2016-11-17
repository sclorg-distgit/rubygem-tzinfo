%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from tzinfo-0.3.26.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tzinfo

%global download_path http://rubygems.org/downloads/

Summary: Daylight-savings aware timezone library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.2
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: http://tzinfo.github.io/
Source0: %{download_path}%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(thread_safe)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix}rubygem(thread_safe)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
Requires: %{?scl_prefix}runtime

%description
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
set -e
ruby -Ilib -e "require './test/ts_all'"
ruby -Ilib -e "require './test/ts_all_zoneinfo.rb'"
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.yardopts
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/%{gem_name}.gemspec
%{gem_docdir}

%changelog
* Wed Apr 06 2016 Pavel Valena <pvalena@redhat.com> - 1.2.2-5
- Fix: build should fail on test failure

* Mon Feb 22 2016 Pavel Valena <pvalena@redhat.com> - 1.2.2-4
- Add scl macros

* Fri Jan 16 2015 Josef Stribny <jstribny@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 0.3.37-2
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Wed Jun 12 2013 Josef Stribny <jstribny@redhat.com> - 0.3.37-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to 0.3.37

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.33-2
- Exclude the cached gem.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.33-1
- Update to Tzinfo 0.3.33.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.32-1
- Rebuilt for scl.
- Updated to 0.3.32

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.30-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.30-1
- Update to tzinfo 0.3.30.

* Sun Apr 10 2011  <Minnikhanov@gmail.com> - 0.3.26-1
- Updated mail to latest upstream release (v.0.3.26 2011-04-01)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011  <Minnikhanov@gmail.com> - 0.3.24-2
- Fix Comment 3 #668098. https://bugzilla.redhat.com/show_bug.cgi?id=668098#c3 

* Tue Jan 18 2011  <Minnikhanov@gmail.com> - 0.3.24-1
- Updated mail to latest upstream release

* Sat Jan 08 2011  <Minnikhanov@gmail.com> - 0.3.23-1
- Initial package
