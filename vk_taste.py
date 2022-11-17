import vk_api
from vk_api.audio import VkAudio
import os
import re
import ffmpeg
import subprocess

def main():
    vk_session = vk_api.VkApi('89134524403', '89134524403m')

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        # Если происходит исключение во время аутентификации, то выводим ошибку и выходи
        print(error_msg)
        return

    # Модуль для получения аудиозаписей без использования официального API.
    vkaudio = VkAudio(vk_session)
    vkaudio.get_audio_by_id('90631289', 'https://cs4-8v4.vkuseraudio.net/s/v1/ac/nhCwNwMU4N0RuMPX0TZZCDeoxUc0zDhSHLUR5VD-aEAIclVoHjEikjCzlReKY3-cVXURxFRSTJle8FwgNcShZopoXTbUh7v3zBfkaCb44BuxkYXeCDhyo72TJ1iWGn4YiCYusDymP-9LwutA92HHsEFEUKJIOCifLdK5jtyrnHBAh6k/index.m3u8')
    i = 0
    for track in vkaudio.get_iter():
        print(f"Исполнитель : {track.get('artist')}")
        print(f"Название трека : {track.get('title')}")
        print(f"Ссылка на трек(url) : {track.get('url')}")
        music_name = track.get('artist') + track.get('title')
        music_name = re.sub(' ', '`', music_name)
        music_url = r'https://cs4-8v4.vkuseraudio.net/s/v1/ac/nhCwNwMU4N0RuMPX0TZZCDeoxUc0zDhSHLUR5VD-aEAIclVoHjEikjCzlReKY3-cVXURxFRSTJle8FwgNcShZopoXTbUh7v3zBfkaCb44BuxkYXeCDhyo72TJ1iWGn4YiCYusDymP-9LwutA92HHsEFEUKJIOCifLdK5jtyrnHBAh6k/index.m3u8'
        # os.system(f'ffmpeg -y -i {music_url} C:\\Users\\m.sentyabov\\Desktop\\Музыка ВК\\{music_name}.mp3')
        subprocess.run(['ffmpeg', '-i', music_url, 'track.mp3'])
        print('--------------------------------------------')
        i += 1
        if i == 10:
            break

if __name__ == '__main__':
    main()
