## Tools that have closed or changed

See [research/NOTES.md](research/NOTES.md) for tools that shut down or became restricted (for example GeoSpy, the original TrueMedia.org and the open-source version of OCCRP Aleph), with a source for each.

## Contributing

Corrections are as welcome as additions: a tool that died, changed its pricing, or has a newly published test of its accuracy.

To add a tool, add an object to `research/entries.json` and run `python3 build_readme.py`. Fields: `category`, `name`, `url`, `what` (one sentence), `type`, `runs` (local, cloud or both), `maintainer`, `status` (active or stale), `last_activity` (YYYY-MM), `checked` (the day you opened the link) and `limit` (a documented limitation with its source, or an empty string). Please do not invent a limit, and keep to the scope above.

## Related

- [india-osint](https://github.com/Ghongha007/india-osint): public records and open data for investigating stories in India
- [chat2net](https://github.com/Ghongha007/chat2net): turn a chat or social-media export into a Gephi network
- [osint-skills](https://github.com/Ghongha007/osint-skills): agent skills for verification, geolocation, chronolocation and fact-checking
- [verify-mcp](https://github.com/Ghongha007/verify-mcp): an MCP server with keyless, read-only verification lookups

## Licence

The list is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The script is MIT. Compiled by [OSINT JOURNO](https://github.com/Ghongha007).
