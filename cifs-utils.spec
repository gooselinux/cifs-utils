#%define pre_release rc1
%define pre_release %nil

Name:           cifs-utils
Version:        4.4
Release:        5%{pre_release}%{?dist}.2
Summary:        Utilities for mounting and managing CIFS mounts

Group:          System Environment/Daemons
License:        GPLv3
URL:            http://linux-cifs.samba.org/cifs-utils/
BuildRoot:      %{_tmppath}/%{name}-%{version}%{pre_release}-%{release}-root-%(%{__id_u} -n)

Source0:        ftp://ftp.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}%{pre_release}.tar.bz2

Patch1:		cifs-utils-mount.cifs-strip-leading-delimiter.patch
Patch2:		cifs-utils-cifs.upcall-use-creduid-parm-by-default.patch
Patch3:		cifs-utils-cifs.upcall-require-a-uid-or-creduid-parm.patch
Patch4:		cifs-utils-cifs.upcall-gssapi-checksum.patch

BuildRequires:  libcap-ng-devel libtalloc-devel krb5-devel keyutils-libs-devel autoconf automake
Requires:       keyutils

%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol. The tools in this package
work in conjunction with support in the kernel to allow one to mount a
SMB/CIFS share onto a client and use it as if it were a standard Linux
file system.

%prep
%setup -q -n %{name}-%{version}%{pre_release}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
/sbin/mount.cifs
%{_sbindir}/cifs.upcall
%{_mandir}/man8/cifs.upcall.8.gz
%{_mandir}/man8/mount.cifs.8.gz

%changelog
* Thu Mar 17 2011 Jeff Layton <jlayton@redhat.com> 4.4-5.el6.0.2
- cifs.upcall: remove fix for '-l' option (bz 668366)

* Mon Jan 10 2011 Jeff Layton <jlayton@redhat.com> 4.4-5.el6.0.1
- cifs.upcall: set GSSAPI checksum in SPNEGO blobs (bz 668366)
- cifs.upcall: fix '-l' option (bz 668366)

* Wed Jul 28 2010 Jeff Layton <jlayton@redhat.com> 4.4-5
- cifs.upcall: handle "creduid=" upcall parameter (bz 618609)

* Fri Apr 30 2010 Jeff Layton <jlayton@redhat.com> 4.4-4
- mount.cifs: fix bug in previous prefixpath patch (bz 586895)

* Thu Apr 29 2010 Jeff Layton <jlayton@redhat.com> 4.4-3
- mount.cifs: strip leading delimiter from prefixpath (bz 586895)

* Wed Apr 28 2010 Jeff Layton <jlayton@redhat.com> 4.4-2
- fix release tagging issue

* Wed Apr 28 2010 Jeff Layton <jlayton@redhat.com> 4.4-1
- update to 4.4

* Sat Apr 17 2010 Jeff Layton <jlayton@redhat.com> 4.3-2
- fix segfault when address list is exhausted (BZ#583230)

* Fri Apr 09 2010 Jeff Layton <jlayton@redhat.com> 4.3-1
- update to 4.3

* Fri Apr 02 2010 Jeff Layton <jlayton@redhat.com> 4.2-1
- update to 4.2

* Tue Mar 23 2010 Jeff Layton <jlayton@redhat.com> 4.1-1
- update to 4.1

* Mon Mar 08 2010 Jeff Layton <jlayton@redhat.com> 4.0-2
- fix bad pointer dereference in IPv6 scopeid handling

* Wed Mar 03 2010 Jeff Layton <jlayton@redhat.com> 4.0-1
- update to 4.0
- minor specfile fixes

* Fri Feb 26 2010 Jeff Layton <jlayton@redhat.com> 4.0-1rc1
- update to 4.0rc1
- fix prerelease version handling

* Mon Feb 08 2010 Jeff Layton <jlayton@redhat.com> 4.0a1-1
- first RPM package build

