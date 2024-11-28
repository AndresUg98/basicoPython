//Contando ovejas

const sheeps = [undefined,null,false,true,true,false,null,undefined]

function countSheeps(arrayOfSheeps) {
    return arrayOfSheeps.filter(Boolean).length;
  }

countSheeps(sheeps)


function lovefunc(flower1, flower2){
  
  if (flower1 % 2 == 0){
    if (flower2 % 2 != 0){
      return true;
    }else{
      return false
    }

  }else if (flower1 % 2 != 0){
    if (flower2 % 2 == 0){
      return true;
    }else{
      return false
    }

  }else{
    return false;
    
  }
}
lovefunc(0,0)




