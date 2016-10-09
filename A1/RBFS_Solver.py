class RBFS_Solver(object):

    def rbfs_helper(self,matrix,node,limit):
        pass

    def eight_puzzle_solver_using_RBFS(self,matrix,method):
        start = self.input_matrix
        if method == 0:
            h_fn = self.heuristics_misplaced_tiles
        elif method == 1:
            h_fn = self.heuristics_manhattan_distance

        # compute the heuristic distance for the start state
        hnode = h_fn(start)
        hnode.append('')
        rbfs_helper(start,method,99999)