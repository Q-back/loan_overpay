def _calculate_single_installment(
    lease_percentage, loan_capital_left, initial_installment_value
) -> int:
    interest_required = (loan_capital_left * (lease_percentage / 100)) / 12
    return initial_installment_value + interest_required


def calculate_loan_installment(
    loan_value_pln: int, lease_percentage: float, number_of_installments: int, overpay_pln: int = 0,
) -> float:
    loan_value_gr = loan_value_pln * 100
    loan_capital_left_gr = loan_value_gr - (overpay_pln * 100)
    already_payed_gr = 0
    initial_installment_value = int(loan_value_gr / number_of_installments)

    for interation in range(number_of_installments):
        already_payed_gr += _calculate_single_installment(
            lease_percentage, loan_capital_left_gr, initial_installment_value
        )
        loan_capital_left_gr -= initial_installment_value
        if loan_capital_left_gr <= 0:
            already_payed_gr += loan_capital_left_gr
            break

    total_payed_pln = (already_payed_gr / 100) + overpay_pln

    value_of_single_installment_gr = int(already_payed_gr / number_of_installments)
    print(
        f"kredyt: {loan_value_pln}, oprocentowanie: {lease_percentage}%, nadpłata: {overpay_pln} rata: "
        f"{value_of_single_installment_gr/100}, zapłacone w sumie: {total_payed_pln}"
    )
    return int(value_of_single_installment_gr / 100)


# Use it like this:
calculate_loan_installment(97366, 4.75, 254, overpay_pln=97366)
calculate_loan_installment(97366, 4.75, 254)
calculate_loan_installment(97366, 4.75, 254, overpay_pln=40000)

