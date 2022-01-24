# ascii-art

This project contains a script, "main.py", to convert an image into ASCII art like the image below.
To use it, just write in the terminal "python main.py \<image directory\>" like "python main.py image_examples/phineas.jpg" in this project directory.
    
Unlike other projects that used 15 characters at maximum to represent all tones, with this project I represent the images with all ASCII characters and instead of eyeballing the 'brightness' of each character I calculated the 'brightness' of each of them by calculating the average value of the pixels of an image representing each character. I have the script that I used to make this in the jupyter notebook 'research.ipynb'.

```text
7i7ICT7777777777777777777777777777777l77f177777777137777777777777777777iiI33uii777777lf3333333Ci(y33333323t7777777
7i7ICT7777777777777777777777777777777i773177777777137777777777777777777iiIf3t77777777lf3333333Ci(y33333323t7777777
7i7ICv777777777777777777777777777lTl7i7T2x7777777Tufl77777777777777777777iil777777777lf33333333sThn3333333u7777777
7i7ICv777777777777777777777777777l77[s7T2F7777777Tufl77777777777777777777777777777777lf33333333FThu3333333n7777777
7i7CCv777777777777777777777777TT7vT)zxv(txv777777Tufl77777777777777777777777777777777lf33333333t7h13333333n7777777
7i7CCv77777777777777T777777Tv7isu2aa4dXXbqVt77777Tufl77777777777777777777777777777777lf33333333t7h13333333n7777777
7ilC177777777777777l3i7l7vvtadD%%NNN$%#XaV[il7777Tn3777777777777777777777777777777777lf33333333IJy13333333I7777777
7iiC17777777777777sOdT7(syGMNMNMNND6envTz3v777777Tn377777777777777777777777777777ll77lf33333333fJyt3333332Cl777777
777ft7777777777771%BCvJh%NMM%MM%d5TvsY7l13v777777Tn3777777777777777777777777777[Fuz77lf333333333xaFf3333333i777777
777ftT777777777vu%MDi2%8MM%NMRo[(TvvssvvCtT7777777nflT777777777777777777777iJxn322s77lf3333333331asC3333333J777777
777CtT777777lJ77MM%%4NMM%%%#y3e66mGGHdtvIJT777777TI37777777777777777777777iI22f332s77lf333333333uysn3333333J777777
7iiCtT77777777)X$%%0N%%M$BDDMNN$NM#Ket77Yi77l7777TI3T777777777777777777777i3333332s77lf3333333333yJu3333333J777777
7ll3tT77777777JMM%%%MM%MB$%%%NMHeF7v1777l77777777TI3T777777777777777777777lf333332si7l32333333333yin3333333z777777
7773tT7l77777vs$M%%%MNNM%%MNDKt7T777f777777777777TI3T7777777777777777777777I23f323s7viI333fn11111hi13333332Y777777
7773tT7ll7T7fw#$M%MM%66#DMDeJvv77l7l37777777777l7TC37[zziJ[JJYsJl7777l77ilTn233332z777Jiill77777Jylt3333332Y777777
7iT31T7l772OMMM%%M8Dv==+rTv(JsFYsiJs3T77777777llT7V2(+<",,,:";/r7sszizlT77J3222232J7777777777777Ja7x3333332Y777777
7iT3t7JTsG8MNM%%MM0u!/===///==+rc)7YI[ssJl7777lTtu=,''---'''---'':!Yc"::'::,;/v3k2z7777777777777Ja7x3333333Y777777
7iT3t77uM$MGb8%MM%ND2L=/=JF/===//=/==+?LTlJzYFs2L:.-'''''''''''''-'';);-''---.-:/unTTl7777777777Je7[nC33323t777777
7lT3t7z8%Xx)68%%BM%M0XJ?/+?===+3r/==//=///==++1c-'''''''''''''''''''':r!''''''''.:=ITi7777777777[elT77iJsttz777777
77T31v[4sTT(UN%N8N%8p(i1[?/==/=?==============x:'''''''''''''''''',7DBmR;'''''''/10&q(i77777777TYe7777777777777777
77T3tv77il7ve8MHa8MMs77T[1T+!v1+==============s'''''''''''''''''',8T2@@@a.'-''-+&1g@&1T77777777TYe7777777777777777
7773t7777777sM$1i%B3(7777TzF(??==============/J;''''''''''''''''-)@&&&&@M""::'.w@@@@@Vv777777777Ye7777777777777777
7773tT777777v2%[T2HT77777lT7sY+/==============+J,.'''''''''''''''!@@@@@@K/+?++/2&&&@&tl777777777Ye7777777777777777
7i73FT7l777777s77T7777777777TiuT//=============+J;'''''''''''''''-lQ&&&d/=====+==Ll337JsszJJi77vFk7777777777777777
7i73FT7l77777777777777777777777zz=/==============(c;:'.-''''''''''.:+xs//========////==+?L)7iJ[sno7i77777777777777
7J72YT7l77777777777777777777777TJs+/===============c)+;,:''''''::"!L)+/==================////=++L(vlJ[zszi777Til77
Ti72YT7l7777777777777777777777777J1+==============/==+?Lr+=====+rr?+==/==========================//==++rcv7itt7777
7J73YT7l7777777777777777777777777[F2r/================/================================================///?TstT777
7J73YT7l7777777777777777777777777I2yec?=/===========================================================/=+rTsYJTllT77
7J73YT7lii7777777777777777777l7Tz3c+)7J?!============/=/=========================================/=+L7Fsl777777777
7J73YT7l77Fs77777777777777777iiv2?!?uL+r===========/=+=/=/====================================//+c7ssl777777777777
7l72s7777733uFJT7777777777777l773L!rYL++===========/=+v?=================================/=/=+c752T777777777777777
7772s7777l333237777777777777777l7CJ+?cc+++=============))+/=============================/=+(JxslI3T777777777777777
7l75s7777J3333n777777777777777i7Tzo2C1x15f==============+cc+====================/======+)iFz7T7TC2T777777777777777
7J75[77l7[3323t777777777777777777J333323Ces==============/+)c+/=================/=/=+(tsz7777777C2T777777777777777
iiT3J7777z3323F7l7777777777777777J333333332(//==============+cc+/==============/=+sssiJT77777777f3T777777777777777
l772J7777s2333z7l777777777777ll77J33333333s3=/================+cc+========/===+vtFl777F77777777733777777l777777777
l772J7777Y233fJ777777TiiJsYt1si77J33333333JFl/=================/=?cL+///=/=?(lJl7l77TJ3l7777777733777777lzJl777777
l772J7777F333f7Jl7777iu3333333lTTlf3333333Yl3+=====================+rLL?+(FsJT7777777x3T777777773nl77777T117777777
l772J7777x333n7777777in3333333J77lf3333332YT1J/=====================/+nt7J77T7l7777J7soT77777777317777777z3v777777
i772J7777u333177l77777C3333333sv77I3333333F7l3===================/=?71[T7l777777777JTJh7777777773u777777JT27777777
J7lo[7777u333177l77777C3333333Yv77I3333333xlT3r/==============/=+vsxzl777l777777777llJ27777777772u777777lvIx777777
il75J7777u333Y7i777777C33333331T7Tu3333332t7T3c/============/=Llts77777777777777777Tliz77777777T5t777777iv11T77777
il75J7777u333sT7777777C3333333n77Tu3333332t7T3)/===========/rYti7777777777777777777i77777777777T5t777777i7sI777777
il75J777lI233zTl77777l33333333Ci77t2333333n77n)=/=======/=)zsJ777777777777777777777777777777777Tkz7777777TJ3777777
il75J777lYssY77i77777l333333333[77x2333333I77Ic=/=====/+cxs777777777777777777777777777777777777Tkz7777777JT2777777
J7lol777777l777777777l33333333fx7TY2333333C(T3c=====/+7F777777777777777777777777777777777777777T5Y7T7777iiv5[7l777
J7lol77777li777777777l33333333317TY2333332fuea+=====c1YT777777777777777777777777777777777777777T5F7T7777l7T3x7i777
J77e77777777777777777l333333333n77s333332CXd2ar+=/+53TT7777777777777777777777777777777777777777Te[777777l7Tuu7[777
J77e77777777777777777l333333333fi7z3333C2enJfoae232KeT77777777777777777777777777777777777777777TVJ777777l7TF37J777
777e777777777l77777ill3333333333zTJ332222+:,!LTYtsv2[777iJ77777777777777777777777J77777777777777yJl77777777[27J777
7lle77777777777iisJTil3333333332Y7l33CaF":::::::,:"LfT77ll7777777777777777777777s1T7777777777777yJi777777777e7ll77
777k777777777iYuf3tT7lf333333333t7if3ys"::::::;:::;+IJ77TT7777777777777777777777z[7777777777777lyJl77777777TeJ7i77
l77k777777lYC33333tTT7C3333333331Tluav<,::::::v":'"=/kTTzJ777777777777777777777777777777777vli7lai777777777T21Tl77
777k777777ln223333tT7lf333333333I77oEuY!;"",::i7/+LI'nFv1s7777777777777777777777777777777777i1l7al777777777TC37777
7FJk77777l71233333tT7i33333333333is63KC33CtYJTUU133KcfE7[J777777777777777777777777777777777Tlz7lai7l77777777u3l777
l3JkT7777l71233333tTTi323333333ffFX2hef2Cf333IXKfffKXCb1l77777777777777777777777777777777777777Jai7777777777t2l777
lsJeT7777l7t233333tTT7FtFsszzJJ7[C?LetIC3fC333VGtYz16f3677777777777777777777777777777777777llz7JVJ7777777777Yk7777
llJkT77777Tt333333xT7l7777777l7TC+'!;"";;;<!/=/2:,::x<,=377777777777777777777777777777777777Jt7iei7777777777Ja7777
Jfxyzsssss[Io555o5uJsssssssssYJFI",),,,,,,,,,,:J":,,T",:33zssssssssssssssssssssssssssssssssztfzFyz[ssssssss[sKzzss
```

For this project what I did was:

1. I wrote a script in the jupyter notebook 'research.ipynb' to automate the process of converting all the ASCII characterS into images using a website that did this conversion, 'https://onlineasciitools.com/convert-ascii-to-image'.
2. Then I calculate the 'brightness' of each character by calculating the average value of each of their pixels and because the values were between 0 and 255 I normalized them to be between 0 and 1 where 0 represented black and 1 white.
3. Than to convert an image into ASCII art I just resized the image into a reasonable size for ASCII art and then replaced each pixel by a character that represented best the tone of that pixel and the result was the above.
