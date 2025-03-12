class verifyOneStop:

    @staticmethod
    def getAllStop(all_stop, stop_type):
        for stop in all_stop:
            if stop_type in stop.text:
                assert stop.is_displayed()




