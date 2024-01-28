from pdf2image import convert_from_path
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pathlib import Path
from tkinter import ttk


def pdf_to_image():
    filePathOfPdf = Path(pdffileName.get())
    pathOfImage = Path(imageDirName.get())
    fileNameOfImage = imageFileName.get()
    dpiOFImage = int(dpi_value.get())
    saveGrayImage = False
    if gray_value.get():
        saveGrayImage = True

    if str(filePathOfPdf) == '':
        showinfo("Error", "Please enter Input File Name")
        return

    if str(pathOfImage) == '':
        showinfo("Error", "Please Select Output Folder")
        return

    if str(fileNameOfImage) == '':
        showinfo("Error", "Please enter Output File Name")
        return

    try:
        pages = convert_from_path(str(filePathOfPdf),
                                  poppler_path=r".\poppler-23.11.0\Library\bin",
                                  dpi=dpiOFImage,
                                  grayscale=saveGrayImage)
        for page in pages:
            page.save(pathOfImage / f'{fileNameOfImage}.jpg')
    except FileNotFoundError as ex:
        # print("Exception occurred:", ex)
        Result = str(ex)
        showinfo("Result", Result)
    else:
        Result = "success"
        showinfo("Result", Result)


def select_file():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./',
        filetypes=filetypes)

    pdffileName.delete(0, END)
    print(str(filename).strip('/'))
    pdffileName.insert(0, filename)


def save_Dir():
    pass

    directory = fd.askdirectory(
        title='Select Save Folder',
        initialdir='./',
    )
    imageDirName.delete(0, END)
    imageDirName.insert(0, directory)


root = Tk()
root.resizable(False, False)
root.geometry('530x110')
root.title("PDF to Image")

Label(root, text="File Name: ").grid(row=1, column=1)
pdffileName = Entry(root, width=50)
pdffileName.grid(row=1, column=2, columnspan=3)
selectFileButton = Button(root, width=15, text="Select File", command=select_file)
selectFileButton.grid(row=1, column=5)

Label(root, text="Save File Location:").grid(row=2, column=1)
imageDirName = Entry(root, width=50)
imageDirName.grid(row=2, column=2, columnspan=3)
selectDirButton = Button(root, width=15, text="Select Directory", command=save_Dir)
selectDirButton.grid(row=2, column=5)

Label(root, text="Save File Name").grid(row=3, column=1)
imageFileName = Entry(root, width=50)
imageFileName.grid(row=3, column=2, columnspan=3)

Label(root, text='Select the DPI').grid(row=4, column=1)
dpi_value = ttk.Combobox(
    state="readonly",
    values=["200", "300", "400", "500"],
    width=10
)
dpi_value.current(0)
dpi_value.grid(row=4, column=2, sticky='W')
Label(root, text="Gray Image :").grid(row=4, column=3)
gray_value = IntVar()
button1 = ttk.Checkbutton(root,
                          variable=gray_value,
                          onvalue=1,
                          offvalue=0)
button1.grid(row=4, column=4)

convertButton = Button(root, width=15, text="Convert", command=pdf_to_image)
convertButton.grid(row=4, column=5)

mainloop()
