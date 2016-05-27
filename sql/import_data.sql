INSERT INTO musictable_song
(id, title, author, scripture, key_lyric, notes, quarantined)
SELECT id, Title, Artist, Scripture, LyricsExcerpt, Notes, Quarantined
FROM musictable_php.songs;

INSERT INTO musictable_attachment
(id, name, location, song_id)
SELECT a.id, a.name, a.url, s.song_id
FROM musictable_php.attachments a
JOIN musictable_php.attachments_songs s
	ON a.id = s.attachment_id;
	
INSERT INTO musictable_tagtype
(id, name)
SELECT id, Name
FROM musictable_php.tagtypes;


INSERT INTO musictable_tag
(id, name, type_id)
SELECT t.id, t.name, tt.tagtype_id
FROM musictable_php.tags t
JOIN musictable_php.tags_tagtypes tt
	ON t.id = tt.tag_id; /* no quarnatine tag */
	
INSERT INTO musictable_song_tags
(id, song_id, tag_id)
SELECT id, song_id, tag_id
FROM musictable_php.songs_tags
WHERE tag_id != 92; /* no quarantine tag */