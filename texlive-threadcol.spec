# revision 28754
# category Package
# catalog-ctan /macros/latex/contrib/threadcol
# catalog-date 2013-01-06 14:14:24 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-threadcol
Version:	1.0
Release:	3
Summary:	Organize document columns into PDF "article thread"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/threadcol
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package combines a document's columns into a PDF "article
thread". PDF readers that support this mechanism (probably
Adobe Acrobat/Reader only) can be instructed to scroll
automatically from column to column, which facilitates on-
screen reading of two-column documents. Even for single-column
documents, threadcol supports the creation of multiple article
threads, which help organize discontiguous but logically
related regions of text into a form that the user can scroll
through as if its contents were contiguous.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/threadcol/threadcol.sty
%doc %{_texmfdistdir}/doc/latex/threadcol/README
%doc %{_texmfdistdir}/doc/latex/threadcol/threadcol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/threadcol/articles-ar9.png
%doc %{_texmfdistdir}/source/latex/threadcol/threadcol.dtx
%doc %{_texmfdistdir}/source/latex/threadcol/threadcol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
