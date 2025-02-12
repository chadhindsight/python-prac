playlist = {
    "title": "Cat lovers playlist",
    "author": 'Devy_G',
    "songs": [
        {
            "title": " Its Meowing time",
            "artist": "Dollie featuring Koya",
            "album": "3AM Mix",
            "duration": 3.15
        },
        {
            "title": "Play Time",
            "artist": "Koya",
            "album": "Chase the laser pointer, protect the humans volume 3",
            "duration": 8.30
        },
        {
            "title": "Food Man is here",
            "artist": "Dollie",
            "album": "FEED",
            "duration": 2.55
        }, 
        ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)    