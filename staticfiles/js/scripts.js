function closeAlerts() {
    const alerts = document.getElementsByClassName('alert');
    if (alerts.length > 0) {
        Array.from(alerts).forEach(alertInstance => {
            setTimeout(() => {
                alertInstance.style.opacity = 0;
                setTimeout(() => {
                    alertInstance.style.display = 'none';
                }, 1000);
            }, 5000);
        });
    }
}
