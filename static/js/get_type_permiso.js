document.addEventListener('DOMContentLoaded', function () {
    const permisoSelect = document.getElementById('id_tipo_permiso');
    const diasField = document.getElementById('dias-field');
    const horasField = document.getElementById('horas-field');
    const diasInput = document.getElementById('id_dias');
    const horasInput = document.getElementById('id_horas');

    if (permisoSelect) {
        permisoSelect.addEventListener('change', function () {
            const permisoId = this.value;

            if (permisoId) {
                fetch(`/api/tipo_permiso/${permisoId}/`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`Error HTTP: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                     
                        if (data.frecuencia_dias) {
                            diasField.style.display = 'block';
                            horasField.style.display = 'none';
                            horasInput.value = '';
                        } else {
                            diasField.style.display = 'none';
                            horasField.style.display = 'block';
                            diasInput.value = '';
                        }

                    })
                    .catch(error => {
                        console.error('Error:', error);
                        // Mostrar ambos campos por defecto si hay error
                        diasField.style.display = 'none';
                        horasField.style.display = 'none';
                    });
            } else {
                // Si no hay permiso seleccionado, ocultar ambos
                diasField.style.display = 'none';
                horasField.style.display = 'none';
            }
        });

        // Disparar el evento change al cargar la página si ya hay un valor seleccionado
        if (permisoSelect.value) {
            permisoSelect.dispatchEvent(new Event('change'));
        }
    }
});