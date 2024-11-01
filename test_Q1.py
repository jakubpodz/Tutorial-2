import Q1;

def test_function():
    assert Q1.a == 1, 'Value of variable a not set correctly'
    assert Q1.b == 2.0, 'Value of variable b not set correctly'
    assert Q1.c == 'Exeter', 'Value of variable c not set correctly'
    assert Q1.d == '3.0', 'Value of variable c not set correctly'
    #type checking
    assert type(Q1.a) == int, 'Variable a has wrong type'
    assert type(Q1.b) == float, 'Variable b has wrong type'
    assert type(Q1.d) == str, 'Variable d has wrong type'