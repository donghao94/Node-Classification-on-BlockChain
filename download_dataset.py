import wget


url1 = 'https://www.dropbox.com/s/5sg20n4w24df1ni/eth_graph.txt?dl=1'
url2 = 'https://www.dropbox.com/s/461t6yww3o1rs8x/address_label.txt?dl=1'

out_fname = './dataset'
wget.download(url1, out=out_fname)
wget.download(url2, out=out_fname)
