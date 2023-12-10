// AudioTube jQuery dynamic functions
$(document).ready(function () {
  // git the data that render by flask
  let listV = $('.tags LI.def').attr('data');
  listV = JSON.parse(listV);
  videos(listV);
  // display the search field when click on the search icon
  $('#searchBtn').click(function () {
    $('.search').css('display', 'flex');
    $('.search').focus();
    $('IMG#searchBtn').hide();
    $('.tags').hide();
  });

  $('#searchInput').blur(function () {
    $(this).hide();
  });
  // hide the serach field when click outside the filter section if the input
  // field empty
  $(document).click(function (event) {
    if (!$(event.target).closest('.filter').length && !$('input').val()) {
      $('.filter .search').hide();
      $('IMG#searchBtn').show();
      $('.tags').show();
    }
  });
  // change content based on the catagory selected
  $('.tags LI').on('click', function () {
    $('LI').removeClass('def');
    $(this).addClass('def');
    $('SECTION.videos').empty();
    $('.load').show();
    if ($(this).attr('data')) {
      const vid = JSON.parse($(this).attr('data'));
      videos(vid);
    } else {
      $.get(`https://aalidrisy.tech/api/v1/catagories/${$(this).attr('id')}`, (data, textStatus) => {
        if (textStatus === 'success') {
          $('.tags LI.def').attr('data', JSON.stringify(data));
          videos(data);
        }
      });
    }
  });
  // handel the search event
  $('.search').on('submit', function (e) {
    e.preventDefault();
    $('SECTION.videos').empty();
    $('.exit').show();
    $('.load').show();
    $.get(`https://aalidrisy.tech/api/v1/search/${$('.input').val()}`, (data, textStatus) => {
      if (textStatus === 'success') {
        videos(data);
      }
    });
  });
  // exit search and gobacke to the main page
  $('.exit').on('click', function (event) {
    $('.filter .search').hide();
    $('.exit').hide();
    $('IMG#searchBtn').show();
    $('.tags').show();
    $('.filter .search .input').val('');
    $('SECTION.videos').empty();
    let listv = $('.tags LI.def').attr('data');
    listv = JSON.parse(listv);
    videos(listv);
  });
  // dispaly play and downloud options
  $(document).on('click', 'DIV.play', function () {
    if (!$(`.video DIV#${$(this).attr('id')}r`).text()) {
      $(`I#${$(this).attr('id')}`).show();
      $(`.video DIV#${$(this).attr('id')}r`).addClass('brd');
      $(`.video DIV#${$(this).attr('id')}r`).append(`<div class="op-play" id="${$(this).attr('id')}" v-id="${$(this).attr('v-id')}">Play</div><div class="op-download" id="${$(this).attr('id')}" v-id="${$(this).attr('v-id')}">Download</div>`);
    }
  });
  // play audio
  $(document).on('click', '.op-play', function () {
    $.get(`https://aalidrisy.tech/api/v1/audios/${$(this).attr('v-id')}`, (data, textStatus) => {
      if (textStatus === 'success') {
        $('.video DIV.player').removeClass('brd');
        $('.ex').hide();
        $('.video DIV.player').empty();
        $(`.video DIV#${$(this).attr('id')}r`).append(`<audio controls autoplay><source src="${data.url}" type="audio/mpeg">Your browser does not support the audio element.</audio>`);
        $(`.video DIV#${$(this).attr('id')}r`).addClass('brd');
        $(`I#${$(this).attr('id')}`).show();
      }
    });
  });
  // display downloud options as video or audio
  $(document).on('click', '.op-download', function () {
    $(`.video DIV#${$(this).attr('id')}r`).empty();
    $(`.video DIV#${$(this).attr('id')}r`).append(`<div class="op-audio" id="${$(this).attr('id')}" v-id="${$(this).attr('v-id')}">Audio</div><div class="op-video" id="${$(this).attr('id')}" v-id="${$(this).attr('v-id')}">Video</div>`);
  });
  // display quality options to downloud videos
  $(document).on('click', '.op-video', function () {
    $.get(`https://aalidrisy.tech/api/v1/formats/${$(this).attr('v-id')}`, (data, textStatus) => {
      if (textStatus === 'success') {
        $(`.video DIV#${$(this).attr('id')}r`).empty();
        for (const vid of data.vformats) {
          const options = `<form action="/download" method="POST"><input name="url" value="${vid.url}" style="display: none;" /> <input name="filename" value="${data.title}.mp4" style="display: none;" /><button class="quality" type="submit">${vid.quality}</button></form>`;
          $(`.video DIV#${$(this).attr('id')}r`).append(options);
        }
      }
    });
  });
  // cleare the play/downloud contener
  $(document).on('click', '.ex', function () {
    $(`.video DIV#${$(this).attr('id')}r`).empty();
    $(`.video DIV#${$(this).attr('id')}r`).removeClass('brd');
    $(`I#${$(this).attr('id')}`).hide();
  });
  // display the downloud formats for audio
  $(document).on('click', '.op-audio', function () {
    $.get(`https://aalidrisy.tech/api/v1/formats/${$(this).attr('v-id')}`, (data, textStatus) => {
      if (textStatus === 'success') {
        const aud = data.aformats[0];
        $(`.video DIV#${$(this).attr('id')}r`).empty();
        const optMp3 = `<form action="/download" method="POST"><input name="url" value="${aud.url}" style="display: none;" /> <input name="filename" value="${data.title}.mp3" style="display: none;" /><button class="quality" type="submit">mp3</button></form>`;
        const optM4a = `<form action="/download" method="POST"><input name="url" value="${aud.url}" style="display: none;" /> <input name="filename" value="${data.title}.m4a" style="display: none;" /><button class="quality" type="submit">m4a</button></form>`;
        $(`.video DIV#${$(this).attr('id')}r`).append(optMp3, optM4a);
      }
    });
  });
  // display videos
  function videos (vidList) {
    $('.load').hide();
    for (const video of vidList) {
      $('SECTION.videos').append(`<div class="video"><div class="play" id="v${video.id}" v-id="${video.id}"><img src="${video.img}" /><p class="time">${video.duration}</p><h3>${video.title}</h3></div><i class="ex" id="v${video.id}"></i><div class="player" id="v${video.id}r"  v-id="${video.id}"></div><div class="detail"><div class="channel"><img src="${video.cimg}" /><p>${video.cname}</p></div><div class="info"><p class="views">${video.views}</p><p class="date">${video.publishedTime}</p></div></div></div>`);
    }
  }
  $('button.menu').click(function () {
    $('nav.navbar').toggleClass('non');
  });
});
