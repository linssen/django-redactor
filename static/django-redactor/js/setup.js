django.jQuery(document).ready(function() {
    var settings = {
        imageUpload: '/redactor/upload/',
        imageUploadErrorCallback: callback
    }
    django.jQuery(".redactor").redactor(settings);

    function callback(obj, json)
    {
        alert(json.error);
        alert(json.anothermessage);	
    }
});
