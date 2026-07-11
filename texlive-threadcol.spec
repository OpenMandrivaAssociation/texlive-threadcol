%global tl_name threadcol
%global tl_revision 28754

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Organize document columns into PDF article thread
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/threadcol
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/threadcol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package combines a document's columns into a PDF "article thread".
PDF readers that support this mechanism (probably Adobe Acrobat/Reader
only) can be instructed to scroll automatically from column to column,
which facilitates on-screen reading of two-column documents. Even for
single-column documents, threadcol supports the creation of multiple
article threads, which help organize discontiguous but logically related
regions of text into a form that the user can scroll through as if its
contents were contiguous.

