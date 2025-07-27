This is my latest project: a Raspberry Pi Zero 2 W-based console running on RetroPie. I've optimized the Bill of Materials (BOM) to include the best and cheapest available items from official retailers for the Raspberry Pi and screen.
When overclocked(necessary for psp), this console should be able to emulate most systems, including Nintendo DS, Game Boy Advance (GBA), Game Boy Color (GBC), PlayStation (PSX), and even some (PSP games.
I am currently setting up the code for the buttons. My design incorporates 18-20 buttons, similar to a PSP, allowing for accurate emulation of those games. By utilizing the Adafruit button script for RetroPie, I anticipate being able to configure controls for most other consoles as well.
The touch functionality will be specifically for Nintendo DS emulation.

what makes it diff to others- i didnt use any expensive pi audio hats but a simple pam amplifier costing less than a dollar to get better audio thaen most,
i shaped it more like the psp the butten config and all there are the l1/l2 r1/r2 buttons on top of console likr the psp unlike most retro gaming consoles

already spemt 30+ hrs will ned to speand a total of  50+ hrs
## Combined Bill of Materials (BOM)

| Component Name | Quantity | Price (INR incl. GST) | Price (USD approx.) | Link | Status |
| :------------------------------------------------------ | :------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| High Quality Aluminium Heat Sink set for Raspberrypi | 1 | ₹41.30 | $0.49 | https://www.silverlineelectronics.in/products/copy-of-high-quality-copper-heatsink-for-raspberry-pi-4-3-zero-heavy-duty?variant=41178553614405 | Needed |
| HP MicroSD U1 TF Card 64GB | 1 | ₹470.00 | $5.62 | https://www.amazon.in/HP-MicroSD-U1-TF-Card-64GB/dp/B07DJGB43S/ref=sr_1_10?adgrpid=67889856604&dib=eyJ2IjoiMSJ9.eWInd2jxeAJZz49EkP6BB_Jy8608_qFAgUX3DCJt0Ot4xaRWhwpWmTv5bvgnhf9jDHQHKDCJbM4PgFxFf7oXyc5KD8bqyZIkOjbY723wpVECJjDVj9FWBsVELky-6uPh00qteTOwBKWjhSTjIkN1gRr_8hhowbbArBWEuIexYASJlXLmgGoRUlBfJft_7zPJnT9AWqim4NdTzEFF2YzcDGqnVxx93ysGK93ysGK9YCAPs7aY.-l9pmx0yie18AyoXHEe0xdyWhMziDidAMvHmm_YORzg&dib_tag=se&ext_vrnc=hi&hvadid=590712386570&hvdev=c&hvlocphy=9303213&hvnetw=g&hvqmt=e&hvrand=3501601652553383134&hvtargid=kwd-1451409456195&hydadcr=24566_2265454&keywords=amazon+in+sd+card&mcid=8d820900b4303655b882bcadd10017d3&nsdOptOutParam=true&qid=1753339654&sr=8-10 | Needed |
| Raspberry Pi Zero 2W | 1 | ₹1,565.86 | $18.70 | https://www.silverlineelectronics.in/products/raspberry-pi-zero-2-silverline-india-authorised-distributor?srsltid=AfmBOopKDfKSIzEPqnLU9wZlhkan6065xBBauW60XlCJVufSuaGN-J0f | Needed |
| Tactile Push Button Switch Assorted Kit - 25 Pieces pack | 1 | ₹149.00 | $1.78 | https://robocraze.com/products/tactile-push-button-switch-assorted-kit-25-pieces-pack?_pos=5&_psq=tact&_ss=e&_v=1.0 | Needed |
| 3.5in Touch Screen LCD Display for Raspberry Pi | 1 | ₹911.00 | $10.87 | https://robocraze.com/products/3-5in-lcd-display-for-raspberry-pi?srsltid=AfmBOooWmyoajuA82d-tPmtNazCUhFErN-cBzXXeqUO3Y-K7Bh1i4BN6 | Needed |
| 4-Pins DIP Momentary Square Tactile Push Button Switch 10 Pieces - 6x6x5mm | 1 | ₹18.00 | $0.21 | https://robocraze.com/products/4-pins-dip-momentary-square-tactile-push-button-switch-10-pieces-6x6x5mm?_pos=9&_sid=25e39f251&_ss=r | Needed |
| 3.7V LiPo Batteries - BIS High Quality | 2 | ₹899.98 | $10.74 | https://thinkrobotics.com/products/bis-certified-3-7v-lipo-batteries?variant=40048541728854&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=googleads&utm_medium=cpc&gad_source=1&gad_campaignid=18239908785&gbraid=0AAAAACk3EvwJWn9nt3NIG_NY4Wmek6bcH&gclid=Cj0KCQjwhO3DBhDkARIsANxrhTpPnq3C8N-1qZAhaAwoMU_7-qtUxPFHU_YGlb16HUxtdIClyg2O6IaAkVuEALw_wcB | Needed |
| 2515 2 Pin JST XH Male Right Angle Connector – 2.54mm Pitch (25 Pcs) | 1 | ₹36.00 | $0.43 | https://roboticsdna.in/product/2515-2-pin-jst-xh-male-right-angle-connector-2-54mm-pitch-25-pcs/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gad_source=1&gad_campaignid=22411741198&gbraid=0AAAAAC-xzeGCjjNIR8MxcHx1pwcM04n0C&gclid=Cj0KCQjwhO3DBhDkARIsANxrhTpPnq3C8N-1qZAhaAwoMU_7-qtUxPFHU_YGlb16HUxtdIClyg2O6IaAkVuEALw_wcB | Needed |
| TP4056 Battery Charger C-Type Module with Protection | 1 | ₹19.00 | $0.23 | https://robocraze.com/products/tp4056-battery-charger-c-type-module-with-protection-1?_pos=1&_sid=bd7cd366c&_ss=r | Needed |
| MT3608 DC-DC Boost Module (2V-24V) | 1 | ₹44.00 | $0.53 | https://robocraze.com/products/mt3608-dc-dc-boost-module-2v-24v?_pos=2&_psq=boost&_ss=e&_v=1.0 | Needed |
| PAM8403 Digital Power Amplifier | 1 | ₹34.00 | $0.41 | https://robocraze.com/products/pam8403-digital-power-amplifier?_pos=1&_sid=4e256fde9&_ss=r | Needed |
| 2030 Cavity Speaker, 8Ω 2W | 1 | ₹300.00 | $3.59 | https://thinkrobotics.com/products/2030-cavity-speaker-8%CF%89-2w?_pos=2&_sid=e26492f4d&_ss=r | Needed |
| Solder Wire 50gm (1mm) | 1 | ₹100.00 | $1.20 | https://thinkrobotics.com/products/solder-wire-40gm-1 | Needed |
| PCB Fabrication (jlc) | 1 | ₹1,254.00 | $15.00 | *N/A (Service Cost)* | Needed |
| 3D Printing Services (printing legionm) | 1 | ₹585.20 | $7.00 | *N/A (Service Cost)* | Needed |
| UNI-T UT33D+ Digital Multi-meter | 1 | ₹875.00 | $10.47 | https://www.amazon.in/UNI-T-UT33D-Digital-Multi-meter-Manual/dp/B08W36VF6H/ref=pd_vtp_h_pd_vtp_h_d_sccl_2/262-9085288-8324515?pd_rd_w=pTEzb&content-id=amzn1.sym.6c9a4279-ad42-4fd6-b9a9-3cd14ede34c9&pf_rd_p=6c9a4279-ad42-4fd6-b9a9-3cd14ede34c9&pf_rd_r=AQWFZQ9FFMCHDGND0GQA&pd_rd_wg=gIHq2&pd_rd_r=2e92b59a-4cb2-4ed3-ab7a-7e505bb798a0&pd_rd_i=B08W36VF6H&psc=1 | Needed |
| M3 10mm SS Screws (25 Pcs) | 1 | ₹83.60 | $1.00 | https://roboticsdna.in/product/m3-10mm-stainless-steel-screws-25-pieces/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gad_source=1&gad_campaignid=22411741198&gbraid=0AAAAAC-xzeFYu4l4B2scm_19-MkV-ks1J&gclid=Cj0KCQjwkILEBhDeARIsAL--pjwVTMkqiyYBPgPZLET7SitmR4p4i6frF9hqcwMqjGWH6tK9m9Dq7pEaAnWKEALw_wcB | Needed |
| M3 Nuts SS (25 Pieces) | 1 | ₹35.40 | $0.42 | https://roboticsdna.in/product/m3-nuts-ss-25-pieces/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gad_source=1&gad_campaignid=22411741198&gbraid=0AAAAAC-xzeHWsnFWhIbOm4RUnes1mhqz-&gclid=Cj0KCQjws4fEBhD-ARIsACC3d29MrUHuIXUFcil_X6_c8k6od2TpDrRg1q5CwJTiWuMUcHyvGuRSuj0aAh2yEALw_wcB | Needed |
| Hookup Wire (Stranded Assortment) | 1 | ₹150.00 | $1.79 | *N/A (Common Component)* | Needed |
| 0.1mm Copper Soldering Solder PPA Enamelled Repair Reel Wire | 1 | ₹25.00 | $0.30 | https://roboticsdna.in/product/0-1mm-copper-soldering-solder-ppa-enamelled-repair-reel-wire/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gad_source=1&gad_campaignid=22411741198&gbraid=0AAAAAC-xzeGXH678XaKVPbIhi9RKIVnVo&gclid=CjwKCAjw1ozEBhAdEiwAn9qbzd7ZAGkXTHaefr0acwciKOwB2wPFmYPZcgyTDhQEBKUefTSgr7LeAxoCFvQQAvD_BwE | Needed |
| 40x2 Female Berg Strip | 3 | ₹51.00 | $0.61 | https://robocraze.com/products/40x2-female-berg-strip?_pos=2&_psq=berg&_ss=e&_v=1.0 | Needed |
| 40x2 Pin 2.54mm Pitch Male Berg Strip | 3 | ₹27.00 | $0.32 | https://robocraze.com/products/40x2-pin-2-54mm-pitch-male-berg-strip?_pos=5&_psq=berg&_ss=e&_v=1.0 | Needed |
| Desoldering Wick | 2 | ₹28.00 | $0.33 | https://robocraze.com/products/desoldering-wick?pr_prod_strat=e5_desc&pr_rec_id=5577d3441&pr_rec_pid=8058430128352&pr_ref_pid=8875386568928&pr_seq=uniform | Needed |
| Noel Soldering Flux Paste 10gm | 1 | ₹22.00 | $0.26 | https://robocraze.com/products/noel-soldering-flux-paste-10gm-pack-yellow?pr_prod_strat=jac&pr_rec_id=5577d3441&pr_rec_pid=8875387945184&pr_ref_pid=8875386568928&pr_seq=uniform | Needed |
| Heat Shrink Tubing | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| Desoldering Tool (Pump) | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| Soldering Iron | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| USB Cables | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| Precision Screwdrivers | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| Multi-screwdriver | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |
| Hot Glue Gun/Glue Sticks | 1 | ₹0.00 | $0.00 | Owned/Pre-owned | Owned/Pre-owned |

---

### Additional Project Costs

| Item | Price (INR approx.) | Price (USD) | Status | Notes |
| :------------------------------- | :------------------ | :---------- | :----- | :---------------------------------- |
| Buffer for Price Increase/Stockout | ₹668.80 | $8.00 | Needed | damn currency conversion of 3percent charged by most retailers, plas biffer if not woulfd be returned |
| Shipping Fees | ₹250.80 | $3.00 | Needed | would be saved and returned |

---

### Total Estimated Project Cost

| Currency | Amount |
| :------- | :----- |
| **INR** | **₹10,054.80** |
| **$USD** | **$120.27** |

---
if the rate of dollar to inr ids more the rest of money cold be returned to hc,
didnt recieve my raspi from raspapi ysws which gavr the participants local raspberrypi 0 2w , now it would have saved hc the price of that 0 2w no ides when i could get it .


some reatilers offer free shiping others still ask 1-2 dollars that the buffer for it
i didnt get thr raspi zero from old ysws , compeleted it could have saved hc some money but its still stuck in limbo

schematic<img width="1442" height="668" alt="image" src="https://github.com/user-attachments/assets/7bc4d126-23b5-4c12-b3cf-6daee8917960" />

pcb-<img width="1864" height="662" alt="image" src="https://github.com/user-attachments/assets/22c4bbed-905f-4b7c-9d7c-48e21c843701" />
2d-<img width="1918" height="799" alt="image" src="https://github.com/user-attachments/assets/91fde730-c040-4c01-bac5-2b72e45f4c25" />


3d pcb<img width="1441" height="716" alt="image" src="https://github.com/user-attachments/assets/22799e19-1980-4801-b9bb-25a944068e4d" />

case-<img width="1919" height="881" alt="image" src="https://github.com/user-attachments/assets/41b728ac-7a07-4841-b24e-aa8da5a9d699" />
<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/57dbb11d-e547-4878-8591-d733298e8375" />


