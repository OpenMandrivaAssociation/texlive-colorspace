%global tl_name colorspace
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Provides PDF color spaces
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorspace
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorspace.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides PDF color spaces. Currently, only spot colors and
overprinting are supported. It requires xcolor, and supports pdfTeX and
LuaTeX.

