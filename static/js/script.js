const element = element => document.querySelector(element)
const verify = (name, email, tel, message) => name && email && tel && message ? true : false

// arrow function de validação de email a partir de uma definição em regex retornano true ou false
const validateEmail = email => {
    let regex = /\S+@\S+\.\S+/
    return regex.test(email)
}

const fieldName = element('#name')
const fieldEmail = element('#email')
const fieldFone = element('#tel')
const areaMessage = element('#message')
const btn = element("section#contacts form button")

let name = false
let email = false
let tel = false
let message = false

fieldName.addEventListener('keyup', () => {
    fieldName.value.length < 1 ? name = false : name = true

    if(verify(name, email, tel, message)){
        btn.removeAttribute('disabled')
        btn.classList.remove('btn-disable')
        btn.classList.add('btn-enable')
    }
    else{
        btn.setAttribute('disabled', '')
        btn.classList.remove('btn-enable')
        btn.classList.add('btn-disable')
    }
})

fieldEmail.addEventListener('keyup', () => {
    validateEmail(fieldEmail.value) ? email = true : email = false

    if(verify(name, email, tel, message)){
        btn.removeAttribute('disabled')
        btn.classList.remove('btn-disable')
        btn.classList.add('btn-enable')
    }
    else{
        btn.setAttribute('disabled', '')
        btn.classList.remove('btn-enable')
        btn.classList.add('btn-disable')
    }
})

fieldFone.addEventListener('keyup', () => {
    fieldFone.value.length < 1 ? tel = false : tel = true
    
    if(verify(name, email, tel, message)){
        btn.removeAttribute('disabled')
        btn.classList.remove('btn-disable')
        btn.classList.add('btn-enable')
    }
    else{
        btn.setAttribute('disabled', '')
        btn.classList.remove('btn-enable')
        btn.classList.add('btn-disable')
    }
})

areaMessage.addEventListener('keyup', () => {
    areaMessage.value.length < 1 ? message = false : message = true
    
    if(verify(name, email, tel, message)){
        btn.removeAttribute('disabled')
        btn.classList.remove('btn-disable')
        btn.classList.add('btn-enable')
    }
    else{
        btn.setAttribute('disabled', '')
        btn.classList.remove('btn-enable')
        btn.classList.add('btn-disable')
    }
})

element('footer p span.year').innerHTML = new Date().getFullYear()