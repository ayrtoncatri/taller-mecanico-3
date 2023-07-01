//Función 1
function enviarDatos(){
    var form = document.getElementById('form');
    form.addEventListener('submit', function(event){
        event.preventDefault();
    })
    console.log('Procesando información...');
    
    var nombre = document.getElementById('nombre');
    var appaterno = document.getElementById('appaterno');
    var apmaterno = document.getElementById('apmaterno');
    var rut = document.getElementById('rut');
    var direccion = document.getElementById('direccion');
    var correo = document.getElementById('correo');
    var telefono = document.getElementById('telefono');

    var soloLetras = /^[a-zA-Z\s]+$/;
    var formatoRut = /^[0-9]{1,2}\.?[0-9]{3}\.?[0-9]{3}-?[0-9kK]{1}$/;
    var formatoTelefono = /^[0-9]+$/;
    var formatoCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    var datosUsuario = [];
    var errorMessage = document.getElementById('errorDiv');
    errorMessage.textContent = '';

    //Validar nombre

    if(nombre.value === ''){ 
        errorMessage.textContent = 'Favor ingrese un valor en el campo de nombre';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!soloLetras.test(nombre.value)){
        errorMessage.textContent = 'El campo de nombre debe contener sólo letras';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(nombre.value);
    }

    //Validar apellido paterno
    if(appaterno.value === ''){
        errorMessage.textContent = 'Favor ingrese un valor en el campo de apellido paterno';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!soloLetras.test(appaterno.value)){
        errorMessage.textContent = 'El campo de apellido paterno debe contener sólo letras';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(appaterno.value);
    }
    //Validar apellido materno
    if(apmaterno.value === ''){
        errorMessage.textContent = 'Favor ingrese un valor en el campo de apellido materno';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!soloLetras.test(apmaterno.value)){
        errorMessage.textContent = 'El campo de apellido materno debe contener sólo letras';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(apmaterno.value);
    }

    //Validar RUT
    if(rut.value === ''){
        errorMessage.textContent = 'Favor ingrese un valor en el campo de RUT';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!formatoRut.test(rut.value)){
        errorMessage.textContent = 'Debe ingresar un RUT válido';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(rut.value);
    }

    //Validar dirección
    if(direccion.value === ''){
        errorMessage.textContent = 'Favor ingrese un valor en el campo de dirección';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!soloLetras.test(direccion.value)){
        errorMessage.textContent = 'El campo de dirección debe contener letras';
        document.querySelector('.containerError').style.display = 'block';
        return;

    }
    else{
        datosUsuario.push(direccion.value);
    }
    //Validar correo electrónico

    if(correo.value === ''){
        errorMessage.textContent = 'Favor ingrese un valor en el campo de correo electrónico';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!formatoCorreo.test(correo.value)){
        errorMessage.textContent = 'Debe ingresar un correo electrónico válido';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(correo.value);
    }

    //Validar teléfono
    if(telefono.value === ''){
        errorMessage.textContent = 'Favor debe ingresar un valor en el campo de teléfono';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else if(!formatoTelefono.test(telefono.value)){
        errorMessage.textContent = 'Ingrese un número de teléfono válido';
        document.querySelector('.containerError').style.display = 'block';
        return;
    }
    else{
        datosUsuario.push(telefono.value);
    }

    var forma = document.getElementById('form').reset();

    console.log(datosUsuario);
    console.log('Formulario enviado');
    alert('Formulario enviado con éxito');
}

