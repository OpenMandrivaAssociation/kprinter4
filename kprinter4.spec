Summary:	Print PostScript documents with KDE print dialog
Name:		kprinter4
Version:	10
Release:	2
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		https://github.com/credativ/kprinter4
Source0:	https://github.com/credativ/kprinter4/archive/%{name}-%{version}.tar.gz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libspectre)
Requires:	ghostscript
Requires:	poster
Requires:	psutils

%description
KPrinter4 is a simple stand-alone PostScript document printer modelled after
the KDE 4 print dialog. It can be used in place of /bin/lpr in order to better
control the print setup of non-KDE applications.

Main features:
- Printing PostScript documents with KDE 4 print dialog.
- Scaling and positioning of documents.
- Poster printing (backported from the known KDE 3 KPrinter tool).

%files -f %{name}.lang
%doc AUTHORS LICENCE README.md
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_iconsdir}/hicolor/*/apps/%{name}.*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

