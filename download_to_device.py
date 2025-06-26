import os, re, datetime, csv, zipfile
from file_methods.csv_file_methods import find_csv_file_location
from file_methods.csv_file_methods import extract_csv_content

def download_file(file_to_download = None):
  # print("file_to_download: ", file_to_download)

  if file_to_download == None:
    print("Nothing has been passed into the file_to_download variable. \nThus, downloading csv file :)")
    file_to_download = find_csv_file_location()
    only_file_name = (((file_to_download.strip('C:')).split('/')[-1]).split('\\')[-1]).split('\\\\')[-1]
    extension = 'csv'

  else: # something has been passed into the file_to_download variable
    only_file_name = (((file_to_download.strip('C:')).split('/')[-1]).split('\\')[-1]).split('\\\\')[-1]

    exists = False

    curr_dir = os.getcwd()
    for folders, _, files in os.walk(curr_dir):
      for file in files:
        if file == only_file_name:
          exists = True
          # print("FILE FOUND!")
          break
      if exists == True:
        break

    if exists == False:
      print("Cannot download file as it doesn't exist :(")
      print("Thus, downloading csv file :)")
      only_file_name = find_csv_file_location()
      extension = 'csv'

    try:
      extension = re.search(r'\.([^.]+)$', only_file_name).group(1)
    except:
      print("Cannot download file as it is not a csv or py :(")
      print("Thus, downloading csv file :)")
      only_file_name = find_csv_file_location()
      extension = 'csv'

  # find downloads folder
  downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
  if os.path.isdir(downloads_path):
    pass
  else:
    # make our own path
    os.makedirs(os.path.join(os.path.expanduser("~"), "Downloads"), exist_ok=True)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

  print(f"\nDownloading .{extension} file now...")

  todai = datetime.datetime.today()
  rn = f"{todai.day}-{todai.month}-{todai.year}_{todai.hour}-{todai.minute}-{todai.second}"

  # for csv only
  file_name_in_downloads = f"Transactions_To_Date_{rn}.{extension}"
  path_to_file_in_downloads = os.path.join(downloads_path, file_name_in_downloads)

  if extension == 'csv':
    #extract csv content first
    fp_for_extraction = os.path.join('./saved_files/', only_file_name)

    data_lines = extract_csv_content(fp_for_extraction)

    f = open(path_to_file_in_downloads, mode='w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_lines)
    f.close()

    print(f"\nDownload of file: {file_name_in_downloads} complete! Check your downloads folder :)")

  else: # if extension == 'py'
    zipper_file_name = f"zippy_{rn}.zip"

    # finding full path
    ful_pat = only_file_name
    for folders, _, files in os.walk(os.getcwd()):
      for file in files:
        if file == only_file_name:
          ful_pat = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
          break
      if ful_pat != only_file_name:
        break

    zippy = zipfile.ZipFile(zipper_file_name, 'w')
    zippy.write(ful_pat, arcname=os.path.basename(ful_pat), compress_type = zipfile.ZIP_DEFLATED)
    zippy.close()

    unzippy = zipfile.ZipFile(zipper_file_name, 'r')
    unzippy.extractall(path = downloads_path)
    unzippy.close()

    print(f"\nDownload of file: {only_file_name} complete! Check your downloads folder :)")

  # deletion of zip files
  curr_dir = os.getcwd()

  for folders, _, files in os.walk(curr_dir):
    for file in files:
      if re.search(r'^zippy_', file):
        os.remove(os.path.join(folders, file))

if __name__ == "__main__":
  # line_demarcator = "\n{}\n".format("~" * 120)

  download_file()
  # print(line_demarcator)

  # download_file("tbh")
  # print(line_demarcator)

  # download_file("tbh.py")
  # print(line_demarcator)

  # download_file("tbh.csv")
  # print(line_demarcator)

  # download_file("csv_26_06_2025_3_48_10.csv")
  # print(line_demarcator)

  # print(line_demarcator)

  # download_file("/Users/rakshita/dev/rakshita/finance-tracker/file_methods/csv_file_methods.py")
  # print(line_demarcator)

  # download_file("main_interface.py")
  # print(line_demarcator)

  # download_file(r"C:\\Users\\Public\\Documents")
  # print(line_demarcator)
