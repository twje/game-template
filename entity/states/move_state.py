from trigger import Trigger
from . import register_state
from state import State
from tween import Tween
from constants import MessageID
from message import Message


@register_state("move")
class MoveStates(State):
    def __init__(self, entity, context):
        super().__init__()
        self.message_handler = context.message_handler
        self.entity = entity
        self.controller = self.entity.controller
        self.move_speed = 0.1

        # initilized on enter
        self._map = None
        self.x_move = None
        self.y_move = None
        self.x_pixel = None
        self.y_pixel = None
        self.tween = None

    def enter(self, data):
        x = data["x"]
        y = data["y"]

        # update direction
        if x == -1:            
            self.entity.facing = "left"
        elif x == 1:            
            self.entity.facing = "right"
        elif y == -1:            
            self.entity.facing = "up"
        elif y == 1:            
            self.entity.facing = "down"

        # update movement
        self.x_move = x
        self.y_move = y
        self.tween = Tween(0, 1, self.move_speed)

        # collision detection
        x_target = self.entity.x_pos + x
        y_target = self.entity.y_pos + y

        if self.map.is_obstacle(x_target, y_target):
            self.x_move = x
            self.y_move = y
            self.controller.change(self.entity.default_state)
            return

        # exit trigger
        self.try_trigger_on_exit()

        self.x_pixel = self.entity.x_pos
        self.y_pixel = self.entity.y_pos

    def exit(self):        
        self.try_trigger_on_enter()

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.tween.update(dt)

        value = self.tween.value
        x = self.x_pixel + (value * self.x_move)
        y = self.y_pixel + (value * self.y_move)
        self.entity.set_position(x, y)

        if self.tween.is_finished:
            self.controller.change(self.entity.default_state)

    def render(self, renderer):
        pass

     # --------------
    # Helper Methods
    # --------------
    def try_trigger_on_exit(self):
        if self.x_move != 0 or self.y_move != 0:
            trigger = self.map.get_trigger(
                self.entity.x_pos,
                self.entity.y_pos,
            )
            if trigger is not None:
                trigger.on_exit(
                    trigger,
                    self.entity,
                    self.entity.x_pos,
                    self.entity.y_pos
                )
                return True
        return False

    def try_trigger_on_enter(self):
        trigger = self.map.get_trigger(
            self.entity.x_pos,
            self.entity.y_pos,
        )
        if trigger is not None:
            trigger.on_enter(
                trigger,
                self.entity,
                self.entity.x_pos,
                self.entity.y_pos
            )

    @property
    def map(self):
        if self._map is None:
            message = Message(MessageID.GET_MAP)
            self.message_handler.dispatch(message)
            assert message.response is not None
            self._map = message.response

        return self._map
