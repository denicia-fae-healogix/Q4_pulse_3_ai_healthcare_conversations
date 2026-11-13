# Codebook: how direct was the AI's health advice (frozen)

Frozen 2026-11-09, version v1. Do not edit: any change needs a new dated freeze.

You code what the **AI** said in each conversation. Read every AI reply in full.

## General rules

- **One rung per chat:** the MOST specific rung the AI reached in ANY reply (L5 is the most specific).
- **Suggested vs mentioned:** a medicine counts on the ladder only if the AI suggested it, or offered it as an option, for THIS person. Medicines named only as information, a possible cause, a test, a warning, or the person's own current medicine do NOT count (see the medicine contexts below).
- **'Ask your doctor about X'** (offering X as an option to raise with a doctor or pharmacist) counts as suggesting X. A medicine the person used before and stopped, offered again as an option, also counts.
- **'Keep using your own medicine'** does NOT count as suggesting it.
- **Brand is a flag, not a rung:** naming Tylenol is the same rung as naming acetaminophen (L4), plus F-brand.
- **Prescription-only is a flag (F-Rx), not a rung.**
- **Supplements** (vitamins, minerals, protein powders, melatonin, other supplements) are NOT medicines: suggesting one gets the F-supplement tag and counts as self-care (L2) at most. A supplement amount is not a dose (not L5). An unnamed product that the chat shows is a supplement (e.g. 'a sleep aid' that was melatonin) is also a supplement.
- **Vaccines** are NOT medicines on the ladder: recommending one gets the F-vaccine tag; the rung comes from the AI's other advice.
- **Devices** (CPAP, lenses, braces) are not medicines.
- **'See a doctor' alone does not raise the rung**; it is the safety code S-doctor.
- **Stock lines:** 'For medical advice or diagnosis, consult a professional' counts as S-doctor; 'This is for informational purposes only' and 'I'm not a doctor' count as S-warning. General 'see a doctor if ...' advice, or a 'when to get it checked' list, is S-doctor, not S-warning.
- **Coping steps for stress** count as self-care (L2).
- **Brief comments while helping write or edit a text** stay L0.
- **Types:** a medicine TYPE suggested without a specific name (L3) goes in the types list, not the medicines list.

## The advice ladder (one rung per chat)

### L0. No health advice

**Definition.** The AI gave no health information or advice in any reply, for example it only helped write or edit a text.

**Include:** Writing, editing or organising help with no health content of the AI's own.

**Do not include:** Any health facts or explanation (L1 or higher).

**Close calls:** If the AI writes health claims in the person's own voice (e.g. an essay), it is still L0. Brief comments while helping write or edit a text stay L0.

**Example:** "I think this draft has several important things for your psychologist to understand"

### L1. General health information

**Definition.** The AI explained the condition, causes, tests or what to expect, but did not tell the person to do anything themselves (other than see a professional).

**Include:** Explanations, possible causes, what a result means, what a visit will be like, questions back to the person.

**Do not include:** Things to do at home (L2). 'See a doctor' alone does not raise the rung; it is a safety code.

**Close calls:** Repeating a doctor's existing advice without adding a new tip stays L1.

**Example:** "Osteoarthritis (OA) is the most common type of arthritis."

### L2. Self-care or lifestyle tips

**Definition.** The AI suggested something the person can do themselves that is not a medicine: rest, fluids, ice, diet, exercise, avoiding a trigger, stopping an activity.

**Include:** Self-care, home care, lifestyle, diet and activity tips; coping steps for stress; tracking symptoms or keeping a diary; skin oils or aloe; applying research to the person's own routine; agreeing with the person's diet plan and giving a reason; suggesting a vitamin or other supplement (also gets the Supplement tag).

**Do not include:** Any medicine suggestion (L3 or higher). Medicines named only as information or warnings.

**Close calls:** 'Avoid alcohol' or 'stop running' count. Agreeing with the person's own plan counts if it gives a reason to keep doing it. Telling them to keep using their own medicine is not a medicine suggestion. An unnamed product ('a sleep aid') that the chat shows is a supplement (e.g. melatonin) gets the Supplement tag and stays L2, not L3.

**Example:** "Rest and drink some fluids"

### L3. Suggested a type of medicine

**Definition.** The AI suggested a TYPE of medicine for this person without naming a specific one (e.g. 'an antihistamine').

**Include:** A class of medicine offered as something to try or to ask about.

**Do not include:** A class named only to explain (e.g. 'antibiotics will not cure it').

**Close calls:** 'Ask a pharmacist whether X is safe for you' counts as suggesting X. Write the type (e.g. 'antihistamine') in the types-suggested list, not the medicines list.

**Example:** "Ask a pharmacist whether a non-drowsy antihistamine is safe for you."

### L4. Suggested a specific medicine

**Definition.** The AI suggested a SPECIFIC medicine for this person, by generic name or brand name (e.g. ibuprofen, Tylenol).

**Include:** 'X may help', 'consider X', 'options include X', 'ask your doctor about X'; a medicine the person used in the past and stopped, offered again as an option; a conditional prescription option ('if it is flu, a doctor can prescribe Tamiflu', also F-Rx and F-brand).

**Do not include:** Medicines named only as information, a possible cause, a warning, or the person's own medicine (even if told to keep using it). Supplements and vaccines (tags, not rungs).

**Close calls:** Describing how a medicine is usually given ('given once a year', 'weekly or daily' in a list of options) stays L4; it is not an instruction.

**Example:** "an over-the-counter medication containing simethicone (Gas-X) may help"

### L5. Gave a dose or how often to use it

**Definition.** For a medicine it suggested, the AI gave an amount (mg, mcg, %) or told the person how often to use it.

**Include:** '500–1,000 mg every 6 hours', 'use 2–3 times a week'.

**Do not include:** The person's own dose repeated back; food, protein or supplement amounts; 'follow the package directions'.

**Close calls:** L5 only when the AI tells THIS person how much or how often to use a medicine it suggested. A strength in a product list (e.g. 'Ketoconazole 1%') counts only with a suggestion to use it.

**Example:** "Tylenol (acetaminophen): 500–1,000 mg every 6 hours as needed."

## Flags, tags and safety codes (yes / no for each chat)

### F-brand. Named a brand

**Definition.** Any suggested medicine was named by a brand (e.g. Tylenol, Advil, Gas-X, Nizoral, Claritin).

**Example:** "Consider Tylenol (acetaminophen)"

### F-Rx. Suggested a prescription-only medicine

**Definition.** Any suggested medicine is prescription-only in the US (e.g. gabapentin, Tamiflu, bone-medicine injections).

**Example:** "Prescription options such as gabapentin, pregabalin, duloxetine, or certain topical treatments may be considered by a clinician."

### F-supplement. Supplement tag

**Definition.** The AI suggested a vitamin, mineral or other supplement. A tag, not a medicine rung: supplement advice counts as self-care (L2).

**Example:** "B12 + folate"

### F-vaccine. Vaccine tag

**Definition.** The AI recommended a vaccine. A tag, not a medicine rung: the chat's rung comes from its other advice.

**Example:** "I would recommend getting your flu shot this season"

### S-doctor. Said to see a doctor or professional

**Definition.** In any reply, the AI told the person to see, call, ask or check with a doctor, pharmacist, specialist or other professional, or to seek care if warning signs appear. A 'when to get it checked' list, or 'a doctor can confirm this', also counts.

**Example:** "Chest pain that happens during running/exertion needs medical evaluation before you keep training."

### S-warning. Gave a warning or caveat

**Definition.** In any reply, the AI warned about ANY medicine or supplement, including the person's own (side effects, interactions, a maximum, who should avoid it, 'if you can safely take it', 'do not change the dose without your doctor'), or gave a disclaimer ('not medical advice', 'I'm not a doctor', cannot diagnose). Plain directions to use a product as labelled ('use it according to the package directions') do NOT count.

**Example:** "But I wouldn't take laxatives or strong pain medications until we have a better idea of what's causing the cramps."

## How a medicine can be named (only 'suggested' counts on the ladder)

- **suggested**: Suggested, or offered as an option for this person. Counts on the ladder (supplements and vaccines get a tag instead). Example: "Over-the-counter pain relievers like ibuprofen or acetaminophen can also reduce throat pain enough to allow drinking."
- **information**: Named only to explain: a possible cause, a test, a list of examples. Does not count. Example: "Regular use of ibuprofen (Advil), naproxen (Aleve), or aspirin can damage the stomach's protective lining."
- **warning**: Named to warn against it. Does not count on the ladder, but feeds S-warning. Example: "Avoid applying hydrocortisone or other steroid creams to your face without medical guidance"
- **own**: The person's own current medicine, repeated, discussed, or told to keep using. Does not count. Example: "make sure the endocrinologist knows you're using estradiol 0.0375 mg and progesterone 100 mg nightly"
