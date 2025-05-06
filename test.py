import unittest

class TestVehicleClasses(unittest.TestCase):

    def test_boat(self):
        boing = Boat("boing", 202, 1200, "boing", 122)
        
        # Initial state: engine should be off and boat should be docked
        self.assertFalse(boing.engine_on)
        self.assertTrue(boing.docked)

        # Start engine
        self.assertEqual(boing.start_engine(), "boing's engine is on")
        self.assertTrue(boing.engine_on)

        # Try to dock while engine is on
        self.assertEqual(boing.dock(), "Can't dock engine is on")

        # Try to sail while docked
        self.assertEqual(boing.sail("north"), "Can't set sail start engine first and undock")

        # Turn off engine, then dock successfully
        boing.stop_engine()
        self.assertEqual(boing.dock(), "Ship docked")
        self.assertTrue(boing.docked)

        # Start engine again
        boing.start_engine()
        boing.docked = False  # Manually undock to simulate undocking
        self.assertEqual(boing.sail("north"), "boing is setting sail towards north")

    def test_car(self):
        car = Car("Toyota", 180, 5, "Petrol", 4)
        self.assertEqual(car.start_engine(), "Toyota's engine is on")
        self.assertEqual(car.move(), "Toyota is moving at 180 its capacity is 5")

        expected_stats = (
            "Name: Toyota \nSpeed: 180 \nCapacity: 5 \nEngine on: True"
            " \nFuel type: Petrol \nNumber of doors: 4"
        )
        self.assertEqual(car.stats(), expected_stats)

    def test_plane(self):
        plane = Plane("Boeing", 900, 300, "Delta", 5000)
        self.assertEqual(plane.take_off("north"), "Can't take off turn engine off first")
        plane.start_engine()
        self.assertEqual(plane.take_off("north"), "Boeing is taking of in north")
        self.assertFalse(plane.landing_gear_deployed)
        self.assertEqual(plane.landing("JFK"), "Boeing is landing in JFK shortly")
        self.assertTrue(plane.landing_gear_deployed)

if __name__ == '__main__':
    unittest.main()
