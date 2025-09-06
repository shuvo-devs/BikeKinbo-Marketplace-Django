// featured bikes owl carousel
$(document).ready(function () {
  $("#featuredBikes").owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    dots: false,
    autoplay: true,
    autoplayTimeout: 2000,
    responsive: {
      0: {
        items: 1,
      },
      767: {
        items: 2,
      },
      991: {
        items: 3,
      },
    },
  });
});
// stats counter
$(".counter").counterUp({
  delay: 10,
  time: 10000,
});
// teams section owl carousel
$(document).ready(function () {
  $("#teamSection").owlCarousel({
    loop: true,
    margin: 20,
    nav: false,
    dots: false,
    autoplay: true,
    autoplayTimeout: 2000,
    responsive: {
      0: {
        items: 1,
      },
      767: {
        items: 2,
      },
      991: {
        items: 4,
      },
    },
  });
});

// alert message timeout
setTimeout(function () {
  $("#message").fadeOut("show");
}, 4000);
