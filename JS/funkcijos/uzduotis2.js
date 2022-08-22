function validAge(customerAge) {
    let leagalAge = 18;
    if (leagalAge <= customerAge) {
        return alert("Gerti energetini galima!")
    } else {
        return window.confirm("Ar gavai tėvų leidimą?")
    }
}