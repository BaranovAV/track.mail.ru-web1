$('document').ready(function() {
    console.log('ready');

    $('form').submit(function(){
        // сериализация всех полей формы
        var data = $(this).serialize();
        $.post(this.action, data, function(data) {
            alert(data);
        });
        return false;
    })

});