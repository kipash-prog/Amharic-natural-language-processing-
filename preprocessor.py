import re
#nltk.download()
from bs4 import BeautifulSoup
import requests # type: ignore
from nltk.tokenize import word_tokenize # type: ignore




# get page content from URL annd remove tags
def remove_tags(url):					
	page = requests.get(url)						

	html = page.content
	soup = BeautifulSoup(html, "html.parser")	

	for data in soup(['style', 'script']):
		data.decompose()						
	return ' '.join(soup.stripped_strings)	



# get rid of english letter and all symbols
def cleaner(text):
    text = re.sub(r'[^\u1200-\u137F\s\w]+', '', text)
    english_words_pattern = r'\b[a-zA-Z]+\b'
    text = re.sub(english_words_pattern, '', text)

    text = re.sub(r'[^\u1200-\u137F\s]+', '', text)
    amharic_punctuation = "።፣፡፤፥፨፦፧፨፠"
    translator = str.maketrans('', '', amharic_punctuation)
    text = text.translate(translator).lower()
    return text



# remove prefix and suffix to bring words to their root word
def stem_prefix_suffix(word):
    prefixes = ["የ", "ለ", "አል", "በ", "ሳይ", "አት", "አስ", "እንደ", "እስኪ", "ያል", "ባለ", "እንዲ", "እያስ", "በስተ", "ወደ", "ያስ", "ት", "ስለ", "እስክ", "ሲ", "እንድ","አስ", "ምት", "በስተ", "ወደ", "ያለ", "ማይ", "የ", "ሳት","ያስ", "እንዲ", " ት", "ያ", "አላ", "እስከ", "በ", "ተ", "ት", "ሚ", "እን", "በት", "ከ", "ተ", "ወ", "አይ", "የ"]
    suffixes = ["ን", "ና", "ሽ", "ነት","ሽው", "ው","ዮሽ", "ቸው", "ህ", "ባት", "ዋ", "ችኋል", "ዎች", "ም", "ለን", "ለት", "ዊ","ቹ", "ውያን", "ዎች", "ዋ", "ኝ", "ኞች", "ያ", "ችን", "ቸው","ች", "ቸው" "ዊ", "በት", "ችሁ", "ዋ", "ን", "ህ","ኛ", "አቸዋል","አችን","ቹ", "ችሁ", "ውያን", "ቻቸው", " ይ", "ቸው", "ህ", "ኞቸ", "ለ", "ት"]

    word=word.replace("ሠ","ሰ")
    word=word.replace("ሃ", "ሀ")
    word=word.replace("ሐ", "ሀ")
    word=word.replace("ሓ", "ሀ")
    word=word.replace("ኅ", "ሀ")
    word=word.replace("ኃ", "ሀ")
    word=word.replace("ኋ", "ኋ")
    word=word.replace("ሗ", "ኋ")
    word=word.replace("ኁ", "ሁ")
    word=word.replace("ኅ", "ህ")
    word=word.replace("ኂ", "ሂ")
    word=word.replace("ኄ", "ሄ")
    word=word.replace("ሑ", "ሁ")
    word=word.replace("ሒ", "ሂ")
    word=word.replace("ሔ", "ሄ")
    word=word.replace("ሕ", "ህ")
    word=word.replace("ሡ", "ሱ")
    word=word.replace("ሖ", "ሆ")
    word=word.replace("ሢ", "ሲ")
    word=word.replace("ሣ", "ሳ")
    word=word.replace("ሤ", "ሴ")
    word=word.replace("ሥ", "ስ")
    word=word.replace("ሦ", "ሶ")
    word=word.replace("ጸ", "ፀ")
    word=word.replace("ጹ", "ፁ")
    word=word.replace("ጺ", "ፂ")
    word=word.replace("ጻ", "ፃ")
    word=word.replace("ጼ", "ፄ")
    word=word.replace("ጽ", "ፅ")
    word=word.replace("ጾ", "ፆ")
    word=word.replace("ዉ", "ው")
    word=word.replace("ዪ", "ይ")
    word=word.replace("ዓ", "አ")
    word=word.replace("ዑ", "ኡ")
    word=word.replace("ዒ", "ኢ")
    word=word.replace("ዐ", "አ")
    word=word.replace("ኣ", "አ")
    word=word.replace("ዔ", "ኤ")
    word=word.replace("ዕ", "እ")
    word=word.replace("ዖ", "ኦ")

    if word.startswith('አ') and word.endswith('ጥ'):
        word = word[:-1]
        if word.startswith('አ'):
             word = word[1:]
             return word
    if word.startswith('አ') and word.endswith('ል'):
        word = word[:-1]
        if word.startswith('አ'):
             word = word[1:]
             return word
    if word.startswith('አ') and word.endswith('ብ'):
        word = word[:-1]
        if word.startswith('አ'):
             word = word[1:]
             return word
    if word.startswith('አስ') and word.endswith('ች'):
        word = word[:-1]
        if word.startswith('አስ'):
            word = word[2:]
            return word
    elif word.endswith('ጆች'):
        word = word[:-2] + 'ጅ'
        return word
    elif word.endswith('ቶች'):
        word = word[:-2] + 'ት'
        return word
    elif word.endswith('ኞች'):
        word = word[:-2] + 'ኛ'
        return word
    elif word.endswith('ጎች'):
        word = word[:-2] + 'ግ'
        return word

    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]
            break

    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break
    return word



# remove stop words from using the list
def remove_stop_words(stemmed_words):
    well_known_stop_words =  [
        "እኔ", "የእኔ", "እኔ ራሴ", "እኛ", "የእኛ", "የእኛ", "እኛ ራሳችን", "አንቺ", "ያንተ", "ራስህን",
        "እራሳችሁ", "እሱ", "የእሱ", "ራሱ", "እሷ", "የእሷ", "እራሷ", "እነሱ", "እነሱን", "የእነሱ",
        "ራሳቸው", "ምንድን", "የትኛው", "የአለም", "ጤና", "ድርጅት", "ማን", "ይህ", "የሚል",
        "ነው", "ናቸው", "ነበር", "ነበሩ", "ሁን", "ቆይቷል", "መሆን", "አላቸው", "አለው", "ነበረው",
        "ያለው", "መ", "ስ", "ሲ", "ራ", "ት", "ያደርጋል", "አደረገ", "ማድረግ", "አንድ", "የ", "እና",
        "ግን", "ከሆነ", "ወይም", "ምክንያቱም", "እንደ", "እስከ", "እያለ", "ለ", "ጋር", "ስለ", "ላይ",
        "መካከል", "ወደ", "በኩል", "ወቅት", "ከዚህ", "በፊት", "በኋላ", "ከላይ", "ከታች", "ወደከ",
        "ወደ", "ላይ", "ታች", "ውስጥ", "ውጭ", "ላይ", "ጠፍቷል", "በላይ", "በታች", "እንደገና",
        "ተጨማሪ", "ከዚያ", "አንድ", "ጊዜ", "እዚህ", "እዚያ", "መቼ", "የት", "እንዴት", "ሁሉም",
        "ማንኛውም", "ሁለቱም", "እያንዳንዳቸው", "ጥቂቶች", "ተጨማሪ", "በጣም", "ሌላ", "አንዳንድ",
        "እንደዚህ", "አይ", "ወይም", "አይደለም", "አይደለም", "ብቻ", "የራሱ", "ተመሳሳይ", "ስለዚህ",
        "ይልቅ", "እንዲሁ", "በጣም", "ት", "ይችላል", "ያደርጋል", "ብቻ", "ዶን", "ይገባል"," " , "አሁን",
        "ውስጥ","እና","","ሆኖ","ው","ቃ", "ጂ", "ናቸ", "ና", "ሆኑ", "እሺ", "አዎ", "ር", "ዚህ", "ዝ",
        "ህ","-","ን","እንደ","የ","አል","ው","ኡ","በ","ተ","ለ","ን","ኦች","ኧ","ና","ከ","አቸው","ት","መ",
        "አ","አት","ዎች","ም","አስ","ኡት","ላ","ይ","ማ","ያ","አ","ቶ","እንዲ","የሚ","ኦ","ይ","እየ","ሲ","ብ",
        "ወደ","ሌላ","ጋር","ኡ","እዚህ","አንድ","ውስጥ","እንድ","እ-ል","ን-ብ-ር","በኩል","ል","እስከ","እና","ድ-ግ-ም",
        "መካከል","ኧት","ሊ","አይ","ምክንያት","ይህ","ኧች","ኢት","ዋና","አን","እየ","ስለ","ች","ስ","ቢ","ብቻ","በየ",
        "ባለ","ጋራ","ኋላ","እነ","አም","ሽ","አዊ","ዋ","ያለ","ግን","ምን","አችን","ወይዘሮ","ወዲህ","ማን","ዘንድ",
        "የት","ናቸው","ላ","ይሁን","ወይም","ታች","እዚያ","እጅግ","እንጅ","በጣም","ወዘተ","ጅ-ም-ር","አሁን","ከነ",
        "ተራ","ም-ል","ጎሽ","አዎ","እሽ","ጉዳይ","ረገድ","ያህል","ይልቅ","ዳር","እንኳ","አዎን","ብ-ዝ","ጥቂት","እኔ","አንተ",
        "እርስዎ","እሳቸው","እሱ","አንች","እኛ","እነሱ","እናንተ","ይኸ","የቱ","መቼ","ወዲያ","ወዴት","እንዴት","ልክ","አጠገብ",
        "ባሻገር","እንትን","እንትና","ሁሉ","እንጂ","ይች","ናት","ምናልባት","በቀር","እስኪ","ወይ","እንዴ","ስንት","መቸ","ከፍ","ቢያንስ",
        "ብ-ቅ","ምሳሌ","እንግዲ","እሷ","ምነው","የተለያዩ","ወይስ","እርስወት","እንቶኔ","እንቶኒት","ኢ","ኛ","ነት","በት","ኤት","ኤ",
        "ለይ","ኦት","ህ-ድ","ዊ","እን","ኧች","ኝ","አዚህ","ዉ","ሁል","ህ","እንዳ","አይነት","መላ","አችሁ","አማካይ","ዘዴ","ነዉ",
        "አችው","እዚያ","በስቲያ","ዉስጥ","አዊት","ኃላ","እስክ","ሳቢያ","ስት","ዬ","ቲ","ወስጥ","ዝ","ቶሎ","ወትሮ","በነ","ኧቸ",
        "ታዲያ","ጋ","ውሰጥ","መቼ","ወይዘሪት","ትናንት","ይኽ","ኤል","ኦቸ","ኢዋ","የለ","ሰሞን","ፊት","ምንጊዜ","አቸን","ኧም",
        "አወ","ኢያ","ነገ","ትላንት","ኣት","እንጃ","ድ-ር-ግ","መልክ"
    ]

    # print(len(well_known_stop_words))

    return  [word for word in stemmed_words if not word in well_known_stop_words]