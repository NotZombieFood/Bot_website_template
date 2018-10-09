function formFail(){
    iziToast.error({
        id: 'error',
        title: 'Error',
        message: 'Por favor rellena todos los campos.',
        position: 'topRight',
        transitionIn: 'fadeInDown',
        icon: 'fas fa-exclamation-triangle'
    });
}