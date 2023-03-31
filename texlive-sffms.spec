Name:		texlive-sffms
Version:	15878
Release:	2
Summary:	Typesetting science fiction/fantasy manuscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sffms
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is designed for typesetting science fiction and
fantasy manuscripts. Sffms now includes several options for
specific publishers as well as extensive documentation aimed at
new LaTeX users.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sffms/sffdumb.sty
%{_texmfdistdir}/tex/latex/sffms/sffms.cls
%{_texmfdistdir}/tex/latex/sffms/sffsmart.sty
%doc %{_texmfdistdir}/doc/latex/sffms/README
%doc %{_texmfdistdir}/doc/latex/sffms/blind.tex
%doc %{_texmfdistdir}/doc/latex/sffms/sffms_manual.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sffms/sffms.dtx
%doc %{_texmfdistdir}/source/latex/sffms/sffms.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
