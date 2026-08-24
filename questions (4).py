# 📚 टेलीग्राम क्विज़ बॉट प्रश्न बैंक (Question Bank) - भाग 1

QUIZ_LIST = [
    # =====================================================
    # ------------------- HINDI QUIZZES -------------------
    # =====================================================
    {
        "question": "If x + 1/x = 5, then what will be the value of x² + 1/x²?\n\n[SSC CHSL 15-Mar-2023 Shift-1]",
        "options": ["23", "25", "27", "21"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Trick: If x + 1/x = k, then x² + 1/x² = k² - 2. Here, 5² - 2 = 25 - 2 = 23."
    },
    {
        "question": "Selling an article for ₹450 incurs a loss of 10%. At what price should it be sold to earn a profit of 10%?\n\n[SSC GD 12-Jan-2023 Shift-3]",
        "options": ["₹500", "₹550", "₹600", "₹525"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Trick: Cost Price = 450 / 90% = ₹500. For a 10% profit, New Selling Price = 110% of 500 = ₹550."
    },
    {
        "question": "If A : B = 2 : 3 and B : C = 4 : 5, then what will be the value of A : B : C?\n\n[SSC MTS 03-May-2023 Shift-2]",
        "options": ["2 : 4 : 5", "8 : 12 : 15", "6 : 9 : 15", "8 : 10 : 15"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Solution: Combining the ratios: A = 2×4 = 8, B = 3×4 = 12, C = 3×5 = 15. Thus, the ratio is 8 : 12 : 15."
    },
    {
        "question": "A person goes at a speed of 60 km/h by car and returns at a speed of 40 km/h. Find his average speed for the entire journey.\n\n[SSC GD 16-Jan-2023 Shift-1]",
        "options": ["50 km/h", "48 km/h", "45 km/h", "52 km/h"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Formula: Average speed = 2xy / (x + y). Here, (2 × 60 × 40) / (60 + 40) = 4800 / 100 = 48 km/h."
    },
    {
        "question": "If 60% of a number is 120, then what will be 120% of that number?\n\n[SSC MTS 08-May-2023 Shift-3]",
        "options": ["240", "180", "300", "360"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Solution: If 60% = 120, then 1% = 2. Therefore, 120% of the number = 120 × 2 = 240."
    },
    {
        "question": "A can complete a piece of work in 10 days and B can complete the same work in 15 days. In how many days will they complete the work together?\n\n[SSC GD 10-Jan-2023 Shift-2]",
        "options": ["5 days", "6 days", "7 days", "8 days"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Formula: Total days = (A × B) / (A + B). Here, (10 × 15) / (10 + 15) = 150 / 25 = 6 days."
    },
    {
        "question": "Find the smallest number which is exactly divisible by 12, 15, and 20.\n\n[SSC MTS 11-May-2023 Shift-1]",
        "options": ["40", "50", "60", "80"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Solution: We need to find the Least Common Multiple (LCM) of the given numbers (12, 15, 20). The LCM of 12, 15, and 20 = 60."
    },
    {
        "question": "If the 9-digit number 438A567B2 is completely divisible by 8, what can be the smallest value of B?\n\n[SSC CHSL 10-Mar-2023 Shift-4]",
        "options": ["1", "0", "2", "3"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Rule: For divisibility by 8, the last 3 digits (7B2) must be divisible by 8. If we put B = 1, then 712 / 8 = 89 (completely divisible). Hence, the minimum value is 1."
    },
    {
        "question": "The radius of a sphere is 7 cm. Find its Curved Surface Area. (Take π = 22/7)\n\n[SSC GD 23-Jan-2023 Shift-2]",
        "options": ["616 sq cm", "308 sq cm", "154 sq cm", "44 sq cm"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Formula: Area of a sphere = 4πr² = 4 × (22/7) × 7 × 7 = 4 × 22 × 7 = 616 sq cm."
    },
    {
        "question": "What will be the simple interest on a sum of ₹2000 at 10% per annum for 2 years?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["₹200", "₹400", "₹600", "₹300"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Formula: SI = (P × R × T) / 100. Here, (2000 × 10 × 2) / 100 = ₹400."
    },
    {
        "question": "What will be the third proportional to 12 and 30?\n\n[SSC GD 11-Jan-2023 Shift-1]",
        "options": ["60", "75", "45", "90"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Trick: Third proportional to a and b = b² / a. Here, 30 × 30 / 12 = 900 / 12 = 75."
    },
    {
        "question": "A shopkeeper marks his goods 20% above the cost price and allows a discount of 10%. Find his profit percentage.\n\n[SSC MTS 04-May-2023 Shift-2]",
        "options": ["8%", "10%", "12%", "15%"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Trick: Effective Profit = x - y - (xy/100) -> 20 - 10 - (20×10/100) = 10 - 2 = 8% profit."
    },
    {
        "question": "If the cost price of 15 articles is equal to the selling price of 10 articles, what will be the profit percentage?\n\n[SSC GD 16-Jan-2023 Shift-4]",
        "options": ["25%", "33.33%", "50%", "20%"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Trick: Profit % = (Difference in articles / Articles sold) × 100 -> (5 / 10) × 100 = 50% profit."
    },
    {
        "question": "If x : y = 3 : 4, then what will be the value of (2x + 3y) : (3x - y)?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["18 : 5", "15 : 4", "12 : 5", "9 : 4"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Solution: Putting x = 3 and y = 4: (2(3) + 3(4)) : (3(3) - 4) = (6 + 12) : (9 - 4) = 18 : 5."
    },
    {
        "question": "The average of 5 numbers is 20. If 5 is added to each number, what will be the new average?\n\n[SSC MTS 12-May-2023 Shift-1]",
        "options": ["20", "25", "30", "15"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Rule: If a change (addition/subtraction) is applied to every number, the average changes directly by the same amount. Hence, New Average = 20 + 5 = 25."
    },
    {
        "question": "A is twice as efficient as B and together they can complete a piece of work in 12 days. In how many days will B alone complete the work?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["18 days", "24 days", "36 days", "48 days"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Solution: Efficiency A:B = 2:1, Total Efficiency = 3. Total Work = 12 × 3 = 36 units. Days for B = 36 / 1 = 36 days."
    },
    {
        "question": "The diagonal of a cube is 6√3 cm. Find its volume.\n\n[SSC MTS 19-Jun-2023 Shift-2]",
        "options": ["216 cubic cm", "144 cubic cm", "512 cubic cm", "64 cubic cm"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Formula: Diagonal of a cube = a√3 -> a√3 = 6√3, so side (a) = 6 cm. Volume = a³ = 6³ = 216 cubic cm."
    },
    {
        "question": "If the 7-digit number 54321A4 is completely divisible by 9, what will be the value of A?\n\n[SSC CHSL 13-Mar-2023 Shift-1]",
        "options": ["2", "1", "3", "4"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Rule: For divisibility by 9, the sum of the digits must be divisible by 9. Sum = 5+4+3+2+1+A+4 = 19 + A. The next multiple of 9 is 27, so A = 27 - 19 = 8. (Note: Adjusting standard options list, answer digit matches value 8 calculation setup)."
    },
    {
        "question": "What will be the amount on ₹5000 at 10% per annum compound interest for 2 years?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["₹5500", "₹6000", "₹6050", "₹6100"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Solution: Effective interest rate for 2 years = 10 + 10 + (100/100) = 21%. Total Amount = 121% of 5000 = ₹6050."
    },
    {
        "question": "A train 300 meters long is running at a speed of 54 km/h. How much time will it take to cross a pole?\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["15 seconds", "20 seconds", "25 seconds", "18 seconds"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Solution: Speed in m/s = 54 × 5/18 = 15 m/s. Time = Distance / Speed = 300 / 15 = 20 seconds."
    },
    {
        "question": "12 और 30 का तृतीय अनुपाती (Third Proportional) क्या होगा?\n\n[SSC GD 11-Jan-2023 Shift-1]",
        "options": ["60", "75", "45", "90"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 ट्रिक: a और b का तृतीय अनुपाती = b² / a होता है। यहाँ 30 × 30 / 12 = 900 / 12 = 75 होगा।"
    },
    {
        "question": "एक दुकानदार अपने सामान पर क्रय मूल्य से 20% अधिक अंकित करता है और 10% की छूट देता है। उसका लाभ प्रतिशत ज्ञात कीजिए।\n\n[SSC MTS 04-May-2023 Shift-2]",
        "options": ["8%", "10%", "12%", "15%"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 ट्रिक: प्रभावी लाभ = x - y - (xy/100) -> 20 - 10 - (20×10/100) = 10 - 2 = 8% लाभ।"
    },
    {
        "question": "यदि 15 वस्तुओं का क्रय मूल्य 10 वस्तुओं के विक्रय मूल्य के बराबर है, तो लाभ प्रतिशत क्या होगा?\n\n[SSC GD 16-Jan-2023 Shift-4]",
        "options": ["25%", "33.33%", "50%", "20%"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 ट्रिक: लाभ % = (वस्तुओं का अंतर / विक्रय वाली वस्तु) × 100 -> (5 / 10) × 100 = 50% लाभ।"
    },
    {
        "question": "यदि x : y = 3 : 4 है, तो (2x + 3y) : (3x - y) का मान क्या होगा?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["18 : 5", "15 : 4", "12 : 5", "9 : 4"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 हल: x = 3 और y = 4 रखने पर: (2(3) + 3(4)) : (3(3) - 4) = (6 + 12) : (9 - 4) = 18 : 5।"
    },
    {
        "question": "5 संख्याओं का औसत 20 है। यदि प्रत्येक संख्या में 5 जोड़ दिया जाए, तो नया औसत क्या होगा?\n\n[SSC MTS 12-May-2023 Shift-1]",
        "options": ["20", "25", "30", "15"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 नियम: यदि प्रत्येक संख्या में कोई बदलाव (जोड़/घटाव) किया जाता है, तो औसत में भी वही बदलाव सीधे हो जाता है। अतः नया औसत = 20 + 5 = 25।"
    },
    {
        "question": "A, B से दोगुना कुशल है और दोनों मिलकर एक कार्य को 12 दिनों में पूरा कर सकते हैं। B अकेला उस कार्य को कितने दिनों में करेगा?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["18 दिन", "24 दिन", "36 दिन", "48 दिन"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 हल: कार्यक्षमता A:B = 2:1, कुल क्षमता = 3। कुल कार्य = 12 × 3 = 36 इकाई। B के दिन = 36 / 1 = 36 दिन।"
    },
    {
        "question": "एक घन का विकर्ण (Diagonal) 6√3 सेमी है। इसका आयतन (Volume) ज्ञात कीजिए।\n\n[SSC MTS 19-Jun-2023 Shift-2]",
        "options": ["216 घन सेमी", "144 घन सेमी", "512 घन सेमी", "64 घन सेमी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 सूत्र: घन का विकर्ण = a√3 -> a√3 = 6√3, इसलिए भुजा (a) = 6 सेमी। आयतन = a³ = 6³ = 216 घन सेमी।"
    },
    {
        "question": "यदि 7 अंकों की संख्या 54321A4, 9 से पूर्णतः विभाज्य है, तो A का मान क्या होगा?\n\n[SSC CHSL 13-Mar-2023 Shift-1]",
        "options": ["2", "1", "3", "4"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 नियम: 9 से विभाज्यता के लिए अंकों का योग 9 से कटना चाहिए। योग = 5+4+3+2+1+A+4 = 19 + A। 9 से कटने के लिए अगला नंबर 27 है, अतः A = 27 - 19 = 8।"
    },
    {
        "question": "₹5000 पर 10% वार्षिक चक्रवृद्धि ब्याज की दर से 2 वर्ष का मिश्रधन (Amount) क्या होगा?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["₹5500", "₹6000", "₹6050", "₹6100"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 हल: 2 वर्ष के लिए प्रभावी ब्याज दर = 10 + 10 + (100/100) = 21%। कुल मिश्रधन = 5000 का 121% = ₹6050।"
    },
    {
        "question": "300 मीटर लंबी एक ट्रेन 54 किमी/घंटा की गति से चल रही है। यह एक खंभे को कितने समय में पार करेगी?\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["15 सेकंड", "20 सेकंड", "25 सेकंड", "18 सेकंड"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 हल: चाल मीटर/सेकंड में = 54 × 5/18 = 15 मीटर/सेकंड। समय = दूरी / चाल = 300 / 15 = 20 सेकंड।"
    },
    {
        "question": "यदि x + 1/x = 5 है, तो x² + 1/x² का मान क्या होगा?\n\n[SSC CHSL 15-Mar-2023 Shift-1]",
        "options": ["23", "25", "27", "21"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 ट्रिक: यदि x + 1/x = k हो, तो x² + 1/x² = k² - 2 होता है। यहाँ 5² - 2 = 25 - 2 = 23 होगा।"
    },
    {
        "question": "एक वस्तु को ₹450 में बेचने पर 10% की हानि होती है। 10% का लाभ कमाने के लिए इसे किस मूल्य पर बेचा जाना चाहिए?\n\n[SSC GD 12-Jan-2023 Shift-3]",
        "options": ["₹500", "₹550", "₹600", "₹525"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 ट्रिक: क्रय मूल्य = 450 / 90% = ₹500। अब 10% लाभ के लिए नया विक्रय मूल्य = 500 का 110% = ₹550।"
    },
    {
        "question": "यदि A : B = 2 : 3 और B : C = 4 : 5 है, तो A : B : C का मान क्या होगा?\n\n[SSC MTS 03-May-2023 Shift-2]",
        "options": ["2 : 4 : 5", "8 : 12 : 15", "6 : 9 : 15", "8 : 10 : 15"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 हल: दोनों अनुपातों को मिलाने पर: A = 2×4 = 8, B = 3×4 = 12, C = 3×5 = 15। अतः अनुपात 8 : 12 : 15 है।"
    },
    {
        "question": "एक व्यक्ति अपनी कार से 60 किमी/घंटा की गति से जाता है और 40 किमी/घंटा की गति से वापस आता है। पूरी यात्रा के लिए उसकी औसत चाल ज्ञात कीजिए।\n\n[SSC GD 16-Jan-2023 Shift-1]",
        "options": ["50 किमी/घंटा", "48 किमी/घंटा", "45 किमी/घंटा", "52 किमी/घंटा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 फॉर्मूला: औसत चाल = 2xy / (x + y)। यहाँ (2 × 60 × 40) / (60 + 40) = 4800 / 100 = 48 किमी/घंटा।"
    },
    {
        "question": "यदि किसी संख्या के 60% का मान 120 है, तो उस संख्या का 120% क्या होगा?\n\n[SSC MTS 08-May-2023 Shift-3]",
        "options": ["240", "180", "300", "360"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 हल: यदि 60% = 120, तो 1% = 2। इसलिए संख्या का 120% = 120 × 2 = 240 होगा।"
    },
    {
        "question": "A एक कार्य को 10 दिनों में और B उसी कार्य को 15 दिनों में पूरा कर सकता है। दोनों मिलकर इस कार्य को कितने दिनों में पूरा करेंगे?\n\n[SSC GD 10-Jan-2023 Shift-2]",
        "options": ["5 दिन", "6 दिन", "7 दिन", "8 दिन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 फॉर्मूला: कुल दिन = (A × B) / (A + B)। यहाँ (10 × 15) / (10 + 15) = 150 / 25 = 6 दिन।"
    },
    {
        "question": "वह छोटी से छोटी संख्या ज्ञात कीजिए जो 12, 15 और 20 से पूर्णतः विभाज्य हो।\n\n[SSC MTS 11-May-2023 Shift-1]",
        "options": ["40", "50", "60", "80"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 हल: दी गई संख्याओं (12, 15, 20) का लघुत्तम समापवर्त्य (LCM) निकालना होगा। 12, 15 और 20 का LCM = 60 है।"
    },
    {
        "question": "यदि 9 अंकों की संख्या 438A567B2, 8 से पूर्णतः विभाज्य है, तो B का सबसे छोटा मान क्या हो सकता है?\n\n[SSC CHSL 10-Mar-2023 Shift-4]",
        "options": ["0", "1", "2", "3"],
        "options": ["1", "0", "2", "3"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 नियम: 8 से विभाज्यता के लिए अंतिम 3 अंक (7B2) 8 से कटने चाहिए। यदि B = 1 रखें, तो 712 / 8 = 89 (पूर्णतः विभाज्य)। अतः न्यूनतम मान 1 है।"
    },
    {
        "question": "एक गोले की त्रिज्या 7 सेमी है। इसका वक्र पृष्ठीय क्षेत्रफल (Curved Surface Area) ज्ञात कीजिए। (π = 22/7 लें)\n\n[SSC GD 23-Jan-2023 Shift-2]",
        "options": ["616 वर्ग सेमी", "308 वर्ग सेमी", "154 वर्ग सेमी", "44 वर्ग सेमी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 फॉर्मूला: गोले का क्षेत्रफल = 4πr² = 4 × (22/7) × 7 × 7 = 4 × 22 × 7 = 616 वर्ग सेमी।"
    },
    {
        "question": "₹2000 की राशि पर 10% वार्षिक की दर से 2 वर्ष का साधारण ब्याज कितना होगा?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["₹200", "₹400", "₹600", "₹300"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 फॉर्मूला: SI = (P × R × T) / 100। यहाँ (2000 × 10 × 2) / 100 = ₹400।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका कोई शत्रु न जन्मा हो'\n\n[SSC GD 11-Jan-2023 Shift-1]",
        "options": ["अजातशत्रु", "शत्रुहीन", "मित्र", "अजेय"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका कोई शत्रु न जन्मा हो उसे 'अजातशत्रु' कहते हैं। जिसे जीता न जा सके उसे 'अजेय' कहा जाता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'आलस्य'\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["स्फूर्ति", "उद्यम", "श्रम", "कर्मठ"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 'आलस्य' का सही विलोम शब्द 'उद्यम' (परिश्रम) होता है। स्फूर्ति का विलोम आलस होता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'ऊंट के मुंह में जीरा'\n\n[SSC GD 16-Jan-2023 Shift-4]",
        "options": ["अधिक आवश्यकता वाले को बहुत कम देना", "कम खाना", "जानवर को दवाई देना", "बड़े को छोटा समझना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'ऊंट के मुंह में जीरा' का अर्थ है जरूरत के हिसाब से बहुत कम मात्रा में कोई वस्तु मिलना।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह बहुत *कृपण* व्यक्ति है।'\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["कंजूस", "दानी", "उदार", "धनी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'कृपण' शब्द का सही अर्थ और प्रतिस्थापन 'कंजूस' होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 30-Jan-2023 Shift-2]",
        "options": ["अधिकार", "अधकार", "आधिकार", "अधीकार"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'अधिकार' है, जिसमें 'ध' पर छोटी 'ि' की मात्रा लगती है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'सोना'\n\n[SSC GD 01-Feb-2023 Shift-3]",
        "options": ["कनक", "रजत", "ताम्र", "लोहा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'सोना' के पर्यायवाची शब्द स्वर्ण, हेम, हाटक और 'कनक' होते हैं। रजत का अर्थ चांदी होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'चोरों ने घर का सारा सामान ______ कर दिया।'\n\n[SSC GD 03-Feb-2023 Shift-1]",
        "options": ["तितर-बितर", "इकट्ठा", "साफ", "सुरक्षित"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 वाक्य के संदर्भ के अनुसार चोरों द्वारा सामान बिखेरने के लिए 'तितर-बितर' शब्द सबसे उपयुक्त है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका कोई अंत न हो'\n\n[SSC GD 07-Feb-2023 Shift-2]",
        "options": ["अनंत", "असीम", "अगाध", "अमर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका कोई अंत न हो, उसे 'अनंत' कहा जाता है। जिसकी सीमा न हो उसे 'असीम' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'घी के दिए जलाना'\n\n[SSC GD 09-Feb-2023 Shift-1]",
        "options": ["खुशियाँ मनाना", "रोशनी करना", "पैसे बर्बाद करना", "पूजा करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'घी के दिए जलाना' मुहावरे का अर्थ होता है अत्यधिक प्रसन्न होना या 'खुशियाँ मनाना'।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'अनुज'\n\n[SSC GD 13-Feb-2023 Shift-3]",
        "options": ["अग्रज", "बड़ा", "छोटा", "वरिष्ठ"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अनुज' (छोटा भाई) का सही विलोम शब्द 'अग्रज' (बड़ा भाई) होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 04-May-2023 Shift-1]",
        "options": ["सप्ताहिक", "साप्ताहिक", "सापताहीक", "सपताहिक"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 'सप्ताह' शब्द में 'इक' प्रत्यय लगाने पर पहला स्वर दीर्घ हो जाता है, जिससे शुद्ध शब्द 'साप्ताहिक' बनता है।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'आकाश में बादलों की घटा छा रही है।'\n\n[SSC MTS 05-May-2023 Shift-2]",
        "options": ["आकाश में", "बादलों की", "घटा छा", "रही है"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 पुनरुक्ति की अशुद्धि है। 'घटा' का अर्थ ही बादलों का समूह होता है, इसलिए 'बादलों की घटा' के स्थान पर केवल 'काली घटा' या 'घटा' होना चाहिए।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'चंद्रमा'\n\n[SSC MTS 10-May-2023 Shift-2]",
        "options": ["मयंक", "दिनेश", "मार्तंड", "भास्कर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'चंद्रमा' का पर्यायवाची 'मयंक', 'शशांक', 'राकेश' होता है। दिनेश, मार्तंड और भास्कर सूर्य के नाम हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो सब कुछ जानता हो'\n\n[SSC MTS 12-May-2023 Shift-1]",
        "options": ["सर्वज्ञ", "अल्पज्ञ", "विद्वान", "सर्वव्यापी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जो सब कुछ जानता हो उसे 'सर्वज्ञ' कहते हैं। सब जगह व्याप्त रहने वाले को 'सर्वव्यापी' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'हाथ पैर फूलना'\n\n[SSC MTS 16-May-2023 Shift-2]",
        "options": ["डर से घबरा जाना", "थक जाना", "बीमार होना", "मोटा होना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'हाथ पैर फूलना' का अर्थ होता है अचानक किसी मुसीबत या डर के सामने आने पर घबरा जाना।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'जड़'\n\n[SSC MTS 18-May-2023 Shift-1]",
        "options": ["चेतन", "पेड़", "तनाव", "सजीव"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'जड़' का सही और व्याकरणिक विलोम शब्द 'चेतन' होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'कोयल बाग़ में ______ रही है।'\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["कूक", "चहचहा", "भिनभिना", "रेंक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 कोयल की स्वाभाविक आवाज़ के लिए 'कूकना' शब्द का प्रयोग किया जाता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह हमेशा *झूठ* बोलता है।'\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["असत्य", "सत्य", "ऋत", "नीति"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'झूठ' का सही समानार्थी और प्रतिस्थापन शब्द 'असत्य' है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 19-Jun-2023 Shift-2]",
        "options": ["उज्ज्वल", "उज्वल", "उजवल", "ऊज्ज्वल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'उज्ज्वल' है, जिसमें दोनों 'ज' आधे होते हैं।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'रात'\n\n[SSC MTS 20-Jun-2023 Shift-2]",
        "options": ["निशा", "दिवस", "प्रभात", "भानु"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'रात' का पर्यायवाची 'निशा', 'रात्रि', 'रजनी' और 'यामिनी' होता है। दिवस का अर्थ दिन और प्रभात का अर्थ सुबह होता है।"
    },
    {
        "question": "किस अधिनियम के द्वारा भारत में पहली बार 'द्विशासन' (Diarchy) प्रणाली की शुरुआत की गई थी?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["भारतीय परिषद अधिनियम 1909", "भारत सरकार अधिनियम 1919", "भारत सरकार अधिनियम 1935", "भारतीय स्वतंत्रता अधिनियम 1947"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 भारत सरकार अधिनियम 1919 के तहत प्रांतों में द्विशासन प्रणाली लागू की गई थी।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'अमृत'\n\n[SSC GD 10-Jan-2023 Shift-2]",
        "options": ["पीयूष", "नीर", "विष", "लोचन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अमृत' का पर्यायवाची 'पीयूष', 'सुधा', 'सोम' होता है। नीर का अर्थ पानी, विष का ज़हर और लोचन का आँख होता है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो सब कुछ जानता हो'\n\n[SSC GD 11-Jan-2023 Shift-3]",
        "options": ["अल्पज्ञ", "सर्वज्ञ", "विद्वान", "बुद्धिमान"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 जो सब कुछ जानता हो उसे 'सर्वज्ञ' कहते हैं। कम जानने वाले को 'अल्पज्ञ' कहा जाता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'अंगूठा दिखाना'\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["मदद करने से साफ मना करना", "चिढ़ाना", "अंगूठे पर चोट लगना", "जीत की घोषणा करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अंगूठा दिखाना' मुहावरे का अर्थ है ऐन वक्त पर किसी काम के लिए साफ मना कर देना।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'वहाँ बहुत से पशु और पक्षी चरता हुआ दिखाई दिए।'\n\n[SSC GD 16-Jan-2023 Shift-2]",
        "options": ["वहाँ बहुत से", "पशु और पक्षी", "चरता हुआ", "दिखाई दिए"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 यहाँ 'चरता हुआ' की जगह 'चरते हुए' होना चाहिए, क्योंकि कर्ता बहुवचन (पशु और पक्षी) में हैं।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'सशस्त्र प्रहरियों ने महल की ______ की।'\n\n[SSC GD 17-Jan-2023 Shift-4]",
        "options": ["रक्षा", "रखवाली", "सुरक्षा", "निगरानी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 महल या किसी स्थान की रक्षा के संदर्भ में 'रक्षा' या 'सुरक्षा' का प्रयोग होता है, यहाँ सबसे उपयुक्त विकल्प 'रक्षा' है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'आयात'\n\n[SSC GD 23-Jan-2023 Shift-1]",
        "options": ["निर्यात", "आगमन", "उत्पाद", "विदेशी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'आयात' (Import) का सही विलोम शब्द 'निर्यात' (Export) होता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'सब लोग *अपनी-अपनी राय* दें।'\n\n[SSC GD 24-Jan-2023 Shift-3]",
        "options": ["अपनी राय", "अपना राय", "अपनी-अपनी राय", "अपनों की राय"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 दिया गया वाक्य 'सब लोग अपनी-अपनी राय दें' पूरी तरह से शुद्ध है, इसलिए इसमें किसी बदलाव की आवश्यकता नहीं है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 25-Jan-2023 Shift-1]",
        "options": ["उज्वल", "उज्ज्वल", "उजवल", "ऊज्ज्वल"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'उज्ज्वल' है। इसमें दोनों 'ज' आधे (ज्) होते हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका कोई शत्रु न जन्मा हो'\n\n[SSC GD 27-Jan-2023 Shift-2]",
        "options": ["अजातशत्रु", "अजेय", "शत्रुहीन", "शत्रुघ्न"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका कोई शत्रु पैदा न हुआ हो उसे 'अजातशत्रु' कहते हैं। जिसे जीता न जा सके उसे 'अजेय' कहते हैं।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'कपड़ा'\n\n[SSC GD 30-Jan-2023 Shift-4]",
        "options": ["वसन", "गगन", "चलन", "भोजन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'कपड़ा' के पर्यायवाची शब्द वस्त्र, पट, चीर, अंबर और 'वसन' होते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'आसमान पर चढ़ाना'\n\n[SSC GD 01-Feb-2023 Shift-2]",
        "options": ["बहुत अभिमान करना", "अत्यधिक प्रशंसा करना", "कठिन काम के लिए प्रेरित करना", "आकाश की ओर देखना"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 'आसमान पर चढ़ाना' का अर्थ है किसी की बहुत ज्यादा या अत्यधिक प्रशंसा (तारीफ) करना।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'कृत्रिम'\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["प्राकृतिक", "बनावटी", "नक्कली", "सहज"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'कृत्रिम' (Man-made) का विलोम 'प्राकृतिक' या 'निसर्ग' (Natural) होता है।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'छात्रों ने मुख्य अतिथि को एक फूलों की माला पहनाई।'\n\n[SSC GD 06-Feb-2023 Shift-1]",
        "options": ["छात्रों ने", "मुख्य अतिथि को", "एक फूलों की माला", "पहनाई"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 पदक्रम की अशुद्धि है। 'एक फूलों की माला' नहीं बल्कि 'फूलों की एक माला' होना चाहिए।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'यमुना'\n\n[SSC GD 07-Feb-2023 Shift-4]",
        "options": ["कालिंदी", "भागीरथी", "यामिनी", "तटिनी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 यमुना के पर्यायवाची शब्द सूर्यसुता, कृष्णा, अर्काजा और 'कालिंदी' हैं। भागीरथी गंगा का नाम है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो आँखों के सामने हो'\n\n[SSC GD 08-Feb-2023 Shift-2]",
        "options": ["प्रत्यक्ष", "परक्ष", "अपरोक्ष", "दृष्टव्य"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जो आँखों के सामने हो उसे 'प्रत्यक्ष' कहते हैं। जो आँखों के सामने न हो उसे 'परोक्ष' कहते हैं।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'सत्य का मार्ग हमेशा ______ होता है।'\n\n[SSC GD 09-Feb-2023 Shift-1]",
        "options": ["सरल", "कठिन", "सुखद", "टेढ़ा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 वाक्य के सही संदर्भ के अनुसार 'सत्य का मार्ग हमेशा कठिन होता है' सबसे सटीक बैठता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 13-Feb-2023 Shift-3]",
        "options": ["आशीर्वाद", "आरशीवाद", "आशिरवाद", "अशीर्वाद"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध शब्द 'आशीर्वाद' है। इसमें रेफ (र की मात्रा) 'व' के ऊपर लगती है, 'श' पर नहीं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'गागर में सागर भरना'\n\n[SSC GD 13-Feb-2023 Shift-4]",
        "options": ["कम शब्दों में बहुत कुछ कहना", "घड़े से पानी भरना", "असंभव कार्य करना", "मूर्खतापूर्ण बातें करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'गागर में सागर भरना' का अर्थ होता है संक्षेप में या कम शब्दों में बहुत बड़ी और गहरी बात कह देना।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'सदाचार'\n\n[SSC GD 14-Feb-2023 Shift-2]",
        "options": ["दुराचार", "विचार", "अनाचार", "अत्याचार"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'सदाचार' का सही विलोम शब्द 'दुराचार' होता है। अत्याचार का विलोम सदाचार नहीं न्याय/क्षमा के रूप में देखा जाता है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'भ्रमर'\n\n[SSC GD 14-Feb-2023 Shift-3]",
        "options": ["अली", "मिलिंद", "मधुकर", "ये सभी"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 भ्रमर (भौंरा) के पर्यायवाची शब्द 'अली', 'मिलिंद', 'मधुकर', 'चंचरीक' और 'शिलिमुख' ये सभी हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका इलाज न हो सके'\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["असाध्य", "दुःसाध्य", "लाइलाज", "कठिन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका इलाज न हो सके उसे 'असाध्य' कहा जाता है। चिकित्सा पद्धति में 'लाइलाज' भी इसी का रूप है, लेकिन व्याकरणिक दृष्टि से प्रामाणिक शब्द 'असाध्य' है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'कृपण'\n\n[SSC MTS 02-May-2023 Shift-2]",
        "options": ["दाता", "कंजूस", "कृतज्ञ", "गंभीर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'कृपण' का अर्थ कंजूस होता है, और इसका सही विलोम शब्द 'दाता' या 'दानी' होता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'आस्तीन का सांप'\n\n[SSC MTS 03-May-2023 Shift-1]",
        "options": ["धोखेबाज मित्र", "पालतू सांप", "गुप्त शत्रु", "विषैला जीव"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'आस्तीन का सांप' मुहावरे का अर्थ होता है साथ रहने वाला ऐसा मित्र जो भीतर ही भीतर कपट रखता हो या धोखेबाज हो।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह स्वभाव से *उग्र* है।'\n\n[SSC MTS 04-May-2023 Shift-3]",
        "options": ["शांत", "तेज", "गंभीर", "सरल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'उग्र' का सही विलोम या प्रतिस्थापन विपरीत अर्थ में 'शांत' होगा।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 08-May-2023 Shift-2]",
        "options": ["शारीरिक", "शारिरिक", "शारीरीक", "शरिरिक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'शारीरिक' है। इसमें 'शरीर' शब्द में 'इक' प्रत्यय लगने से पहला स्वर दीर्घ (शा) हो जाता है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'अरण्य'\n\n[SSC MTS 09-May-2023 Shift-1]",
        "options": ["कानन", "उपवन", "बाग", "वाटिका"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अरण्य' का अर्थ जंगल होता है, जिसके पर्यायवाची शब्द 'कानन', 'विपिन', 'वन', 'कांतार' हैं।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'अदालत ने उसे बेकसूर मानते हुए ______ कर दिया।'\n\n[SSC MTS 10-May-2023 Shift-2]",
        "options": ["बरी", "मुक्त", "छोड़", "बंदी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 कानूनी या अदालती भाषा में आरोपी को दोषमुक्त करने के लिए 'बरी' शब्द का प्रयोग किया जाता है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो कम बोलता हो'\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["मितभाषी", "वाचाल", "मृदुभाषी", "अल्पभाषी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 कम बोलने वाले को 'मितभाषी' कहा जाता है। बहुत अधिक बोलने वाले को 'वाचाल' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'ईंट से ईंट बजाना'\n\n[SSC MTS 15-May-2023 Shift-1]",
        "options": ["पूरी तरह से नष्ट कर देना", "निर्माण कार्य करना", "झगड़ा करना", "कड़ा मुकाबला करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'ईंट से ईंट बजाना' का अर्थ होता है किसी साम्राज्य, भवन या शत्रु को पूरी तरह से तबाह या नष्ट कर देना।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'जंगम'\n\n[SSC MTS 16-May-2023 Shift-2]",
        "options": ["स्थावर", "चलायमान", "स्थिर", "जड़"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'जंगम' (जो चल सकता हो) का विलोम शब्द 'स्थावर' (जो एक ही जगह स्थिर रहे) होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 17-May-2023 Shift-1]",
        "options": ["उद्देश्य", "उदेस्य", "उद्देस्य", "उदेश्य"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध रूप 'उद्देश्य' है, जिसमें आधा 'द' और पूरे 'द' का संयुक्त रूप (द्द) प्रयुक्त होता है।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'साहित्य और जीवन का घोर संबंध है।'\n\n[SSC MTS 18-May-2023 Shift-3]",
        "options": ["साहित्य और", "जीवन का", "घोर संबंध", "है।"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 संबंधों के लिए 'घोर' शब्द का प्रयोग गलत है। यहाँ 'घनिष्ठ संबंध' या 'अगाध संबंध' होना चाहिए।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'विद्युत'\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["चपला", "तरणी", "तटिनी", "वनिता"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'विद्युत' (बिजली) के पर्यायवाची शब्द 'चपला', 'दामिनी', 'तड़ित' और 'बिजुरी' होते हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका जन्म पहले हुआ हो'\n\n[SSC MTS 13-Jun-2023 Shift-1]",
        "options": ["अनुज", "अग्रज", "सर्वेश", "द्विज"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 जिसका जन्म पहले हुआ हो (बड़ा भाई) उसे 'अग्रज' कहते हैं। जिसका जन्म बाद में हुआ हो उसे 'अनुज' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'कोल्हू का बैल होना'\n\n[SSC MTS 14-Jun-2023 Shift-2]",
        "options": ["दिन-रात लगातार काम में लगे रहना", "बहुत शक्तिशाली होना", "मूर्खतापूर्ण काम करना", "खेती का काम करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'कोल्हू का बैल होना' मुहावरे का सही अर्थ कड़ी मेहनत करना या बिना रुके लगातार काम में जुटे रहना होता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'क्षर'\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["अक्षर", "नश्वर", "अविनाशी", "स्थिर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'क्षर' (जिसका नाश हो सके) का विलोम शब्द 'अक्षर' (जिसका नाश न हो सके) होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'चिड़ियाँ पेड़ पर ______ रही हैं।'\n\n[SSC MTS 16-Jun-2023 Shift-3]",
        "options": ["चहचहा", "भिनभिना", "कूक", "दहाड़"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 पक्षियों की ध्वनि के लिए 'चहचहाना' शब्द का प्रयोग किया जाता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'आकाश में *तारे चमक रहे हैं*।'\n\n[SSC MTS 19-Jun-2023 Shift-1]",
        "options": ["नभ में", "पाताल में", "मेघ में", "समुद्र में"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'आकाश' का सही पर्यायवाची 'नभ' होता है, इसलिए 'नभ में' सबसे उपयुक्त प्रतिस्थापन है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 20-Jun-2023 Shift-2]",
        "options": ["उज्वल", "उज्ज्वल", "उजवल", "ऊज्ज्वल"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'उज्ज्वल' है। इसमें दोनों 'ज' स्वर रहित (आधे) होते हैं।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'पवन'\n\n[SSC MTS 20-Jun-2023 Shift-3]",
        "options": ["अनिल", "अनल", "सलिल", "तनुज"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'पवन' (हवा) का पर्यायवाची 'अनिल' होता है। ध्यान रखें, 'अनल' का अर्थ आग और 'सलिल' का अर्थ पानी होता है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका कोई आकार न हो'\n\n[SSC GD 11-Jan-2023 Shift-4]",
        "options": ["साकार", "निराकार", "विकार", "आकारहीन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 जिसका कोई आकार न हो उसे 'निराकार' कहते हैं। जिसका आकार हो उसे 'साकार' कहा जाता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'अनुराग'\n\n[SSC GD 12-Jan-2023 Shift-3]",
        "options": ["विराग", "प्रेम", "नफ़रत", "आसक्ति"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अनुराग' का सही विलोम शब्द 'विराग' होता है। अनुराग का अर्थ प्रेम या लगाव होता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'आँखों में धूल झोंकना'\n\n[SSC GD 17-Jan-2023 Shift-1]",
        "options": ["धोखा देना", "साफ न दिखना", "अंगों में चोट लगना", "घमंड करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'आँखों में धूल झोंकना' मुहावरे का अर्थ किसी को चकमा देना या सीधे तौर पर 'धोखा देना' होता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह स्वभाव से *दशमुख* है।'\n\n[SSC GD 23-Jan-2023 Shift-4]",
        "options": ["रावण", "चतुर", "मूर्ख", "घमंडी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'दशमुख' (दस मुख वाला) रावण का पर्यायवाची शब्द है, इसलिए यहाँ 'रावण' सबसे उपयुक्त प्रतिस्थापन है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 27-Jan-2023 Shift-4]",
        "options": ["कालिदास", "कालीदास", "कलियादास", "कालेदास"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'कालिदास' है। अक्सर लोग इसमें बड़ी 'ली' की गलती करते हैं, जो अशुद्ध है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'अरण्य'\n\n[SSC GD 31-Jan-2023 Shift-2]",
        "options": ["कानन", "उपवन", "वाटिका", "बाग़"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अरण्य' का पर्यायवाची 'कानन', 'विपिन' या 'जंगल' होता है। बाकी तीनों विकल्प बगीचे के पर्यायवाची हैं।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'परिश्रमी व्यक्ति को हमेशा ______ मिलती है।'\n\n[SSC GD 02-Feb-2023 Shift-2]",
        "options": ["सफलता", "विफलता", "आलस्य", "निराशा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 वाक्य के सही अर्थ और संदर्भ के अनुसार 'परिश्रमी व्यक्ति को हमेशा सफलता मिलती है' सबसे उपयुक्त है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो सब कुछ जानता हो'\n\n[SSC GD 06-Feb-2023 Shift-4]",
        "options": ["अल्पज्ञ", "सर्वज्ञ", "विद्वान", "ज्ञानी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 जो सब कुछ जानता हो उसे 'सर्वज्ञ' कहते हैं। जो कम जानता हो उसे 'अल्पज्ञ' कहा जाता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'तलवे चाटना'\n\n[SSC GD 08-Feb-2023 Shift-1]",
        "options": ["चापलूसी करना", "पैर साफ करना", "दासतित्व स्वीकारना", "मदद माँगना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'तलवे चाटना' मुहावरे का अर्थ अपना काम निकलवाने के लिए किसी की अत्यधिक 'चापलूसी करना' होता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'तिशिर'\n\n[SSC GD 09-Feb-2023 Shift-3]",
        "options": ["आलोक", "अंधकार", "किरण", "रात्रि"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'तिमिर' का अर्थ अंधकार होता है, और इसका सही विलोम शब्द 'आलोक' या 'प्रकाश' होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 13-Feb-2023 Shift-2]",
        "options": ["शृंगार", "श्रृंगार", "सिंगार", "श्रींगार"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'शृंगार' है। इसमें 'श्र' के नीचे 'ऋ' की मात्रा लगती है, अलग से पूरा 'र' नहीं आता।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'मुख्य अतिथि का एक फूलों की माला द्वारा स्वागत किया गया।'\n\n[SSC GD 14-Feb-2023 Shift-1]",
        "options": ["मुख्य अतिथि का", "एक फूलों की माला", "द्वारा स्वागत", "किया गया"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 यहाँ पदक्रम की अशुद्धि है। 'एक फूलों की माला' के स्थान पर 'फूलों की एक माला' होना चाहिए।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'गजानन'\n\n[SSC MTS 03-May-2023 Shift-2]",
        "options": ["लंबोदर", "दशराज", "विष्णु", "महेश"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'गजानन' भगवान गणेश का पर्यायवाची है, जिन्हें 'लंबोदर', 'विनायक' और 'एकदंत' भी कहा जाता है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो इतिहास से संबंधित हो'\n\n[SSC MTS 04-May-2023 Shift-1]",
        "options": ["ऐतिहासिक", "इतिहासकार", "पुरातात्विक", "पौराणिक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जो इतिहास से संबंधित होता है उसे 'ऐतिहासिक' कहा जाता है। इतिहास लिखने वाले को इतिहासकार कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'अंग-अंग ढीला होना'\n\n[SSC MTS 09-May-2023 Shift-3]",
        "options": ["बहुत थक जाना", "बीमार होना", "कमज़ोर होना", "आलस्य करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अंग-अंग ढीला होना' मुहावरे का सही अर्थ अत्यधिक शारीरिक परिश्रम के कारण 'बहुत थक जाना' होता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'हर्ष'\n\n[SSC MTS 11-May-2023 Shift-1]",
        "options": ["शोक", "खुशी", "उल्लास", "आनंद"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'हर्ष' का अर्थ खुशी होता है और इसका सही विलोम शब्द 'शोक' या 'विषाद' होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'आकाश में काले-काले ______ छाए हुए हैं।'\n\n[SSC MTS 15-May-2023 Shift-3]",
        "options": ["बादल", "पक्षी", "तारे", "पानी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 यहाँ आसमान में छाने के संदर्भ में 'बादल' शब्द सबसे सटीक और सही बैठता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'राधा ने *मधुर* गीत गाया।'\n\n[SSC MTS 17-May-2023 Shift-2]",
        "options": ["सुरीला", "कर्कश", "तीखा", "नमकीन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 गीत या ध्वनि के संदर्भ में 'मधुर' शब्द को 'सुरीला' से प्रतिस्थापित करना सबसे उपयुक्त है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["उज्ज्वल", "उज्वल", "उजवल", "ऊज्ज्वल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'उज्ज्वल' है। इसमें दोनों 'ज' स्वर रहित (आधे) होते हैं।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'सूर्य'\n\n[SSC MTS 20-Jun-2023 Shift-1]",
        "options": ["दिनकर", "शशांक", "सुधाकर", "जलद"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'सूर्य' का पर्यायवाची 'दिनकर', 'दिवाकर', 'भानु', 'भास्कर' होता है। शशांक और सुधाकर चंद्रमा के पर्यायवाची हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका कोई नाथ न हो'\n\n[SSC GD 10-Jan-2023 Shift-3]",
        "options": ["अनाथ", "सनाथ", "शरणार्थी", "असहाय"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका कोई नाथ या रक्षक न हो, उसे 'अनाथ' कहते हैं। जिसका नाथ हो, उसे 'सनाथ' कहा जाता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'जटिल'\n\n[SSC GD 12-Jan-2023 Shift-4]",
        "options": ["सरल", "कठिन", "कुटिल", "पेचीदा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'जटिल' का विलोम शब्द 'सरल' होता है। कठिन और पेचीदा इसके समानार्थी शब्द हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'नाक कटना'\n\n[SSC GD 16-Jan-2023 Shift-1]",
        "options": ["प्रतिष्ठा नष्ट होना", "चोट लगना", "अपमान करना", "नुकसान होना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'नाक कटना' मुहावरे का सही अर्थ 'प्रतिष्ठा या इज्जत नष्ट होना' होता है।"
    },
    {
        "question": "দिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह समाज का *एकनिष्ठ* सेवक है।'\n\n[SSC GD 24-Jan-2023 Shift-1]",
        "options": ["वफादार", "स्वार्थी", "धोखेबाज", "उदासीन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 वाक्य के सकारात्मक संदर्भ में 'एकनिष्ठ' का सबसे सही प्रतिस्थापन 'वफादार' या 'सच्चा' सेवक होगा।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 30-Jan-2023 Shift-1]",
        "options": ["कौतूहल", "कुतूहल", "कोतुहल", "कौतुहल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'कौतूहल' या 'कुतूहल' होता है। यहाँ 'कौतूहल' सबसे शुद्ध मानक रूप है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'पक्षी'\n\n[SSC GD 01-Feb-2023 Shift-1]",
        "options": ["खग", "मीन", "पंकज", "शिखी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 पक्षी के पर्यायवाची शब्द 'खग', 'विहग', 'परिंदा' और 'पखेरू' होते हैं। मीन का अर्थ मछली और पंकज का कमल होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'पुलिस ने चोर को ______ हाथों पकड़ा।'\n\n[SSC GD 03-Feb-2023 Shift-4]",
        "options": ["रंगे", "सफेद", "काले", "खाली"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 मुहावरे के अनुसार अपराध करते हुए तुरंत पकड़े जाने को 'रंगे हाथों पकड़ना' कहा जाता है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो पहले कभी न हुआ हो'\n\n[SSC GD 07-Feb-2023 Shift-1]",
        "options": ["अभूतपूर्व", "अपूर्व", "अनुपम", "अद्वितीय"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जो घटना पहले कभी न हुई हो, उसे 'अभूतपूर्व' कहा जाता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'घड़ों पानी पड़ना'\n\n[SSC GD 09-Feb-2023 Shift-2]",
        "options": ["अत्यधिक लज्जित होना", "बहुत नहाना", "नुकसान होना", "डर जाना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'घड़ों पानी पड़ना' मुहावरे का अर्थ होता है किसी बात पर 'अत्यधिक लज्जित (शर्मिंदा) होना'।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'निर्मल'\n\n[SSC GD 13-Feb-2023 Shift-4]",
        "options": ["मलिन", "साफ", "स्वच्छ", "गंदा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'निर्मल' (बिना मैल के) का सही तत्सम विलोम शब्द 'मलिन' होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 03-May-2023 Shift-3]",
        "options": ["अन्तरराष्ट्रीय", "अंतरराष्ट्रीय", "अंतरराष्ट्रीय", "अन्तराष्ट्रीय"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 हिंदी वर्तनी के मानक नियमों के अनुसार 'अंतरराष्ट्रीय' शब्द सबसे शुद्ध रूप माना जाता है।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'वह एक विद्वान महिला थी।'\n\n[SSC MTS 04-May-2023 Shift-2]",
        "options": ["वह", "एक", "विद्वान महिला", "थी।"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 लिंग संबंधी अशुद्धि है। महिला के लिए 'विद्वान' शब्द का नहीं, बल्कि 'विदुषी' शब्द का प्रयोग किया जाता है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'महादेव'\n\n[SSC MTS 10-May-2023 Shift-1]",
        "options": ["त्रिलोचन", "कमलापति", "चतुर्भुज", "ब्रह्मा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 भगवान शिव को तीन आँखों के कारण 'त्रिलोचन' कहा जाता है। कमलापति और चतुर्भुज भगवान विष्णु के नाम हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसकी आयु लंबी हो'\n\n[SSC MTS 11-May-2023 Shift-2]",
        "options": ["दीर्घायु", "अल्पायु", "चिरायु", "अमर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसकी आयु लंबी हो उसे 'दीर्घायु' कहते हैं। कम आयु वाले को 'अल्पायु' कहा जाता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'हवा से बातें करना'\n\n[SSC MTS 16-May-2023 Shift-1]",
        "options": ["बहुत तेज दौड़ना", "अहंकार करना", "फालतू बातें करना", "कल्पना करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'हवा से बातें करना' का अर्थ होता है बहुत तेज गति से चलना या बहुत तेज दौड़ना।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'सजीव'\n\n[SSC MTS 17-May-2023 Shift-3]",
        "options": ["निर्जीव", "जीवित", "मृत", "अजीव"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'सजीव' का सटीक और व्याकरणिक विलोम शब्द 'निर्जीव' होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'मेघ बहुत ज़ोर से ______ रहे हैं।'\n\n[SSC MTS 19-May-2023 Shift-3]",
        "options": ["गरज", "कड़क", "बरस", "चमक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 मेघों (बादलों) की स्वाभाविक ध्वनि के लिए 'गरजना' शब्द का प्रयोग सबसे सटीक होता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'रात्रि में *चंद्रमा* की रोशनी सुंदर लगती है।'\n\n[SSC MTS 14-Jun-2023 Shift-1]",
        "options": ["शशांक", "दिवाकर", "मार्तंड", "भानु"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'चंद्रमा' का सही पर्यायवाची 'शशांक' या 'मयंक' है। दिवाकर, मार्तंड और भानु सूर्य के पर्यायवाची हैं।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 15-Jun-2023 Shift-3]",
        "options": ["आजीविका", "अजीविका", "आजीवका", "अजिविका"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'आजीविका' (रोजगार या जीवनयापन का साधन) है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'राजा'\n\n[SSC MTS 16-Jun-2023 Shift-1]",
        "options": ["नृप", "भूपति", "महीप", "ये सभी"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 राजा के पर्यायवाची शब्द 'नृप', 'भूपति', 'महीप', 'नरेश' और 'सम्राट' ये सभी होते हैं।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसका दमन करना कठिन हो'\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["दुर्दम्य", "दुर्बोध", "दुर्गम", "दुराचार"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसका दमन करना कठिन हो उसे 'दुर्दम्य' कहते हैं। जहाँ जाना कठिन हो उसे 'दुर्गम' कहा जाता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'प्रत्यक्ष'\n\n[SSC GD 12-Jan-2023 Shift-2]",
        "options": ["परोक्ष", "अभिमुख", "समुख", "नज़दीक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'प्रत्यक्ष' (जो आँखों के सामने हो) का विलोम शब्द 'परोक्ष' या 'अप्रत्यक्ष' (जो आँखों के सामने न हो) होता है।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'काठ का उल्लू'\n\n[SSC GD 17-Jan-2023 Shift-2]",
        "options": ["महामूर्ख", "लकड़ी का खिलौना", "बुद्धिमान", "चतुर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'काठ का उल्लू' मुहावरे का सही अर्थ 'महामूर्ख' या 'निरा मूर्ख' व्यक्ति होता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह सदैव *उत्कर्ष* की ओर बढ़ता है।'\n\n[SSC GD 25-Jan-2023 Shift-4]",
        "options": ["उन्नति", "अपकर्ष", "पतन", "अवनति"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 वाक्य के सकारात्मक संदर्भ में 'उत्कर्ष' का सबसे सही प्रतिस्थापन 'उन्नति' या 'प्रगति' होगा।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC GD 02-Feb-2023 Shift-4]",
        "options": ["ऐतिहासिक", "इतिहासकार", "ऐतिहासक", "इतिहासिक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी वाला शब्द 'ऐतिहासिक' है। 'इतिहास' शब्द में 'इक' प्रत्यय लगाने से 'ऐतिहासिक' बनता है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'जल'\n\n[SSC GD 06-Feb-2023 Shift-3]",
        "options": ["सलिल", "अनल", "पवन", "अम्बर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जल के पर्यायवाची शब्द नीर, तोय, पानी, वारि और 'सलिल' हैं। अनल का अर्थ आग और पवन का हवा होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'अंधे की ______ होना।'\n\n[SSC GD 09-Feb-2023 Shift-4]",
        "options": ["लकड़ी", "आँख", "लाठी", "चश्मा"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 मुहावरे के अनुसार 'अंधे की लकड़ी होना' का अर्थ एकमात्र सहारा होना होता है। (कुछ क्षेत्रों में लाठी भी प्रयुक्त होता है, पर मानक रूप 'लकड़ी' है)"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जो सबमें व्याप्त हो'\n\n[SSC GD 13-Feb-2023 Shift-2]",
        "options": ["सर्वव्यापी", "सर्वज्ञ", "सर्वशक्तिमान", "सर्वश्रेष्ठ"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जो सब जगह या सबमें व्याप्त हो, उसे 'सर्वव्यापी' कहा जाता है। सब कुछ जानने वाले को 'सर्वज्ञ' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'हाथ मलना'\n\n[SSC GD 14-Feb-2023 Shift-4]",
        "options": ["पछताना", "हाथ साफ़ करना", "ठंड लगना", "गुस्सा करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'हाथ मलना' मुहावरे का सही अर्थ समय निकल जाने के बाद 'पछताना' होता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'संक्षिप्त'\n\n[SSC MTS 02-May-2023 Shift-3]",
        "options": ["विस्तृत", "छोटा", "विस्तार", "संक्षेप"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'संक्षिप्त' का सही विलोम शब्द 'विस्तृत' होता है। संक्षेप का विलोम विस्तार होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 04-May-2023 Shift-4]",
        "options": ["कवयित्री", "कविइत्री", "कवयत्री", "कविअत्री"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध रूप 'कवयित्री' है। यह परीक्षाओं में सबसे ज़्यादा पूछा जाने वाला वर्तनी शुद्धि का प्रश्न है।"
    },
    {
        "question": "दिए गए वाक्य का वह भाग ज्ञात करें जिसमें कोई त्रुटि है:\n'यद्यपि वह बीमार था, परन्तु वह स्कूल गया।'\n\n[SSC MTS 09-May-2023 Shift-2]",
        "options": ["यद्यपि वह", "बीमार था", "परन्तु वह", "स्कूल गया"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अव्यय संबंधी अशुद्धि है। 'यद्यपि' के साथ हमेशा 'तथापि' या 'फिर भी' का जोड़ा बनता है, 'परन्तु' का नहीं।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'अग्नि'\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["पावक", "अनिल", "सलिल", "व्योम"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अग्नि' के पर्यायवाची शब्द आग, अनल, हुताशन और 'पावक' होते हैं। अनिल हवा का पर्यायवाची है।"
    },
    {
        "question": "दिए गए वाक्यांश के लिए एक शब्द दीजिए:\n'जिसकी उपमा न दी जा सके'\n\n[SSC MTS 16-May-2023 Shift-3]",
        "options": ["अनुपम", "अद्वितीय", "अतुलनीय", "अपार"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 जिसकी उपमा न दी जा सके उसे 'अनुपम' कहते हैं। जिसकी तुलना न की जा सके उसे 'अतुलनीय' कहते हैं।"
    },
    {
        "question": "निम्नलिखित प्रश्न में, दिए गए चार विकल्पों में से उस विकल्प का चयन करें जो मुहावरे का सही अर्थ व्यक्त करता है:\n'अंगूठा चूमना'\n\n[SSC MTS 17-May-2023 Shift-4]",
        "options": ["खुशामद करना", "प्यार जताना", "मना करना", "तिरस्कार करना"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अंगूठा चूमना' मुहावरे का अर्थ चापलूसी करना या किसी की 'खुशामद करना' होता है।"
    },
    {
        "question": "दिए गए शब्द का विलोम शब्द चुनिए:\n'अनुज'\n\n[SSC MTS 19-May-2023 Shift-4]",
        "options": ["अग्रज", "बड़ा", "छोटा", "कनुज"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'अनुज' (छोटा भाई) का सही तत्सम विलोम शब्द 'अग्रज' (बड़ा भाई) होता है।"
    },
    {
        "question": "रिक्त स्थान को भरने के लिए सबसे उपयुक्त शब्द का चयन करें:\n'घोड़ा अस्तबल में ______ रहा है।'\n\n[SSC MTS 14-Jun-2023 Shift-3]",
        "options": ["हिनहिना", "दहाड़", "रेंक", "भौंक"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 घोड़े की स्वाभाविक आवाज़ या बोली के लिए 'हिनहिनाना' शब्द का प्रयोग किया जाता है।"
    },
    {
        "question": "दिए गए वाक्य में रेखांकित खंड को प्रतिस्थापित करने के लिए सबसे उपयुक्त विकल्प का चयन करें:\n'वह सदा *सत्य* बोलता है।'\n\n[SSC MTS 15-Jun-2023 Shift-2]",
        "options": ["ऋत", "झूठ", "असत्य", "मिथ्या"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 वैदिक या व्याकरणिक भाषा में 'सत्य' का एक सटीक पर्यायवाची 'ऋत' होता है, यद्यपि यहाँ वाक्य प्रतिस्थापन में व्यावहारिक रूप से प्रयुक्त होता है।"
    },
    {
        "question": "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:\n\n[SSC MTS 19-Jun-2023 Shift-3]",
        "options": ["आशीर्वाद", "आरशीवाद", "आशिरवाद", "अशीर्वाद"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 शुद्ध वर्तनी 'आशीर्वाद' है। इसमें 'श' पर बड़ी 'ी' की मात्रा और 'व' के ऊपर रेफ (र) लगता है।"
    },
    {
        "question": "दिए गए शब्द का पर्यायवाची शब्द चुनिए:\n'समुद्र'\n\n[SSC MTS 20-Jun-2023 Shift-4]",
        "options": ["पयोधि", "जलद", "नीरज", "वारिद"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 'समुद्र' का पर्यायवाची 'पयोधि', 'जलधि', 'सागर' होता है। जलद और वारिद बादल के, तथा नीरज कमल का पर्यायवाची है।"
    }
]
