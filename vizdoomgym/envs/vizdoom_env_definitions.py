from vizdoomgym.envs.vizdoomenv import VizdoomEnv

class VizdoomBasic(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomBasic, self).__init__(0, **kwargs)

class VizdoomCorridor5(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridor5, self).__init__(1, no_reward=no_reward, **kwargs)

class VizdoomCorridor1(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridor1, self).__init__(12, no_reward=no_reward, **kwargs)

class VizdoomCorridor3(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridor3, self).__init__(13, no_reward=no_reward, **kwargs)

class VizdoomCorridor7(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridor7, self).__init__(14, no_reward=no_reward, **kwargs)

class VizdoomCorridorSparse5(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridorSparse5, self).__init__(10, no_reward=no_reward, **kwargs)

class VizdoomCorridorSparse1(VizdoomEnv):
    def __init__(self, no_reward, **kwargs):
        super(VizdoomCorridorSparse1, self).__init__(11, no_reward=no_reward, **kwargs)


class VizdoomDeathmatch(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDeathmatch, self).__init__(8, **kwargs)


class VizdoomDefendCenter(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDefendCenter, self).__init__(2, **kwargs)


class VizdoomDefendLine(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDefendLine, self).__init__(3, **kwargs)


class VizdoomHealthGathering(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomHealthGathering, self).__init__(4, **kwargs)


class VizdoomHealthGatheringSupreme(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomHealthGatheringSupreme, self).__init__(9, **kwargs)


class VizdoomMyWayHome(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomMyWayHome, self).__init__(5, **kwargs)


class VizdoomPredictPosition(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomPredictPosition, self).__init__(6, **kwargs)


class VizdoomTakeCover(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomTakeCover, self).__init__(7, **kwargs)
