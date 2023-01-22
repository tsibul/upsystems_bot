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