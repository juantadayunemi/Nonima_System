    const API_URL = '/api/employee/';
    document.addEventListener('DOMContentLoaded', function () {
        const employeeSelect = document.getElementById('id_employee');
        const salaryInput = document.getElementById('id_salary');

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

            // Cargar salario inicial si ya hay un empleado seleccionado (en edición)
            const selectedEmployee = employeeSelect.value;
            if (selectedEmployee) {
                fetch(`${API_URL}${selectedEmployee}/`)
                    .then(response => response.json())
                    .then(data => {
                        salaryInput.value = data.salary;
                    });
            }
        }
    });