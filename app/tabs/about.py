import gradio as gr


def render():
    with gr.Tab("À propos"):
        gr.Markdown(
            """
            # À propos d'Eco Maestro

            Eco Maestro est un outil intelligent qui rend l'IA générative plus responsable et efficace.
            Il sélectionne le modèle le plus adapté à chaque tâche tout en affichant la consommation énergétique et les émissions de CO2.

            ## Concept

            Eco Maestro permet de :
            - **Identifier la tâche** : OCR, analyse d'image, recherche web, génération de fichiers, etc.
            - **Choisir le modèle optimal** : Sélectionner celui qui consomme le moins tout en garantissant la qualité.
            - **Afficher l'impact** : Visualiser la consommation énergétique et les émissions de CO2 par requête.

            L'objectif est de répondre efficacement aux besoins des utilisateurs tout en limitant l'empreinte écologique.

            ### ℹ️ À propos de ces métriques
            - **Énergie** : Mesurée en Watt-heure (Wh). Une requête moyenne utilise 0,002 à 0,030 Wh
            - **CO2** : Mesuré en grammes. Basé sur l'intensité moyenne du réseau électrique mondial (~475 g CO2/kWh)
            - **Pour contexte** : La charge d'un smartphone typique utilise environ 5-10 Wh
            """
        )
