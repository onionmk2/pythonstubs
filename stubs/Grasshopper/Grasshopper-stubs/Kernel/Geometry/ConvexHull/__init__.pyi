from typing import Tuple, Set, Iterable, List


class Solver:
    def Compute(nodes: Node2List, hull: List) -> bool: ...
    @overload
    def ComputeHull(GH_pts: Iterable[GH_Point]) -> Polyline: ...
    @overload
    def ComputeHull(GH_pts: Iterable[GH_Point], plane: Plane) -> Tuple[Polyline, Plane]: ...
    @overload
    def ComputeHull(pts: Node2List) -> Polyline: ...
