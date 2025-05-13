function setupModalForm(triggerId, fetchUrl) {
    const modalEl = document.getElementById('modalGeneral');
    const modal = new bootstrap.Modal(modalEl);
    const modalContent = document.getElementById('modalGeneralContent');

    document.getElementById(triggerId).addEventListener('click', function (e) {
        e.preventDefault();

        fetch(fetchUrl)
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.text(); // Changed from json() to text()
            })
            .then(html => {
                modalContent.innerHTML = html;
                modal.show();

                const form = document.getElementById('formCreateDoctor');
                if (form) {
                    form.addEventListener('submit', function (e) {
                        e.preventDefault();
                        const formData = new FormData(this);
                        
                        fetch(fetchUrl, {
                            method: 'POST',
                            headers: {
                                'X-Requested-With': 'XMLHttpRequest',
                            },
                            body: formData
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.success) {
                                modal.hide();
                                location.reload();
                            } else {
                                // Handle errors if needed
                                console.error(data.errors);
                            }
                        })
                        .catch(error => console.error('Error:', error));
                    });
                }
            })
            .catch(error => console.error('Error loading modal:', error));
    });
}

// En tu show_modal.js o archivo similar
function setupUpdateModal(triggerClass) {
    document.querySelectorAll(triggerClass).forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const doctorId = this.getAttribute('data-id');
            console.log('doctor id '+doctorId);      
            // Construye la URL usando la URL de Django
            const url = `/clinic/doctor_update/${doctorId}/`;
            
            fetch(url, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'text/html'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(html => {
                document.getElementById('modalGeneralContent').innerHTML = html;
                const modal = new bootstrap.Modal(document.getElementById('modalGeneral'));
                modal.show();
                
                // Resto de tu código para manejar el formulario...
            })
            .catch(error => {
                console.error('Loading error:', error);
                alert(`Error al cargar el formulario: ${error.message}`);
            });
        });
    });
}


// En tu archivo JavaScript
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    
    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            window.location.href = data.redirect;
        } else {
            // Mostrar error en el modal
            alert(data.error); // O puedes crear un div para errores
        }
    });
});

