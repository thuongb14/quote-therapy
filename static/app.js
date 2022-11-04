let audios = document.querySelectorAll('audio');

const loveTracks = [
    "https://audio.jukehost.co.uk/mxFLvAHdwVy1ZPvWTbn6hupKYDXE1Uar", //her,
    "https://audio.jukehost.co.uk/QlNv7mcwD7C7b9cvGEjngOssK80jYPKb", //perfect on your own
    "https://audio.jukehost.co.uk/OZSCEjPNMq9wetnvysJSxOK2FI180mUS", //too easily
]

const hapinessTracks = [
    "https://audio.jukehost.co.uk/bNk6Uijdz44HUFWT9DorrXi65OMEqvJN", //I miss you
    "https://audio.jukehost.co.uk/7CPqHPM8Sh16Z3529pHhGYxS75UjsiRO", //spring waltz
    "https://audio.jukehost.co.uk/YcxyBlQRzffjkrSk8Jv9lNwoPmqd31Et", //sunday
]

const motivationalTracks = [
    "https://audio.jukehost.co.uk/fjAaLKtRwL7tsIt9vEuVjNO7MWmQDq8I", //cold brew coffee
    "https://audio.jukehost.co.uk/nPL5qCGnE536fygRbWfObGb6wmz8kgow", //dreams
    "https://audio.jukehost.co.uk/2aUc6bFEi7nnr3w1byEB9hsfOax5HwOT", //samba
]

const inspirationalTracks = [
    "https://audio.jukehost.co.uk/dPgY14X0YypFJXDLgYqGVKr7RoKAVnO4", //sorry not answering
    "https://audio.jukehost.co.uk/7UQXHsTBzEVa8oBCkjVmxy97tbLbajZB", //affection
    "https://audio.jukehost.co.uk/A8eAfeHb1wJXseUaFdhMkriLTmjey4BR", //steps

]

audios.forEach((audio) => {
    if (audio.className === 'happiness') {
        audio.src = hapinessTracks[Math.round(Math.random() * hapinessTracks.length)]
    } if(audio.className === 'motivational') {
        audio.src = motivationalTracks[Math.round(Math.random() * motivationalTracks.length)]
    } if(audio.className === 'love') {
        audio.src = loveTracks[Math.round(Math.random() * loveTracks.length)]
    } if(audio.className === 'inspirational') {
        audio.src = inspirationalTracks[Math.round(Math.random() * inspirationalTracks.length)]
    } 
});

