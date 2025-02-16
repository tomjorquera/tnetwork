import unittest
import tnetwork as tn
import tnetwork.DCD as DCD
import shutil


class DCDTestCase(unittest.TestCase):


    def test_simple_matching(self):
        my_scenario = tn.ComScenario()
        [to_merge, absorb, to_split] = my_scenario.INITIALIZE([4, 6, 12], ["to_merge", "absorb", "to_split"])
        absorbing = my_scenario.MERGE([to_merge, absorb], absorb.name(), t=5)
        (split_large, split_small) = my_scenario.SPLIT(to_split, ["to_split", "other"], [8, 4], waitFor=absorbing)
        my_scenario.MERGE([split_small, absorbing], absorbing.name())
        born = my_scenario.BIRTH(3, t=6)
        my_scenario.DEATH(born, t=22)
        (dyn_graph, dyn_com) = my_scenario.run()

        self.assertEqual(len(dyn_graph.graph_at_time(0).nodes),4+6+12)
        self.assertEqual(len(dyn_com.snapshot_communities(0)), 3)
        self.assertEqual(len(dyn_com.snapshot_communities(dyn_com.end - 1)), 2)
        self.assertEqual(len(dyn_graph.graph_at_time(dyn_com.end-1).nodes),4+6+12)

    def test_theseus(self):
        my_scenario = tn.ComScenario()
        [to_merge, absorb, to_split] = my_scenario.INITIALIZE([4, 6, 12], ["to_merge", "absorb", "to_split"])
        my_scenario.THESEUS(to_merge)

        (dyn_graph, dyn_com) = my_scenario.run()



if __name__ == '__main__':
    unittest.main()
