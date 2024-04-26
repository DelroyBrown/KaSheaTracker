function downloadDocument(docName) {
    alert('Download ' + docName);
}

function deleteDocument(docName) {
    confirm('Are you sure you want to delete ' + docName + '?') && alert(docName + ' deleted');
}
