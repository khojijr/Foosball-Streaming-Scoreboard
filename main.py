from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from foldercreator import FolderCreator

class MyGrid(GridLayout):
    """ STREAM SCOREBOARD SOFTWARE
        UPDATES TO MAKE:
            STREAM DECK IMPLEMENTATION"""

    """ ***** TEAM ROW VARIABLES ***** """
    team_one_name = ""
    team_two_name = ""

    """ ***** SCORE ROW VARIABLES ***** """
    team_one_score = 0
    team_two_score = 0

    """ ***** TIMEOUT ROW VARIABLES ***** """
    team_one_timeout = 2
    team_two_timeout = 2

    """ ***** GAME ROW VARIABLES ***** """
    team_one_game = 0
    team_two_game = 0

    """ ***** MATCH INFORMATION ROW VARIABLES ***** """
    tournament = ""
    game_number = ""
    round_number = ""

    """ ***** MISC ROW VARIABLES ***** """
    misc_one = ""
    misc_two = ""
    misc_three = ""
    misc_four = ""

    """ ***** TEAM ROW FUNCTIONS ***** """

    def switch_team(self, *args):
        self.team_one_name = self.team_one_name_display.text
        self.team_two_name = self.team_two_name_display.text

        copy_name_one = self.team_one_name
        copy_name_two = self.team_two_name

        self.team_one_name = copy_name_two
        self.team_two_name = copy_name_one

        self.team_one_name_display.text = copy_name_two
        self.team_two_name_display.text = copy_name_one

        f = open("Files\\t1name.txt", "w+")
        f.write(self.team_one_name)
        f.close()

        f = open("Files\\t2name.txt", "w+")
        f.write(self.team_two_name)
        f.close()

    def switch_team_one_position(self, *args):
        self.team_one_name = self.team_one_name_display.text

        copy_name_one = self.team_one_name

        if '\n' in copy_name_one:
            team_one_separate = copy_name_one.splitlines()
            self.team_one_name = team_one_separate[1] + '\n' + team_one_separate[0]

        self.team_one_name_display.text = self.team_one_name

        f = open("Files\\t1name.txt", "w+")
        f.write(self.team_one_name)
        f.close()

    def switch_team_two_position(self, *args):
        self.team_two_name = self.team_two_name_display.text

        copy_name_two = self.team_two_name

        if '\n' in copy_name_two:
            team_two_separate = copy_name_two.splitlines()
            self.team_two_name = team_two_separate[1] + '\n' + team_two_separate[0]

        self.team_two_name_display.text = self.team_two_name

        f = open("Files\\t2name.txt", "w+")
        f.write(self.team_two_name)
        f.close()

    """ ***** SCORE ROW FUNCTIONS ***** """

    def add_team_one_score(self, *args):
        self.team_one_score += 1
        self.team_one_score_display.text = str(self.team_one_score)
        f = open("Files\\t1score.txt", "w+")
        f.write(str(self.team_one_score))
        f.close()

    def subtract_team_one_score(self, *args):
        if self.team_one_score != 0:
            self.team_one_score -= 1
            self.team_one_score_display.text = str(self.team_one_score)
        f = open("Files\\t1score.txt", "w+")
        f.write(str(self.team_one_score))
        f.close()

    def add_team_two_score(self, *args):
        self.team_two_score += 1
        self.team_two_score_display.text = str(self.team_two_score)
        f = open("Files\\t2score.txt", "w+")
        f.write(str(self.team_two_score))
        f.close()

    def subtract_team_two_score(self, *args):
        if self.team_two_score != 0:
            self.team_two_score -= 1
            self.team_two_score_display.text = str(self.team_two_score)
        f = open("Files\\t2score.txt", "w+")
        f.write(str(self.team_two_score))
        f.close()

    def reset_score(self, *args):
        self.team_one_score = 0
        self.team_two_score = 0
        self.team_one_score_display.text = "0"
        self.team_two_score_display.text = "0"
        f = open("Files\\t1score.txt", "w+")
        f.write("0")
        f.close()
        f = open("Files\\t2score.txt", "w+")
        f.write("0")
        f.close()

    """ ***** TIMEOUT ROW FUNCTIONS ***** """

    def subtract_team_one_timeout(self, *args):
        if self.team_one_timeout != 0:
            self.team_one_timeout -= 1
            self.team_one_timeout_display.text = str(self.team_one_timeout)
        f = open("Files\\t1TO.txt", "w+")
        f.write(str(self.team_one_timeout))
        f.close()

    def subtract_team_two_timeout(self, *args):
        if self.team_two_timeout != 0:
            self.team_two_timeout -= 1
            self.team_two_timeout_display.text = str(self.team_two_timeout)
        f = open("Files\\t2TO.txt", "w+")
        f.write(str(self.team_two_timeout))
        f.close()

    def reset_timeout(self, *args):
        self.team_one_timeout = 2
        self.team_two_timeout = 2
        self.team_one_timeout_display.text = "2"
        self.team_two_timeout_display.text = "2"
        f = open("Files\\t1TO.txt", "w+")
        f.write("2")
        f.close()
        f = open("Files\\t2TO.txt", "w+")
        f.write("2")
        f.close()

    """ ***** GAME ROW FUNCTIONS ***** """

    def add_team_one_game(self, *args):
        self.team_one_game += 1
        self.team_one_game_display.text = str(self.team_one_game)
        f = open("Files\\t1games.txt", "w+")
        f.write(str(self.team_one_game))
        f.close()

    def add_team_two_game(self, *args):
        self.team_two_game += 1
        self.team_two_game_display.text = str(self.team_two_game)
        f = open("Files\\t2games.txt", "w+")
        f.write(str(self.team_two_game))
        f.close()

    def reset_game(self, *args):
        self.team_one_game = 0
        self.team_two_game = 0
        self.team_one_game_display.text = "0"
        self.team_two_game_display.text = "0"
        f = open("Files\\t1games.txt", "w+")
        f.write("0")
        f.close()
        f = open("Files\\t2games.txt", "w+")
        f.write("0")
        f.close()

    """ ***** MATCH INFORMATION ROW FUNCTIONS ***** """

    def game_num(self, game, *args):
        self.game_number = game
        f = open("Files\\game_number.txt", "w+")
        f.write(game)
        f.close()

    def round_num(self, round, *args):
        self.round_number = round
        f = open("Files\\round.txt", "w+")
        f.write(round)
        f.close()

    """ ***** UPDATE ROW FUNCTIONS ***** """

    def update_all(self, *args):
        # Team 1 Name
        self.team_one_name = self.team_one_name_display.text
        f = open("Files\\t1name.txt", "w+")
        f.write(self.team_one_name)
        f.close()

        # Team 2 Name
        self.team_two_name = self.team_two_name_display.text
        f = open("Files\\t2name.txt", "w+")
        f.write(self.team_two_name)
        f.close()

        # Misc 1
        self.misc_one = self.misc_one_display.text
        f = open("Files\\misc1.txt", "w+")
        f.write(self.misc_one)
        f.close()

        # Misc 2
        self.misc_two = self.misc_two_display.text
        f = open("Files\\misc2.txt", "w+")
        f.write(self.misc_two)
        f.close()

        # Misc 3
        self.misc_three = self.misc_three_display.text
        f = open("Files\\misc3.txt", "w+")
        f.write(self.misc_three)
        f.close()

        # Misc 4
        self.misc_four = self.misc_four_display.text
        f = open("Files\\misc4.txt", "w+")
        f.write(self.misc_four)
        f.close()

    """ ***** RESET ROW FUNCTIONS ***** """

    def reset_players(self, *args):
        self.team_one_name = ""
        self.team_two_name = ""

        self.team_one_name_display.text = ""
        self.team_two_name_display.text = ""

        f = open("Files\\t1name.txt", "w+")
        f.write(self.team_one_name)
        f.close()

        f = open("Files\\t2name.txt", "w+")
        f.write(self.team_two_name)
        f.close()

    def reset_misc(self, *args):
        self.misc_one = ""
        self.misc_two = ""
        self.misc_three = ""
        self.misc_four = ""

        self.misc_one_display.text = ""
        self.misc_two_display.text = ""
        self.misc_three_display.text = ""
        self.misc_four_display.text = ""

        f = open("Files\\misc1.txt", "w+")
        f.write(self.misc_one)
        f.close()

        f = open("Files\\misc2.txt", "w+")
        f.write(self.misc_two)
        f.close()

        f = open("Files\\misc3.txt", "w+")
        f.write(self.misc_three)
        f.close()

        f = open("Files\\misc4.txt", "w+")
        f.write(self.misc_four)
        f.close()

    def reset_game_number(self, *args):
        self.game_dropdown.select("Game Number")
        self.game_number = ""
        f = open("Files\\game_number.txt", "w+")
        f.write("")
        f.close()

    def reset_round(self, *args):
        self.round_dropdown.select("Round Number")
        self.round_number = ""
        f = open("Files\\round.txt", "w+")
        f.write("")
        f.close()

    def reset_all(self, *args):
        self.reset_players()
        self.reset_score()
        self.reset_timeout()
        self.reset_game()
        self.reset_misc()
        self.reset_game_number()
        self.reset_round()

    def reset_new_game(self, *args):
        self.reset_score()
        self.reset_timeout()

    def reset_new_match(self, *args):
        self.reset_players()
        self.reset_score()
        self.reset_timeout()
        self.reset_game()
        self.reset_game_number()
        self.reset_round()

    def __init__(self, **kwargs):
        # Initialize Scoreboard Grid
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        Window.size = (645, 355)
        self.row_default_height = Window.height / 12

        """ ***** TEAM ROW ***** """
        self.team_row = GridLayout()
        self.team_row.cols = 7

        # Team 1
        self.team_row.add_widget(Label(text="Team 1 Name", font_size=12, padding_y=15))
        self.team_one_name_display = TextInput(multiline=True, font_size=10)
        self.team_row.add_widget(self.team_one_name_display)

        # Switches
        self.switch_positions = Button(text="Switch positions", font_size=11)
        self.switch_positions.bind(on_press=self.switch_team_one_position)
        self.team_row.add_widget(self.switch_positions)
        self.switch_teams = Button(text="Switch sides", font_size=12)
        self.switch_teams.bind(on_press=self.switch_team)
        self.team_row.add_widget(self.switch_teams)
        self.switch_positions = Button(text="Switch positions", font_size=11)
        self.switch_positions.bind(on_press=self.switch_team_two_position)
        self.team_row.add_widget(self.switch_positions)

        # Team 2
        self.team_two_name_display = TextInput(multiline=True, font_size=10)
        self.team_row.add_widget(self.team_two_name_display)
        self.team_row.add_widget(Label(text="Team 2 Name", font_size=12))

        # Add Team Row
        self.add_widget(self.team_row)

        """ ***** SCORE ROW ***** """
        self.score_row = GridLayout()
        self.score_row.cols = 7

        # Team 1 Score
        self.minus_team_one_score = Button(text="-", font_size=40)
        self.minus_team_one_score.bind(on_press=self.subtract_team_one_score)
        self.score_row.add_widget(self.minus_team_one_score)
        self.team_one_score_display = Label(text="0", font_size=40)
        self.score_row.add_widget(self.team_one_score_display)
        self.plus_team_one_score = Button(text="+", font_size=40)
        self.plus_team_one_score.bind(on_press=self.add_team_one_score)
        self.score_row.add_widget(self.plus_team_one_score)

        # Reset Score
        self.reset_team_score = Button(text="Reset Score", font_size=14)
        self.reset_team_score.bind(on_press=self.reset_score)
        self.score_row.add_widget(self.reset_team_score)

        # Team 2 Score
        self.minus_team_two_score = Button(text="-", font_size=40)
        self.minus_team_two_score.bind(on_press=self.subtract_team_two_score)
        self.score_row.add_widget(self.minus_team_two_score)
        self.team_two_score_display = Label(text="0", font_size=40)
        self.score_row.add_widget(self.team_two_score_display)
        self.plus_team_two_score = Button(text="+", font_size=40)
        self.plus_team_two_score.bind(on_press=self.add_team_two_score)
        self.score_row.add_widget(self.plus_team_two_score)

        # Add Score Row
        self.add_widget(self.score_row)

        """ ***** TIMEOUT ROW ***** """
        self.timeout_row = GridLayout()
        self.timeout_row.cols = 5

        # Team 1 Time Outs
        self.minus_team_one_timeout = Button(text="-", font_size=40, size_hint_x=.67)
        self.minus_team_one_timeout.bind(on_press=self.subtract_team_one_timeout)
        self.timeout_row.add_widget(self.minus_team_one_timeout)
        self.team_one_timeout_display = Label(text="2", font_size=40, size_hint_x=.67)
        self.timeout_row.add_widget(self.team_one_timeout_display)

        # Reset Time Outs
        self.reset_team_timeout = Button(text="Reset Time Outs", font_size=14, size_hint_x=2)
        self.reset_team_timeout.bind(on_press=self.reset_timeout)
        self.timeout_row.add_widget(self.reset_team_timeout)

        # Team 2 Time Outs
        self.team_two_timeout_display = Label(text="2", font_size=40, size_hint_x=.67)
        self.timeout_row.add_widget(self.team_two_timeout_display)
        self.minus_team_two_timeout = Button(text="-", font_size=40, size_hint_x=.67)
        self.minus_team_two_timeout.bind(on_press=self.subtract_team_two_timeout)
        self.timeout_row.add_widget(self.minus_team_two_timeout)

        # Add Timeout Row
        self.add_widget(self.timeout_row)

        """ ***** GAME ROW ***** """
        self.game_row = GridLayout()
        self.game_row.cols = 5

        # Team 1 Game Count
        self.plus_team_one_game = Button(text="+", font_size=40, size_hint_x=.67)
        self.plus_team_one_game.bind(on_press=self.add_team_one_game)
        self.game_row.add_widget(self.plus_team_one_game)
        self.team_one_game_display = Label(text="0", font_size=40, size_hint_x=.67)
        self.game_row.add_widget(self.team_one_game_display)
        # Reset Game Count
        self.reset_game_count = Button(text="Reset Game Count", font_size=14, size_hint_x=2)
        self.reset_game_count.bind(on_press=self.reset_game)
        self.game_row.add_widget(self.reset_game_count)
        # Team 2 Game Count
        self.team_two_game_display = Label(text="0", font_size=40, size_hint_x=.67)
        self.game_row.add_widget(self.team_two_game_display)
        self.plus_team_two_game = Button(text="+", font_size=40, size_hint_x=.67)
        self.plus_team_two_game.bind(on_press=self.add_team_two_game)
        self.game_row.add_widget(self.plus_team_two_game)

        # Add Game Row
        self.add_widget(self.game_row)

        """ ***** MATCH INFORMATION ROW ***** """
        self.match_info_row = GridLayout()
        self.match_info_row.cols = 2

        # Game Number
        self.game_dropdown = DropDown()
        f = open("Configs\\games.txt", "r")
        games = f.read()
        games_ray = games.splitlines()
        gm_st_btn = Button(text='Game Number', size_hint_y=None, height=30)
        gm_st_btn.bind(on_release=lambda gm_st_btn: self.game_dropdown.select(gm_st_btn.text),
                       on_press=lambda gm_st_btn: self.game_num(""))
        self.game_dropdown.add_widget(gm_st_btn)
        for index in range(len(games_ray)):
            btn = Button(text=games_ray[index], size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.game_dropdown.select(btn.text),
                     on_press=lambda btn: self.game_num(btn.text))
            self.game_dropdown.add_widget(btn)

        game_main_button = Button(text='Game Number')

        game_main_button.bind(on_release=self.game_dropdown.open)

        self.game_dropdown.bind(on_select=lambda instance, x: setattr(game_main_button, 'text', x))
        self.match_info_row.add_widget(game_main_button)

        # Round Number
        self.round_dropdown = DropDown()
        f = open("Configs\\rounds.txt", "r")
        rounds = f.read()
        rounds_ray = rounds.splitlines()
        st_btn = Button(text='Round Number', size_hint_y=None, height=30)
        st_btn.bind(on_release=lambda st_btn: self.round_dropdown.select(st_btn.text),
                    on_press=lambda st_btn: self.round_num(""))
        self.round_dropdown.add_widget(st_btn)
        for index in range(len(rounds_ray)):
            btn = Button(text=rounds_ray[index], size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.round_dropdown.select(btn.text),
                     on_press=lambda btn: self.round_num(btn.text))
            self.round_dropdown.add_widget(btn)

        round_main_button = Button(text='Round Number')

        round_main_button.bind(on_release=self.round_dropdown.open)

        self.round_dropdown.bind(on_select=lambda instance, x: setattr(round_main_button, 'text', x))
        self.match_info_row.add_widget(round_main_button)

        # Add Match Information Row
        self.add_widget(self.match_info_row)

        """ ***** UPDATE ROW ***** """
        self.update_row = GridLayout()
        self.update_row.cols = 1

        # Update
        self.update = Button(text="Update", font_size=30)
        self.update.bind(on_press=self.update_all)
        self.update_row.add_widget(self.update)

        # Add Update Row
        self.add_widget(self.update_row)

        """ ***** MISC ROW ***** """
        self.misc_row = GridLayout()
        self.misc_row.cols = 4

        # Misc 1
        self.misc_row.add_widget(Label(text="Misc 1", font_size=12, size_hint_x=(.39)))
        self.misc_one_display = TextInput(multiline=False, font_size=10)
        self.misc_row.add_widget(self.misc_one_display)

        # Misc 2
        self.misc_two_display = TextInput(multiline=False, font_size=10)
        self.misc_row.add_widget(self.misc_two_display)
        self.misc_row.add_widget(Label(text="Misc 2", font_size=12, size_hint_x=(.39)))

        # Misc 3
        self.misc_row.add_widget(Label(text="Misc 3", font_size=12, size_hint_x=(.39)))
        self.misc_three_display = TextInput(multiline=False, font_size=10)
        self.misc_row.add_widget(self.misc_three_display)

        # Misc 4
        self.misc_four_display = TextInput(multiline=False, font_size=10)
        self.misc_row.add_widget(self.misc_four_display)
        self.misc_row.add_widget(Label(text="Misc 4", font_size=12, size_hint_x=(.39)))

        # Add Misc Row
        self.add_widget(self.misc_row)

        """ ***** RESET ROW ***** """
        self.settings_row = GridLayout()
        self.settings_row.cols = 3

        # New Game
        self.new_game = Button(text="Reset Game", font_size=30)
        self.new_game.bind(on_press=self.reset_new_game)
        self.settings_row.add_widget(self.new_game)

        # New Match
        self.new_match = Button(text="Reset Match", font_size=30)
        self.new_match.bind(on_press=self.reset_new_match)
        self.settings_row.add_widget(self.new_match)

        # Full Reset
        self.full_reset = Button(text="Full Reset", font_size=30)
        self.full_reset.bind(on_press=self.reset_all)
        self.settings_row.add_widget(self.full_reset)

        # Add Settings Row
        self.add_widget(self.settings_row)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    folderCreator = FolderCreator()
    MyApp().run()
