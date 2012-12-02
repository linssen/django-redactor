django.jQuery(document).ready(function() {
    var settings = {
        imageUpload: '/redactor/upload/',
        imageUploadErrorCallback: callback,
        imageGetJson: '/redactor/images/'
    }
    django.jQuery(".redactor").redactor(settings);

    function callback(obj, json)
    {
        alert(json.error);
        alert(json.anothermessage);	
    }
});
