# 📚 टेलीग्राम क्विज़ बॉट प्रश्न बैंक (Question Bank) - भाग 1

QUIZ_LIST = [
    # =====================================================
    # ------------------- HINDI QUIZZES -------------------
    # =====================================================
    {
        "question": "भारतीय संविधान सभा की प्रारूप समिति (Drafting Committee) के अध्यक्ष कौन थे?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["डॉ. राजेन्द्र प्रसाद", "जवाहरलाल नेहरू", "डॉ. बी.आर. अम्बेडकर", "सरदार पटेल"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 डॉ. बी.आर. अम्बेडकर प्रारूप समिति के अध्यक्ष थे। इस समिति में कुल 7 सदस्य थे।"
    },
    {
        "question": "भारतीय संविधान में 'मौलिक अधिकार' (Fundamental Rights) किस देश के संविधान से लिए गए हैं?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["ब्रिटेन", "संयुक्त राज्य अमेरिका (USA)", "कनाडा", "सोवियत संघ"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 मौलिक अधिकार अमेरिका के संविधान से लिए गए हैं, जो संविधान के भाग-3 (अनुच्छेद 12 से 35) में वर्णित हैं।"
    },
    {
        "question": "भारतीय संविधान का कौन सा अनुच्छेद 'अस्पृश्यता का अंत' (Abolition of Untouchability) से संबंधित है?\n\n[SSC CHSL 14-Mar-2023 Shift-3]",
        "options": ["अनुच्छेद 14", "अनुच्छेद 17", "अनुच्छेद 19", "अनुच्छेद 21"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 17 के तहत अस्पृश्यता (छुआछूत) को समाप्त कर दिया गया है और इसका किसी भी रूप में आचरण प्रतिबंधित है।"
    },
    {
        "question": "वर्तमान में भारतीय संविधान में कुल कितनी अनुसूचियां (Schedules) हैं?\n\n[SSC GD 16-Jan-2023 Shift-4]",
        "options": ["8 अनुसूचियां", "10 अनुसूचियां", "12 अनुसूचियां", "14 अनुसूचियां"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 मूल संविधान में केवल 8 अनुसूचियां थीं, लेकिन विभिन्न संशोधनों के बाद वर्तमान में कुल 12 अनुसूचियां हैं।"
    },
    {
        "question": "भारतीय संविधान के किस संशोधन द्वारा 'मौलिक कर्तव्यों' (Fundamental Duties) को जोड़ा गया था?\n\n[SSC MTS 08-May-2023 Shift-2]",
        "options": ["42वां संशोधन", "44वां संशोधन", "61वां संशोधन", "86वां संशोधन"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 42वें संविधान संशोधन अधिनियम 1976 द्वारा सरदार स्वर्ण सिंह समिति की सिफारिश पर भाग 4(A) और अनुच्छेद 51(A) के तहत मौलिक कर्तव्य जोड़े गए।"
    },
    {
        "question": "भारत के राष्ट्रपति को पद की शपथ कौन दिलाता है?\n\n[SSC GD 24-Jan-2023 Shift-1]",
        "options": ["उपराष्ट्रपति", "प्रधानमंत्री", "भारत के मुख्य न्यायाधीश (CJI)", "लोकसभा अध्यक्ष"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारतीय संविधान के अनुच्छेद 60 के अनुसार, भारत के मुख्य न्यायाधीश (Chief Justice of India) राष्ट्रपति को शपथ दिलाते हैं।"
    },
    {
        "question": "राष्ट्रपति बनने के लिए भारत के नागरिक की न्यूनतम आयु कितनी होनी चाहिए?\n\n[SSC MTS 15-Jun-2023 Shift-2]",
        "options": ["25 वर्ष", "30 वर्ष", "35 वर्ष", "40 वर्ष"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 राष्ट्रपति, उपराष्ट्रपति और राज्यपाल बनने के लिए न्यूनतम आयु 35 वर्ष होनी अनिवार्य है।"
    },
    {
        "question": "लोकसभा का सदस्य चुने जाने के लिए न्यूनतम आयु सीमा क्या है?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["18 वर्ष", "21 वर्ष", "25 वर्ष", "30 वर्ष"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 लोकसभा सदस्य (MP) और विधानसभा सदस्य (MLA) बनने के लिए न्यूनतम आयु 25 वर्ष है, जबकि राज्यसभा के लिए 30 वर्ष है।"
    },
    {
        "question": "संसद के दोनों सदनों की संयुक्त बैठक (Joint Session) की अध्यक्षता कौन करता है?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["राष्ट्रपति", "प्रधानमंत्री", "राज्यसभा का सभापति", "लोकसभा अध्यक्ष (Speaker)"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 108 के तहत संयुक्त बैठक राष्ट्रपति द्वारा बुलाई जाती है, लेकिन इसकी अध्यक्षता हमेशा लोकसभा अध्यक्ष करता है।"
    },
    {
        "question": "सर्वोच्च न्यायालय (Supreme Court) के न्यायाधीश कितनी आयु में सेवानिवृत्त (Retire) होते हैं?\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["60 वर्ष", "62 वर्ष", "65 वर्ष", "68 वर्ष"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 सुप्रीम कोर्ट के न्यायाधीश 65 वर्ष की आयु में सेवानिवृत्त होते हैं, जबकि हाई कोर्ट के न्यायाधीशों की सेवानिवृत्ति आयु 62 वर्ष होती है।"
    },
    {
        "question": "किस संविधान संशोधन द्वारा मतदान की आयु 21 वर्ष से घटाकर 18 वर्ष की गई थी?\n\n[SSC GD 06-Feb-2023 Shift-1]",
        "options": ["42वां संशोधन", "44वां संशोधन", "61वां संशोधन", "73वां संशोधन"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 61वें संविधान संशोधन अधिनियम 1989 के द्वारा मतदान की न्यूनतम आयु सीमा को 21 वर्ष से घटाकर 18 वर्ष किया गया था।"
    },
    {
        "question": "भारतीय संविधान की 11वीं अनुसूची निम्नलिखित में से किससे संबंधित है?\n\n[SSC MTS 12-May-2023 Shift-3]",
        "options": ["नगरपालिका", "पंचायती राज", "दल-बदल कानून", "आधिकारिक भाषाएं"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 11वीं अनुसूची को 73वें संशोधन (1992) द्वारा जोड़ा गया था, जो पंचायती राज संस्थाओं के कार्य और शक्तियों से संबंधित है।"
    },
    {
        "question": "Who was the Chairman of the Drafting Committee of the Indian Constituent Assembly?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["Dr. Rajendra Prasad", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Sardar Patel"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Dr. B.R. Ambedkar was the chairman of the Drafting Committee. There were a total of 7 members in this committee."
    },
    {
        "question": "From the constitution of which country have the 'Fundamental Rights' been borrowed in the Indian Constitution?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["United Kingdom (UK)", "United States of America (USA)", "Canada", "Soviet Union"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Fundamental Rights are borrowed from the US Constitution and are described in Part III (Articles 12 to 35) of the Constitution."
    },
    {
        "question": "Which Article of the Indian Constitution is related to the 'Abolition of Untouchability'?\n\n[SSC CHSL 14-Mar-2023 Shift-3]",
        "options": ["Article 14", "Article 17", "Article 19", "Article 21"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Under Article 17, untouchability is abolished and its practice in any form is forbidden."
    },
    {
        "question": "How many Schedules are there in the Indian Constitution at present?\n\n[SSC GD 16-Jan-2023 Shift-4]",
        "options": ["8 Schedules", "10 Schedules", "12 Schedules", "14 Schedules"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 There were only 8 schedules in the original Constitution, but after various amendments, there are a total of 12 schedules now."
    },
    {
        "question": "By which amendment of the Indian Constitution were the 'Fundamental Duties' added?\n\n[SSC MTS 08-May-2023 Shift-2]",
        "options": ["42nd Amendment", "44th Amendment", "61st Amendment", "86th Amendment"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Fundamental Duties were added under Part IV(A) and Article 51(A) by the 42nd Constitutional Amendment Act 1976 on the recommendation of the Swaran Singh Committee."
    },
    {
        "question": "Who administers the oath of office to the President of India?\n\n[SSC GD 24-Jan-2023 Shift-1]",
        "options": ["Vice-President", "Prime Minister", "Chief Justice of India (CJI)", "Speaker of Lok Sabha"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 According to Article 60 of the Indian Constitution, the Chief Justice of India administers the oath to the President."
    },
    {
        "question": "What is the minimum age required for a citizen to become the President of India?\n\n[SSC MTS 15-Jun-2023 Shift-2]",
        "options": ["25 years", "30 years", "35 years", "40 years"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The minimum age required to become the President, Vice-President, or Governor is 35 years."
    },
    {
        "question": "What is the minimum age limit to be elected as a member of the Lok Sabha?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["18 years", "21 years", "25 years", "30 years"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The minimum age to become a member of Lok Sabha (MP) and Legislative Assembly (MLA) is 25 years, while for Rajya Sabha it is 30 years."
    },
    {
        "question": "Who presides over the Joint Session of both Houses of Parliament?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["President", "Prime Minister", "Chairman of Rajya Sabha", "Speaker of Lok Sabha"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Under Article 108, a joint session is called by the President, but it is always presided over by the Speaker of the Lok Sabha."
    },
    {
        "question": "At what age do the judges of the Supreme Court retire?\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["60 years", "62 years", "65 years", "68 years"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Supreme Court judges retire at the age of 65, whereas High Court judges retire at the age of 62."
    },
    {
        "question": "By which Constitutional Amendment was the voting age reduced from 21 years to 18 years?\n\n[SSC GD 06-Feb-2023 Shift-1]",
        "options": ["42nd Amendment", "44th Amendment", "61st Amendment", "73rd Amendment"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The minimum age limit for voting was reduced from 21 years to 18 years by the 61st Constitutional Amendment Act 1989."
    },
    {
        "question": "The 11th Schedule of the Indian Constitution is related to which of the following?\n\n[SSC MTS 12-May-2023 Shift-3]",
        "options": ["Municipalities", "Panchayati Raj", "Anti-Defection Law", "Official Languages"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The 11th Schedule was added by the 73rd Amendment (1992) and deals with the functions and powers of Panchayati Raj institutions."
    },
    {
        "question": "भारतीय संविधान में 'समान नागरिक संहिता' (Uniform Civil Code) का उल्लेख किस अनुच्छेद में है?\n\n[SSC GD 10-Jan-2023 Shift-4]",
        "options": ["अनुच्छेद 40", "अनुच्छेद 44", "अनुच्छेद 48", "अनुच्छेद 50"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 44 राज्य के नीति निर्देशक तत्वों (DPSP) के तहत भारत के पूरे क्षेत्र में नागरिकों के लिए एक समान नागरिक संहिता सुनिश्चित करने का निर्देश देता है।"
    },
    {
        "question": "संसद के उच्च सदन (Upper House) अर्थात् 'राज्यसभा' के सदस्यों का कार्यकाल कितने वर्ष का होता है?\n\n[SSC MTS 03-May-2023 Shift-3]",
        "options": ["4 वर्ष", "5 वर्ष", "6 वर्ष", "स्थायी"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 राज्यसभा एक स्थायी सदन है जो कभी भंग नहीं होता, लेकिन इसके सदस्यों का कार्यकाल 6 वर्ष का होता है और प्रत्येक दो वर्ष में एक-तिहाई सदस्य सेवानिवृत्त हो जाते हैं।"
    },
    {
        "question": "भारतीय संविधान में प्रथम संशोधन (First Amendment) किस वर्ष किया गया था?\n\n[SSC CHSL 15-Mar-2023 Shift-2]",
        "options": ["1950", "1951", "1952", "1955"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 प्रथम संविधान संशोधन 1951 में हुआ था, जिसके तहत संविधान में '9वीं अनुसूची' जोड़ी गई थी ताकि भूमि सुधार कानूनों को चुनौती न दी जा सके।"
    },
    {
        "question": "संवैधानिक उपचारों का अधिकार (Right to Constitutional Remedies) किस अनुच्छेद के अंतर्गत आता है जिसे डॉ. अम्बेडकर ने संविधान की आत्मा कहा था?\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["अनुच्छेद 19", "अनुच्छेद 21", "अनुच्छेद 32", "अनुच्छेद 226"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 32 के तहत नागरिकों को मौलिक अधिकारों के उल्लंघन पर सीधे सुप्रीम कोर्ट जाने का अधिकार मिलता है, जिसे डॉ. बी.आर. अम्बेडकर ने 'संविधान का हृदय और आत्मा' कहा था।"
    },
    {
        "question": "राष्ट्रपति पर महाभियोग (Impeachment) चलाने की प्रक्रिया संविधान के किस अनुच्छेद में वर्णित है?\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["अनुच्छेद 52", "अनुच्छेद 56", "अनुच्छेद 61", "अनुच्छेद 72"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 61 के तहत संविधान के उल्लंघन के आधार पर राष्ट्रपति पर महाभियोग का प्रस्ताव संसद के किसी भी सदन में लाया जा सकता है।"
    },
    {
        "question": "भारतीय संविधान का कौन सा भाग 'मौलिक अधिकारों' (Fundamental Rights) से संबंधित है?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["भाग II", "भाग III", "भाग IV", "भाग IV-A"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 संविधान का भाग III (अनुच्छेद 12 से 35) मौलिक अधिकारों से संबंधित है, जिसे भारत का 'मैग्नाकार्टा' भी कहा जाता है।"
    },
    {
        "question": "पंचायती राज व्यवस्था का मूल उद्देश्य क्या सुनिश्चित करना है?\n\n[SSC CHSL 11-Aug-2023 Shift-2]",
        "options": ["राजनीतिक जवाबदेही", "लोकतांत्रिक विकेंद्रीकरण", "वित्तीय संग्रहण", "प्रशासनिक नियंत्रण"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 पंचायती राज का मूल उद्देश्य सत्ता को निचले स्तर तक पहुँचाना अर्थात् 'लोकतांत्रिक विकेंद्रीकरण' (Democratic Decentralization) सुनिश्चित करना है।"
    },
    {
        "question": "भारत के उपराष्ट्रपति पदेन अध्यक्ष (Ex-officio Chairman) किसके होते हैं?\n\n[SSC MTS 16-Jun-2023 Shift-1]",
        "options": ["लोकसभा", "नीति आयोग", "राज्यसभा", "राष्ट्रीय विकास परिषद"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 64 के अनुसार, भारत का उपराष्ट्रपति राज्यसभा का पदेन सभापति (अध्यक्ष) होता है, जिसके पास राज्यसभा की बैठकों के संचालन की शक्ति होती है।"
    },
    {
        "question": "भारतीय संविधान में 'एकल नागरिकता' (Single Citizenship) की अवधारणा किस देश से ली गई है?\n\n[SSC GD 25-Jan-2023 Shift-1]",
        "options": ["यूनाइटेड किंगडम (UK)", "संयुक्त राज्य अमेरिका (USA)", "ऑस्ट्रेलिया", "आयरलैंड"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 भारत ने ब्रिटेन (UK) के संविधान से एकल नागरिकता और संसदीय शासन प्रणाली को अपनाया है, जबकि अमेरिका में दोहरी नागरिकता की व्यवस्था है।"
    },
    {
        "question": "कोई विधेयक 'धन विधेयक' (Money Bill) है या नहीं, इसका अंतिम निर्णय कौन करता है?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["राष्ट्रपति", "प्रधानमंत्री", "वित्त मंत्री", "लोकसभा अध्यक्ष (Speaker)"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 110(3) के तहत यदि यह प्रश्न उठता है कि कोई विधेयक धन विधेयक है या नहीं, तो उस पर लोकसभा अध्यक्ष (Speaker) का निर्णय अंतिम होता है।"
    },
    {
        "question": "In which Article of the Indian Constitution is the 'Uniform Civil Code' mentioned?\n\n[SSC GD 10-Jan-2023 Shift-4]",
        "options": ["Article 40", "Article 44", "Article 48", "Article 50"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Under the Directive Principles of State Policy (DPSP), Article 44 directs the State to secure a Uniform Civil Code for citizens throughout the territory of India."
    },
    {
        "question": "What is the tenure of the members of the 'Rajya Sabha' (Upper House) of Parliament?\n\n[SSC MTS 03-May-2023 Shift-3]",
        "options": ["4 years", "5 years", "6 years", "Permanent"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Rajya Sabha is a permanent house that is never dissolved, but the tenure of its members is 6 years, with one-third of the members retiring every two years."
    },
    {
        "question": "In which year was the First Amendment made to the Indian Constitution?\n\n[SSC CHSL 15-Mar-2023 Shift-2]",
        "options": ["1950", "1951", "1952", "1955"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The First Constitutional Amendment took place in 1951, which added the '9th Schedule' to protect land reform laws from judicial review."
    },
    {
        "question": "Under which Article does the 'Right to Constitutional Remedies' fall, which Dr. Ambedkar called the soul of the constitution?\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["Article 19", "Article 21", "Article 32", "Article 226"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Under Article 32, citizens have the right to approach the Supreme Court directly for the enforcement of fundamental rights. Dr. Ambedkar called it the 'heart and soul of the constitution'."
    },
    {
        "question": "Which Article of the Constitution describes the process of 'Impeachment' of the President?\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["Article 52", "Article 56", "Article 61", "Article 72"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Under Article 61, a motion for impeachment can be initiated by either house of Parliament based on the grounds of violation of the Constitution."
    },
    {
        "question": "Which Part of the Indian Constitution deals with 'Fundamental Rights'?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["Part II", "Part III", "Part IV", "Part IV-A"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Part III (Articles 12 to 35) of the Constitution deals with Fundamental Rights and is often referred to as the 'Magna Carta' of India."
    },
    {
        "question": "What is the primary objective of the Panchayati Raj System?\n\n[SSC CHSL 11-Aug-2023 Shift-2]",
        "options": ["Political accountability", "Democratic decentralization", "Financial collection", "Administrative control"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The core objective of Panchayati Raj is to distribute power to the grassroots level, thereby ensuring 'Democratic Decentralization'."
    },
    {
        "question": "The Vice-President of India is the Ex-officio Chairman of which body?\n\n[SSC MTS 16-Jun-2023 Shift-1]",
        "options": ["Lok Sabha", "NITI Aayog", "Rajya Sabha", "National Development Council"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 According to Article 64, the Vice-President of India acts as the Ex-officio Chairman of the Rajya Sabha, presiding over its sessions."
    },
    {
        "question": "From which country is the concept of 'Single Citizenship' borrowed in the Indian Constitution?\n\n[SSC GD 25-Jan-2023 Shift-1]",
        "options": ["United Kingdom (UK)", "United States of America (USA)", "Australia", "Ireland"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 India adopted single citizenship and the parliamentary form of government from the UK Constitution, unlike the USA which features dual citizenship."
    },
    {
        "question": "Who takes the final decision on whether a bill is a 'Money Bill' or not?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["President", "Prime Minister", "Finance Minister", "Speaker of Lok Sabha"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Under Article 110(3), if any question arises whether a bill is a Money Bill or not, the decision of the Speaker of the Lok Sabha remains final."
    },
    

]
