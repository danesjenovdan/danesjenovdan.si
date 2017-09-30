var LANDING_TEMPLATES = {
  makeProjectTile: function(title, text, url, image) {
    return '\
      <div class="col-md-4 col-sm-6">\
        <div class="landing-tile">\
          <a href="' + url + '" target="_blank" class="landing-tile__link">\
            <div class="landing-tile__image" style="background-image: url(\'' + image + '\');">\
              <span class="icon-arrow-right"></span>\
            </div>\
            <div class="landing-tile__content">\
              <h1 class="landing-tile__title">' + title + '</h1>\
              <p class="landing-tile__text">' + text + '</p>\
            </div>\
          </a>\
        </div>\
      </div>\
    ';
  },
}

$.getJSON('http://djapi.knedl.si/djndLanding/projects/3/')
  .done(function(json) {
    if (json.status != 'OK') {
      return;
    }
    var container = $('#landing-append-projects');
    for (var i = 0; i < json.data.length; i++) {
      var data = json.data[i];
      var tile = LANDING_TEMPLATES.makeProjectTile(data.title, data.label, data.url, data.image);
      container.append(tile);
    }
    $('.landing-tile').equalizeHeights();
  });
