Name:    pv
Version: 1.6.6
Release: 6
Summary: A tool for monitoring the progress of data through a pipeline
License: Artistic 2.0
Source0: http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
URL:     http://www.ivarch.com/programs/pv.shtml

BuildRequires:  gcc gettext initscripts

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%package_help

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

%check
make test

%files -f %{name}.lang
%license doc/COPYING
%{_bindir}/%{name}

%files help
%doc README doc/NEWS doc/TODO
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Mar 3 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.6.6-6
- Package init
