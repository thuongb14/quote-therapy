const audios = document.querySelectorAll('audio');
const quotes = document.querySelectorAll('#quote');
const search = document.querySelector('.searchButton');
const modal = document.querySelector('.modal');
const imagesQuote = document.querySelectorAll('.quote-image');
const modalContent = document.querySelector('.modal-content');

// require('dotenv').config()

// const clientId = process.env.SPOTIFY_CLIENT_ID
// const clientSecret = process.env.SPOTIFY_CLIENT_SECRET

//Spotify API
const APIController = (() => {
  const clientId = '982b5eff3b2e4aeb91756e5de416f734';
  const clientSecret = '68083fb1d45244ec9bb7c480fd22bdc4';

  const getToken = async () => {
    const result = await fetch('https://accounts.spotify.com/api/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        Authorization: 'Basic ' + btoa(clientId + ':' + clientSecret),
      },
      body: 'grant_type=client_credentials',
    });

    const data = await result.json();
    return data.access_token;
  };

  const getPlaylist = async (token, playlist_id) => {
    const result = await fetch(
      `https://api.spotify.com/v1/playlists/${playlist_id}/tracks`,
      {
        method: 'GET',
        headers: { Authorization: 'Bearer ' + token },
      }
    );

    const data = await result.json();
    console.log(data.items);
    return data.items;
  };

  return {
    getToken() {
      return getToken();
    },
    getPlaylist(token, playlist_id) {
      return getPlaylist(token, playlist_id);
    },
  };
})();

const getTrack = (mood, audio) => {
  let trackName = mood[Math.round(Math.random() * 40)].track;
  let trackSource = trackName.preview_url;
  while (trackSource === null) {
    trackName = mood[Math.round(Math.random() * 40)].track;
    trackSource = trackName.preview_url;
    audio.src = trackSource;
    audio.dataset.name = trackName.name;
    audio.dataset.artist = trackName.artists[0]['name'];
  }
  audio.src = trackSource;
  audio.dataset.name = trackName.name;
  audio.dataset.artist = trackName.artists[0]['name'];
};

const loadPlaylist = async () => {
  const token = await APIController.getToken();

  const lovePlaylist = await APIController.getPlaylist(
    token,
    '3sCQjOcQ2OM9ubafs3cuOm'
  );
  const motivationalPlaylist = await APIController.getPlaylist(
    token,
    '2zZ6WRxzy9aByUvHRGc3Sw'
  );
  const inspirationalPlaylist = await APIController.getPlaylist(
    token,
    '3li1XfQKJnor5pi1TrEIop'
  );
  const happinessPlaylist = await APIController.getPlaylist(
    token,
    '4gWQkYXJODwOgk9ay6uuWF'
  );

  audios.forEach((audio) => {
    if (audio.className === 'happiness') {
      getTrack(happinessPlaylist, audio);
    }
    if (audio.className === 'motivational') {
      getTrack(motivationalPlaylist, audio);
    }
    if (audio.className === 'love') {
      getTrack(lovePlaylist, audio);
    }
    if (audio.className === 'inspirational') {
      getTrack(inspirationalPlaylist, audio);
    }
  });
};

loadPlaylist();

//Control audio tag
const audioPlayers = document.querySelectorAll('.audio-player');

if (audioPlayers.length) {
  audioPlayers.forEach(function (audioPlayer) {
    let audio = audioPlayer.querySelector('audio');
    let playerButton = audioPlayer.querySelector('.player-button');
    playerButton.addEventListener('click', (e) => {
      let current = e.currentTarget;
      let audio = current.closest('.audio-player').querySelector('audio');
      let btnSvg = current.querySelector('.useBtn');
      if (!audio.paused) {
        btnSvg.setAttribute('href', '#icon-play');
        audio.pause();
      } else {
        btnSvg.setAttribute('href', '#icon-pause');
        audio.play();
      }
    });

    let timeline = audioPlayer.querySelector('.timeline');
    timeline.addEventListener('change', () => {
      let time = (timeline.value * audio.duration) / 100;
      audio.currentTime = time;
    });

    audio.addEventListener('ended', () => {
      timeline.value = 0;
    });

    audio.addEventListener('timeupdate', () => {
      let percentagePosition = (100 * audio.currentTime) / audio.duration;
      timeline.value = percentagePosition;
    });
  });
}

//Search function
search.addEventListener('click', (e) => {
  let input = document.querySelector('.searchTerm').value.toLowerCase();
  quotes.forEach((quote) => {
    if (quote.className !== input) {
      quote.style = 'display: none';
    } else if (quote.className === input) {
      quote.style = 'display: ';
    }
    if (input == '') {
      quote.style = 'display: ';
    }
  });
  e.preventDefault();
});

//Quote pop up modal
imagesQuote.forEach((quote) => {
  quote.addEventListener('click', (e) => {
    modal.classList.remove('hidden');
    modalContent.innerHTML = `
    <h5 class="quote-name">${quote.nextElementSibling.innerText}</h5>
    <img class="quote-img" src="${quote.src}">
    <p class="track-name">Track name: ${quote.nextElementSibling.nextElementSibling.firstElementChild.dataset.name}
    </p>
    <p class="track-artist">Artist: ${quote.nextElementSibling.nextElementSibling.firstElementChild.dataset.artist}
    </p>
    <p>Posted by <a style="color: blue" href='/user_profile/${quote.dataset.id}'>${quote.dataset.name}</a></p>

    `;
  });
});

window.addEventListener('click', (e) => {
  if (e.target.className === 'modal') {
    modal.classList.add('hidden');
  }
});
