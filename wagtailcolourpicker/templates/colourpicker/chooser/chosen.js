function(modal) {
    modal.respond('colourAdded', '{{ colour.feature_name_upper }}', '{{ colour }}', {{ created|yesno:"true,false" }});
    modal.respond('colourChosen', '{{ colour.feature_name_upper }}', ['{{colours|join:"','"}}']);
    modal.close();
}