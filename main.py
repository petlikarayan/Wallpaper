import requests
import ctypes
import os
import shutil

url= 'https://source.unsplash.com/collection/317099/3840x2400'
liked = -1
run = True

while run:
    with open('wallpaper.jpg', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/petli/Documents/Projects/Wallpaper/wallpaper.jpg" , 0)
    
    while True: 
        choice = input('Would you like to (k)eep, (l)ike, or (s)kip: ')
        if (choice == 'k' or choice == 'l' or choice == 's'):
            break;
        else:
            print('invalid choice')
    
    
    if (choice == 'k'):
        break;
    elif (choice == 'l'):
        if (os.path.exists('like.txt')):
            f = open('like.txt', 'r')
            liked = int(f.readline().strip())
        else:
            f = open('like.txt', 'a')
            f.write('0' +'\n')
            f.close()
            os.mkdir('Wallpapers')
        
        f = open('like.txt', 'a')
        f.write(f'[{liked + 1}] ' + str(response.url) +'\n')
        f.close()
        
        shutil.copy(os.path.join(os.getcwd(), 'wallpaper.jpg'), (os.getcwd() + "\\Wallpapers\\"))
        os.rename((os.path.join((os.getcwd() + "\\Wallpapers"), 'wallpaper.jpg')), f'{liked + 1}.jpg')
        shutil.move(f'{liked + 1}.jpg', "Wallpapers\\")
        
        with open("like.txt") as f:
            lines = f.readlines()
        lines[0] = str(liked + 1) + '\n'
        with open("like.txt", "w") as f:
            f.writelines(lines)
        
        break;
    