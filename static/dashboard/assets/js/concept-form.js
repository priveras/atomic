$(function () {

        $(".errorlist").css({'list-style-type': 'none', 'color': 'red', 'padding': 0});
        $(".errorlist").parent().addClass("has-danger text-danger");

        $("#id_name").keypress(function () {
            $(".errorlist").attr("style", "display:none");
            $('label[for="id_name"]').removeClass('form-control-label');

        });

        var errorMsg = "This field is required";
        var required = "required";

        $("form[name='company-register']").validate({
            rules: {
                name: required,
                goa: required,
                group: required,
                stage: required,
                status: required
            },
            messages: {
                name: errorMsg,
                goa: errorMsg,
                group: errorMsg,
                stage: errorMsg,
                status: errorMsg
            },

            errorClass: 'form-control-danger text-danger',
            validClass: 'form-control-line',
            errorElement: 'span',
            divErrorClass: 'has-danger',

            highlight: function(element, errorClass, validClass) {
              $(element).parents("div.form-group").addClass('has-danger');
            },

            unhighlight: function(element, errorClass, validClass) {
                $(element).parents("div.form-group").removeClass('has-danger');
            },

            submitHandler: function (form) {
                form.submit();
            }
        });
});
