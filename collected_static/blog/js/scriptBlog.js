$('document').ready(function() {

    console.log('ready');

    $('#like').click(function(e) {
        $.get('like/',
        {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        function(data) {
            var headBlogText = 'Всего блогов на сайте - ' + data.count;
            if (data.countFiltered) {
                headBlogText += '; отфильтровано - ' + data.countFiltered;
            }
            history.pushState(null,"s", document.location+"/?search="+searchStr+"&blogOnPage="+blogOnPage);
            $('#blogsBlock').children('pre').text(headBlogText);
           $('#blogItems').children().remove();
            data.items = JSON.parse(data.data);
            for(var i=0;i<data.items.length;i++) {
                $('#blogItems').append(
                    $('<div class="blog-item">'+
                        '<h3><a href="/blogs/'+data.items[i].pk+'/">Блог "'+data.items[i].fields.title+'"</a></h3>'+
                        '<pre>'+data.items[i].fields.text+'</pre>'+
                        '</div>')
                );
            }

        });
    });
});