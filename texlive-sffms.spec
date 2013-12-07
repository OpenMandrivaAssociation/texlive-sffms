# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sffms
# catalog-date 2007-01-14 22:06:18 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-sffms
Version:	2.0
Release:	4
Summary:	Typesetting science fiction/fantasy manuscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sffms
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sffms.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 755918
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719516
- texlive-sffms
- texlive-sffms
- texlive-sffms

