from PySide2.QtCore import QTimer, QRect, QEvent
from UI.ui_tikplayer import *
import os
import sys
from pathlib import Path
import time
from client import *
import vlc

from vlc import EventType

class VideoWidget(QWidget):
    def __init__(self, video_path, title, width, height, parent=None):
        super().__init__()
        
        self.ui= Ui_VideoWidget()
        self.ui.setupUi(self, width, height)
        self.video_path = video_path
        self.client = APIClient()
        self.title = title
        self.width = width
        self.height = height
       
        
        self.ui.label.setScaledContents(True)
        if not Path(f"images/thumbnail/{self.title}{self.width}x{self.height}.png").exists():
            pix = self.client.get_thumbnail(self.title, self.width, self.height)
        else:
            pix = QPixmap(f"images/thumbnail/{self.title}{self.width}x{self.height}.png")
        
        if  not Path(self.video_path).exists():
            self.client.get_video_data(self.title)
            print("## Video PATH : ", Path(self.video_path))
            
       
        
     
        # Video with VLC libr
   
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()
        self.vlc_player.set_hwnd(self.ui.label.winId())   
        
        # VLC Event Manager
        self.event_manager = self.vlc_player.event_manager()
        # event_manager.event_attach(vlc.EventType.MediaParsedChanged, self.on_media_parsed_changed)
        # event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged, self.set_slider_value)
        
        self.event_manager.event_attach(vlc.EventType.MediaParsedChanged, self.on_media_parsed_changed)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged, self.update_time_label)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerPositionChanged, self.update_slider)
        self.event_manager.event_attach(EventType.MediaPlayerEndReached, self.video_ended)
        
        self.vlc_player.video_set_scale(0)
        self.vlc_player.video_set_mouse_input(True)
        self.vlc_player.video_set_key_input(False)
        self.media = self.vlc_instance.media_new(self.video_path)
        self.media.parse_with_options(vlc.MediaParseFlag.network, 1000)
        self.vlc_player.set_media(self.media)
        
        
    
        time.sleep(2)
        
        
         # self.ui.controlWidget.hide()
        self.setMouseTracking(True)
        self.ui.label.setMouseTracking(True)
        # self.installEventFilter(self)

       
        # self.ui.label.enterEvent = self.on_mouse_enter
        # self.ui.label.leaveEvent = self.on_mouse_leave
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(100)
        
        # # # Connect signals and slots
        # self.ui.label.enterEvent = self.showWidget
        # self.ui.label.leaveEvent = self.hideWidget
        
        
        
        snap = self.vlc_player.video_take_snapshot(0, 'C://Users/sassi/py_projects/ikarma-dev/snap.png', 212, 380)
        print('snap taken : ', snap)
        
        
        # Get the size of the QLabel widget
        label_size = self.ui.label.size()
        print('label size: ', label_size)
        label_ratio = label_size.width() / label_size.height()
        print("label Ration: ", label_ratio)


        # Get the size of the video
        video_size = self.vlc_player.video_get_size()
        print('video size : ',video_size)
        parsed = self.media.get_parsed_status()
        print('Parsed one: ', parsed)
        
        
        
        # Calculate the aspect ratio of the video
        video_aspect_ratio = video_size[0] / video_size[1]
        print('video ration : ', video_aspect_ratio)
        
        # Calculate the scale factor to fit the video in the QLabel widget while maintaining aspect ratio
        if label_ratio < video_aspect_ratio:
            scale_factor = label_size.width() / video_size[0]
        else:
            scale_factor = label_size.height() / video_size[1]

        # Set the scale factor for the video
        print('scale factor : ', scale_factor)
        
        # pim = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor)
        self.ui.label.setPixmap(pix)
        
        self.vlc_player.video_set_scale(scale_factor)
        
        
        print(self.vlc_player.get_position())
        print('###################################')
        print('video length: ', self.media.get_duration())
        self.video_duration = time.strftime('%M:%S', time.gmtime(self.media.get_duration()/1000))
        current_video_time = time.strftime('%M:%S', time.gmtime(self.vlc_player.get_time()/1000))
        self.ui.timeLabel.setText(f'00:00:{ self.video_duration}')
        print('media tracks: ', self.media.tracks_get().__dir__)
        ar = self.vlc_player.video_get_aspect_ratio()
        time_cu = self.vlc_player.get_time()
        print('Atime : ',time_cu)
        
        
        
        
       
        
        # # Set up the position slider
        # self.ui.QSlider.setRange(0, 100)
        # self.ui.QSlider.setValue(0)
        # self.ui.QSlider.valueChanged.connect(self.set_slider_position)
        
        
        self.vlc_player.audio_set_mute(True)
        
        
        ## Connect signals and slots
        self.ui.playButton.clicked.connect(self.play_stop)
        self.ui.QSlider.sliderMoved.connect(self.set_position)
        self.ui.soundButton.clicked.connect(self.toogleMute)
        
        
############################################################################################################
## Player Contole Methods
###########################################################################################################

    # def eventFilter(self, source, event):
    #     if source is self and event.type() == QEvent.MouseMove:
    #         mouse_pos = event.globalPos()
    #         print(f"Mouse position: ({mouse_pos.x()}, {mouse_pos.y()})")
    #         # Forward the mouse move event to the controlWidget
    #         mouse_event = QMouseEvent(event.type(), event.localPos(), event.windowPos(), event.screenPos(),
    #                                    event.button(), event.buttons(), event.modifiers())
    #         QApplication.sendEvent(self.ui.controlWidget, mouse_event)

    #     return super().eventFilter(source, event)

    def toogleMute(self):
        if self.vlc_player.audio_get_mute():
            self.vlc_player.audio_set_mute(False)
            self.ui.soundButton.setIcon(QIcon(u"icons/feather/volume-2.svg"))
            
        else:
            self.vlc_player.audio_set_mute(True)
            self.ui.soundButton.setIcon(QIcon(u"icons/feather/volume-x.svg"))
                


    def set_position(self, value):
        pos = value / 100
        print('current position :', pos)
        self.vlc_player.set_position(pos)
        
    def update_slider(self, event):
        position = self.vlc_player.get_position() * 100
        # print('position slider: ',position)
        self.ui.QSlider.setValue(position)

    def update_time_label(self, event):
        time_in_ms = self.vlc_player.get_time()
        duration_in_ms = self.vlc_player.get_length()
        video_time = time.strftime('%M:%S', time.gmtime(self.media.get_duration()/1000))
        video_current_time = time.strftime('%M:%S', time.gmtime(self.vlc_player.get_time()/1000))
        # print('timing here: ',self.vlc_player.get_time()/1000)
        if self.vlc_player.get_state() == vlc.State.Ended:
            self.ui.timeLabel.setText(f'{video_time}:{video_time}')
            
        self.ui.timeLabel.setText(f'{video_current_time}:{video_time}')
            
        

    def video_ended(self, event):
        # This function will be called when the video playback has ended
        self.ui.playButton.setIcon(QIcon(u"icons/feather/rotate-ccw.svg"))
        self.ui.QSlider.setValue(100)
        self.ui.timeLabel.setText(f'{self.video_duration}:{self.video_duration}')
        

    def update_slider_position(self):
        # Get the current position of the media player
        pos = self.vlc_player.get_position()
        if pos is not None:
            # Convert position to integer between 0 and maximum value of slider
            slider_pos = int(pos * self.ui.QSlider.maximum())
            # Update slider position
            self.ui.QSlider.setValue(slider_pos)

  
    
    def check_mouse_position(self):
        label_pos = self.ui.label.mapToGlobal(self.ui.label.pos())
        label_rect = QRect(label_pos, self.ui.label.size())
        mouse_pos = QCursor.pos()
        if label_rect.contains(mouse_pos) or self.underMouse():
            self.ui.controlWidget.show()
        else:
            self.ui.controlWidget.hide()
        
       
        
    def set_slider_position(self):
        pos = self.ui.QSlider.value() / self.ui.QSlider.maximum()
        self.vlc_player.set_position(pos)


    def play_stop(self):
        if self.vlc_player.is_playing():
            self.vlc_player.pause()
            self.ui.playButton.setIcon(QIcon(u"icons/feather/play.svg"))
        else:
            if self.vlc_player.get_state() == vlc.State.Ended:
                self.vlc_player.stop()
                self.media = self.vlc_instance.media_new(self.video_path)
                self.vlc_player.set_media(self.media)
            # self.video_player.resume()
            self.vlc_player.play()
            
            self.ui.playButton.setIcon(QIcon(u"icons/feather/pause.svg"))
            
            
    def on_media_parsed_changed(self, event):
        # Get the size of the video
        video_width, video_height = self.vlc_player.video_get_size()
        
        # Get the size of the QLabel
        label_width, label_height = self.ui.label.width(), self.ui.label.height()
        
        # Calculate the scale factor
        width_scale_factor = label_width / video_width
        height_scale_factor = label_height / video_height
        scale_factor = min(width_scale_factor, height_scale_factor)
        
        # Set the scale factor of the video
        self.vlc_player.video_set_scale(scale_factor)

    def closeEvent(self, event):
        self.vlc_player.stop()
        time.sleep(0.10)
        # Path(self.video_path).unlink(missing_ok=True)
