class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sam = 14
        assert a+b == expected_sam, f"Sum of variables a and b equal tu{expected_sam}"


    def test_check_math2(self):
        a = 5
        b = 11
        expected_sam = 14
        assert a+b == expected_sam, f"Sum of variables a and b equal tu {expected_sam}"

