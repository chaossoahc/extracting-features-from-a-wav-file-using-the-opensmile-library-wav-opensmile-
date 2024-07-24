import opensmile
import PySimpleGUI as sg
sg.theme('Dark Grey 13')

layout = [[sg.Text('Выберите аудио фаил в формате WAW')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()
# чтение файла 


i=0
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков ComParE_2016')
smile_ComParE_2016 = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y_feature_set_ComParE_2016 = smile_ComParE_2016.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков GeMAPSv01a')
smile_GeMAPSv01a = opensmile.Smile(
    feature_set=opensmile.FeatureSet.GeMAPSv01a,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)

y2_feature_set_GeMAPSv01a = smile_GeMAPSv01a.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков GeMAPSv01b')
smile_GeMAPSv01b = opensmile.Smile(
feature_set=opensmile.FeatureSet.GeMAPSv01b,
feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y3_feature_set_GeMAPSv01b = smile_GeMAPSv01b.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков eGeMAPSv01a')
smile_eGeMAPSv01a = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv01a,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y4_feature_set_eGeMAPSv01a = smile_eGeMAPSv01a.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков eGeMAPSv01b')
smile_eGeMAPSv01b = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv01b,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y5_feature_set_eGeMAPSv01b = smile_eGeMAPSv01b.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков eGeMAPSv02')
smile_eGeMAPSv02 = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y6_feature_set_eGeMAPSv02 = smile_eGeMAPSv02.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'Прогресс','Извлечения признаков emobase')
smile_emobase = opensmile.Smile(
    feature_set=opensmile.FeatureSet.emobase,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
y7_feature_set_emobase = smile_emobase.process_file(values[0])
i = i+1
sg.one_line_progress_meter('Обработка', i, 7, 'прогресс','Готово')


sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Rename files or folders')],
      [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
      [sg.Text('Source for Files ', size=(15, 1)), sg.InputText()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('Rename Files or Folders', layout)

event, values = window.read()
window.close()
folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
kh=0
fin = 14
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков ComParE_2016')
y_feature_set_ComParE_2016.to_csv(r''+folder_path+"/"+file_path+'y_feature_set_ComParE_2016.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков GeMAPSv01a')
y2_feature_set_GeMAPSv01a.to_csv(r''+folder_path+"/"+file_path+'y2_feature_set_GeMAPSv01a.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков GeMAPSv01b')
y3_feature_set_GeMAPSv01b.to_csv(r''+folder_path+"/"+file_path+'y3_feature_set_GeMAPSv01b.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv01a')
y4_feature_set_eGeMAPSv01a.to_csv(r''+folder_path+"/"+file_path+'y4_feature_set_eGeMAPSv01a.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv01b')
y5_feature_set_eGeMAPSv01b.to_csv(r''+folder_path+"/"+file_path+'y5_feature_set_eGeMAPSv01b.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv02')
y6_feature_set_eGeMAPSv02.to_csv(r''+folder_path+"/"+file_path+'y6_feature_set_eGeMAPSv02.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков emobase')
y7_feature_set_emobase.to_csv(r''+folder_path+"/"+file_path+'y7_feature_set_emobase.txt', header=True, index=None, sep=',', mode='a')
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков ComParE_2016')
y_feature_set_ComParE_2016.to_csv(folder_path+"/"+file_path+"y_feature_set_ComParE_2016.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков GeMAPSv01a')
y2_feature_set_GeMAPSv01a.to_csv(folder_path+"/"+file_path+"y2_feature_set_GeMAPSv01a.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков GeMAPSv01b')
y3_feature_set_GeMAPSv01b.to_csv(folder_path+"/"+file_path+"y3_feature_set_GeMAPSv01b.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv01a')
y4_feature_set_eGeMAPSv01a.to_csv(folder_path+"/"+file_path+"y4_feature_set_eGeMAPSv01a.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv01b')
y5_feature_set_eGeMAPSv01b.to_csv(folder_path+"/"+file_path+"y5_feature_set_eGeMAPSv01b.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков eGeMAPSv02')
y6_feature_set_eGeMAPSv02.to_csv(folder_path+"/"+file_path+"y6_feature_set_eGeMAPSv02.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков emobase')
y7_feature_set_emobase.to_csv(folder_path+"/"+file_path+"y7_feature_set_emobase.csv")
kh=kh+1
sg.one_line_progress_meter('Обработка', kh, fin, 'Прогресс','сохранение признаков emobase')

sg.popup('Процесс завершен!', 'Программа будет закрыта')