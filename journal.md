Title: Maximum retro console 
Author: Riston Rodrigues 
Description: this is a  a console running on raspi 02w running retopie which when overclocked should be able to emulate most old conslote games
waas entriely designed and done by me , includes amplifier and good speakers for immersive sound.
Created at: 27/7/25

what it does- adds better sound to the retro console using amplifier chip, sdesigned for psx psp games should un psp gsmes when pi is overclocked

Total time speant-30+ total time required -50hrs

cost of the project-120 dollars

day-18/7/25

i reserched and create d the bom as wekl the basic schematic on easyeda pro
<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/8a104270-dd87-42aa-b23e-b7e2cbe7045d" />
added right tactile buttims 12 by 12 by 7.3 after considerations
<img width="1904" height="745" alt="image" src="https://github.com/user-attachments/assets/b2098a8e-d7b0-45ae-8f4c-0afd478d3b1a" />

<img width="1854" height="643" alt="image" src="https://github.com/user-attachments/assets/b5771f90-3179-491c-ab92-8b10f3c3f912" />
right naming convenctions

right gnd connections to the d pad and face buttons-<img width="1301" height="490" alt="image" src="https://github.com/user-attachments/assets/b2e3f45a-1c9e-4c1a-b719-665e3059c23b" />
so if i want to emulate psx i need 18 buttons aND adc chip which wont work with gba and snes

right wiring add resst of buttons-<img width="1919" height="776" alt="image" src="https://github.com/user-attachments/assets/cff27e97-1199-49af-af06-6e7b3a08ec6e" />

14 pins added rightly-<img width="1489" height="776" alt="image" src="https://github.com/user-attachments/assets/7b522fc8-029c-4cc8-adc8-5bddea8a10b8" />

wirinf got messed up-<img width="1623" height="797" alt="image" src="https://github.com/user-attachments/assets/954267e1-f7b4-46ff-8540-5e3186eb67f9" />

added the raspi 3.5 inch scfreen it had no fot print has tri create customtook an hour 
<img width="240" height="385" alt="image" src="https://github.com/user-attachments/assets/8e4ab88d-36d8-4481-84fd-0af021c75f24" />
<img width="1763" height="820" alt="image" src="https://github.com/user-attachments/assets/bf78bc72-2842-488b-8d04-eb17afb573ab" />

i need to add the l 1l2 rf1 r2 on top as putting them on main pch makes no sense safter some reserch and work incan dividne use rigt angled headers to achievee the same
<img width="240" height="385" alt="image" src="https://github.com/user-attachments/assets/11712d55-3e66-47e0-a6f2-9200187d67c0" />
<img width="1563" height="778" alt="image" src="https://github.com/user-attachments/assets/f8f553a6-9a60-41f6-98eb-a5a4013ccd4d" /> now the top button panel will be cut and put on top like psp buttond ia bentg male headers

<img width="1919" height="829" alt="image" src="https://github.com/user-attachments/assets/0aa4da0f-53d6-4bcc-82e4-b64c95d37443" />

made right sdjustment it is 2 cm bif noe man just shouldnt get too ugly



time speant -6 hrs

day 2 19/7/25
task- exact placemtn of the components additonl button addition and placement , getting the dimensions right
<img width="1919" height="812" alt="image" src="https://github.com/user-attachments/assets/0a43b18c-6d88-4040-908a-b97ba46e58e0" />
<img width="1919" height="856" alt="image" src="https://github.com/user-attachments/assets/171ebb31-0b3d-4853-9a01-da7df9ebdc86" />
<img width="1916" height="795" alt="image" src="https://github.com/user-attachments/assets/5ab80d33-5cc8-414f-9755-1d43e5f9f683" />

added the place and made right adjustments for lcd plkacements<img width="1919" height="742" alt="image" src="https://github.com/user-attachments/assets/6999ecd8-2c9a-4997-9300-a3c76532641c" />

added the right dimensions and arrangd the components these need to be placed rightly to gibe it correctly feel manually adjusting the coordinates-<img width="1919" height="818" alt="image" src="https://github.com/user-attachments/assets/072045d7-15ec-4540-b328-0cb5dc372997" />

<img width="1915" height="816" alt="image" src="https://github.com/user-attachments/assets/d0c159d9-e26f-4303-8c80-0521f494f14c" />
got the exact right dshape next task adding remaining buttons
<img width="1919" height="827" alt="image" src="https://github.com/user-attachments/assets/1a9a4e9d-0228-42d9-aef7-8d9633ab8da7" />
was loing for attries and good barrries flat ones dont exkist most are cheap ripoffs cant use cylindrical as theyll mess up the most of things
will have to use 2 of 3.7V LiPo Batteries - BIS High Quality 20 it brings thr bil up by 10dollars
added the right routing both l1 l2 r1 r2 will be on top side by sidce will make the console more compact
<img width="1847" height="661" alt="image" src="https://github.com/user-attachments/assets/d6091a32-901f-404a-9acb-f68a013b779b" />

ok new realizarion cant as the pi zero directly below the screen ading it belo the pcb will increae consile sixe woll ned to change placemntd
<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/52545b81-9795-4f76-9c09-a1ecd32941c9" />
priblem make it compact vs longer
<img width="1919" height="813" alt="image" src="https://github.com/user-attachments/assets/860edebd-c747-4eec-9a67-a826d48ac25d" />
increased theight by a few cm cut its not that thick

time spent 5 hrs

day 3 20/7/25

adding the tppy4056 charging module boost converter battries placenmt , i reserched and theres no way i could place the raspi below 5he 3.5 inc lcb placing it on opp side of the board increases board height by 2-3 cm and it destryos compactnes compeletely so stuck what to do more
so i increased the length by 8 cm
<img width="1919" height="880" alt="image" src="https://github.com/user-attachments/assets/3c967158-f6b3-47e9-813c-ebd622582f64" />
<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/c5859b8b-7343-4188-a487-98b65ef50f3b" />
<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/ee035f7c-e6c3-4def-9dc5-badf758bede1" /> the module i think i shouls increase the body part rounf scre to make it symmetric

i addedte tp4056 , mt booster battderis pins to yhe schematic and pcb
<img width="1919" height="872" alt="image" src="https://github.com/user-attachments/assets/9e2372ba-0188-4075-af56-119947f80ca5" />

connecte the charging and battery protectgion to sdpt to power on off then booster to the main circut.

<img width="1919" height="829" alt="image" src="https://github.com/user-attachments/assets/9baa7d47-55df-4d47-b3cb-2ed4e660ab73" />

<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/695f9c86-e0df-42eb-894b-df10abfe4dc5" />
corecting the c onnections
<img width="1502" height="667" alt="image" src="https://github.com/user-attachments/assets/6ef604de-e51c-4998-a78c-ca237d0f3753" />

wired the correct rest home vol and hold butonds
<img width="1915" height="884" alt="image" src="https://github.com/user-attachments/assets/8e24702e-6dcf-438e-94f3-5f305fa289d2" />

<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/72a98b9f-0f06-4c4f-962c-c7e0c40ee9d9" />
coonnected reserched the pwm circut need to reroute some paths and tgings

<img width="1760" height="804" alt="image" src="https://github.com/user-attachments/assets/84a530cc-a6b1-4b11-8672-08806d0aa772" />rewired wire the pam

found added right speajkers
everything except the touch screen for nintendo consoles is done<img width="1919" height="881" alt="image" src="https://github.com/user-attachments/assets/fbbcf991-a168-4990-92a0-19f701e75d53" />

time spent 5 hrs

day 5 23/7/25

tasks done added the righrt 134mil holes on 4 sides of pcb to fir ti in case
binded all 3d model as neded
now the task is crrating approprite case the budget is going above 100 bom is best optimized man hope it doesnt getr fckd too bad as the highway accc has no mony left

<img width="1421" height="608" alt="image" src="https://github.com/user-attachments/assets/0ab6506a-86ef-4193-9be1-4d31a4e3e402" />

boolen 2 to smoothe render derived board****<img width="1915" height="831" alt="image" src="https://github.com/user-attachments/assets/d5fa272f-5c67-4d6f-a922-0e9bf8a3e963" />
shiftd jsxt to nbotom rerouted the nets and paths, fixed 6,, buttons
<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/e1a2d8f7-d1eb-4592-8f7a-0f42850730fb" />

importrd correct model now cadsde design begins found 2-3 erroes in netlist-<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/303c3bae-9789-4174-855e-0b027ac81624" />

really bad mirroring<img width="1847" height="797" alt="image" src="https://github.com/user-attachments/assets/97061cf4-0733-47f7-aa2c-39f2f064d7a2" />
<img width="1918" height="865" alt="image" src="https://github.com/user-attachments/assets/af791d2c-bbce-4774-8c0b-5ea6050021c0" />
<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/09e9d394-3384-40c8-a6f9-1dbbf53120ed" />
 toip cover<img width="1919" height="887" alt="image" src="https://github.com/user-attachments/assets/77962b9c-6b39-4d2c-b663-01aa6d92d986" />

<img width="1916" height="873" alt="image" src="https://github.com/user-attachments/assets/cf36fd58-73cd-4fc8-ba1c-67cb691c0358" />
the case upper part
<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/4bdec599-e987-4a9e-931b-3da3b79ea858" />
addeed upper /lower case parts extrudes fot both usb-c top l1 ,l2 buttons
removed thr derived pcb to correct each indvivdaul sketch<img width="1918" height="956" alt="image" src="https://github.com/user-attachments/assets/4ded48af-648d-49b0-b70e-79a66a6b297e" />
<img width="1919" height="879" alt="image" src="https://github.com/user-attachments/assets/af8d6286-2e74-4e33-b0c3-7019b4c612da" />
<img width="1907" height="841" alt="image" src="https://github.com/user-attachments/assets/7bac863d-ca07-4bac-8733-c2f9668993fe" />
fotgot yhr buttons<img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/e3ddd861-277d-4b51-9c56-9b2698218676" />


total time 8hrs

day 27/7/25
tasks-fixed the entire bom, added right links to bom, tored to find cheapest alternatives but the biggest problems id non acceptane og hcb and aliexpress doesnt dielever at my place

the buttons for the d pad and the o x A keys im did them<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/e7b5564a-1b88-423e-b004-a34a16acda6f" />

<img width="1917" height="866" alt="image" src="https://github.com/user-attachments/assets/efdc322b-ddcf-4e9a-a0f2-0bb5910164ab" />
<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/c67cf495-9e87-4553-807f-dda9f54b6c9f" />

too slow lagginf on my old laptop<img width="1919" height="840" alt="image" src="https://github.com/user-attachments/assets/9547ce39-0606-49be-a74b-641c38b23c42" />

the button finishwed tge basic shaoe for that<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/b0a8f7a2-36fd-4348-b0ae-60cd131a0eae" />
<img width="1919" height="864" alt="image" src="https://github.com/user-attachments/assets/5836f84e-1920-47dc-a982-95dfbab5b375" />
the deriving cobsole didnt work- new thinga to dpo-<img width="1919" height="860" alt="image" src="https://github.com/user-attachments/assets/afff47f0-9e5a-4f77-8de0-839fe818d868" />


just too slow-<img width="1919" height="808" alt="image" src="https://github.com/user-attachments/assets/5e4fa0b1-1682-46c3-9c09-ef6cea422079" />
came to know that wculd hidce individcual patrs of cad many this savesso much time<img width="1919" height="872" alt="image" src="https://github.com/user-attachments/assets/bac9a357-2853-4694-a268-ef299d9a2b00" />

extrusuin to match shell thcckness-<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/e778014c-e6de-458f-9dca-7b3c3b83d953" />

<img width="1919" height="862" alt="image" src="https://github.com/user-attachments/assets/09f00d81-6ddb-4ec1-9807-41aae071ad7f" />
the other symbol pad finished-<img width="1919" height="822" alt="image" src="https://github.com/user-attachments/assets/25c6af6a-d8be-44af-b821-9c54273bc8f6" />

finished thre right pd-<img width="983" height="396" alt="image" src="https://github.com/user-attachments/assets/a0b0d933-f133-4983-a8f5-f04dc321d392" />

a problem with the derived sketchd as i try to get them thsurpress the below things they get messedup

<img width="1919" height="856" alt="image" src="https://github.com/user-attachments/assets/fb037572-408a-427f-81ec-57f4edaf9c6b" />
finished d pad-<img width="1918" height="891" alt="image" src="https://github.com/user-attachments/assets/2a930b89-806e-4051-8424-5d3e055c308b" />


<img width="1919" height="948" alt="image" src="https://github.com/user-attachments/assets/8e08781a-9f25-4a06-a0e6-bb238f640dd4" />

<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/b0fc40ea-d767-44aa-ad00-9de6efa6a272" />
errors when i asembe the whols case gotta fix that

ok i exported the leftpad and right pad imported and problem solved

<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/66962503-c343-4eb5-9092-3d4766611f64" />

final assemblu unitl oi hey the board -<img width="1919" height="881" alt="image" src="https://github.com/user-attachments/assets/f46d191b-9914-49d4-89b7-f548ec49a160" />


tatal time 5.5 hrs



























