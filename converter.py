from PIL import Image
import os

in_fmt = ('.tga',',png','.ppm','.jpeg','.tiff','.bmp','.jpg')
out_fmt = '.tga'
def make_resized_images_large_done(flag_dic, medium_dic, small_dic, in_fmt, out_fmt):
    medium = (41, 26)
    small = (10, 7)
    os.chdir(medium_dic)
    print('Converting medium sized flags...')
    for filename in os.listdir(flag_dic):
        if filename.endswith(in_fmt):
            print('Moving ' + filename + ' to ' + medium_dic)
            Image.open(flag_dic + '\\' +  filename).save(filename[:filename.index('.')] + out_fmt, compression = None )
    for filename in os.listdir(medium_dic):
        print('Resizing ' + filename + ' to medium size')
        Image.open(filename).resize(medium).save(filename,compression = None )
    print('Converting small sized flags...')
    os.chdir(small_dic)
    for filename in os.listdir(medium_dic):
        if filename.endswith(out_fmt):
            print('Moving ' + filename + ' to ' + small_dic)
            Image.open(medium_dic + '\\' +  filename).save(filename,compression = None)
    for filename in os.listdir(small_dic):
        print('Resizing ' + filename + ' to small size')
        Image.open(filename).resize(small).save(filename,compression = None)
    done = input('Done! Press ENTER to exit.')

def make_resized_images(flag_dic, large_dic, medium_dic, small_dic, in_fmt, out_fmt):
    large = (82, 52)
    medium = (41, 26)
    small = (10, 7)
    os.chdir(large_dic)
    print('Converting standard sized flags...')
    for filename in os.listdir(flag_dic):
        if filename.endswith(in_fmt):
            print('Moving ' + filename + ' to ' + large_dic)
            Image.open(flag_dic + '\\' +  filename).save(filename[:filename.index('.')] + out_fmt,compression = None)
    for filename in os.listdir(large_dic):
        print('Resizing ' + filename + ' to standard size')
        Image.open(filename).resize(large).save(filename,compression = None)
    print('Converting medium sized flags...')
    os.chdir(medium_dic)
    for filename in os.listdir(large_dic):
        if filename.endswith(in_fmt):
            print('Moving ' + filename + ' to ' + medium_dic)
            Image.open(large_dic + '\\' +  filename).save(filename,compression = None)
    for filename in os.listdir(medium_dic):
        print('Resizing ' + filename + ' to medium size')
        Image.open(filename).resize(medium).save(filename,compression = None)
    print('Converting small sized flags...')
    os.chdir(small_dic)
    for filename in os.listdir(medium_dic):
        if filename.endswith(out_fmt):
            print('Moving ' + filename + ' to ' + small_dic)
            Image.open(medium_dic + '\\' +  filename).save(filename,compression = None)
    for filename in os.listdir(small_dic):
        print('Resizing ' + filename + ' to small size')
        Image.open(filename).resize(small).save(filename,compression = None)
    done = input('Done! Press ENTER to exit.')
    

def main():
    can_code = input('Have you edited the parameters in the .py file already? Answer \"Y\" for yes or \"N\" for no\n')
    if can_code.lower().startswith('y'):
        main_for_people_who_code()
    else:
        print('It is really important that you follow instructions EXACTLY or it will mess up the code.\nYou should have already named all your flags in the correct format (for example AFG_communism, JAP_fascism, ZIM_democractic).\nAll your flags should be in \".tga\", \",png\", \".ppm\", \".jpeg\", \".tiff\", \".bmp\", or  \".jpg\" formats.\nThe dictortory should ONLY contain the flag files')
        large_done = input('Have you already converted the flags to 82x52 resolution .tga files? Answer \"Y\" for yes or \"N\" for no.\n')
        if large_done.lower().startswith('y'):
            flag_dic = input('Enter the directory the flag files.\n')
            medium_dic = input('Enter the directory you want the medium size flags to be placed in\n')
            small_dic = input('Enter the directory you want the small size flags to be placed in\n')
            make_resized_images_large_done(flag_dic, medium_dic, small_dic, in_fmt, out_fmt)
        else:
            flag_dic = input('Enter the directory the flag files.\n')
            large_dic = input('Enter the directory you want the standard size flags to be placed in\n')
            medium_dic = input('Enter the directory you want the medium size flags to be placed in\n')
            small_dic = input('Enter the directory you want the small size flags to be placed in\n')
            make_resized_images(flag_dic, large_dic, medium_dic, small_dic, in_fmt, out_fmt)

def main_for_people_who_code():
    large_done = False
    flag_dic = 'D:\Documents\hoi4 flags'
    large_dic = 'D:\Documents\hoi4 flags\standard'
    medium_dic = 'D:\Documents\hoi4 flags\medium'
    small_dic = 'D:\Documents\hoi4 flags\small'
    if large_done:
        make_resized_images_large_done(flag_dic, medium_dic, small_dic, in_fmt, out_fmt)
    else:
        make_resized_images(flag_dic, large_dic, medium_dic, small_dic, in_fmt, out_fmt)
        
main()
