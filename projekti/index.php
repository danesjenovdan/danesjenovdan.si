<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- meta info + OG tags -->
    <title>Projekti</title>
    <meta name="description" content="Živimo, kar delamo. Delamo, v kar verjamemo. Verjamemo, kar govorimo. Govorimo, kar nočete slišati. Slišite, ker vam znamo povedati. Povemo vam, ker je to naša dolžnost. Vaša dolžnost je, da poveste naprej.">
    <meta name="author" content="Danes je nov dan, Inštitut za druga vprašanja">
    <link rel="shortcut icon" href="https://danesjenovdan.si/favicon.ico">

    <meta property="og:title" content="Projekti" />
    <meta property="og:type" content="article" />
    <meta property="og:description" content="Živimo, kar delamo. Delamo, v kar verjamemo. Verjamemo, kar govorimo. Govorimo, kar nočete slišati. Slišite, ker vam znamo povedati. Povemo vam, ker je to naša dolžnost. Vaša dolžnost je, da poveste naprej." />
    <meta property="og:image" content="https://danesjenovdan.si/img/djndog.png" />

    <!-- Bootstrap -->
    <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

    <!-- font -->
    <link href='https://fonts.googleapis.com/css?family=Titillium+Web:200,300,400,600,700&subset=latin-ext,latin' rel='stylesheet' type='text/css'>

    <!-- icons -->
    <link href="/icons_/icons.css" rel="stylesheet">

    <!-- CSS -->
    <link href="/css/guide.css?180804" rel="stylesheet">

    <!-- WP fix -->
    <script>
        (function () {
            if ("-ms-user-select" in document.documentElement.style && navigator.userAgent.match(/IEMobile\/10\.0/)) {
                var msViewportStyle = document.createElement("style");
                msViewportStyle.appendChild(
                    document.createTextNode("@-ms-viewport{width:auto!important}")
                );
                document.getElementsByTagName("head")[0].appendChild(msViewportStyle);
            }
        })();
    </script>

</head>

<body>

    <style>
        a {
            color: #704a45;
            font-weight: bold;
        }
        a:hover {
            color: #704a45;
        }
    </style>

    <div id="menucontent">
        <div id="menuheader">
            <div id="menuclose">
                <div id="menucloseicon" class="icon col-light-red">×</div>
            </div>
            <div id="menutitle" class="bck-light-red">Danes je nov dan</div>
            <div class="col-light-red" id="menutitleback">Danes je nov dan</div>
        </div>
        <div class="menuitem menuitem-agrument" data-menu="agrument">
            <div class="ribbon bck-light-green"></div>Agrument</div>
        <div class="menuitem" data-menu="obcasnik/">
            <div class="ribbon bck-light-red"></div>Občasnik</div>
        <div class="menuitem active" data-menu="projekti/">
            <div class="ribbon bck-light-red"></div>Projekti</div>
        <div class="menuitem" data-menu="krivi/">
            <div class="ribbon bck-light-green"></div>Krivi</div>
        <div class="menuitem" data-menu="dolzni/">
            <div class="ribbon bck-light-gold"></div>Dolžni</div>
        <div class="menuitem" data-menu="konsenz/">
            <div class="ribbon bck-light-green"></div>Konsenz</div>
        <div class="menuitem" data-menu="formalnosti/">
            <div class="ribbon bck-light-gold"></div>Formalnosti</div>
    </div>

    <div class="container-fluid">
        <div class="row bck-red" id="header">
            <div class="container">
                <div class="row">
                    <div id="menu" class="bck-light-red">
                        <div class="menutoggle">
                            <div class="icon-menu"></div>
                        </div>
                        <h1 class="nologo">Meni</h1>
                    </div>
                    <div class="languagetoggle bck-light-red" data-href="/en/">
                        <h1 class="nologo">En</h1>
                    </div>
                    <div class="col-md-12">
                        <h1 id="intro"><span id="title">PROJEKTI /</span> Živimo, kar delamo. Delamo, v kar verjamemo. Verjamemo, kar govorimo. Govorimo, kar nočete slišati. Slišite, ker vam znamo povedati. Povemo vam, ker je to naša dolžnost. Vaša dolžnost je, da poveste naprej.</h1>
                    </div>
                </div>
            </div>
        </div>

        <div class="container">

            <div class="row">
                <div class="col-xs-12">
                    <div class="cookiewarning cookiewarning-red">
                        <span class="cookiewords">Soglašam z uporabo piškotkov</span><br class="visible-xs">
                        <div class="confirmcookies btn-cookie bck-red">V REDU</div>
                        <div class="cookiemoreinfo btn-cookie bck-light-red">Želim več informacij</div>
                    </div>
                </div>
            </div>

            <div class="row flex-row">


<?php

error_reporting(0);

$projekti = json_decode(file_get_contents('projekti.json'), true);

foreach ($projekti['projects'] as $index => $projekt) {
  if (isset($projekt['show']) && $projekt['show']) {
    echo('
      <div class="col-md-4 col-sm-6 col-project">
        <div class="tile tile-project '.($projekt['pinned'] ? 'tile-project--pinned': '').'" id="'.$projekt['id'].'" data-href="'.$projekt['popup'].'">
          <div class="obcasniktileimage" style="height:180px;" data-img="'.$projekt['image'].'" style="max-width:auto"></div>
          <h1 class="projecttiletitle">'.$projekt['title'].'</h1>
          <p class="projecttiletext">'.$projekt['text'].'</p>
          <div class="projectnumbercontainer">
            '.$projekt['projectNumberHTML'].'
            <div class="arrow-down-right bck-red arrow-project">
              <div class="icon-arrow-down-right icon-arrow-turn-up"></div>
            </div>
          </div>
        </div>
      </div>
    ');
  }
}

?>


            </div>

        </div>
        <!-- end of container -->

        <div class="row" id="footer">
            <svg id="footerdivider" xmlns="http://www.w3.org/2000/svg" version="1.1" width="100%" height="40px" viewBox="0 0 100 102" preserveAspectRatio="none">
                <path d="M0 0 L50 300 L100 0 Z"></path>
            </svg>
            <div class="container">
                <div class="row">
                    <div class="col-md-3 footerline">
                        <div id="newsletter" data-href="signup" class="icon-newsletter col-red buzz-out"></div>
                        <p id="newslettertext" class="footertext"><a class="footerlink link-red" href="/jaz/">Naroči se na e-novice.</a> Pišemo samo, kadar imamo res kaj povedati.</p>
                    </div>
                    <div class="col-md-3 footerline">
                        <div id="socialcontainer">
                            <div class="social push bck-red" data-href="https://www.facebook.com/danesjenovdan">
                                <div class="icon icon-facebook"></div>
                            </div>
                            <div class="social push bck-red" data-href="https://twitter.com/danesjenovdan">
                                <div class="icon icon-twitter"></div>
                            </div>
                            <div class="social push bck-red" data-href="https://github.com/danesjenovdan">
                                <div class="icon icon-github"></div>
                            </div>
                            <div class="social push bck-red" data-href="https://vimeo.com/user26914674">
                                <div class="icon icon-vimeo"></div>
                            </div>
                            <div class="social push bck-red" data-href="https://www.youtube.com/channel/UCWMqx3p_QtWjdDRq58Hfh_w">
                                <div class="icon icon-youtube"></div>
                            </div>
                            <div class="social push bck-red" data-href="https://agrument.danesjenovdan.si/rss/">
                                <div class="icon icon-rss"></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 footerline">
                        <span id="podpri"><object data="/img/heart2.svg" class="icon-heart-line" type="image/svg+xml" /></object><span class="icon icon-heart col-red"></span>Podpri nas!</span>
                    </div>
                    <div class="col-md-3 footerline">
                        <p class="footertext" id="izkaznica"><a class="link-red" href="/formalnosti/">Danes je nov dan</a>
                            <br>Inštitut za druga vprašanja
                            <br>Parmova ulica 20
                            <br>1000 Ljubljana
                            <br>
                            <br><a class="footerlink link-red" href="mailto:vsi@danesjenovdan.si">vsi@danesjenovdan.si</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <!-- end of container-fluid -->

    <div class="popup popup-red centermycontentvertically" id="signup">
        <div class="popupclose">
            <div class="icon-close"></div>
        </div>
        <div class="container popupcontainer centermevertically">
            <div class="row">
                <div class="col-md-6 col-md-offset-3">
                    <p class="popuptext">Dodajte me na mailing listo.</p>
                    <form class="ac-custom ac-checkbox ac-checkmark">
                        <input id="newsletteremail" type="email" class="form-control" placeholder="ti@email.com">
                        <ul>
                            <li>
                                <input id="dodajme" name="dodajme" type="checkbox">
                                <label for="dodajme">dodaj me na listo podpornikov</label>
                                <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"></svg>
                            </li>
                        </ul>
                        <div class="hider">
                            <p class="popuptext">Zaupaj nam še svoje polno ime.</p>
                            <input id="newslettername" type="text" class="form-control" placeholder="Ime Priimek">
                        </div>
                    </form>
                    <button class="btn btn-popup push" id="submitemail">Oddaj!</button>
                </div>
            </div>
        </div>
    </div>


<?php

function get_popup_ids($n) {
  return $n['popup'];
}

function find_prop($prop, $id, $array) {
  foreach ($array as $key => $val) {
    if ($val[$prop] === $id) {
      return $val;
    }
  }
  return null;
}

function popup_for_id($n) {
  global $projekti;
  return find_prop('id', $n, $projekti['popups']);
}

$popup_ids = array_map('get_popup_ids', $projekti['projects']);
$popups = array_map('popup_for_id', $popup_ids);

foreach ($popups as $index => $popup) {
  $prev = isset($popups[$index-1]) ? $popups[$index-1]['title'] : '';
  $next = isset($popups[$index+1]) ? $popups[$index+1]['title'] : '';
  echo('
    <div class="popup popup-projekt popup-red centermycontentvertically" id="'.$popup['id'].'">
      <div class="popupclose">
        <div class="icon-close"></div>
      </div>
      '.(
        $prev
          ? '<div class="previousproject arrow-obcasnik-left bck-red hidden-xs hidden-sm">
               <div class="titlenext titlenext-left">'.$prev.'</div>
               <div class="icon icon-arrow-left"></div>
             </div>'
          : ''
      ).'
      '.(
        $next
          ? '<div class="nextproject arrow-obcasnik-right bck-red hidden-xs hidden-sm">
               <div class="titlenext titlenext-right">'.$next.'</div>
               <div class="icon icon-arrow-right"></div>
             </div>'
          : ''
      ).'
      <div class="container popupcontainer centermevertically">
        <div class="row">
          <div class="col-md-6 col-md-offset-3">
            <h1 class="popuptitle">'.$popup['title'].'</h1>
            <p class="popuptext">'.$popup['text'].'</p>
            '.(
              (isset($popup['href']) && isset($popup['buttonText']))
                ? '<div class="btn btn-popup push btn-projekt" data-href="'.$popup['href'].'">'.$popup['buttonText'].'</div>'
                : ''
            ).'
            <div class="btn btn-popup push btn-zapri">Zapri</div>
          </div>
        </div>
      </div>
    </div>
  ');
}

?>


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/bootstrap/js/bootstrap.min.js"></script>

    <!-- jQuery cookie -->
    <script src="/js/jquery.cookie.js"></script>
    <!-- NSA -->
    <script src="/js/nsa.js"></script>

    <!-- frontend magic -->
    <script src="/js/front.js?180920"></script>

<!-- Matomo -->
<script type="text/javascript">
  var _paq = _paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['setDoNotTrack', true]);
  _paq.push(['disableCookies']);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u='//track.djnd.si/';
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', '6']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//track.djnd.si/piwik.php?idsite=6&rec=1" style="border:0;" alt="" /></p></noscript>
<!-- End Matomo Code -->
</body>

</html>
