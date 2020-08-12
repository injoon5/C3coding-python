files = [
    'apple.jpg  20180101', 'Frozen.mp4     20140507',
    'Rough.mp3 20160305', 'LoveWhisper.mp3 20170909',
    'pizza.jpg   20120505', 'Avengers.mp4 20111225',
    'Navillera.mp3  20161005', 'Incredibles2.mp4 20180905',
    'lion.jpg 20180726', 'PacificRim.mp4   20131231'
    ] #원본파일
img = []#이마지 리스트 생성
aud = []#오디오 리스트 생성
vid = []#비디오 리스트 생성
for ord in files:#files 리스트에 있는 항목을 하나씩 ord 변수에 넣는다.
      ord = ord[0:-8].strip()#ord의 끝의 숫자 8자리를 제거하고 띄어쓰기를 제거한다.
      if ord.endswith('jpg'):#만약 jpg로 끝나면
            img.append(ord)#img 리스트에 넣는다.
      if ord.endswith('mp4'):#만약 mp4로 끝나면
            vid.append(ord)#vid 리스트에 넣는다.
      if ord.endswith('mp3'):#만약 mp3로 끝나면
            aud.append(ord)#aud 리스트에 넣는다.
print("images =",img)#리스트 출력
print("audios =",aud)#리스트 출력
print("videos =",vid)#리스트 출력

#---------------------------------------
#Coded by injoon.
#Github: https://github.com/injoon5
            
