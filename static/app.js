let audios = document.querySelectorAll('audio');

audios.forEach((audio) => {
    if (audio.className === 'happiness') {
        audio.src = 'https://audio.jukehost.co.uk/bNk6Uijdz44HUFWT9DorrXi65OMEqvJN'
    } if(audio.className === 'motivational') {
        audio.src = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3'
    } if(audio.className === 'love') {
        audio.src = 'https://audio.jukehost.co.uk/mxFLvAHdwVy1ZPvWTbn6hupKYDXE1Uar'
    } if(audio.className === 'self-love') {
        audio.src = 'https://audio.jukehost.co.uk/mxFLvAHdwVy1ZPvWTbn6hupKYDXE1Uar'
    } if(audio.className === 'friendship') {
        audio.src = 'https://audio.jukehost.co.uk/mxFLvAHdwVy1ZPvWTbn6hupKYDXE1Uar'
    }
})