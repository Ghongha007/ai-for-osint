# Research notes (checked 2026-11-16)

## (a) Dead, shut or restricted

- **GeoSpy**: public version closed Q1 2025 after 404 Media reporting; now "qualified government and enterprise" only. https://geospy.ai/blog/why-america-s-heroes-deserve-the-visual-super-intelligence
- **TrueMedia.org**: non-profit closed January 2025 and open-sourced its models (unmaintained); revived at Georgetown, beta by request. https://www.geekwire.com/2025/truemedia-is-back-deepfake-detection-tool-revived-now-managed-by-georgetown-university/
- **OCCRP Aleph (open source)**: OCCRP moved to Aleph Pro, not open source; DARC's OpenAleph fork continues. https://www.occrp.org/en/announcement/occrp-announces-a-new-chapter-for-its-investigative-data-platform-aleph-pro
- **OpenAI AI Text Classifier**: withdrawn July 2023 for low accuracy. https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
- **Unreachable today, status unconfirmed**: scanner.deepware.ai, invid-project.eu, idir.claimbuster.org.

## (b) Prior art

OSINT MCP servers (stars, last commit):

- https://github.com/OpenOSINT/OpenOSINT (1,939; 2026-11): 21 tools, DNS/RDAP/WHOIS/GDELT/dorks keyless, rest keyed.
- https://github.com/marc-shade/world-intel-mcp (1,079; 2026-10): 160 tools, conflict, aircraft, maritime, sanctions, markets.
- https://github.com/w0h1v/mcp-maigret (273; 2026-11): username search across sites. Excluded from entries (people-finding).
- https://github.com/frishtik/osint-tools-mcp-server (250; 2025-08, stale): wraps username/email tools. Excluded.
- https://github.com/w0h1v/mcp-shodan (191; 2026-11): Shodan, needs key.
- https://github.com/nso-india/esankhyiki-mcp (148; 2026-11): official MoSPI statistics.
- https://github.com/Mearman/mcp-wayback-machine (66; 2026-10): Wayback check/fetch/save.
- https://github.com/badchars/osint-mcp-server (62; 2026-03): 37 tools, 21 keyless.

Skill packs:

- https://github.com/Oldcircle/geo-sleuth (7,088; 2026-11): photo geolocation only.
- https://github.com/elementalsouls/Claude-OSINT (3,055; 2026-10): security recon, dorks, secret patterns. Excluded (pentest).
- https://github.com/jamditis/claude-skills-journalism (453; 2026-11): source verification, C2PA, web archiving, FOIA.
- https://github.com/assafkip/investigators-copilot (76; 2026-11): case management, evidence capture, source grading.
- https://github.com/UseOSINT/Skills (63; 2026-08): 28 skills, largely person/phone/email profiling. Excluded.
- https://github.com/reichaves/osint-investigation (7; 2026-05): Berkeley Protocol lead sheets, Brazil records.

Gaps. (i) India public records: only statistics (MoSPI) and two near-dead 2-star projects (data.gov.in, tenders); nothing for MCA company data, eCourts, land records, election affidavits, gazettes or RTI. Skill packs cover US FOIA, Brazil and France only. (ii) Verification workflow: archiving and source verification exist (jamditis, OSINT Forge, Investigators Co-Pilot), as do geolocation (geo-sleuth) and claim-by-claim checking (bullshit-detector, 163 stars). jamditis has a hook flagging unattributed quotes, but I found no skill for tracing a claim to its first source. Chronolocation appears only as a sub-technique inside UseOSINT/Skills; the MCP list's media-verification section has one entry. (iii) Keyless: partial tiers exist (OpenOSINT, badchars, GDELT, Wayback), but they are infrastructure-focused; no keyless server bundles verification lookups (fact-check search, archive, EXIF/C2PA, sun position, OSM).

## (c) Existing lists

- https://github.com/ubikron/Awesome-AI-OSINT: 802 stars, about 100 links, last commit 2026-05.
- https://github.com/soxoj/awesome-osint-mcp-servers: 548 stars, about 115 servers, 2026-11.
- https://github.com/osintshifu/awesome-osint-repos: 106 stars, about 500 links, 2026-11.
- https://github.com/shvyac/awesome-osint-ai: 0 stars, about 60 links, 2026-10.
- https://github.com/jivoi/awesome-osint: 31,120 stars, general OSINT, 2026-11.
