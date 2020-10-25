from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QStyle

from Rare.Dialogs import InstallDialog
from Rare.utils import legendaryUtils


class GameWidget(QWidget):
    def __init__(self, game):
        super(GameWidget, self).__init__()

        self.title = game.title
        self.app_name = game.app_name
        self.version = game.version
        self.size = game.install_size
        self.launch_params = game.launch_parameters
        #self.dev =

        self.layout = QHBoxLayout()

        pixmap = QPixmap(f"../images/{game.app_name}/FinalArt.png")
        pixmap = pixmap.scaled(240, 320)
        self.image = QLabel()
        self.image.setPixmap(pixmap)
        self.layout.addWidget(self.image)

        ##Layout on the right
        self.childLayout = QVBoxLayout()

        play_icon = self.style().standardIcon(getattr(QStyle, 'SP_MediaPlay'))
        settings_icon = self.style().standardIcon(getattr(QStyle, 'SP_DirIcon'))
        self.title_widget = QLabel(f"<h1>{self.title}</h1>")
        self.launch_button = QPushButton(play_icon, "Launch")
        self.launch_button.clicked.connect(self.launch)
        self.wine_rating = QLabel("Wine Rating: " + self.get_rating())
        self.version_label = QLabel("Version: " + str(self.version))
        self.size_label = QLabel(f"Installed size: {round(self.size / (1024 ** 3), 2)} GB")
        self.settings = QPushButton(settings_icon, " Settings (Icon TODO)")

        self.childLayout.addWidget(self.title_widget)
        self.childLayout.addWidget(self.launch_button)
        self.childLayout.addWidget(self.wine_rating)
        self.childLayout.addWidget(self.version_label)
        self.childLayout.addWidget(self.size_label)
        self.childLayout.addWidget(self.settings)

        self.childLayout.addStretch(1)
        # self.layout.addWidget(QLabel(game.title))
        self.layout.addLayout(self.childLayout)
        self.setLayout(self.layout)

    def launch(self):
        print(f"launch {self.title}")
        self.launch_button.setText("Running")
        self.launch_button.setDisabled(True)
        legendaryUtils.start(self.app_name) # adding launch params #TODO

    def get_rating(self) -> str:
        return "gold"  # TODO


class UninstalledGameWidget(QWidget):
    def __init__(self, game):
        super(UninstalledGameWidget, self).__init__()
        self.title = game.app_title
        self.layout = QHBoxLayout()
        self.game = game

        self.visible = True
        pixmap = QPixmap(f"../images/{game.app_name}/UninstalledArt.png")
        pixmap = pixmap.scaled(240, 320)
        self.image = QLabel()
        self.image.setPixmap(pixmap)

        self.child_layout = QVBoxLayout()

        self.title_label = QLabel(f"<h2>{self.title}</h2>")
        self.install_button = QPushButton("Install")
        self.install_button.clicked.connect(self.install)

        self.child_layout.addWidget(self.title_label)
        self.child_layout.addWidget(self.install_button)
        self.child_layout.addStretch(1)
        self.layout.addWidget(self.image)
        self.layout.addLayout(self.child_layout)

        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def install(self):
        print("install " + self.title)
        #TODO
        # dialog = InstallDialog(self.game)