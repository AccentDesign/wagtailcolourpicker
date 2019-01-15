COLOURPICKER_CHOOSER_MODAL_ONLOAD_HANDLERS = {
    'chooser': function(modal, jsonData) {
        $('form.colour-form', modal.body).on('submit', function() {
            var formdata = new FormData(this);
            $.ajax({
                url: this.action,
                data: formdata,
                processData: false,
                contentType: false,
                type: 'POST',
                dataType: 'text',
                success: modal.loadResponseText
            });
            return false;
        });
    },
    'colour_chosen': function(modal, jsonData) {
        modal.respond('colourChosen', jsonData['toggled_feature'], jsonData['all_features']);
        modal.close();
    }
};
