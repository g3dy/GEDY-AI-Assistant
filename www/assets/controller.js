$(document),ready(function() {
    // Display spoken message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    }

    // Displaying whats u
    eel.expose(ShowHood)
    function ShowHood() {
        $("#oval").attr("hidden", false)
        $("#siri-wave").attr("hidden", true)
    }
});