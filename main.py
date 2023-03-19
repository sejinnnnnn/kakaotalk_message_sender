import win32api, time, win32con, win32gui

kakao_talk_list = ['19학번 공지방', '18학번 공지방', '17학번 공지방', '16학번 공지방', '15학번 공지방', '14학번 공지방', '고학번 공지방', '19년도 전편입생 공지방', '18년도 전편입생 공지방', '17년도 전편입생 공지방']

def kakao_sendtext(chatroom_name, text):
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit20W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# 친구목록 검색
def open_chatroom(chatroom_name):
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)
    SendReturn(hwndkakao_edit3)
    
def main():

    # 전달할 공지 내용 여기에 !
    text = ""

    for i in range(len(kakao_talk_list)):
        open_chatroom(kakao_talk_list[i])
        kakao_sendtext(kakao_talk_list[i], text)

if __name__ == '__main__':
    main()