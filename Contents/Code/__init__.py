#! -*- coding:utf-8 -*-
# local media assets agent

import localmedia

PERSONAL_MEDIA_IDENTIFIER = "com.plexapp.agents.none"


class LocalSubsTV(Agent.TV_Shows):
    name = 'Local Subs (TV)'
    languages = [Locale.Language.NoLanguage]
    primary_provider = False
    persist_stored_files = False
    contributes_to = ['com.plexapp.agents.none']

    def search(self, results, media, lang):
        results.Append(MetadataSearchResult(id='null', score=100))

    def update(self, metadata, media, lang):
        # Look for subtitles for each episode.
        for s in media.seasons:
            # If we've got a date based season, ignore it for now, otherwise it'll collide with S/E folders/XML and PMS
            # prefers date-based (why?)
            if int(s) < 1900 or metadata.guid.startswith(PERSONAL_MEDIA_IDENTIFIER):
                for e in media.seasons[s].episodes:
                    for i in media.seasons[s].episodes[e].items:
                        # Look for subtitles.
                        for part in i.parts:
                            localmedia.findSubtitles(part)
            else:
                # Whack it in case we wrote it.
                # del metadata.seasons[s]
                pass
