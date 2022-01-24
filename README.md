# ascii-art

This project contains a script, 'main.py', to convert an image into ASCII art like the image below.
To use it, just write in the terminal "python main.py \<image directory\>" like "python main.py image_examples/phineas.jpg" in this project directory.
    
Unlike other projects that used 15 characters at maximum to represent all tones, with this project I represent the images with all ASCII characters and instead of eyeballing the 'brightness' of each character I calculated the 'brightness' of each of them by calculating the average value of the pixels of an image representing each character. I have the script that I used to make this in the jupyter notebook 'research.ipynb'.

```text
Ji3Jlllllllllllllllllllllis37lll7tulllllllllllliY23sillilu22233sYV33323Jllll
ii3JllllllllllllllllllllJis37lll7tul7lllllllllllJFsilllilu22233xxk32223[7lll
ii3Jllllllllllllllll777vslJu7lll7tul7llllllllllll77llllilu222221t532232s7lll
li3Jllllllll77lll777z132KyaXIJll7tul7llllllllllllllllllilu22222n1j32232s7lll
iJ3Jl7lllll7[eJ7l1ZR%M$N%6kVsJll7tu7lllllllllllllllllliJlu222223u232222s7lll
ii3Jl7llll7YD6v3#M$$NOhxt7l37lll7tu7lllllllllllllll7JYtJlu2222233332222Y7lll
i73JllllilzDBad$8M%d2tt1jYJn7lll71u77lllllllllllliYu323Jlu2222233332222x7lll
iJ3illlliTd$8NNMBMOO%M%HKtJY7iil71u7lllllllllllllJ32323Jlu222223jff2232t7lll
iJ3iiill7[NMMN880N8MH5Ylx7lillll71u7llllllllllllli32323J7nj22233kuf232217lll
ii3iii7lfX$MNMRO%%U177lJ17llllli713zziilJssJilJJzJ3j223l7sxFsz[J3nn2322u7lll
il3ii72O88M8Ni=+LcLvJ[JtuJJillilzf(!",,:,"/rzzr++?712k3lll777ll7I113222u7lll
il3JJ6B%%8MNNf?/+v===++?L)TiJzsuL:----''----:;<''-''"?tl7illlll7I1x3322ullll
ll37eD27GM$$N$3v+?==c)/=/====+c)''''''''''''';Lc:'''''=hxl7llll7f17iJzFsllll
773lz[7vmBH%BZTJF(+?(========/);''''''''''':5K@&L.--'yA@N7lllll73t7ll777llll
ii3illl738FUO7lll[zv+=========+?'-''''''''-=@&@@w;",;&@@&l7llll73t7lllllllll
lJ3iiill73JJx7lllllsl+/========r+:''''''''':b&@0r=+++[kHylzzz[J73x7lllllllll
lJ3iiilll7l77lllllllJs?=========+r!,''---''':?s+/====///=++?L)v7nY[JJJii7lil
iJ3liillllllllllllllllFr==========+?+=;;;;/=??/==================+?L)v7iF[ll
iJ3liilllllllllllllll7tkv============++++++==========================+L7YJ7l
iJ3liJilll7llllllllil[17[7+/====================================/=+clJzili7l
iJ3liizu[i7llllllllJlu++z?+=======/++==========================+vl[Jilllllll
lJ3lllY233lllllllllliszL)c?+========rL+=====================?)J[ks7lllllllll
iJ37iix223illllllllli7ujfI32+========+rL+================?(7sJl72s7lllllllll
Ji3liit22nilllllli7ll7t22222u==========+Lr+===========?TlY[i7ll72sllllllllll
ii3lllu22tlilllllJJJJlt222231v/==========+??+====/+?)zsJixilllll2z7llJJJllll
ii3ll7u22silllzn3333J7F22222st+=============+???+vJJJll7i3llllli2zlllluJllll
ii3ll7I23zlllls32222[7s22222sFv/=============+TtiJl7illJl2illlli3[llll1s7lll
JJ3lll323zlil7s23222s7s23222FiF============r7Ys7iilllllJl3Jlllli2[llli[u7lll
JJ37ll323iill7s23222t7[32222F71=========+v[sJlllllllllllJ[lllll72JlllJlI7lll
JJ37li32flill7s22222u7J32222tlt+=====/+(zsillllllllllllil7llllll2iilli7nilll
JJ37lisszlill7Y22222fii32222t7t+====?(sJilllllllllllllllllllllli2Jllliln[lll
JJ37lllJillll7Y222223Jl32222f3u/==+7Yillllllllllllllllllllllllll2J7llJ7nYJil
JJ37lllilllll7Y222233sl3233jXy27Lvas7lllllllllllllllllllllllllli2llllJ7ttJll
JJ37llllil77iiY222222t7I22kJ;=infx5J7JJlllllllllllllllJlllllllli2llllilsIJil
iz37lll77Jstz7Y222222u7n2k+::::,:"7YiilllllllllllllllsY7lllllllJji7llllJ3lJl
iJ37lilzu322F7s232223I71kr::::"<'"=tlJilllllllllllllliilllll7lJ[27illlll3iil
iz37lllt5222F7s22222237ja1?+!;/3rl()uss7llllllllllllllllllll7JFJ27illll73s7l
Y137llix2222F7Y2222233fhhk52235m2jX5XJillllllllllllllllllllllliz27illll73Y7l
JY37lliY2222F7JFssz[JYv+JvlJzYFK(?snsI7llllllllllllllllllllllJzz2llllll7ft7l
Y13Jzzzt5555tzszzzzszu"<",,,"",L":;=:7n[zzzzzzzzzzzzzzzzzzzz[F1F2JszzzzJ3fJz
```

For this project what I did was:

1. I wrote a script in the jupyter notebook 'research.ipynb' to automate the process of converting all the ASCII characterS into images using a website that did this conversion, 'https://onlineasciitools.com/convert-ascii-to-image'.
2. Then I calculate the 'brightness' of each character by calculating the average value of each of their pixels and because the values were between 0 and 255 I normalized them to be between 0 and 1 where 0 represented black and 1 white.
3. Than to convert an image into ASCII art I just resized the image into a reasonable size for ASCII art and then replaced each pixel by a character that represented best the tone of that pixel and the result was the above.
