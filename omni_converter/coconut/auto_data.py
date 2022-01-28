#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf042a20b

# Compiled with Coconut version 1.6.0 [Vocational Guidance Counsellor]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == "__coconut__":
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == "__coconut__":
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

from typing import Mapping  # from typing import Mapping, Callable
from typing import Callable  # from typing import Mapping, Callable
from IPython.display import display  # from IPython.display import display
import dill  # to make the lambda functions picklable  # import dill # to make the lambda functions picklable
from loguru import logger  # from loguru import logger
import numpy as np  # import numpy as np
"""
What I want to achieve is to generate a class.
I want to generate a AutoImage class form AutoData
well the solution is to just use partially applied constructor. that's it.
"""  # """
def identity(a):  # def identity(a):
    return (a)  #     return a

class _CastLambda:  # class _CastLambda:
    def __init__(self, rule, name, swap, cost=1):  #     def __init__(self,rule,name,swap,cost=1):
        self.rule = rule  #         self.rule = rule
        self.name = name  #         self.name = name
        self.swap = swap  #         self.swap = swap
        self.cost = cost  #         self.cost = cost
    def __call__(self, state):  #     def __call__(self,state):
        new_states = self.rule(state)  #         new_states = self.rule(state)
        if new_states is not None:  #         if new_states is not None:
            if self.name is None:  #             if self.name is None:
                cast_name = "{_coconut_format_0}".format(_coconut_format_0=(self.rule.__name__))  #                 cast_name = f"{self.rule.__name__}"
            else:  #             else:
                cast_name = self.name  #                 cast_name=self.name
            if self.swap:  #             if self.swap:
                return ([(identity, new_state, cast_name, self.cost) for new_state in new_states])  #                 return [(identity,new_state,cast_name,self.cost) for new_state in new_states]
            else:  #             else:
                return ([(identity, new_state, self.cost, cast_name) for new_state in new_states])  #                 return [(identity,new_state,self.cost,cast_name) for new_state in new_states]
        else:  #         else:
            return (None)  #             return None
_coconut_call_set_names(_CastLambda)  # class _ConversionLambda:
class _ConversionLambda:  # class _ConversionLambda:
    def __init__(self, rule, cost=1):  #     def __init__(self,rule,cost=1):
        self.rule = rule  #         self.rule = rule
        self.cost = cost  #         self.cost = cost
    def __call__(self, state):  #     def __call__(self,state):
        edges = self.rule(state)  #         edges = self.rule(state)
        if edges is None:  #         if edges is None:
            return ([])  #             return []
        result = []  #         result = []
        for edge in edges:  #         for edge in edges:
            _coconut_case_match_to_0 = edge  #             case edge:
            _coconut_case_match_check_0 = False  #             case edge:
            _coconut_match_set_name_converter = _coconut_sentinel  #             case edge:
            _coconut_match_set_name_new_state = _coconut_sentinel  #             case edge:
            if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #             case edge:
                _coconut_match_set_name_converter = _coconut_case_match_to_0[0]  #             case edge:
                _coconut_match_set_name_new_state = _coconut_case_match_to_0[1]  #             case edge:
                _coconut_case_match_check_0 = True  #             case edge:
            if _coconut_case_match_check_0:  #             case edge:
                if _coconut_match_set_name_converter is not _coconut_sentinel:  #             case edge:
                    converter = _coconut_case_match_to_0[0]  #             case edge:
                if _coconut_match_set_name_new_state is not _coconut_sentinel:  #             case edge:
                    new_state = _coconut_case_match_to_0[1]  #             case edge:
            if _coconut_case_match_check_0:  #             case edge:
                result.append((converter, new_state, self.cost, converter.__name__))  #                     result.append((converter,new_state,self.cost,converter.__name__))
            if not _coconut_case_match_check_0:  #                 match (converter,new_state,name):
                _coconut_match_set_name_converter = _coconut_sentinel  #                 match (converter,new_state,name):
                _coconut_match_set_name_new_state = _coconut_sentinel  #                 match (converter,new_state,name):
                _coconut_match_set_name_name = _coconut_sentinel  #                 match (converter,new_state,name):
                if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3):  #                 match (converter,new_state,name):
                    _coconut_match_set_name_converter = _coconut_case_match_to_0[0]  #                 match (converter,new_state,name):
                    _coconut_match_set_name_new_state = _coconut_case_match_to_0[1]  #                 match (converter,new_state,name):
                    _coconut_match_set_name_name = _coconut_case_match_to_0[2]  #                 match (converter,new_state,name):
                    _coconut_case_match_check_0 = True  #                 match (converter,new_state,name):
                if _coconut_case_match_check_0:  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_converter is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        converter = _coconut_case_match_to_0[0]  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_new_state is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        new_state = _coconut_case_match_to_0[1]  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        name = _coconut_case_match_to_0[2]  #                 match (converter,new_state,name):
                if _coconut_case_match_check_0:  #                 match (converter,new_state,name):
                    result.append((converter, new_state, self.cost, name))  #                     result.append((converter,new_state,self.cost,name))
            if not _coconut_case_match_check_0:  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_converter = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_new_state = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_name = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_score = _coconut_sentinel  #                 match (converter,new_state,name,score):
                if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 4):  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_converter = _coconut_case_match_to_0[0]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_new_state = _coconut_case_match_to_0[1]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_name = _coconut_case_match_to_0[2]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_score = _coconut_case_match_to_0[3]  #                 match (converter,new_state,name,score):
                    _coconut_case_match_check_0 = True  #                 match (converter,new_state,name,score):
                if _coconut_case_match_check_0:  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_converter is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        converter = _coconut_case_match_to_0[0]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_new_state is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        new_state = _coconut_case_match_to_0[1]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        name = _coconut_case_match_to_0[2]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_score is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        score = _coconut_case_match_to_0[3]  #                 match (converter,new_state,name,score):
                if _coconut_case_match_check_0:  #                 match (converter,new_state,name,score):
                    result.append((converter, new_state, score, name))  #                     result.append((converter,new_state,score,name))
            if not _coconut_case_match_check_0:  #                 match _:
                _coconut_case_match_check_0 = True  #                 match _:
                if _coconut_case_match_check_0:  #                 match _:
                    raise RuntimeError("rule:{_coconut_format_0} returned invalid edge:{_coconut_format_1}.".format(_coconut_format_0=(self.rule), _coconut_format_1=(edge)))  #                     raise RuntimeError(f"rule:{self.rule} returned invalid edge:{edge}.")
        return (result)  #         return result
_coconut_call_set_names(_ConversionLambda)  # class _SmartConversionLambda:
class _SmartConversionLambda:  # class _SmartConversionLambda:
    def __init__(self, rule, cost=1):  #     def __init__(self,rule,cost=1):
        self.rule = rule  #         self.rule = rule
        self.cost = cost  #         self.cost = cost
    def __call__(self, state, end):  #     def __call__(self,state,end):
        edges = self.rule(state, end)  #         edges = self.rule(state,end)
        if edges is None:  #         if edges is None:
            return ([])  #             return []
        result = []  #         result = []
        for edge in edges:  #         for edge in edges:
            _coconut_case_match_to_1 = edge  #             case edge:
            _coconut_case_match_check_1 = False  #             case edge:
            _coconut_match_set_name_converter = _coconut_sentinel  #             case edge:
            _coconut_match_set_name_new_state = _coconut_sentinel  #             case edge:
            if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2):  #             case edge:
                _coconut_match_set_name_converter = _coconut_case_match_to_1[0]  #             case edge:
                _coconut_match_set_name_new_state = _coconut_case_match_to_1[1]  #             case edge:
                _coconut_case_match_check_1 = True  #             case edge:
            if _coconut_case_match_check_1:  #             case edge:
                if _coconut_match_set_name_converter is not _coconut_sentinel:  #             case edge:
                    converter = _coconut_case_match_to_1[0]  #             case edge:
                if _coconut_match_set_name_new_state is not _coconut_sentinel:  #             case edge:
                    new_state = _coconut_case_match_to_1[1]  #             case edge:
            if _coconut_case_match_check_1:  #             case edge:
                result.append((converter, new_state, self.cost, converter.__name__))  #                     result.append((converter,new_state,self.cost,converter.__name__))
            if not _coconut_case_match_check_1:  #                 match (converter,new_state,name):
                _coconut_match_set_name_converter = _coconut_sentinel  #                 match (converter,new_state,name):
                _coconut_match_set_name_new_state = _coconut_sentinel  #                 match (converter,new_state,name):
                _coconut_match_set_name_name = _coconut_sentinel  #                 match (converter,new_state,name):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 3):  #                 match (converter,new_state,name):
                    _coconut_match_set_name_converter = _coconut_case_match_to_1[0]  #                 match (converter,new_state,name):
                    _coconut_match_set_name_new_state = _coconut_case_match_to_1[1]  #                 match (converter,new_state,name):
                    _coconut_match_set_name_name = _coconut_case_match_to_1[2]  #                 match (converter,new_state,name):
                    _coconut_case_match_check_1 = True  #                 match (converter,new_state,name):
                if _coconut_case_match_check_1:  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_converter is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        converter = _coconut_case_match_to_1[0]  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_new_state is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        new_state = _coconut_case_match_to_1[1]  #                 match (converter,new_state,name):
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #                 match (converter,new_state,name):
                        name = _coconut_case_match_to_1[2]  #                 match (converter,new_state,name):
                if _coconut_case_match_check_1:  #                 match (converter,new_state,name):
                    result.append((converter, new_state, self.cost, name))  #                     result.append((converter,new_state,self.cost,name))
            if not _coconut_case_match_check_1:  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_converter = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_new_state = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_name = _coconut_sentinel  #                 match (converter,new_state,name,score):
                _coconut_match_set_name_score = _coconut_sentinel  #                 match (converter,new_state,name,score):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 4):  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_converter = _coconut_case_match_to_1[0]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_new_state = _coconut_case_match_to_1[1]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_name = _coconut_case_match_to_1[2]  #                 match (converter,new_state,name,score):
                    _coconut_match_set_name_score = _coconut_case_match_to_1[3]  #                 match (converter,new_state,name,score):
                    _coconut_case_match_check_1 = True  #                 match (converter,new_state,name,score):
                if _coconut_case_match_check_1:  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_converter is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        converter = _coconut_case_match_to_1[0]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_new_state is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        new_state = _coconut_case_match_to_1[1]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        name = _coconut_case_match_to_1[2]  #                 match (converter,new_state,name,score):
                    if _coconut_match_set_name_score is not _coconut_sentinel:  #                 match (converter,new_state,name,score):
                        score = _coconut_case_match_to_1[3]  #                 match (converter,new_state,name,score):
                if _coconut_case_match_check_1:  #                 match (converter,new_state,name,score):
                    result.append((converter, new_state, score, name))  #                     result.append((converter,new_state,score,name))
            if not _coconut_case_match_check_1:  #                 match _:
                _coconut_case_match_check_1 = True  #                 match _:
                if _coconut_case_match_check_1:  #                 match _:
                    raise RuntimeError("rule:{_coconut_format_0} returned invalid edge:{_coconut_format_1}.".format(_coconut_format_0=(self.rule), _coconut_format_1=(edge)))  #                     raise RuntimeError(f"rule:{self.rule} returned invalid edge:{edge}.")
        return (result)  #         return result
_coconut_call_set_names(_SmartConversionLambda)  # class AutoSolver:
class AutoSolver:  # class AutoSolver:
    """
    TODO stop using local lambda in order to make this class picklable
    Factory for an AutoData class
    """  #     """
#def __init__(self,rules,smart_rules,heuristics=lambda x,y:0,edge_cutter=lambda x,y,end:False,debug_hook=None):
    def __init__(self, rules, smart_rules, heuristics, edge_cutter, debug_hook):  #     def __init__(self,rules,smart_rules,heuristics,edge_cutter,debug_hook):
        """
        smart_rules accepts not only current state but also the target state so that it can return the next edge smartly
        """  #         """
        self.initial_rules = rules  #         self.initial_rules = rules
        self.smart_rules = smart_rules  #         self.smart_rules = smart_rules
        self.solver = AStarSolver(rules=list(self.initial_rules), smart_rules=list(self.smart_rules), heuristics=heuristics, edge_cutter=edge_cutter, debug_hook=debug_hook)  #         self.solver = AStarSolver(

    @staticmethod  #     @staticmethod
    def create_cast_rule(rule, name=None, _swap=False, cost=1):  #     def create_cast_rule(rule,name=None,_swap=False,cost=1):
        """
        rule: State->List[State] # should return list of possible casts without data conversion.
        """  #         """
        return (_CastLambda(rule, name, _swap, cost=cost))  #         return _CastLambda(rule,name,_swap,cost=cost)

    def add_cast(self, rule, name=None):  #     def add_cast(self,rule,name=None):
        """
        rule: State->List[State] # should return list of possible casts without data conversion.
        """  #         """

        self.add_conversion(AutoSolver.create_cast_rule(rule, name=name, _swap=True))  #         self.add_conversion(AutoSolver.create_cast_rule(rule,name=name,_swap=True))

    def add_alias(self, a, b):  #     def add_alias(self,a,b):
        self.add_cast(lambda state: [b, ] if state == a else None, name="alias: {_coconut_format_0}->{_coconut_format_1}".format(_coconut_format_0=(a), _coconut_format_1=(b)))  #         self.add_cast(state->[b] if state == a else None,name=f"alias: {a}->{b}")
        self.add_cast(lambda state: [a, ] if state == b else None, name="alias: {_coconut_format_0}->{_coconut_format_1}".format(_coconut_format_0=(b), _coconut_format_1=(a)))  #         self.add_cast(state->[a] if state == b else None,name=f"alias: {b}->{a}")

    @staticmethod  #     @staticmethod
    def create_alias_rule(a, b):  #     def create_alias_rule(a,b):
        def caster(state):  #         def caster(state):
            if state == a:  #            if state == a:
                return ([b, ])  #                return [b]
            elif state == b:  #            elif state == b:
                return ([a, ])  #                return [a]
        return (AutoSolver.create_cast_rule(caster, "alias:{_coconut_format_0}=={_coconut_format_1}".format(_coconut_format_0=(a), _coconut_format_1=(b))))  #         return AutoSolver.create_cast_rule(caster,f"alias:{a}=={b}")

    @staticmethod  #     @staticmethod
    def create_conversion_rule(rule):  #     def create_conversion_rule(rule):
        return (_ConversionLambda(rule))  #         return _ConversionLambda(rule)
    @staticmethod  #     @staticmethod
    def create_smart_conversion_rule(rule):  #     def create_smart_conversion_rule(rule):
        return (_SmartConversionLambda(rule))  #         return _SmartConversionLambda(rule)

    def add_conversion(self, rule):  #     def add_conversion(self,rule):
        """
        rule: State->List[(converter,new_state,name(optional),cost(optional))]
        """  #         """
        self.solver.add_rule(AutoSolver.create_conversion_rule(rule))  #         self.solver.add_rule(AutoSolver.create_conversion_rule(rule))

    def debug_conversion(self, a, b, samples):  #     def debug_conversion(self,a,b,samples):
        x = samples  #         x = samples
        edges = self.solver.search_direct(a, b).edges  #         edges = self.solver.search_direct(a,b).edges
        for edge in edges:  #         for edge in edges:
            print(edge)  #             print(edge)
            print(edge.f)  #             print(edge.f)
            x = edge.f(x)  #             x = edge.f(x)
            print("converted to type:{_coconut_format_0}".format(_coconut_format_0=(type(x))))  #             print(f"converted to type:{type(x)}")
            if (isinstance)(x, np.ndarray):  #             if x `isinstance` np.ndarray:
                print(x.shape)  #                 print(x.shape)
            print("converted:{_coconut_format_0}".format(_coconut_format_0=(x)))  #             print(f"converted:{x}")
        return (x)  #         return x



_coconut_call_set_names(AutoSolver)  # class TagMatcher:
class TagMatcher:  # class TagMatcher:
    def __init__(self, **kwargs):  #     def __init__(self,**kwargs):
        self.kwargs = kwargs  #         self.kwargs = kwargs

    def __call__(self, state):  #     def __call__(self,state):
        if isinstance(state, Mapping):  #         if isinstance(state,Mapping):
            for k, v in self.kwargs.items():  #             for k,v in self.kwargs.items():
                if not k in state or not state[k] == v:  #                 if not k in state or not state[k] == v:
                    return (False)  #                     return False
            return (True)  #every item matched.  #             return True #every item matched.
        else:  #         else:
            return (False)  #             return False
    @property  #     @property
    def __name__(self):  #     def __name__(self):
        return ("TagMatcher|{_coconut_format_0}".format(_coconut_format_0=(self.kwargs)))  #         return f"TagMatcher|{self.kwargs}"

    def __str__(self):  #     def __str__(self):
        return (self.__name__)  #         return self.__name__


_coconut_call_set_names(TagMatcher)  # @memoize(1024)
@memoize(1024)  # @memoize(1024)
def tag_matcher(**kwargs):  # def tag_matcher(**kwargs):
    return (TagMatcher(**kwargs))  #     return TagMatcher(**kwargs)

class Tracer:  # class Tracer:
    def __init__(self, solver, state, creator):  #     def __init__(self,solver,state,creator):
        self.state = state  #         self.state = state
        self.solver = solver  #         self.solver = solver
        self.creator = creator  #         self.creator = creator
    def nexts(self):  #     def nexts(self):
        edges = self.solver.solver.neighbors(self.state)  #         edges = self.solver.solver.neighbors(self.state)
        return ([Tracer(self.solver, new_state, creator) for _, new_state, _, creator in edges])  #         return [Tracer(self.solver,new_state,creator) for _,new_state,_,creator in edges]
    def __getitem__(self, item):  #     def __getitem__(self,item):
        return (self.nexts()[item])  #         return self.nexts()[item]
    def __repr__(self):  #     def __repr__(self):
        res = []  #         res = []
        self_str = "Tracer: {_coconut_format_0:30s} -> {_coconut_format_1}".format(_coconut_format_0=(self.creator), _coconut_format_1=(self.state))  #         self_str = f"Tracer: {self.creator:30s} -> {self.state}"
        res.append(self_str)  #         res.append(self_str)
        for i, n in enumerate(self.nexts()):  #         for i,n in enumerate(self.nexts()):
            res.append("{_coconut_format_0:>6d}: {_coconut_format_1:30s} -> {_coconut_format_2}".format(_coconut_format_0=(i), _coconut_format_1=(n.creator), _coconut_format_2=(n.state)))  #             res.append(f"{i:>6d}: {n.creator:30s} -> {n.state}")
        return ("\n".join(res))  #         return "\n".join(res)

_coconut_call_set_names(Tracer)  # class AutoData:
class AutoData:  # class AutoData:
    """
    Interface class for a user
    """  #     """
    def to_debug(self, format):  #     def to_debug(self,format):
        format = parse_def(format)  #         format = parse_def(format)
        return (AutoData.debug_conversion(self.format, format, self.value))  #         return AutoData.debug_conversion(self.format,format,self.value)

    def __init__(self, value, format, solver_getter):  #     def __init__(self,value,format,solver_getter):
        self.value = value  #         self.value = value
        self.format = format  #         self.format = format
        self.solver_getter = solver_getter  #         self.solver_getter = solver_getter
        assert isinstance(solver_getter, Callable)  #         assert isinstance(solver_getter,Callable)

    @property  #     @property
    def solver(self):  #     def solver(self):
# We need to know how to make a solver on another process.
# if all the rules were picklable, it is fine. but actually they are not.
        return (self.solver_getter())  #         return self.solver_getter()

    def converter(self, format=None, **kwargs):  #     def converter(self,format=None,**kwargs):
        if format is not None:  #         if format is not None:
            return (self.solver.solver.search_direct(self.format, format))  #             return self.solver.solver.search_direct(self.format,format)
        else:  #         else:
            return (self.solver.solver.search(self.format, tag_matcher(**kwargs)))  #             return self.solver.solver.search(self.format,tag_matcher(**kwargs))

    def convert(self, format=None, **kwargs) -> 'AutoData':  #     def convert(self,format=None,**kwargs) -> AutoData:
        """converts internal data to specified format."""  #         """converts internal data to specified format."""
        conversion = self.converter(format, **kwargs)  #         conversion = self.converter(format,**kwargs)
        if conversion.edges:  #         if conversion.edges:
            return (self.__class__(conversion(self.value), conversion.edges[-1].dst, self.solver_getter))  #             return self.__class__(conversion(self.value),conversion.edges[-1].dst,self.solver_getter)
        else:  #         else:
            return (self)  #             return self
    def search_converter(self, f):  #     def search_converter(self,f):
        return (self.solver.solver.search(self.format, f))  #         return self.solver.solver.search(self.format,f)

    def search(self, matcher, ignore_error=True) -> 'AutoData':  #     def search(self,matcher,ignore_error=True) -> AutoData:
        if ignore_error:  #         if ignore_error:
            def _matcher(state):  #             def _matcher(state):
                try:  #                 try:
                    return (matcher(state))  #                     return matcher(state)
                except Exception as e:  #                 except Exception as e:
                    pass  #                     pass
            conversion = self.search_converter(_matcher)  #             conversion = self.search_converter(_matcher)
        else:  #         else:
            conversion = self.search_converter(matcher)  #             conversion = self.search_converter(matcher)
        if conversion.edges:  #         if conversion.edges:
            return (self.__class__(conversion(self.value), conversion.edges[-1].dst, self.solver_getter))  #             return self.__class__(conversion(self.value),conversion.edges[-1].dst,self.solver_getter)
        else:  #         else:
            return (self)  #             return self

    def to(self, format=None, **kwargs):  # I want 'to' to accept format string too  #     def to(self,format=None,**kwargs): # I want 'to' to accept format string too
# if format is given, use direct matching.
# else use tag matching
# format can be of any type, but you need to have a conversion rule to tag_dict, otherwise you won't get any result
# so, ask user to provide any state and state->tag_dict rule.
# That's it.
        converted = self.convert(format=format, **kwargs)  #         converted = self.convert(format=format,**kwargs)
        return (converted.value)  #         return converted.value

    def map(self, f, new_format=None):  #     def map(self,f,new_format=None):
        if new_format is not None:  #         if new_format is not None:
            format = new_format  #             format = new_format
        else:  #         else:
            format = self.format  #             format = self.format
        return (self.__class__(f(self.value), format, self.solver_getter))  #         return self.__class__(f(self.value),format,self.solver_getter)

    def map_in(self, start_format, f, new_format=None):  #     def map_in(self,start_format,f,new_format=None):
        return (self.__class__(f(self.to(start_format)), (lambda _coconut_x: self.format if _coconut_x is None else _coconut_x)(new_format), self.solver_getter))  #         return self.__class__(f(self.to(start_format)),new_format??self.format,self.solver_getter)

    def neighbors(self):  #     def neighbors(self):
        return (self.solver.solver.neighbors(self.format))  #         return self.solver.solver.neighbors(self.format)
    def tracer(self):  #     def tracer(self):
        return (Tracer(self.solver, self.format, "origin"))  #         return Tracer(self.solver,self.format,"origin")
    def to_widget(self):  #     def to_widget(self):
        return (self.to("widget"))  #         return self.to("widget")

    def _repr_html_(self):  #     def _repr_html_(self):
        (display)(self.format)  #         self.format |> display
        (display)(self.to("widget"))  #         self.to("widget") |> display

    def __repr__(self):  #     def __repr__(self):
        return ("{_coconut_format_0}({_coconut_format_1})".format(_coconut_format_0=(self.__class__.__name__), _coconut_format_1=(self.format)))  #         return f"{self.__class__.__name__}({self.format})"

    def _repr_png_(self):  #     def _repr_png_(self):
        try:  #         try:
            return (self.to(type="image")._repr_png_())  #             return self.to(type="image")._repr_png_()
        except Exception as e:  #         except Exception as e:
            logger.warning("cannot convert data to an image:{_coconut_format_0}".format(_coconut_format_0=(self.format)))  #             logger.warning(f"cannot convert data to an image:{self.format}")
            return (None)  #             return None

    def cast(self, format):  #     def cast(self,format):
        return (self.__class__(self.value, format, self.solver_getter))  #         return self.__class__(self.value,format,self.solver_getter)

    def imshow(self):  #     def imshow(self):
        while True:  #         from matplotlib.pyplot import imshow
            from matplotlib.pyplot import imshow  #         from matplotlib.pyplot import imshow
            try:  #         return imshow(self.to("numpy_rgb"))
                _coconut_tre_check_0 = imshow is _coconut_recursive_func_37  #         return imshow(self.to("numpy_rgb"))
            except _coconut.NameError:  #         return imshow(self.to("numpy_rgb"))
                _coconut_tre_check_0 = False  #         return imshow(self.to("numpy_rgb"))
            if _coconut_tre_check_0:  #         return imshow(self.to("numpy_rgb"))
                self = self.to("numpy_rgb")  #         return imshow(self.to("numpy_rgb"))
                continue  #         return imshow(self.to("numpy_rgb"))
            else:  #         return imshow(self.to("numpy_rgb"))
                return imshow(self.to("numpy_rgb"))  #         return imshow(self.to("numpy_rgb"))


            return None  #     def show(self,block=True):
    _coconut_recursive_func_37 = imshow  #     def show(self,block=True):
    def show(self, block=True):  #     def show(self,block=True):
        """show assumes that internal state always converts to rgba domain."""  #         """show assumes that internal state always converts to rgba domain."""
# so if you want to visualize spectrum you have to cast it.
        from matplotlib.pyplot import show as mpl_show  #         from matplotlib.pyplot import show as mpl_show
        self.imshow()  #         self.imshow()
        return (mpl_show(block=block))  #         return mpl_show(block=block)


#    def __getstate__(self):


_coconut_call_set_names(AutoData)  # def AutoData.call(self,name,*args,**kwargs):
try:  # def AutoData.call(self,name,*args,**kwargs):
    _coconut_name_store_0 = call  # def AutoData.call(self,name,*args,**kwargs):
except _coconut.NameError:  # def AutoData.call(self,name,*args,**kwargs):
    _coconut_name_store_0 = _coconut_sentinel  # def AutoData.call(self,name,*args,**kwargs):
def call(self, name, *args, **kwargs):  # def AutoData.call(self,name,*args,**kwargs):
    return (self.to(name)(*args, **kwargs))  #     return self.to(name)(*args,**kwargs)

AutoData.call = call  #     return self.to(name)(*args,**kwargs)
if _coconut_name_store_0 is not _coconut_sentinel:  #     return self.to(name)(*args,**kwargs)
    call = _coconut_name_store_0  #     return self.to(name)(*args,**kwargs)
