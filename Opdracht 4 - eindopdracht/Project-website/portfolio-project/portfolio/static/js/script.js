const nav = document.querySelector("nav");

window.onscroll = () => {
  if (
    // document.body.scrollTop > window.innerHeight
    // ||
    document.documentElement.scrollTop > window.innerHeight
  ) {
    nav.style.top = "0";
  } else {
    nav.style.top = "-50px";
  }
};
