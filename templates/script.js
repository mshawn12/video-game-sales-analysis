const button = document.querySelector('.button');

const mouseHoverAnimation = () => {
    anime({
        targets: button,
        width: '100%',
        scale: {
            delay: 800,
            value: 1.5
        },
        duration: 1500
    })
}

const mouseOutAnimation = () => {
    anime({
        targets: button,
        width: '50%',
        scale: {
            delay: 800,
            value: 1
        },
        duration: 1500
    })
}

anime({
    targets: '.youtube path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 1500,
    direction: 'alternate',
    loop: true
})


button.addEventListener('mouseover', mouseHoverAnimation)
button.addEventListener('mouseout', mouseOutAnimation)
