#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : janus
Version  : 1.0.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/b8/a8/facab7275d7d3d2032f375843fe46fad1cfa604a108b5a238638d4615bdc/janus-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/a8/facab7275d7d3d2032f375843fe46fad1cfa604a108b5a238638d4615bdc/janus-1.0.0.tar.gz
Summary  : Mixed sync-async queue to interoperate between asyncio tasks and classic threads
Group    : Development/Tools
License  : Apache-2.0
Requires: janus-license = %{version}-%{release}
Requires: janus-python = %{version}-%{release}
Requires: janus-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(wheel)

%description
=======
janus
=======
.. image:: https://github.com/aio-libs/janus/actions/workflows/ci.yml/badge.svg
:target: https://github.com/aio-libs/janus/actions/workflows/ci.yml
.. image:: https://codecov.io/gh/aio-libs/janus/branch/master/graph/badge.svg
:target: https://codecov.io/gh/aio-libs/janus
.. image:: https://img.shields.io/pypi/v/janus.svg
:target: https://pypi.python.org/pypi/janus
.. image:: https://badges.gitter.im/Join%20Chat.svg
:target: https://gitter.im/aio-libs/Lobby
:alt: Chat on Gitter

%package license
Summary: license components for the janus package.
Group: Default

%description license
license components for the janus package.


%package python
Summary: python components for the janus package.
Group: Default
Requires: janus-python3 = %{version}-%{release}

%description python
python components for the janus package.


%package python3
Summary: python3 components for the janus package.
Group: Default
Requires: python3-core
Provides: pypi(janus)
Requires: pypi(typing_extensions)

%description python3
python3 components for the janus package.


%prep
%setup -q -n janus-1.0.0
cd %{_builddir}/janus-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639760282
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/janus
cp %{_builddir}/janus-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/janus/840d2e227459bbd5c33423550411f4dac2758ee5
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/janus/840d2e227459bbd5c33423550411f4dac2758ee5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
