$(document).ready(function () {
    // Guard: if the textillate CDN ever fails to load, don't throw — just
    // leave the plain text visible instead of breaking the whole page.
    if (typeof $.fn.textillate !== 'function') {
        console.warn('textillate.js did not load — skipping text animation.');
        return;
    }

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        },
    });

    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style: 'ios9',
    amplitude: "1",
    speed: "0.3",
    autostart: true,
  });

  $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true
        },
        out: {
            effect: 'fadeOutUp',
            sync: true,
        },
    });

    $('#micBtn').click(function() {
        $('#oval').attr("hidden", true);
        $('#SiriWave').attr("hidden", false);
        eel.micClickSound();
    })

});