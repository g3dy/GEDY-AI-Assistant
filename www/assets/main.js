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
});