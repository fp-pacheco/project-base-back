from typing import List


def build_payload(
    user,
    employee=None,
    customer=None,
    employee_companies: List = None,
    customer_companies: List = None,
) -> dict:
    """
    Constrói o payload do token JWT para multi-empresa.

    Suporta contexto de employee OU customer, nunca ambos no
    mesmo token — cada rota de signin gera o token adequado.
    """
    companies = []
    roles = []

    if employee_companies:
        for ec in employee_companies:
            companies.append(str(ec.company_id))

            employee_roles = getattr(ec.employee, "employee_roles", [])

            if employee_roles:
                for er in employee_roles:
                    roles.append(
                        {
                            "company_id": str(ec.company_id),
                            "role_id": er.role.id,
                            "role_name": er.role.name,
                            "position": ec.position,
                            "status": ec.status,
                        }
                    )
            else:
                roles.append(
                    {
                        "company_id": str(ec.company_id),
                        "role_id": None,
                        "role_name": "employee",
                        "position": ec.position,
                        "status": ec.status,
                    }
                )

    if customer_companies:
        for cc in customer_companies:
            company_id = str(cc.company_id)
            if company_id not in companies:
                companies.append(company_id)

            roles.append(
                {
                    "company_id": company_id,
                    "role_id": None,
                    "role_name": "customer",
                    "position": None,
                    "status": True,
                }
            )

    return {
        "user_id": str(user.id),
        "employee_id": str(employee.id) if employee else None,
        "customer_id": str(customer.id) if customer else None,
        "user": {
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
        },
        "companies": companies,
        "roles": roles,
    }
