function fillGameModal(strObj){
    document.getElementById('game_id').value = strObj.dataset.id;
    document.getElementById('name').value = strObj.dataset.name;
    document.getElementById('description').value = strObj.dataset.description;
}

function clearGameModal(){
    document.getElementById('game_id').value = null;
    document.getElementById('name').value = null;
    document.getElementById('description').value = null;
}

function fillResultModal(strObj){
    document.getElementById('result_id').value = strObj.dataset.id;
    document.getElementById('result').value = strObj.dataset.result;
    document.getElementById('game').value = strObj.dataset.game;
}

function clearResultModal(){
    document.getElementById('result_id').value = null;
    document.getElementById('result').value = null;
    document.getElementById('game').value = null;
}

function fillRoleModal(strObj){
    document.getElementById('role_id').value = strObj.dataset.id;
    document.getElementById('role').value = strObj.dataset.role;
    document.getElementById('description').value = strObj.dataset.description;
    document.getElementById('side').value = strObj.dataset.side;
    document.getElementById('game').value = strObj.dataset.game;
}

function clearRoleModal(){
    document.getElementById('role_id').value = null;
    document.getElementById('role').value = null;
    document.getElementById('description').value = null;
    document.getElementById('side').value = null;
    document.getElementById('game').value = null;
}

function fillLocationModal(strObj){
    document.getElementById('loc_id').value = strObj.dataset.id;
    document.getElementById('name').value = strObj.dataset.name;
    document.getElementById('address').value = strObj.dataset.address;
    document.getElementById('direction').textContent = strObj.dataset.directions;
    document.getElementById('point').value = strObj.dataset.point;
    if(document.getElementById('loc_id') != null){
        document.getElementById('photo_form').hidden = true;
        document.getElementById('scheme_form').hidden = true;
        document.getElementById('locModalLabel').textContent = 'Редактировать локацию'

    }
//    document.getElementById('photo').textContent = "фото " + strObj.dataset.photo;
//    document.getElementById('scheme').textContent = "схема " + strObj.dataset.scheme;
}

function cleaLocationModal(){
    document.getElementById('loc_id').value = null;
    document.getElementById('name').value = null;
    document.getElementById('address').value = null;
    document.getElementById('direction').textContent = null;
    document.getElementById('point').value = null;
    document.getElementById('photo_form').hidden = false;
    document.getElementById('scheme_form').hidden = false;
    document.getElementById('locModalLabel').textContent = 'Добавить локацию'

//    document.getElementById('photo').value = null;
//    document.getElementById('scheme').value = null;
}

function fillPromoModal(thisObj){
    document.getElementById('promo_id').value = thisObj.dataset.id;
    document.getElementById('date').value = thisObj.dataset.date;
    document.getElementById('par1').value = thisObj.dataset.par1;
    document.getElementById('text1').textContent = thisObj.dataset.text1;
    document.getElementById('par2').value = thisObj.dataset.par2;
    document.getElementById('text2').textContent = thisObj.dataset.text2;
    document.getElementById('par3').value = thisObj.dataset.par3;
    document.getElementById('text3').textContent = thisObj.dataset.text3;
    document.getElementById('par4').value = thisObj.dataset.par4;
    document.getElementById('text4').textContent = thisObj.dataset.text4;
}

function clearPromoModal(){
    document.getElementById('promo_id').value = null;
    document.getElementById('date').value = null;
    document.getElementById('par1').value = null;
    document.getElementById('text1').textContent = null;
    document.getElementById('par2').value = null;
    document.getElementById('text2').textContent = null;
    document.getElementById('par3').value = null;
    document.getElementById('text3').textContent = null;
    document.getElementById('par4').value = null;
    document.getElementById('text4').textContent = null;
}

function fillSchModal(obj){
    unBlock('save');
    document.getElementById('sch_id').value = obj.dataset.id;
    document.getElementById('date').value = obj.dataset.date;
    document.getElementById('time_begin').value = obj.dataset.begin;
    document.getElementById('time_end').value = obj.dataset.end;
    document.getElementById('location').value = obj.dataset.location;
    document.getElementById('game').value = obj.dataset.game;

}

function clearSchModal() {
    document.getElementById('sch_id').value = null;
    document.getElementById('date').value = null;
    document.getElementById('time_begin').value = null;
    document.getElementById('time_end').value = null;
    document.getElementById('location').value = null;
    document.getElementById('game').value = null;
}

function butBlock(obj){
    obj.disabled = true;
}

function unBlock(id){
    document.getElementById(id).disabled = false;
}