const header = document.querySelector('header')
const modalPhone = document.querySelector('.modal')
const modalForm = document.querySelector('.modal-form')
const boxContainer = document.querySelector('.box-container')
const navbar = document.querySelector('.navbar')


const handlerHeader = (e) => {
    if (e.target.id === 'phone-number') {
            console.log(e.target.id)
            modalPhone.classList.toggle('active')
    }
    if (e.target.id === 'menu-bars') {
        navbar.classList.toggle('active')

    }

}

const handlerModalPhone = (e) => {
    if (e.target.id === 'close-modal') {
        modalPhone.classList.toggle('active')
    }
}

const handlerBoxContainer = (e) => {
    if (e.target.id === 'btn-booking') {
        modalForm.style.display = 'flex'
    }
}

if (modalForm) {

    const handlerModalForm = (e) => {
        if (modalForm) {
            if (e.target.id === 'close-form') {
                modalForm.style.display = 'flex'
            }
            if (e.target.id === 'close-form') {
                modalForm.style.display = 'none'
            }
        }
    }
    modalForm.addEventListener('click', handlerModalForm)
}

header.addEventListener('click', handlerHeader)
modalPhone.addEventListener('click', handlerModalPhone)
boxContainer.addEventListener('click', handlerBoxContainer)



var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

var swiper = new Swiper(".review-slider", {
  spaceBetween: 20,
  centeredSlides: true,
  autoplay: {
    delay: 7500,
    disableOnInteraction: false,
  },
  loop:true,
  breakpoints: {
    0: {
        slidesPerView: 2,
    },
    640: {
      slidesPerView: 3,
    },
    768: {
      slidesPerView: 4,
    },
    1024: {
      slidesPerView: 5,
    },
  },
});