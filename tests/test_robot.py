from  lajornada.theme.testing import LAJORNADA_THEME_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=LAJORNADA_THEME_FUNCTIONAL_TESTING)
    ])
    return suite