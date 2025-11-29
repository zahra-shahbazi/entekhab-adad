#esme karbaar ra migirim
esm_karbar=input('esmet chie?')
#yek khoshamad goyi sade chap miknim;ba fasele monaseb (f-string)
print(f'salam{esm_karbar},khosh omadi!') 
# az karbar mikhaahim yek adad sahih vard konad;
adad_sahih=int(input(f'{esm_karbar}\n yek adad sahih(int) vard kon:'))
# az karbar mikhahim yek adad ashari vard kond;
adad_ashari=float(input(f'{esm_karbar}\n yek addad ashari(float) vard kon(masalan 3.5):'))
#az karbar mikhahim yek adaad tarkibi vard kod;
adad_mokhtalet=complex(input(f'{esm_karbar}\n yek adad mokhtalet(complex) vard con (masalan 4j+6):'))
#jam adad ra hesab miknim
jam=adad_sahih+adad_ashari+adad_mokhtalet
#tafrigh ra hesab miknim;
tafrigh=adad_sahih-adad_ashari-adad_mokhtalet
#zarb ra hesab mikni
zarb=adad_sahih*adad_ashari*adad_mokhtalet
#ataayej ra chop miknim
print(f'\n jam ={jam}')
print(f'\n tafrigh={tafrigh}')
print(f'\n zarb={zarb}')

