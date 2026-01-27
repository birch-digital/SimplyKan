class addSprintDialog
{
    constructor()
    {
        this.dialog = document.getElementById('_add_dialog');
        this.openBtn = document.getElementById('_add_sprint');
        this.closeBtn = document.getElementById('_dialog_close');
        this.openBtnBig = document.getElementById('_add_sprint_big');

        if (this.openBtnBig !== null) {this.openBtnBig.addEventListener('click', this.#open);}
        this.openBtn.addEventListener('click', this.#open);
        this.closeBtn.addEventListener('click', this.#close);

    }

    #open = e => {
        this.dialog.showModal();
    }

    #close = e => {
        this.dialog.close();
    }
}

new addSprintDialog();