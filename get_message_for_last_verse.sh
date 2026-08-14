#!/bin/bash

USED_FILE="memory/used_quotes.txt"
if [ ! -f "$USED_FILE" ]; then
    echo "No used quotes file"
    exit 1
fi
LAST_VERSE=$(tail -1 "$USED_FILE")

# Define arrays (same as before)
sanskrit=(
    "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गो���ऽस्त्वकर्मणि॥"
    "उद्धरेदात्मना आत्मानम् । नात्मनमवसादयेत् ।"
    "यदा यदा हि धर्मस्य ग्लानिर्भवति भारतः। अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥"
    "शान्ति�ि��िः परमं ज्ञानम्।"
    "योगः कर्मसु कौशलम्।"
)
english=(
    "You have the right to work only, but never to the fruits of work."
    "One must elevate, not degrade, oneself by one's own mind."
    "Whenever and wherever there is a decline in righteousness, O descendant of Bharata, and a rise in evil, then I manifest Myself."
    "Peace is the supreme knowledge."
    "Yoga is skill in action."
)
hindi=(
    "कर्म करने का अधिकार सिर्फ आपके पास है, लेकिन फल की इच्छा मत रखिए।"
    "एक व्यक्ति को अपने मन से खुद को उठाना चाहिए, नहीं तो गिराना।"
    "जब-जब धर्म में गिरावट होती है, हे भारत के वंशज, और अधर्म का उदय होता है, तब-तब मैं स्वयं प्रकट होता हूं।"
    "शांति supreme ज्ञान है।"
    "योग कर्म में दक्षता है।"
)
application=(
    "Focus on your duties today without worrying about the results. Do your best and let go of the outcome."
    "Use your mind to lift yourself up today. Avoid negative thoughts that bring you down."
    "When you see injustice or wrongdoing, remember that you have the inner strength to stand up for what is right."
    "Cultivate inner peace through meditation and mindfulness. It is the highest wisdom."
    "Approach your tasks with mindfulness and excellence. Yoga is not just postures, but skill in everything you do."
)

# Find index
index=-1
for i in "${!sanskrit[@]}"; do
    if [[ "${sanskrit[$i]}" == "$LAST_VERSE" ]]; then
        index=$i
        break
    fi
done

if [ $index -eq -1 ]; then
    echo "Verse not found in list"
    exit 1
fi

# Format message (same as before, but without the "This verse was selected..." line)
message="���������🌟 *Daily Motivation* ���� �� �� 🌟

���������📜 *Sanskrit Verse*:
${sanskrit[$index]}

���������🌐 *English Translation*:
${english[$index]}

���������🇮���������🇳 *Hindi Meaning*:
${hindi[$index]}

���������💡 *Practical Application for Today*:
${application[$index]}"

echo "$message"