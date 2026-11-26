# AI for OSINT

AI tools, models and agent tooling that open-source investigators and journalists use, with the limits written next to each one.

**{N} entries. Every link was opened on {CHECKED}.** The same entries are on [Hugging Face as a dataset](https://huggingface.co/datasets/Ghongha007/ai-for-osint) you can filter or load in code.

Most AI tool lists tell you what a tool promises. This one also tells you two things that matter more in an investigation: **where your material goes** when you use the tool, and **what is known about how it fails**.

## How to read the tables

- **Runs** is the source-protection column. *Local* means the tool works on your own machine and your files stay there. *Cloud* means you upload material to someone else's servers. Do not put leaked documents, unpublished footage or anything that identifies a source into a cloud tool unless you have decided that risk is acceptable.
- **Type** is *Open source*, *Free web tool*, *Freemium*, *Paid* or *Restricted* (available only to vetted organisations or on request).
- **Known limit** is a documented limitation or risk. Where it is blank, we found nothing documented on the pages we checked. That is not the same as the tool having no limits.
- **Last activity** is the latest release, commit or post we could see. Tools marked *(stale)* have had no visible update for over a year.

## Three rules before you use any of these

1. **AI output is a lead, not a finding.** A transcript, a translation, a location guess or a detector score tells you where to look. Check it against the source material before it goes into a story.
2. **Detectors and geolocation models are confidently wrong, often.** Published tests in the last section show deepfake detectors losing much of their accuracy on real-world media, and language models inventing locations and citations. Never publish a detector score as proof.
3. **Speech-to-text models can invent words.** Check quotes against the audio.

## What is deliberately left out

Face-recognition services that identify private individuals, people-search and username or phone lookup tools, anything built on breached data, and penetration-testing toolkits. This list is about verifying media, reading documents, working across languages, analysing imagery and public records.
