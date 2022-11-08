const audios = document.querySelectorAll('audio');
const quotes = document.querySelectorAll('#quote');
const search = document.querySelector('.searchButton');
const modal = document.querySelector('.modal');

//Spotify API
const APIController = (function () {
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
      let happinessTrack =
        happinessPlaylist[Math.round(Math.random() * 30)].track;
      let artists = happinessTrack.artists;
      audio.src = happinessTrack.preview_url;
      audio.dataset.name = happinessTrack.name;
      audio.dataset.artist = artists[0]['name'];
    }
    if (audio.className === 'motivational') {
      let motivationalTrack =
        motivationalPlaylist[Math.round(Math.random() * 30)].track;
      let artists = motivationalTrack.artists;
      audio.src = motivationalTrack.preview_url;
      audio.dataset.name = motivationalTrack.name;
      audio.dataset.artist = artists[0]['name'];
    }
    if (audio.className === 'love') {
      let loveTrack = lovePlaylist[Math.round(Math.random() * 30)].track;
      let artists = loveTrack.artists;
      audio.src = loveTrack.preview_url;
      audio.dataset.name = loveTrack.name;
      audio.dataset.artist = artists[0].name;
    }
    if (audio.className === 'inspirational') {
      let inspirationalTrack =
        inspirationalPlaylist[Math.round(Math.random() * 30)].track;
      let artists = inspirationalTrack.artists;
      audio.src = inspirationalTrack.preview_url;
      audio.dataset.name = inspirationalTrack.name;
      audio.dataset.artist = artists[0]['name'];
    }
  });
};

loadPlaylist();

//Control audio tag
const audioPlayers = document.querySelectorAll('.audio-player');

if (audioPlayers.length) {
  audioPlayers.forEach(function (audioPlayer, i) {
    let audio = audioPlayer.querySelector('audio');
    let playerButton = audioPlayer.querySelector('.player-button');
    playerButton.addEventListener('click', function (e) {
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
    timeline.addEventListener('change', function (e) {
      let time = (timeline.value * audio.duration) / 100;
      audio.currentTime = time;
    });

    audio.addEventListener('ended', function (e) {
      timeline.value = 0;
    });

    audio.addEventListener('timeupdate', function (e) {
      let percentagePosition = (100 * audio.currentTime) / audio.duration;
      timeline.value = percentagePosition;
    });
  });
}

//Search function
search.addEventListener('click', () => {
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
});

const imagesQuote = document.querySelectorAll('.quote-image');
const modalContent = document.querySelector('.modal-content');

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
    <p>Posted by ${quote.dataset.avatar}
    </p>
    `;
  });
});

window.addEventListener('click', (e) => {
  if (e.target.className === 'modal') {
    modal.classList.add('hidden');
  }
});
