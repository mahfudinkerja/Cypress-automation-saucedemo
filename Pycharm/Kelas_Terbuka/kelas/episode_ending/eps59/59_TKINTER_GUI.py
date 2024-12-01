# GUI ->  Graphical User Interface

import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

window = tk.Tk()
window.configure( bg = 'white' )
window.geometry( '300x200' )
window.resizable( False, False )
window.title( 'Sapa Dia!' )

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


def tombol_click():
	pesan = f"{NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Keren Abiiiezzz!"
	showinfo( title = 'Whastuppp!', message = pesan )


# Frame Input
input_frame = ttk.Frame( window )
# penempatan Grid,Pack, Place
input_frame.pack( padx = 10, pady = 10, fill = 'x', expand = True )

# komponen - komponen
# 1. Label nama depan
label_nama_depan = ttk.Label( input_frame, text = 'Nama Depan : ' )
label_nama_depan.pack( padx = 10, fill = 'x', expand = True )

# 2. Entry Nama depan
entry_nama_depan = ttk.Entry( input_frame, textvariable = NAMA_DEPAN )
entry_nama_depan.pack( padx = 10, pady = 10, fill = 'x', expand = True )

# 3. Label nama belakang
label_nama_belakang = ttk.Label( input_frame, text = 'Nama Belakang : ' )
label_nama_belakang.pack( padx = 10, fill = 'x', expand = True )

# 4. Entry Nama belakang
entry_nama_belakang = ttk.Entry( input_frame, textvariable = NAMA_BELAKANG )
entry_nama_belakang.pack( padx = 10, pady = 10, fill = 'x', expand = True )

# 5. Tombol / Button
tombol_sapa = ttk.Button( input_frame, text = "Sapa!", command = tombol_click )
tombol_sapa.pack( padx = 10, pady = 10, fill = 'x', expand = True )

window.mainloop()
