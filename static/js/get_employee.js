    const API_URL = '/api/employee/';
    const API_URL_PERMISO = '/api/permiso/';
    document.addEventListener('DOMContentLoaded', function () {
        const employeeSelect = document.getElementById('id_employee');
        const salaryInput = document.getElementById('id_salary');

        const permisoSelect = document.getElementById('id_permiso');
        const frecuanciaInput = document.getElementById('id_frecuencia_dias');

        if (employeeSelect && salaryInput) {
            employeeSelect.addEventListener('change', function () {
                const employeeId = this.value;

                if (employeeId) {
                    // Realiza la solicitud Fetch con la URL dinámica
                    fetch(`${API_URL}${employeeId}/`)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error(`Error HTTP: ${response.status}`);
                            }
                            return response.json();
                        })
                        .then(data => {
                            salaryInput.value = data.salary;
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                } else {
                    salaryInput.value = '';
                }
            });

        }



    });