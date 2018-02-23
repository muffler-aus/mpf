"""Post an event to trigger an eject."""
import asyncio

from mpf.devices.ball_device.ball_device_ejector import BallDeviceEjector


class EventEjector(BallDeviceEjector):

    """Post an event to trigger an eject."""

    def eject_one_ball(self, is_jammed, eject_try):
        """Post event."""
        for events in self.config["events_when_eject_try"]:
            self.machine.events.post(event, is_jammed=is_jammed, eject_try=eject_try)

    def eject_all_balls(self):
        """Not implemented nor used."""
        raise NotImplementedError()

    def ball_search(self, phase, iteration):
        """Run ball search."""
        for events in self.config["events_when_ball_search"]:
            self.machine.events.post(event, phase=phase, iteration=iteration)

        # do not wait for this device
        return False

