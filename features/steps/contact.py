from pytest_bdd import scenario, given, when, then


@given("Je crée un contact avec les informations suivantes")
def step_impl(context, contact):
    raise NotImplementedError(u"""STEP: Given Je crée un contact avec les informations suivantes
                              {
                                "nom":"Ose",
                                "prenom":"Jose",
                                "telephone":"0789453569",
                                "mail":"toto@toto.fr"
                              }
                              """)
