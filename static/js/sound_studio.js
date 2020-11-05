const backToTop = document.querySelector('.back-to-top');
backToTop.addEventListener('click',goToTop);

function goToTop(){
  window.scrollTo(0,0);
  console.log('moved to top');
}
