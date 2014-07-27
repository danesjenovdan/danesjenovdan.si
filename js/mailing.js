// create a new instance of the Mandrill class with your API key
var m = new mandrill.Mandrill('fztWSmGdJFPbxPx7eNe1Zg');

function sendTheMail(email, html) {
// Send the email!
    
    // create a variable for the API call parameters
    var params = {
        'message': {
            'from_email': 'vsi@danesjenovdan.si',
            'to':[{
                'email': email
            }],
            'subject': 'Hvala',
            'html': html,
            'autotext': true,
            'track_opens': true,
            'track_clicks': true
        }
    };

    m.messages.send(params, function(res) {
        console.log(res);
    }, function(err) {
        console.log(err);
    });
}

function sendTheNaturalijeMail(email, html) {
// Send the email!
    
    // create a variable for the API call parameters
    var params = {
        'message': {
            'from_email': 'vsi@danesjenovdan.si',
            'to':[{
                'email': email
            }],
            'subject': 'Nekdo je obljubil naturalije',
            'html': html,
            'autotext': true,
            'track_opens': true,
            'track_clicks': true
        }
    };

    m.messages.send(params, function(res) {
        console.log(res);
    }, function(err) {
        console.log(err);
    });
}


// paypal po pošti HTML
var paypalmajicaHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, s katerim izkazuješ visoko mero cinične ozaveščenosti in upora proti dejanju, ki se mnogokrat kaže kot edino možno: spokat culo in vamos. Majico damo na pošto takoj, ko prejmemo plačilo prek Paypala.</p>',
                        '<p>Če med čakanjem nanjo bereš <a href="http://agrument.danesjenovdan.si/">Agrumente</a>, garantirano prej pride.</p>',
                        '<p>Dobro jo nosi.</p>',
                        '<p>Iskreno upajoč, da ti majica paše dovolj dobro za novo profilko na družbenih omrežjih, te pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var paypalrizleHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, ki te uvršča med urbane šamane, ruralne čudake ali v srednješolsko populacijo. Od preostalih pripadnic in pripadnikov omenjenih skupin pa te od bližajočega se trenutka, ko uleti tisti/-a, ki (poleg neke verske skupnosti) menda edini zvoni dvakrat, prične ločiti vsaj to, da ne uporabljaš nekih brezveznih rizel. Plačati mu/ji ni treba nič, saj bomo tvoje rizle odposlali takoj, ko prejmemo plačilo preko Paypala.</p>',
                        '<p>Za nadaljnje točke razhajanj z ljudsko povprečnostjo med čakanjem na najbolj politično odgovoren užitkarski pribor priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                        '<p>Iskreno upajoč, da ti vsak dan uspe zadovoljno prikimati starodavni modrosti, ki jo najdeš v paketku, te lepo pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var paypalvseHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup. Vemo, da tvoj izbor obeh artiklov ni posledica tega, da se ne znaš odločiti, ampak prav nasprotno - dokaz, da se znaš. Čestitke za to. Roba gre na pošto takoj, ko prejmemo plačilo prek Paypala. In ker očitno hočeš ves naš merch, spoiler alert, dobiš še presenečenje.</p>',
                     '<p>Medtem pa, ko čakaš na majico, ki bo krasila tvojo novo profilko na družbenih omrežjih, in rizle, ki bodo razvadi pridodale politično dimenzijo, za krajšanje časa priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                     '<p>Iskreno upajoč, da ti bo kupljeno v veselje, te lepo pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');


// poloznica po pošti HTML
var poloznicamajicaHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup, s katerim izkazuješ visoko mero cinične ozaveščenosti in upora proti dejanju, ki se mnogokrat kaže kot edino možno: spokat culo in vamos. Takoj, ko plačaš račun, gre tvoja majica na pošto in se odpošlje. Kar sama. Resno.</p>',
                     '<p>Če med čakanjem nanjo bereš <a href="http://agrument.danesjenovdan.si/">Agrumente</a>, garantirano prej pride.</p>',
                     '<p>Dobro jo nosi.</p>',
                     '<p>Iskreno upajoč, da ti majica paše dovolj dobro za novo profilko na družbenih omrežjih, te pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var poloznicarizleHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, ki te uvršča med urbane šamane, ruralne čudake ali v srednješolsko populacijo. Od preostalih pripadnic in pripadnikov omenjenih skupin pa te od trenutka, ko plačaš pripet račun in mi tvoje naročilo nemudoma odnesemo na pošto, prične ločiti vsaj to, da ne uporabljaš nekih brezveznih rizel.</p>',
                        '<p>Za nadaljnje točke razhajanj z ljudsko povprečnostjo med čakanjem na najbolj politično odgovoren užitkarski pribor priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                        '<p>Iskreno upajoč, da ti vsak dan uspe zadovoljno prikimati starodavni modrosti, ki jo najdeš v paketku, te lepo pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var poloznicavseHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup. Vemo, da tvoj izbor obeh artiklov ni posledica tega, da se ne znaš odločiti, ampak prav nasprotno - dokaz, da se znaš. Čestitke za to. Čimprej plačaj priložen račun, da robo takoj odpremimo na pošto. In ker očitno hočeš ves naš merch, spoiler alert, dobiš še presenečenje.</p>',
                     '<p>Medtem pa, ko čakaš na majico, ki bo krasila tvojo novo profilko na družbenih omrežjih, in rizle, ki bodo razvadi pridodale politično dimenzijo, za krajšanje časa priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                     '<p>Iskreno upajoč, da ti bo kupljeno v veselje, te lepo pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

// po povzetju po pošti
var popovzetjumajicaHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup, s katerim izkazuješ visoko mero cinične ozaveščenosti in upora proti dejanju, ki se mnogokrat kaže kot edino možno: spokat culo in vamos. Majico damo nemudoma na pošto, račun pa poravnaj pri tistemu/-i, ki (poleg neke verske skupnosti) menda edini zvoni dvakrat.</p>',
                     '<p>Če med čakanjem nanjo bereš <a href="http://agrument.danesjenovdan.si/">Agrumente</a>, garantirano prej pride.</p>',
                     '<p>Dobro jo nosi.</p>',
                     '<p>Iskreno upajoč, da ti majica paše dovolj dobro za novo profilko na družbenih omrežjih, te pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var popovzetjurizleHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, ki te uvršča med urbane šamane, ruralne čudake ali v srednješolsko populacijo. Od preostalih pripadnic in pripadnikov omenjenih skupin pa te od bližajočega se trenutka, ko uleti tisti/-a, ki (poleg neke verske skupnosti) menda edini zvoni dvakrat, prične ločiti vsaj to, da ne uporabljaš nekih brezveznih rizel. Prosimo, če mu/ji plačaš tudi račun.</p>',
                        '<p>Za nadaljnje točke razhajanj z ljudsko povprečnostjo med čakanjem na najbolj politično odgovoren užitkarski pribor priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                        '<p>Iskreno upajoč, da ti vsak dan uspe zadovoljno prikimati starodavni modrosti, ki jo najdeš v paketku, te lepo pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var popovzetjuvseHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup. Vemo, da tvoj izbor obeh artiklov ni posledica tega, da se ne znaš odločiti, ampak prav nasprotno - dokaz, da se znaš. Čestitke za to. Roba gre direkt na pošto, plačaj pa stricu poštarju ali teti poštarki. In ker očitno hočeš ves naš merch, spoiler alert, dobiš še presenečenje.</p>',
                     '<p>Medtem pa, ko čakaš na majico, ki bo krasila tvojo novo profilko na družbenih omrežjih, in rizle, ki bodo razvadi pridodale politično dimenzijo, za krajšanje časa priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                     '<p>Iskreno upajoč, da ti bo kupljeno v veselje, te lepo pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');





// paypal dvignem HTML
var paypalmajicadvignemHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, s katerim izkazuješ visoko mero cinične ozaveščenosti in upora proti dejanju, ki se mnogokrat kaže kot edino možno: spokat culo in vamos. Takoj, ko prejmemo tvoje plačilo preko Paypala, bo majica že na poti na izbrano prevzemno mesto. Ti javimo, ko prispe.</p>',
                        '<p>Če med čakanjem nanjo bereš <a href="http://agrument.danesjenovdan.si/">Agrumente</a>, garantirano prej pride.</p>',
                        '<p>Dobro jo nosi.</p>',
                        '<p>Iskreno upajoč, da ti majica paše dovolj dobro za novo profilko na družbenih omrežjih, te pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var paypalrizledvignemHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, ki te uvršča med urbane šamane, ruralne čudake ali v srednješolsko populacijo. Od preostalih pripadnic in pripadnikov omenjenih skupin pa te od trenutka, ko se oglasiš na izbranem prevzemnem mestu, prične ločiti vsaj to, da ne uporabljaš nekih brezveznih rizel. Javimo, ko prejmemo plačilo preko Paypala in bo vse pripravljeno zate.</p>',
                        '<p>Za nadaljnje točke razhajanj z ljudsko povprečnostjo med čakanjem na najbolj politično odgovoren užitkarski pribor priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                        '<p>Iskreno upajoč, da ti vsak dan uspe zadovoljno prikimati starodavni modrosti, ki jo najdeš v paketku, te lepo pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var paypalvsedvignemHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup. Vemo, da tvoj izbor obeh artiklov ni posledica tega, da se ne znaš odločiti, ampak prav nasprotno - dokaz, da se znaš. Čestitke za to. Robo bomo na izbrano prevzemno mesto odpravili takoj, ko prejmemo plačilo preko Paypala - ti javimo, ko bo tam. In ker očitno hočeš ves naš merch, spoiler alert, dobiš še presenečenje.</p>',
                     '<p>Medtem pa, ko čakaš na majico, ki bo krasila tvojo novo profilko na družbenih omrežjih, in rizle, ki bodo razvadi pridodale politično dimenzijo, za krajšanje časa priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                     '<p>Iskreno upajoč, da ti bo kupljeno v veselje, te lepo pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');


// poloznica po pošti HTML
var poloznicamajicadvignemHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup, s katerim izkazuješ visoko mero cinične ozaveščenosti in upora proti dejanju, ki se mnogokrat kaže kot edino možno: spokat culo in vamos. Takoj, ko plačaš račun, se tvoja majica odpravi na izbrano prevzemno mesto, kamor bo prispela najverjetneje že jutri. Ti javimo.</p>',
                     '<p>Če med čakanjem nanjo bereš <a href="http://agrument.danesjenovdan.si/">Agrumente</a>, garantirano prej pride.</p>',
                     '<p>Dobro jo nosi.</p>',
                     '<p>Iskreno upajoč, da ti majica paše dovolj dobro za novo profilko na družbenih omrežjih, te pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var poloznicarizledvignemHTML = ['<p>Zdravo,</p>',
                        '<p>hvala lepa za tvoj nakup, ki te uvršča med urbane šamane, ruralne čudake ali v srednješolsko populacijo. Od preostalih pripadnic in pripadnikov omenjenih skupin pa te od trenutka, ko plačaš pripet račun in mi tvoje naročilo odnesemo na izbrano prevzemno mesto, prične ločiti vsaj to, da ne uporabljaš nekih brezveznih rizel.</p>',
                        '<p>Za nadaljnje točke razhajanj z ljudsko povprečnostjo med čakanjem na najbolj politično odgovoren užitkarski pribor priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                        '<p>Iskreno upajoč, da ti vsak dan uspe zadovoljno prikimati starodavni modrosti, ki jo najdeš v paketku, te lepo pozdravljamo</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var poloznicavsedvignemHTML = ['<p>Zdravo,</p>',
                     '<p>hvala lepa za tvoj nakup. Vemo, da tvoj izbor obeh artiklov ni posledica tega, da se ne znaš odločiti, ampak prav nasprotno - dokaz, da se znaš. Čestitke za to. Čimprej plačaj priložen račun, da robo takoj odpremimo na izbrano prevzemno mesto. In ker očitno hočeš ves naš merch, spoiler alert, dobiš še presenečenje.</p>',
                     '<p>Medtem pa, ko čakaš na majico, ki bo krasila tvojo novo profilko na družbenih omrežjih, in rizle, ki bodo razvadi pridodale politično dimenzijo, za krajšanje časa priporočamo branje <a href="http://agrument.danesjenovdan.si/">Agrumenta</a>.</p>',
                     '<p>Iskreno upajoč, da ti bo kupljeno v veselje, te lepo pozdravljamo</p>',
                     '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

// donacija
var enkratnadonacijaHTML = ['<p>Ta-daaaa! H-V-A-L-A za donacijo! S prejetim denarjem bomo ravnali namensko, odgovorno in transparentno. Karkoli te v zvezi s porabo zanima, vprašaj, nemudoma ti bomo odgovorili. Pa tudi na druga vprašanja ;)</p>',
                           '<p>Ob tvoji odločitvi smo klobuke, kape in rute sneli</p>',
                           '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var rednadonacijaHTML = ['<p>Ta-daaaa! H-V-A-L-A za to odločitev. S prejetim denarjem bomo ravnali namensko, odgovorno in transparentno. Karkoli te v zvezi s porabo zanima, vprašaj, nemudoma ti bomo odgovorili. Pa tudi na druga vprašanja ;)</p>',
                           '<p>Ob tvoji odločitvi smo klobuke, kape in rute sneli</p>',
                        '<p>Eva, Filip, Jasmina, Karmen, Nika in Žiga.</p>'].join('');

var racunHTML = '<p>Račun najdeš <a href="http://djapi.danesjenovdan.si/nsa/racun?id={{ id }}">na tem linku</a>. Če ga ne moreš klikniti, odpri nov zavihek in v naslovno vrstico skopiraj: http://djapi.danesjenovdan.si/nsa/racun?id={{ id2 }}</p>';