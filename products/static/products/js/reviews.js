$(document).ready(function() {
    /* all ingredients toggle */
    var ingredientsToggle = $('[data-toggle="collapse"]');
    var chevronIcon = ingredientsToggle.find('i.fas');

    ingredientsToggle.on('click', function() {
      chevronIcon.toggleClass('fa-chevron-up fa-chevron-down');
    });

    $('#ingredientsCollapse').on('hidden.bs.collapse', function () {
      chevronIcon.removeClass('fa-chevron-up').addClass('fa-chevron-down');
    });

    $('#ingredientsCollapse').on('shown.bs.collapse', function () {
      chevronIcon.removeClass('fa-chevron-down').addClass('fa-chevron-up');
    });
 
    // Edit/delete reviews buttons
    const $reviewForm = $("#reviewForm");
    const $submitButton = $reviewForm.find("button[type='submit']");
    const deleteModal = new bootstrap.Modal($("#deleteModal")[0]);
    const $deleteConfirm = $("#deleteConfirm");

    $(".btn-edit").on("click", function(e) {
      let reviewId = $(this).attr("comment_id");
      let reviewContent = $(`#comment${reviewId}`).text().trim();
      $reviewForm.find('textarea').first().val(reviewContent);
      $submitButton.text("Update");
      
      // Get the current product_id from the URL
      let productId = window.location.pathname.split('/')[2];
      $reviewForm.attr("action", `${productId}/edit_review/${reviewId}`);
  });

    $(".btn-delete").on("click", function(e) {
      let reviewId = $(this).attr("comment_id");
      let productId = window.location.pathname.split('/')[2]; // Get product_id from URL
      $deleteConfirm.attr("href", `${productId}/delete_review/${reviewId}`);
      deleteModal.show();
  });
});