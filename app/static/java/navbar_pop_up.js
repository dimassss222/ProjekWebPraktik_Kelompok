var user = document.getElementById('user');
var user_pop_up = document.getElementById('user_pop_up')
user.style.cursor = 'pointer';
user_pop_up.style.display = 'none'

user.onclick = function () {
    switch (user_pop_up.style.display){
        case 'none':
            user_pop_up.style.display = 'block'
            break
        case 'block':
            user_pop_up.style.display = 'none'
            break
    }
}