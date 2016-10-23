$('document').ready( function() {
        $('#logout').click(function(e) {
        $.post('/logout/',
            {'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
            function() {
                document.location="/";
            }
        );
    });
});