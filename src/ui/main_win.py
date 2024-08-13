from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.metrics import dp

class ModernKivyApp(App):
    def build(self):
        # 메인 레이아웃
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))

        # 버튼 생성
        self.button = Button(
            text="Start Progress",
            size_hint=(None, None),
            size=(dp(200), dp(50)),  # DP 단위로 크기 설정
            pos_hint={'center_x': 0.5},
            background_color=(0.3, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            font_size=dp(18)  # DP 단위로 폰트 크기 설정
        )
        self.button.bind(on_press=self.start_progress)
        layout.add_widget(self.button)

        # 프로그레스 바 생성
        self.progress_bar = ProgressBar(max=100, value=0, size_hint_y=None, height=dp(20))
        layout.add_widget(self.progress_bar)

        return layout

    def start_progress(self, instance):
        self.button.disabled = True  # 진행 중에는 버튼 비활성화
        self.progress_bar.value = 0
        Clock.schedule_interval(self.update_progress, 0.05)  # 50ms 마다 update_progress 호출

    def update_progress(self, dt):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 1
            return True
        else:
            self.button.disabled = False  # 진행 완료 후 버튼 다시 활성화
            return False  # 인터벌 정지

if __name__ == '__main__':
    ModernKivyApp().run()
