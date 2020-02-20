document.addEventListener('DOMContentLoaded',()=>{
    console.log("opoooop")
    anime.timeline({
        easing:'easeOutExpo',
        
}
    )
    .add({
        targets:'#nav',
        width:['0px','100%'],
        easing:'linear'
        // delay:500
    })
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
        targets:'#quin',
        translateY:['-100','0'],
        opacity:['0','1']
    })
    .add({
        targets:'#container',
        translateY:['0','-800'],
        offset:'+=1000',
    })
    .add({
        targets:'.container1',
        width:['0%','75%'],
        // display:'block'
    })
    .add({
        targets:'#container',
        translateY:['-800','0'],
        offset:'+=1000',
        delay:1000
    })
    .add({
        targets:'.container1',
        width:['75%','-0px']
    })

let waypoint = new waypoint({
    element: document.querySelector('#home'),
    handler: function(){
        anime.timeline({
         targets:'#home',
         translateY:['-100','0'],
         easing:'easyOutExpo'
        })
    },
    content:document.querySelector('.home'),
})})