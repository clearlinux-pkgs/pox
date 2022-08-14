#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pox
Version  : 0.3.1
Release  : 8
URL      : https://github.com/uqfoundation/pox/releases/download/pox-0.3.1/pox-0.3.1.tar.gz
Source0  : https://github.com/uqfoundation/pox/releases/download/pox-0.3.1/pox-0.3.1.tar.gz
Summary  : utilities for filesystem exploration and automated builds
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pox-bin = %{version}-%{release}
Requires: pox-license = %{version}-%{release}
Requires: pox-python = %{version}-%{release}
Requires: pox-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# scripts to augment the user's environment for distrubted computing
== bash_profile ============
FEATURES:
- default entry point for pathos distributed communications
- activates enviroment aliases and functions provided by other files

%package bin
Summary: bin components for the pox package.
Group: Binaries
Requires: pox-license = %{version}-%{release}

%description bin
bin components for the pox package.


%package license
Summary: license components for the pox package.
Group: Default

%description license
license components for the pox package.


%package python
Summary: python components for the pox package.
Group: Default
Requires: pox-python3 = %{version}-%{release}

%description python
python components for the pox package.


%package python3
Summary: python3 components for the pox package.
Group: Default
Requires: python3-core
Provides: pypi(pox)

%description python3
python3 components for the pox package.


%prep
%setup -q -n pox-0.3.1
cd %{_builddir}/pox-0.3.1
pushd ..
cp -a pox-0.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656427144
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pox
cp %{_builddir}/pox-0.3.1/LICENSE %{buildroot}/usr/share/package-licenses/pox/89215dbe96039235796b31ac8e2aa8f659d5c12b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pox

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pox/89215dbe96039235796b31ac8e2aa8f659d5c12b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
