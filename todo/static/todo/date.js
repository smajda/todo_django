//https://github.com/dbushell/Pikaday
var picker = new Pikaday({
    field: document.getElementById('add_date'),
    format: 'M/D/YYYY',
    toString(date, format) {
        const day = date.getDate();
        const month = date.getMonth() + 1;
        const year = date.getFullYear();
        return `${month}/${day}/${year}`;
    },
});

var picker = new Pikaday({
    field: document.getElementById('due_date'),
    format: 'M/D/YYYY',
    toString(date, format) {
        const day = date.getDate();
        const month = date.getMonth() + 1;
        const year = date.getFullYear();
        return `${month}/${day}/${year}`;
    },
});
