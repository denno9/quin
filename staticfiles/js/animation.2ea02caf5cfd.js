document.addEventListener('DOMContentLoaded',function(){
    console.log("opoooop");
    anime.timeline({
        easing:'easeOutExpo',
        
}
    )
    
    .add({
        targets:'.maincontent1',
        width:['0px','100%']
    })
    .add({
        targets:'#welcome',
        translateY:['-100','0'],
        opacity:['0','1']
    })
    .add({
        targets:'#neno',
        translateX:['-100','0'],
        offset:'+=3000',
        opacity:['0','1']
    })
    .add({
        targets:'#qlogo',
        rotateY:['0','360'],
        offset:'+=500',
        opacity:['0','1'],
        easing:'easeInOutSine'
    })
    .add({
        targets:'#more',
        translateY:['-100','0'],
        opacity:['0','1']
    })
    .add({
        targets:'#quin',
        translateY:['-100','0'],
        easing: 'linear',
        opacity:['0','1']
    }).add([{
        targets:'#container',
        translateY:['0','0']
    }]);

   

});


// .add({
//     targets:'#nav',
//     width:['0px','100%'],
//     easing:'linear'
    
// })