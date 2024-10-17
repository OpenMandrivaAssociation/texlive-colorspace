Name:		texlive-colorspace
Version:	50585
Release:	2
Summary:	Provides PDF color spaces
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorspace
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorspace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorspace.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides PDF color spaces. Currently, only spot
colors and overprinting are supported. It requires xcolor, and
supports pdfTeX and LuaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/colorspace
%doc %{_texmfdistdir}/doc/latex/colorspace

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
