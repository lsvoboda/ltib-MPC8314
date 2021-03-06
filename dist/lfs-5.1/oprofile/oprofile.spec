%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : System-wide profiler for Linux systems
Name            : oprofile
Version         : 0.9.3
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Stuart Hughes/WMSG
Group           : Development/Tools
Source          : %{name}-%{version}.tar.gz
Patch0          : oprofile-0.9.3-arm11-update-l2cache-events.patch
Patch1          : oprofile-0.9.3-bfd_get_synthetic_symtab-hack.patch
Patch2		: oprofile-0.9.3-armv6-l1event-counters.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
BuildRequires   : popt, binutils

%Description
%{summary}

Note:
binutils is required for libbfd only
This only support 2.6 kernels

%Prep
%setup 
%patch0 -p1
%patch1 -p1
%patch2 -p1

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} \
            --with-kernel-support \
            --config-cache --mandir=%{_mandir} \
            --with-binutils=$DEV_IMAGE/usr
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
