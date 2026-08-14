#!/bin/bash

# Set up
MEMORY_DIR="memory"
USED_FILE="$MEMORY_DIR/used_quotes.txt"
mkdir -p "$MEMORY_DIR"
touch "$USED_FILE"

# Read used quotes into an array
mapfile -t used_quotes < "$USED_FILE"

# Define our quotes
declare -a sanskrit=(
    "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गो�ऽस्त्वकर्मणि॥"
    "उद्धरेदात्मना आत्मानम् । नात्मनमवसादयेत् ।"
    "यदा यदा हि धर्मस्य ग्लानिर्भवति भारतः। अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥"
    "शान्ति�िः परमं ज्ञानम्।"
    "योगः कर्मसु कौशलम्।"
)

declare -a english=(
    "You have the right to work only, but never to the fruits of work."
    "One must elevate, not degrade, oneself by one's own mind."
    "Whenever and wherever there is a decline in righteousness, O descendant of Bharata, and a rise in evil, then I manifest Myself."
    "Peace is the supreme knowledge."
    "Yoga is skill in action."
)

declare -a hindi=(
    "कर्म करने का अधिकार सिर्फ आपके पास है, लेकिन फल की इच्छा मत रखिए।"
    "एक व्यक्ति को अपने मन से खुद को उठाना चाहिए, नहीं तो गिराना।"
    "जब-जब धर्म में गिरावट होती है, हे भारत के वंशज, और अधर्म का उदय होता है, तब-तब मैं स्वयं प्रकट होता हूं।"
    "शांति supreme ज्ञान है।"
    "योग कर्म में दक्षता है।"
)

declare -a application=(
    "Focus on your duties today without worrying about the results. Do your best and let go of the outcome."
    "Use your mind to lift yourself up today. Avoid negative thoughts that bring you down."
    "When you see injustice or wrongdoing, remember that you have the inner strength to stand up for what is right."
    "Cultivate inner peace through meditation and mindfulness. It is the highest wisdom."
    "Approach your tasks with mindfulness and excellence. Yoga is not just postures, but skill in everything you do."
)

# Number of quotes
count=${#sanskrit[@]}

# Filter indices that are not used
available_indices=()
for i in $(seq 0 $((count-1))); do
    # Check if sanskrit[i] is in used_quotes
    found=0
    for used in "${used_quotes[@]}"; do
        if [[ "${sanskrit[$i]}" == "$used" ]]; then
            found=1
            break
        fi
    done
    if [ $found -eq 0 ]; then
        available_indices+=($i)
    fi
done

# If none available, reset used quotes and use all
if [ ${#available_indices[@]} -eq 0 ]; then
    > "$USED_FILE"  # clear the file
    used_quotes=()  # reset the array
    available_indices=($(seq 0 $((count-1))))
fi

# Pick a random index from available_indices
random_index=${available_indices[$RANDOM % ${#available_indices[@]}]}

# Get the quote details
sanskrit_quote="${sanskrit[$random_index]}"
english_quote="${english[$random_index]}"
hindi_quote="${hindi[$random_index]}"
application_quote="${application[$random_index]}"

# Format the message
message="���🌟 *Daily Motivation* �� 🌟

���📜 *Sanskrit Verse*:
$sanskrit_quote

���🌐 *English Translation*:
$english_quote

���🇮���🇳 *Hindi Meaning*:
$hindi_quote

���💡 *Practical Application for Today*:
$application_quote

���🔁 This verse was selected from the pool of unused verses."

# Output the message
echo "$message"

# Append the used quote to the file
echo "$sanskrit_quote" >> "$USED_FILE"