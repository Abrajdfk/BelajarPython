def selamat_datang (nama):
    print(f'halo {nama}, selamat datang!')

selamat_datang('Firman')
selamat_datang('Aliyandhika')
selamat_datang('isa')
selamat_datang('neko')

def outer_fuction(siapa):

    def inner_fuction():
        print(f"hello,{siapa}")
    inner_fuction()

outer_fuction("Firman")