# Activity Book Validator Module
# This module contains answer validation for Week 3 exercises
# Students import this to check their answers

import hashlib

def _h(x):
    """Hash function for answer validation"""
    return hashlib.md5(str(x).lower().strip().encode()).hexdigest()

def check_exercise_1_1(answer_1, answer_2, answer_3):
    """Check Exercise 1.1 answers about dataset basics"""
    print("Results:")
    
    # Q1: Total entries (149)
    if _h(answer_1) == "f2217062e9a397a1dca429e7d70bc6ca":
        print("  1. Total entries: Correct")
    else:
        print("  1. Total entries: Incorrect - check df.info() output")
    
    # Q2: Missing values (yes)
    if _h(answer_2) == "a6105c0a611b41b08f1209506350279e":
        print("  2. Missing values: Correct")
    else:
        print("  2. Missing values: Incorrect - look at Non-Null Count")
    
    # Q3: Data type (object)
    if _h(answer_3) == "a8cfde6331bd59eb2ac96f8911c4b666":
        print("  3. Data type: Correct")
    else:
        print("  3. Data type: Incorrect - check Dtype column")

def check_assessment_1(blank_1, blank_2, blank_3, blank_4, blank_5):
    """Check Assessment Question 1 - Fill in the blanks"""
    answers = [
        ("4c85b3625c95b8bf313d47934599eef5", "Data Cleaning"),
        ("3935f8feee087b4547de27296ec777b9", "Data Transformation"),
        ("281858037f7dcf7ed49271bb92c60526", "Ordinal encoding"),
        ("27369b3bf4483e8dcfd85ba9a39a947f", "hot"),
        ("615e65e2e8e3ffbc003c70f624779685", "coerce parameter")
    ]
    
    user_answers = [blank_1, blank_2, blank_3, blank_4, blank_5]
    score = 0
    
    print("Results:")
    for i, (correct_hash, _) in enumerate(answers, 1):
        if _h(user_answers[i-1]) == correct_hash:
            print(f"  {i}. Correct")
            score += 1
        else:
            print(f"  {i}. Incorrect")
    
    print(f"\nScore: {score}/5")

def check_assessment_2(mapping):
    """Check Assessment Question 2 - Priority mapping"""
    try:
        medium_val = mapping.get("Medium")
        high_val = mapping.get("High")
        
        # Medium should be 2, High should be 3
        if _h(medium_val) == "c81e728d9d4c2f636f067f89cc14862c" and \
           _h(high_val) == "eccbc87e4b5ce2fe28308fd9f2a7baf3":
            print("Correct! Your mapping follows the correct ordinal order.")
            return True
        else:
            print("Incorrect - remember ordinal values should reflect the order")
            print("Hint: Low=1, so what should Medium and High be?")
            return False
    except:
        print("Error: Please make sure your mapping is a dictionary with 'Medium' and 'High' keys")
        return False

def check_exercise_4_1(mapping):
    """Check Exercise 4.1 - Attendance ordinal encoding"""
    try:
        val_75_90 = mapping.get("75-90%")
        val_above_90 = mapping.get("Above 90%")
        
        results = []
        if _h(val_75_90) == "eccbc87e4b5ce2fe28308fd9f2a7baf3":
            results.append("75-90% mapping: Correct")
        else:
            results.append("75-90% mapping: Incorrect")
            
        if _h(val_above_90) == "a87ff679a2f3e71d9181a67b7542122c":
            results.append("Above 90% mapping: Correct")
        else:
            results.append("Above 90% mapping: Incorrect")
        
        for r in results:
            print(r)
            
        if "Incorrect" not in str(results):
            print("\nAll correct! Encoding ready to apply.")
            return True
        return False
    except:
        print("Error: Please replace ___ with numeric values")
        return False

def check_exercise_5_1(digital_engagement_series):
    """Check Exercise 5.1 - Digital engagement feature"""
    try:
        if digital_engagement_series is not None and len(digital_engagement_series) > 0:
            print("Feature created successfully!")
            print(f"  Min value: {digital_engagement_series.min()}")
            print(f"  Max value: {digital_engagement_series.max()}")
            print(f"  Mean value: {digital_engagement_series.mean():.2f}")
            return True
        else:
            print("Feature not created. Check your code.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
