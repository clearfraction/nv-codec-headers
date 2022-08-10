Name:           nv-codec-headers
Version:        11.1.5.1
Release:        1
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source:         %url/archive/n%{version}/%{name}-n%{version}.tar.gz
BuildRequires:  make
%description
FFmpeg version of headers required to interface with Nvidias codec APIs.

%prep
%autosetup -n %{name}-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

# Extract license
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=lib64

%install
%make_install PREFIX=%{_prefix} LIBDIR=lib64

%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_libdir}/pkgconfig/ffnvcodec.pc

%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=26434

