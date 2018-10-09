window.onload = function() {
    function validateForm(){
        var inputs = document.getElementsByTagName("input"), input = null, flag = true;
        for(var i = 0, len = inputs.length; i < len; i++) {
            input = inputs[i];
            if(!input.value) {
                iziToast.show({
                    title: 'Hey',
                    message: 'Welcome!'
                });
                flag = false;
                input.focus();
                alert("Please fill all the inputs");
                break;
            }
        }
        return(flag);
    }
    
document.querySelector("#form").addEventListener("submit", function(e){
    if(!validateForm){
        e.preventDefault();   
    }
});
}