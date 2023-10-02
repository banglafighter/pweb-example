jQuery(document).ready(function () {
    jQuery('.delete-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to delete?'
    });

    jQuery('.cancel-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to cancel?'
    });
});