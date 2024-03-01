from NumberOfRecentCalls.python.ping import RecentCounter

class TestPing:
    def test_ping(self):
        methods, params_list = ["RecentCounter","ping","ping","ping","ping"], [[],[1],[100],[3001],[3002]]
        results = []
        instance = None
        for (method, params) in zip(methods, params_list):
            if method == "RecentCounter":
                instance = RecentCounter()
                results.append(None)
            elif method == "ping":
                results.append(instance.ping(*params))
            else:
                assert False, "Unexpected case"
        assert [None,1,2,3,3] == results
