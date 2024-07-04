const openMenu= document.querySelector('.menu')
const menu= document.querySelector('.right')
const closeMenu= document.querySelector('.close')

openMenu.addEventListener('click', () =>{
    menu.classList.add('active')
})
closeMenu.addEventListener('click', () =>{
    menu.classList.remove('active')
})

const labels = document.querySelectorAll('.form-control label')

labels.forEach(label =>{
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx)=> `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})



