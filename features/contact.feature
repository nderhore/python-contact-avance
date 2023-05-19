
Feature: Contact
  # Enter feature description here
Narrative:

  Dans le but d'un live studi
  Je souhaite créer , modifier et supprimer un contact

  Scenario: Création dun contact
    Given Je crée un contact avec les informations suivantes
    """
    {
      "nom":"Ose",
      "prenom":"Jose",
      "telephone":"0789453569",
      "mail":"toto@toto.fr"
    }
    """
    Then Je verifie qu'il a été crée, et le retour doit être
    """
    Jose
    """
