$(document).ready(function() {
    const $commentText = $("#id_body");
    const $commentForm = $("#commentForm");
    const $submitButton = $("#submitButton");
    const deleteModal = new bootstrap.Modal($("#deleteModal")[0]);
    const $deleteConfirm = $("#deleteConfirm");

    $(".btn-edit").on("click", function(e) {
        let commentId = $(this).attr("comment_id");
        let commentContent = $(`#comment${commentId}`).text();
        $commentText.val(commentContent);
        $submitButton.text("Update");
        $commentForm.attr("action", `edit_comment/${commentId}`);
    });

    $(".btn-delete").on("click", function(e) {
        let commentId = $(this).attr("comment_id");
        $deleteConfirm.attr("href", `delete_comment/${commentId}`);
        deleteModal.show();
    });
});