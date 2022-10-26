# python_pytest

**PyTest** demonstration in **Python 3**

Libraries: *pytest*

```latex
\documentclass[10pt,a4paper]{article}

% Packages
\usepackage{fancyhdr}           % For header and footer
\usepackage{multicol}           % Allows multicols in tables
\usepackage{tabularx}           % Intelligent column widths
\usepackage{tabulary}           % Used in header and footer
\usepackage{hhline}             % Border under tables
\usepackage{graphicx}           % For images
\usepackage{xcolor}             % For hex colours
%\usepackage[utf8x]{inputenc}    % For unicode character support
\usepackage[T1]{fontenc}        % Without this we get weird character replacements
\usepackage{colortbl}           % For coloured tables
\usepackage{setspace}           % For line height
\usepackage{lastpage}           % Needed for total page number
\usepackage{seqsplit}           % Splits long words.
%\usepackage{opensans}          % Can't make this work so far. Shame. Would be lovely.
\usepackage[normalem]{ulem}     % For underlining links
% Most of the following are not required for the majority
% of cheat sheets but are needed for some symbol support.
\usepackage{amsmath}            % Symbols
\usepackage{MnSymbol}           % Symbols
\usepackage{wasysym}            % Symbols
%\usepackage[english,german,french,spanish,italian]{babel}              % Languages

% Document Info
\author{nanditha}
\pdfinfo{
  /Title (pytest.pdf)
  /Creator (Cheatography)
  /Author (nanditha)
  /Subject (Pytest Cheat Sheet)
}

% Lengths and widths
\addtolength{\textwidth}{6cm}
\addtolength{\textheight}{-1cm}
\addtolength{\hoffset}{-3cm}
\addtolength{\voffset}{-2cm}
\setlength{\tabcolsep}{0.2cm} % Space between columns
\setlength{\headsep}{-12pt} % Reduce space between header and content
\setlength{\headheight}{85pt} % If less, LaTeX automatically increases it
\renewcommand{\footrulewidth}{0pt} % Remove footer line
\renewcommand{\headrulewidth}{0pt} % Remove header line
\renewcommand{\seqinsert}{\ifmmode\allowbreak\else\-\fi} % Hyphens in seqsplit
% This two commands together give roughly
% the right line height in the tables
\renewcommand{\arraystretch}{1.3}
\onehalfspacing

% Commands
\newcommand{\SetRowColor}[1]{\noalign{\gdef\RowColorName{#1}}\rowcolor{\RowColorName}} % Shortcut for row colour
\newcommand{\mymulticolumn}[3]{\multicolumn{#1}{>{\columncolor{\RowColorName}}#2}{#3}} % For coloured multi-cols
\newcolumntype{x}[1]{>{\raggedright}p{#1}} % New column types for ragged-right paragraph columns
\newcommand{\tn}{\tabularnewline} % Required as custom column type in use

% Font and Colours
\definecolor{HeadBackground}{HTML}{333333}
\definecolor{FootBackground}{HTML}{666666}
\definecolor{TextColor}{HTML}{333333}
\definecolor{DarkBackground}{HTML}{377D2C}
\definecolor{LightBackground}{HTML}{F2F6F1}
\renewcommand{\familydefault}{\sfdefault}
\color{TextColor}

% Header and Footer
\pagestyle{fancy}
\fancyhead{} % Set header to blank
\fancyfoot{} % Set footer to blank
\fancyhead[L]{
\noindent
\begin{multicols}{3}
\begin{tabulary}{5.8cm}{C}
    \SetRowColor{DarkBackground}
    \vspace{-7pt}
    {\parbox{\dimexpr\textwidth-2\fboxsep\relax}{\noindent
        \hspace*{-6pt}\includegraphics[width=5.8cm]{/web/www.cheatography.com/public/images/cheatography_logo.pdf}}
    }
\end{tabulary}
\columnbreak
\begin{tabulary}{11cm}{L}
    \vspace{-2pt}\large{\bf{\textcolor{DarkBackground}{\textrm{Pytest Cheat Sheet}}}} \\
    \normalsize{by \textcolor{DarkBackground}{nanditha} via \textcolor{DarkBackground}{\uline{cheatography.com/124877/cs/23933/}}}
\end{tabulary}
\end{multicols}}

\fancyfoot[L]{ \footnotesize
\noindent
\begin{multicols}{3}
\begin{tabulary}{5.8cm}{LL}
  \SetRowColor{FootBackground}
  \mymulticolumn{2}{p{5.377cm}}{\bf\textcolor{white}{Cheatographer}}  \\
  \vspace{-2pt}nanditha \\
  \uline{cheatography.com/nanditha} \\
  \end{tabulary}
\vfill
\columnbreak
\begin{tabulary}{5.8cm}{L}
  \SetRowColor{FootBackground}
  \mymulticolumn{1}{p{5.377cm}}{\bf\textcolor{white}{Cheat Sheet}}  \\
   \vspace{-2pt}Published 7th August, 2020.\\
   Updated 7th August, 2020.\\
   Page {\thepage} of \pageref{LastPage}.
\end{tabulary}
\vfill
\columnbreak
\begin{tabulary}{5.8cm}{L}
  \SetRowColor{FootBackground}
  \mymulticolumn{1}{p{5.377cm}}{\bf\textcolor{white}{Sponsor}}  \\
  \SetRowColor{white}
  \vspace{-5pt}
  %\includegraphics[width=48px,height=48px]{dave.jpeg}
  Measure your website readability!\\
  www.readability-score.com
\end{tabulary}
\end{multicols}}




\begin{document}
\raggedright
\raggedcolumns

% Set font size to small. Switch to any value
% from this page to resize cheat sheet text:
% www.emerson.emory.edu/services/latex/latex_169.html
\footnotesize % Small font.

\begin{multicols*}{2}

\begin{tabularx}{8.4cm}{x{4.24 cm} x{3.76 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{Basic}}  \tn
% Row 0
\SetRowColor{LightBackground}
pytest test\_mod.py & Run tests in a module. \tn 
% Row Count 2 (+ 2)
% Row 1
\SetRowColor{white}
pytest testing/ & Run tests in a directory. \tn 
% Row Count 4 (+ 2)
% Row 2
\SetRowColor{LightBackground}
pytest \seqsplit{test\_mod.py::test\_func} & Run a specific test within a module. \tn 
% Row Count 6 (+ 2)
% Row 3
\SetRowColor{white}
pytest \seqsplit{test\_mod.py::TestClass::test\_method} & Run a specific method of a class. \tn 
% Row Count 8 (+ 2)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}

\begin{tabularx}{8.4cm}{x{2.64 cm} x{5.36 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{General}}  \tn
% Row 0
\SetRowColor{LightBackground}
-k "expression" & Run tests by keyword expression. \tn 
% Row Count 2 (+ 2)
% Row 1
\SetRowColor{white}
-m "expression" & Run tests by marker expression. \tn 
% Row Count 4 (+ 2)
% Row 2
\SetRowColor{LightBackground}
-{}-fixtures & Shows builtin and custom fixtures. \tn 
% Row Count 6 (+ 2)
% Row 3
\SetRowColor{white}
-{}-markers & Shows builtin and custom markers. \tn 
% Row Count 8 (+ 2)
% Row 4
\SetRowColor{LightBackground}
-{}-lf, -{}-last-failed & Run only the failed tests from the previous run. \tn 
% Row Count 10 (+ 2)
% Row 5
\SetRowColor{white}
-{}-ff, -{}-failed-first & Rerun the failures first and then successful tests. \tn 
% Row Count 12 (+ 2)
% Row 6
\SetRowColor{LightBackground}
-x, -{}-exitfirst & Exit immediately on first error or failed test. \tn 
% Row Count 14 (+ 2)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}

\begin{tabularx}{8.4cm}{x{4 cm} x{4 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{Reporting}}  \tn
% Row 0
\SetRowColor{LightBackground}
-v, -{}-verbose & More verbosity. \tn 
% Row Count 1 (+ 1)
% Row 1
\SetRowColor{white}
-q, -{}-quiet & Less  verbosity. \tn 
% Row Count 2 (+ 1)
% Row 2
\SetRowColor{LightBackground}
-{}-disable-warnings, \{\{nl\}\} -{}-disable-pytest-warnings & Disable the display of warnings summary. \tn 
% Row Count 5 (+ 3)
% Row 3
\SetRowColor{white}
-{}-html=path & Generate the HTML report at given path {[}pytest-html{]}. \tn 
% Row Count 8 (+ 3)
% Row 4
\SetRowColor{LightBackground}
-r & Display a short test summary info. \tn 
% Row Count 10 (+ 2)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\SetRowColor{LightBackground}
\mymulticolumn{2}{x{8.4cm}}{The -r option accepts a number of characters after it. Default is fE to list failures and errors. \newline f - failed \newline E - error \newline s - skipped \newline x - xfailed \newline X - xpassed \newline p - passed \newline P - passed with output \newline Special characters for (de)selection of groups: \newline a - all except pP \newline A - all \newline N - none, this can be used to display nothing (since fE is the default)}  \tn 
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}

\begin{tabularx}{8.4cm}{x{3.04 cm} x{4.96 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{Debugging}}  \tn
% Row 0
\SetRowColor{LightBackground}
-l, \{\{nl\}\} -{}-showlocals & Show local variable in traceback. \tn 
% Row Count 2 (+ 2)
% Row 1
\SetRowColor{white}
-{}-full-trace & Show complete tracebacks. Default is to cut. \tn 
% Row Count 4 (+ 2)
% Row 2
\SetRowColor{LightBackground}
-{}-pdb & Pytest places a debugger breakpoint whenever an error occurs in tests. \tn 
% Row Count 7 (+ 3)
% Row 3
\SetRowColor{white}
-{}-co,\{\{nl\}\}-{}-collect-only & Collect tests, don't execute them. \tn 
% Row Count 9 (+ 2)
% Row 4
\SetRowColor{LightBackground}
-{}-help & Lists all the Pytest and dependent packages command line options. \tn 
% Row Count 12 (+ 3)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}

\begin{tabularx}{8.4cm}{x{3.44 cm} x{4.56 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{Parallelization {[}pytest-xdist{]}}}  \tn
% Row 0
\SetRowColor{LightBackground}
-n numprocesses & Number of processes to start. Can be a positive integer or Use 'auto' for auto detection CPUs number. \tn 
% Row Count 5 (+ 5)
% Row 1
\SetRowColor{white}
-{}-dist no/ loadscope/ loadfile & Select the test distribution algorithm with the -{}-dist option. \tn 
% Row Count 8 (+ 3)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\SetRowColor{LightBackground}
\mymulticolumn{2}{x{8.4cm}}{Distributing algorithm values are  \newline {\bf{no}}: -{}-numprocesses will send pending tests to any worker that is available, without any guaranteed order. \newline {\bf{loadscope}}: Tests are grouped by the module for test functions and by class for test methods. \newline {\bf{loadfile}}: Tests are grouped by their containing file.}  \tn 
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}

\begin{tabularx}{8.4cm}{x{3.28 cm} x{4.72 cm} }
\SetRowColor{DarkBackground}
\mymulticolumn{2}{x{8.4cm}}{\bf\textcolor{white}{Testrail  {[}pytest-testrail{]}}}  \tn
% Row 0
\SetRowColor{LightBackground}
-{}-testrail & Create and update testruns. \tn 
% Row Count 2 (+ 2)
% Row 1
\SetRowColor{white}
-{}-tr-config=path & Defaults to testrail.cfg . \tn 
% Row Count 4 (+ 2)
% Row 2
\SetRowColor{LightBackground}
-{}-testrail-run-name & Name given to Testrun. \tn 
% Row Count 6 (+ 2)
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\SetRowColor{LightBackground}
\mymulticolumn{2}{x{8.4cm}}{{\bf{pytest -{}-testrail -{}-tr-config= testrail.cfg}} \newline Testrail config file template: \newline {[}API{]} \newline url = \seqsplit{https://yoururl.testrail.net/} \newline email = user@email.com \newline password = \textless{}api\_key\textgreater{} \newline  \newline {[}TESTRUN{]} \newline assignedto\_id = \textless{}user-id\textgreater{} \newline project\_id = \textless{}project-id\textgreater{} \newline suite\_id = \textless{}test-suite-id\textgreater{} \newline name = \textless{}test-run-name\textgreater{}}  \tn 
\hhline{>{\arrayrulecolor{DarkBackground}}--}
\end{tabularx}
\par\addvspace{1.3em}


% That's all folks
\end{multicols*}

\end{document}
```
