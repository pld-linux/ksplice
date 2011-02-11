Summary:	Patching a Linux kernel without reboot
Name:		ksplice
Version:	0.9.9
Release:	1
License:	GPL v2
Group:		Base/Kernel
URL:		http://www.ksplice.com/
Source0:	http://www.ksplice.com/dist/%{name}-%{version}-src.tar.gz
# Source0-md5:	ceb4301c51d9b075731050b57d9ecd80
BuildRequires:	autoconf
BuildRequires:	binutils-devel
BuildRequires:	perl-base
BuildRequires:	zlib-devel
Requires:	bash >= 2.03
Requires:	binutils >= 2.12
Requires:	bzip2
Requires:	diffutils
Requires:	findutils
Requires:	gawk
Requires:	gcc >= 6:3.4.2
Requires:	gzip
Requires:	m4
Requires:	make >= 3.78
Requires:	module-init-tools
Requires:	patch >= 2.5.4
Requires:	perl
Requires:	sh-utils
Requires:	tar
Requires:	util-linux
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksplice allows system administrators to apply security patches to the
Linux kernel without having to reboot. Ksplice takes as input a source
code change in unified diff format and the kernel source code to be
patched, and it applies the patch to the corresponding running kernel.
The running kernel does not need to have been prepared in advance in
any way.

%prep
%setup -q

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
%doc README
%attr(755,root,root) %{_bindir}/ksplice-*
%attr(755,root,root) %{_sbindir}/ksplice-*
%{_libdir}/ksplice-*
%{_datadir}/ksplice
%{_mandir}/man8/ksplice-*
