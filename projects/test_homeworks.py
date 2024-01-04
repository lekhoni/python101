import io
import sys
import unittest
from projects.homeworks import *


class TestHello(unittest.TestCase):
    def setUp(self):
        self.stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout_backup

    def test_fizz_buzz_output(self):
        hello()
        output = sys.stdout.getvalue()
        expected_output = "Hello, World!\n"
        self.assertEqual(output, expected_output)


class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(5), 78.53981633974483, places=5)

    def test_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_negative_radius(self):
        self.assertEqual(calculate_circle_area(-5), "Radius cannot be negative.")


class TestEvenSum(unittest.TestCase):
    def test_even_sum(self):
        self.assertEqual(sum_of_even_numbers(), 2550)


class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative_number(self):
        self.assertEqual(
            factorial(-5), "Factorial is not defined for negative numbers."
        )


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")


class TestIsPrime(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-1))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout_backup

    def test_fizz_buzz_output(self):
        fizz_buzz()
        output = sys.stdout.getvalue()
        expected_output = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"
        self.assertEqual(output, expected_output)


class TestWordCounter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)

    def test_multiple_words(self):
        self.assertEqual(count_words("This is a test"), 4)

    def test_words_with_extra_spaces(self):
        self.assertEqual(count_words("   Extra    spaces   "), 2)


class TestFindLargest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_largest([]))

    def test_single_element_list(self):
        self.assertEqual(find_largest([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(find_largest([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_largest([-5, -3, -1, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_largest([10, -20, 30, -40]), 30)


class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("deified"))

    def test_single_word_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_sentence_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_sentence_not_palindrome(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))


class TestSumOfDigits(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(987654321), 45)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

    def test_negative_integer(self):
        self.assertEqual(
            sum_of_digits(-123), "Invalid input. Please enter a positive integer."
        )

    def test_non_integer(self):
        self.assertEqual(
            sum_of_digits("abc"), "Invalid input. Please enter a positive integer."
        )


class TestIsLeapYear(unittest.TestCase):
    def test_leap_years(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2400))

    def test_non_leap_years(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2022))

    def test_invalid_input(self):
        self.assertRaises(ValueError, is_leap_year, "abc")
        self.assertRaises(ValueError, is_leap_year, -2000)


class TestGenerateMultiplicationTable(unittest.TestCase):
    def test_valid_input(self):
        expected_table = [
            "3 x 1 = 3",
            "3 x 2 = 6",
            "3 x 3 = 9",
            "3 x 4 = 12",
            "3 x 5 = 15",
        ]
        self.assertEqual(generate_multiplication_table(3, 5), expected_table)

    def test_invalid_input(self):
        self.assertEqual(
            generate_multiplication_table(0, 5),
            "Invalid input. Both number and range should be positive integers.",
        )
        self.assertEqual(
            generate_multiplication_table(3, 0),
            "Invalid input. Both number and range should be positive integers.",
        )
        self.assertEqual(
            generate_multiplication_table(-2, 5),
            "Invalid input. Both number and range should be positive integers.",
        )


class TestFindGCD(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_gcd(24, 36), 12)
        self.assertEqual(find_gcd(56, 48), 8)
        self.assertEqual(find_gcd(81, 27), 27)

    def test_zero(self):
        self.assertEqual(find_gcd(0, 42), 42)
        self.assertEqual(find_gcd(42, 0), 42)
        self.assertEqual(find_gcd(0, 0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, find_gcd, -24, 36)
        self.assertRaises(ValueError, find_gcd, 56, -48)


class TestCalculatePower(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_power(2, 3), 8)
        self.assertEqual(calculate_power(5, 2), 25)
        self.assertEqual(calculate_power(3, 4), 81)

    def test_zero_exponent(self):
        self.assertEqual(calculate_power(10, 0), 1)
        self.assertEqual(calculate_power(2.5, 0), 1)

    def test_negative_exponent(self):
        self.assertEqual(calculate_power(4, -2), 0.0625)
        self.assertEqual(calculate_power(8, -1), 0.125)


class TestReverseList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverse_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_list([42]), [42])

    def test_list_of_integers(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_list_of_strings(self):
        self.assertEqual(
            reverse_list(["apple", "banana", "cherry"]), ["cherry", "banana", "apple"]
        )


class TestRemoveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(
            remove_duplicates(["apple", "banana", "apple", "cherry"]),
            ["apple", "banana", "cherry"],
        )

    def test_list_without_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(
            remove_duplicates(["apple", "banana", "cherry"]),
            ["apple", "banana", "cherry"],
        )


class TestCountVowelsAndConsonants(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels_and_consonants(""), (0, 0))

    def test_all_vowels(self):
        self.assertEqual(count_vowels_and_consonants("AEIOUaeiou"), (10, 0))

    def test_mixed_vowels_and_consonants(self):
        self.assertEqual(count_vowels_and_consonants("Hello, World!"), (3, 7))

    def test_special_characters(self):
        self.assertEqual(count_vowels_and_consonants("12345!@#$"), (0, 0))


class TestGeneratePrimesInRange(unittest.TestCase):
    def test_invalid_ranges(self):
        self.assertRaises(ValueError, generate_primes_in_range_slow, -10, 10)
        self.assertRaises(ValueError, generate_primes_in_range_slow, 10, 5)

    def test_empty_range(self):
        self.assertEqual(generate_primes_in_range_slow(0, 0), [])

    def test_prime_ranges(self):
        self.assertEqual(generate_primes_in_range_slow(1, 10), [2, 3, 5, 7])
        self.assertEqual(generate_primes_in_range_slow(11, 20), [11, 13, 17, 19])


class TestFilterPalindromes(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_palindromes([]), [])

    def test_no_palindromes(self):
        self.assertEqual(filter_palindromes(["apple", "banana", "cherry"]), [])

    def test_single_letter_palindromes(self):
        self.assertEqual(
            filter_palindromes(["a", "b", "c", "d", "e", "f"]),
            ["a", "b", "c", "d", "e", "f"],
        )

    def test_mixed_palindromes(self):
        self.assertEqual(
            filter_palindromes(["racecar", "level", "hello", "world"]),
            ["racecar", "level"],
        )


class TestGenerateFibonacciSequence(unittest.TestCase):
    def test_zero_numbers(self):
        self.assertEqual(generate_fibonacci_sequence(0), [])

    def test_one_number(self):
        self.assertEqual(generate_fibonacci_sequence(1), [0])

    def test_two_numbers(self):
        self.assertEqual(generate_fibonacci_sequence(2), [0, 1])

    def test_positive_numbers(self):
        self.assertEqual(generate_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(
            generate_fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        )

    def test_negative_number(self):
        self.assertEqual(generate_fibonacci_sequence(-3), [])


class TestTransposeMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(transpose_matrix([]), [])

    def test_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transposed_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose_matrix(matrix), transposed_matrix)

    def test_rectangular_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        transposed_matrix = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(transpose_matrix(matrix), transposed_matrix)


class TestFactorInteger(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(factor_integer(17), [17])

    def test_composite_number(self):
        self.assertEqual(factor_integer(60), [2, 2, 3, 5])
        self.assertEqual(factor_integer(126), [2, 3, 3, 7])

    def test_large_number(self):
        self.assertEqual(factor_integer(999999), [3, 3, 3, 7, 11, 13, 37])

    def test_zero_and_negative_numbers(self):
        self.assertEqual(factor_integer(0), [])
        self.assertEqual(factor_integer(-42), [])
        self.assertEqual(factor_integer(-999), [])


class TestReverseWords(unittest.TestCase):
    def test_empty_sentence(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word_sentence(self):
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_sentence_with_punctuation(self):
        self.assertEqual(reverse_words("Hello, World!"), "World! Hello,")

    def test_multiple_spaces_between_words(self):
        self.assertEqual(reverse_words("   Hello     World!  "), "World! Hello")

    def test_complex_sentence(self):
        self.assertEqual(
            reverse_words("The quick brown fox jumps over the lazy dog"),
            "dog lazy the over jumps fox brown quick The",
        )


class TestFindCommonElements(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(find_common_elements([], []), [])

    def test_no_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3], [4, 5, 6]), [])

    def test_some_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])

    def test_duplicate_elements(self):
        self.assertEqual(find_common_elements([1, 1, 2, 3], [1, 2, 2, 3]), [1, 2, 3])


class TestDecimalToBinary(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(15), "1111")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")

    def test_negative_decimal(self):
        self.assertEqual(decimal_to_binary(-10), "-1010")
        self.assertEqual(decimal_to_binary(-15), "-1111")


class TestSumOfSquaresDifference(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_of_squares(5), 55)
        self.assertEqual(square_of_sum(5), 225)
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(square_of_sum(10), 3025)

    def test_zero(self):
        self.assertEqual(sum_of_squares(0), 0)
        self.assertEqual(square_of_sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(sum_of_squares(-5), 0)
        self.assertEqual(square_of_sum(-5), 0)


class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("example@example.com"))
        self.assertTrue(is_valid_email("user1234@example.co.uk"))
        self.assertTrue(is_valid_email("user.name@subdomain.example-domain.org"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("invalid_email.com"))
        self.assertFalse(is_valid_email("user@invalid@domain.com"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user@domain"))


class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_three_rows(self):
        self.assertEqual(generate_pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])


class TestPrintPascalsTriangle(unittest.TestCase):
    def test_printing(self):
        triangle = [[1], [1, 1], [1, 2, 1]]
        expected_output = "  1  \n 1 1 \n1 2 1\n"
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buf, redirect_stdout(buf):
            print_pascals_triangle(triangle)
            output = buf.getvalue()

        self.assertEqual(output, expected_output)


class TestMatrixMultiply(unittest.TestCase):
    def test_matrix_multiply(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        result = matrix_multiply(matrix1, matrix2)
        expected_result = [[58, 64], [139, 154]]
        self.assertEqual(result, expected_result)

        matrix3 = [[1, 2], [3, 4]]
        matrix4 = [[5, 6], [7, 8]]
        result = matrix_multiply(matrix3, matrix4)
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(result, expected_result)

    def test_invalid_matrix_multiply(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)


class TestFindCommonCharacters(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(find_common_characters("", ""), "")

    def test_no_common_characters(self):
        self.assertEqual(find_common_characters("hello", "world"), "lo")

    def test_some_common_characters(self):
        self.assertEqual(find_common_characters("programming", "python"), "nop")

    def test_duplicate_characters(self):
        self.assertEqual(find_common_characters("hello", "yellow"), "elo")


class TestIsArmstrongNumber(unittest.TestCase):
    def test_single_digit_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(0))
        self.assertTrue(is_armstrong_number(1))
        self.assertTrue(is_armstrong_number(2))
        self.assertTrue(is_armstrong_number(3))
        self.assertTrue(is_armstrong_number(4))
        self.assertTrue(is_armstrong_number(5))
        self.assertTrue(is_armstrong_number(6))
        self.assertTrue(is_armstrong_number(7))
        self.assertTrue(is_armstrong_number(8))
        self.assertTrue(is_armstrong_number(9))

    def test_two_digit_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(10))
        self.assertFalse(is_armstrong_number(11))  # Not an Armstrong number
        self.assertFalse(is_armstrong_number(12))  # Not an Armstrong number
        self.assertTrue(is_armstrong_number(89))

    def test_three_digit_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(153))
        self.assertTrue(is_armstrong_number(370))
        self.assertTrue(is_armstrong_number(371))
        self.assertTrue(is_armstrong_number(407))
        self.assertFalse(is_armstrong_number(123))  # Not an Armstrong number
        self.assertFalse(is_armstrong_number(999))  # Not an Armstrong number

    def test_large_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(9474))
        self.assertTrue(is_armstrong_number(9475))
        self.assertTrue(is_armstrong_number(93084))


class TestIsArmstrongNumber(unittest.TestCase):
    def test_single_digit_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(0))
        self.assertTrue(is_armstrong_number(1))
        self.assertTrue(is_armstrong_number(2))
        self.assertTrue(is_armstrong_number(3))
        self.assertTrue(is_armstrong_number(4))
        self.assertTrue(is_armstrong_number(5))
        self.assertTrue(is_armstrong_number(6))
        self.assertTrue(is_armstrong_number(7))
        self.assertTrue(is_armstrong_number(8))
        self.assertTrue(is_armstrong_number(9))

    def test_two_digit_armstrong_numbers(self):
        self.assertFalse(is_armstrong_number(10))
        self.assertFalse(is_armstrong_number(11))  # Not an Armstrong number
        self.assertFalse(is_armstrong_number(12))  # Not an Armstrong number
        self.assertFalse(is_armstrong_number(89))

    def test_three_digit_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(153))
        self.assertTrue(is_armstrong_number(370))
        self.assertTrue(is_armstrong_number(371))
        self.assertTrue(is_armstrong_number(407))
        self.assertFalse(is_armstrong_number(123))  # Not an Armstrong number
        self.assertFalse(is_armstrong_number(999))  # Not an Armstrong number

    def test_large_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(9474))
        self.assertFalse(is_armstrong_number(9475))
        self.assertTrue(is_armstrong_number(93084))


class TestStringCompressor(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(compress_string(""), "")

    def test_no_consecutive_duplicates(self):
        self.assertEqual(compress_string("abcdefg"), "a1b1c1d1e1f1g1")

    def test_consecutive_duplicates(self):
        self.assertEqual(compress_string("aaabbbcccdddaaa"), "a3b3c3d3a3")

    def test_mixed_characters(self):
        self.assertEqual(compress_string("aabbaaac"), "a2b2a3c1")

    def test_single_characters(self):
        self.assertEqual(compress_string("a"), "a1")
        self.assertEqual(compress_string("xyz"), "x1y1z1")


class TestStringCompressor(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(compress_string2(""), "")

    def test_no_consecutive_duplicates(self):
        self.assertEqual(compress_string2("abcdefg"), "abcdefg")

    def test_consecutive_duplicates(self):
        self.assertEqual(compress_string2("aaabbbcccdddaaa"), "a3b3c3d3a3")
        self.assertEqual(compress_string2("aaabbcdeeff"), "a3b2cde2f2")

    def test_mixed_characters(self):
        self.assertEqual(compress_string2("aabbaaac"), "a2b2a3c")

    def test_single_characters(self):
        self.assertEqual(compress_string2("a"), "a")
        self.assertEqual(compress_string2("xyz"), "xyz")


class TestCountSubstringOccurrences(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(count_substring_occurrences("", ""), 0)

    def test_no_occurrences(self):
        self.assertEqual(count_substring_occurrences("abcdefg", "xyz"), 0)

    def test_single_occurrence(self):
        self.assertEqual(count_substring_occurrences("aaabbbcccdddaaa", "bbb"), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_substring_occurrences("aaabbbcccdddaaa", "aa"), 4)
        self.assertEqual(count_substring_occurrences("aaabbcdeeff", "e"), 2)

    def test_overlapping_occurrences(self):
        self.assertEqual(count_substring_occurrences("aaaaa", "aa"), 4)
        self.assertEqual(count_substring_occurrences("aaaaa", "aaa"), 3)


class TestFindLargestPalindromeProduct(unittest.TestCase):
    def test_example(self):
        self.assertEqual(find_largest_palindrome_product(), 906609)


class TestSumPrimesBelowLimit(unittest.TestCase):
    def test_limit_below_2(self):
        self.assertEqual(sum_primes_below_limit(1), 0)
        self.assertEqual(sum_primes_below_limit(2), 0)

    def test_limit_10(self):
        self.assertEqual(sum_primes_below_limit(10), 17)

    def test_limit_20(self):
        self.assertEqual(sum_primes_below_limit(20), 77)

    def test_limit_50(self):
        self.assertEqual(sum_primes_below_limit(50), 328)


class TestCalculateQuadraticRoots(unittest.TestCase):
    def test_two_real_roots(self):
        self.assertEqual(calculate_quadratic_roots(1, -3, 2), (2.0, 1.0))

    def test_one_real_root(self):
        self.assertEqual(calculate_quadratic_roots(1, -4, 4), (2.0,))

    def test_no_real_roots(self):
        self.assertIsNone(calculate_quadratic_roots(1, 2, 5))

    def test_no_real_roots(self):
        self.assertIsNone(calculate_quadratic_roots(1, 2, 5))
        self.assertIsNone(calculate_quadratic_roots(2, 3, 10))
        self.assertIsNone(calculate_quadratic_roots(5, -4, 9))


class TestRemoveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        nums = []
        self.assertEqual(remove_duplicates(nums), 0)
        self.assertEqual(nums, [])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(nums), 5)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_duplicates_removed(self):
        nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
        self.assertEqual(remove_duplicates(nums), 5)
        self.assertEqual(nums[:5], [1, 2, 3, 4, 5])


class TestVigenereCipher(unittest.TestCase):
    def test_encryption_and_decryption(self):
        keyword = "KEY"
        plain_text = "HELLO"
        encrypted_text = vigenere_encrypt(plain_text, keyword)
        decrypted_text = vigenere_decrypt(encrypted_text, keyword)
        self.assertEqual(encrypted_text, "RIJVS")
        self.assertEqual(decrypted_text, plain_text)


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        message = "Hello, World!"
        shift = 3
        encrypted_message = caesar_encrypt(message, shift)
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        self.assertEqual(decrypted_message, message)

    def test_case_insensitivity(self):
        message = "AbCdEfGhIjKlMnOpQrStUvWxYz"
        shift = 5
        encrypted_message = caesar_encrypt(message, shift)
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        self.assertEqual(decrypted_message, message)

    def test_special_characters(self):
        message = "12345!@#$"
        shift = 1
        encrypted_message = caesar_encrypt(message, shift)
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        self.assertEqual(decrypted_message, message)
