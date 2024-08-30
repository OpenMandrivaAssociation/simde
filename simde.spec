Name:           simde
Version:        0.8.2
Release:        1
Summary:        SIMD instruction sets for systems which don't natively support them
License:        MIT
Group:          Development/C
URL:            https://simd-everywhere.github.io/blog/
Source0:        https://github.com/simd-everywhere/simde/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  cmake

%description
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which doesn't natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g., SSE/AVX runs at full speed on x86, NEON
on ARM, etc.).

%package devel
Summary:        Development header files for %{name}
Group:          Development/C

%description devel
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which doesn't natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g., SSE/AVX runs at full speed on x86, NEON
on ARM, etc.).

%prep
%autosetup -p1

%build
%meson --libdir=%{_datadir} -Dtests=false
%meson_build

%install
%meson_install

%files devel
%doc README.*
%license COPYING
%{_includedir}/simde/
%{_datadir}/pkgconfig/simde.pc
