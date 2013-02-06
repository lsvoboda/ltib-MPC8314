%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 1.1.3
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Olivia Yin
Group           : Applications/System
Source          : %{name}-%{version}-mpc8349emds.tgz
Patch0          : u-boot-1.1.3_mpc8349e_pciagent.patch
Patch1          : u-boot-1.1.3-mpc8349itx-all-20060628.patch
Patch2          : u-boot-1.1.3-large-image-boot.patch
Patch3          : u-boot-1.1.3-mpc8349itx-gp-mod-20060831.patch
Patch4          : u-boot-1.1.3-mpc8349itx-gp-hrcw-20060914.patch
Patch5          : u-boot-1.1.3-Fix-make-3.81-2.patch
Patch6          : u-boot-1.1.3-gcc4-1.patch
Patch7          : u-boot-1.1.3-mpc8349itx-gp-rodata-str-1.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

All source and patches from Freescale.

%Prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%Build
PKG_U_BOOT_CONFIG_TYPE=${PKG_U_BOOT_CONFIG_TYPE:-MPC8349ADS_config}
make HOSTCC="$BUILDCC" CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_CONFIG_TYPE
make -j1 HOSTCC="$BUILDCC" HOSTSTRIP="$BUILDSTRIP" \
     CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_BUILD_ARGS all

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/boot
for i in u-boot.bin u-boot
do
    cp $i $RPM_BUILD_ROOT/%{pfx}/boot
done

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
