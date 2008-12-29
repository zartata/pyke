# test.py

import os.path
from pyke import knowledge_engine

Engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'Test.CanNotProve.compiled_krb')

def test(kb, ke, arg):
    Engine.reset()
    Engine.activate('rules')
    try:
        Engine.prove_1(kb, ke, (arg,), 0)
    except knowledge_engine.CanNotProve:
        pass

def dotests():
    test('facts', 'fact1', 2)
    test('facts', 'fact2', 2)
    test('rules', 'rule1', 2)
    test('rules', 'rule2', 2)