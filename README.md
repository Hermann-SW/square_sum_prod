This fork mission statement:
============================

Use only "gaussian" tool, under symbolic link "square_sum_prod".  
Assert on even or "≡3 (mod 4)" factors.  
Instead of "a + b\*i" output "(a\*\*2 + b\*\*2)".  
Output " * " between factors, and final " == " followed by input.  

Because of [Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares) each factor "≡1 (mod 4)" has unique representation as sum of two squares.

@alpertron's cool gaussian calculator allows to process 120-digit number in less than a second !

Just "make" shows demo after build:  

    pi@pi400-64:~/square_sum_prod $ make
    ./square_sum_prod 97
    (9**2 + 4**2) == 97
    
    ./square_sum_prod 693342667110830181197325401899700641361965863127336680673013|\
    python -c 'import sys;l=sys.stdin.read().rstrip();print(l,"\n"+str(eval(l)))'
    (832050675380196295918334279642**2 + 32161167736719180733109944457**2) == 693342667110830181197325401899700641361965863127336680673013 
    True
    
    ./square_sum_prod 1105|\
    python -c 'import sys;l=sys.stdin.read().rstrip();print(l,"\n"+str(eval(l)))'
    (2**2 + 1**2) * (3**2 + 2**2) * (4**2 + 1**2) == 1105 
    True
    
    pi@pi400-64:~/square_sum_prod $ 


Original README.md:
===================

Results of static analysis and code coverage of this software using [Codacy](https://app.codacy.com/gh/alpertron/calculators/dashboard).

Badges from [SonarCloud](https://sonarcloud.io/summary/overall?id=alpertron_calculators):

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=bugs)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=code_smells)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=coverage)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=ncloc)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=alert_status)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=security_rating)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=sqale_index)](https://sonarcloud.io/dashboard?id=alpertron_calculators)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=alpertron_calculators&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=alpertron_calculators)

If you like these calculators and you want to support free software, you can donate by clicking in one of the buttons below:

Paypal: [![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=MR65QPWZM5JT6)

Liberapay: [<img src="https://liberapay.com/assets/widgets/donate.svg"/>](https://liberapay.com/alpertron/donate)
