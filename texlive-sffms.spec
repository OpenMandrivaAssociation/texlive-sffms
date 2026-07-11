%global tl_name sffms
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Typesetting science fiction/fantasy manuscripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sffms
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is designed for typesetting science fiction and fantasy
manuscripts. Sffms now includes several options for specific publishers
as well as extensive documentation aimed at new LaTeX users.

