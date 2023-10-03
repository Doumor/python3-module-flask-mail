%define pypi_name flask-mail

%def_enable check

Name:    python3-module-%pypi_name
Version: 0.9.1
Release: alt1

Summary: Flask-Mail adds SMTP mail sending to your Flask applications
License: BSD
Group:   Development/Python3
URL:     https://github.com/mattupstate/flask-mail

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires: python3-module-flask
BuildRequires: python3-module-blinker
BuildRequires: python3-module-nose2
BuildRequires: python3-module-mock
BuildRequires: python3-module-contextlib2
#BuildRequires: python3-module-speaklater

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
#%%tox_check_pyproject -- -vra
python3 tests.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/flask_mail.py
%python3_sitelibdir/__pycache__/flask_mail*.py*
%python3_sitelibdir/Flask_Mail-%version.dist-info

%changelog
* Tue Oct 03 2023 Danilkin Danila <danild@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus
