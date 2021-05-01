import pikepdf


input_path_source = r'/home/jfgcisneros/Desktop/DC-260-D91FC21183_all.pdf'
input_path_destination = r'/home/jfgcisneros/Desktop/G-28.pdf'

page_to_replace_source =  4
page_to_be_replaced_destination =  3

output_path = r'/home/jfgcisneros/Desktop/test.pdf'
temp_folder = r'/home/jfgcisneros/Desktop/temp/'

with pikepdf.open(input_path_source) as pdf_source:
    dst = pikepdf.new()
    dst.pages.append(pdf_source.pages[page_to_replace_source-1])
    #dst.save(output_path)

with pikepdf.open(input_path_destination) as pdf_destination:
    pdf_destination.pages[page_to_be_replaced_destination-1] = dst.pages[0] 
    dst2 = pdf_destination
    filename = 'G-28_Signed.pdf'
    path = temp_folder + filename 
    dst2.save(path)

