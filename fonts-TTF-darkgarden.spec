%define		_name	darkgarden
Summary:	Dark Garden font
Summary(pl.UTF-8):	Czcionka dark garden
Name:		fonts-TTF-%{_name}
Version:	1.1
Release:	1
License:	GPL
Group:		Fonts
Source0:	http://darkgarden.sourceforge.net/%{_name}-%{version}.ttf.zip
# Source0-md5:	53bceb50cb4733c4bfcdf1e136ea8802
URL:		http://www.kde-look.org/content/show.php?content=12772
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description
Dark Garden is a decorative outline font of unusual shape. The
typeface is based on author's original hand drawings. The letterform
is complex, with all characters decorated with spikes resembling
thorns or flames, character spacing is very dense. Includes west and
central European characters and some punctuation marks. Every non
ASCII letter has been drawn anew instead of basing on the ASCII
equivalent.

%description -l pl.UTF-8
Dark Garden to dekoracyjna czcionka konturowa o niezwykłym kształcie.
Jej krój jest wzorowany na charakterze pisma autora. Styl liter jest
zróżnicowany, wszystkie są udekorowane kolcami podobnymi do cierni lub
płomieni. Odstępy między znakami. Zawiera litery z alfabetów
zachodniej i środkowej Europy oraz niektóre znaki interpunkcyjne.
Każda litera spoza ASCII została stworzona od zera, bez bazowania na
jej odpowiedniku z ASCII.

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README.txt ChangeLog.txt
%{ttffontsdir}/*.ttf
