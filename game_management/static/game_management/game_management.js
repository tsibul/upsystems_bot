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
    document.getElementById('direction').value = strObj.dataset.directions;
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
    document.getElementById('direction').value = null;
    document.getElementById('point').value = null;
    document.getElementById('photo_form').hidden = false;
    document.getElementById('scheme_form').hidden = false;
    document.getElementById('locModalLabel').textContent = 'Добавить локацию'

//    document.getElementById('photo').value = null;
//    document.getElementById('scheme').value = null;
}

function locIdCheck(){
    var result = 'True'
    if(document.getElementById('loc_id').value == null){
        result = 'False'
    }
    return result
}