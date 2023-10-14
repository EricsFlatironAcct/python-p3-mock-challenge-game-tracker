class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, '_title'):
            self._title = title
        return self._title
    
    def results(self):
        return [r for r in Result.all if r.game==self]

    def players(self):
        return list(set([r.player for r in Result.all if r.game==self]))

    def average_score(self, player):
        player_scores = [r.score for r in Result.all if r.player == player and r.game ==self]
        return (sum(player_scores)/len(player_scores))


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [r for r in Result.all if r.player == self]

    def games_played(self):
        return list(set([r.game for r in Result.all if r.player == self]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([r for r in Result.all if r.game == game and r.player == self])
    
    @classmethod
    def highest_scored(cls, game):
        result_list = game.results()
        result_list.sort(key=lambda r:r.score, reverse=True)
        return result_list[0].player

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <=5000 and not hasattr(self, '_score'):
            self._score = score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
