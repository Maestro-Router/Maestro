from sentence_transformers import SentenceTransformer
import numpy as np


class Maestro:
    def __init__(self, embedding_model="all-MiniLM-L6-v2", threshold=0.40):
        """
        embedding_model: name of the embedding model (E5 recommended)
        threshold: minimum cosine similarity to route to a specific model
        """

        self.task_descriptions = {
            "summarizer": "Résumé automatique de textes courts, ton concis et neutre.",
            # "translator": "Traduction français ↔ anglais, fidélité au sens.",
            # "math_explainer": "Explication claire de concepts mathématiques simples.",
            # "python_coder": "Génération de code Python clair, commenté.",
            "web_searcher": "Recherche d'informations en ligne et fourniture de liens pertinents."
        }

        self.encoder = SentenceTransformer(embedding_model)
        self.threshold = threshold

        # desc_texts = [model_descriptions[name] for name in self.model_names]
        # self.model_vectors = self.encoder.encode(desc_texts, normalize_embeddings=True)

        print("Maestro initialized with tasks:", self.task_descriptions.keys())

    # def _web_search(self, query):
    #     d = [
    #             {
    #                 "url": "https://example.com/1",
    #             },
    #             {
    #                 "url": "https://example.com/2",
    #             }
    #         ]
    #     return d

    # def route(self, query) -> str:
    #     query_vec = self.encoder.encode([query], normalize_embeddings=True)
    #     scores = (query_vec @ self.model_vectors.T)[0]
    #     best_idx = np.argmax(scores) # renvoie l’indice du modèle dont la description est la plus proche de la requête.
    #     best_score = scores[best_idx] # renvoie le score correspondant à cet indice
    #     best_model = self.model_names[best_idx] # renvoie le nom du modèle correspondant à cet indice

    #     print("\n--- Routing Debug ---")
    #     print(f"User query: {query!r}") # Le !r force l’affichage repr(), donc les guillemets et caractères spéciaux sont visibles
    #     for name, score in zip(self.model_names, scores):
    #         print(f" {name:20s} : {score:.3f}")
    #     print("---------------------")

    #     # Threshold logic - si aucun modèle n'obtient un score de similarité cosine supérieur à treshold, il répond par ce texte :
    #     if best_score < self.threshold:
    #         print(f"Pas de modèle suffisamment pertinent - au-dessus du seuil de ({self.threshold}). Using fallback.")
    #         return None

    #     print(f"→ Routed to: {best_model} (score {best_score:.3f})")
    #     return best_model

    def handle_request(self, query, fallback_fn=None):
        return "Coucou le Hamster !"
        # """
        # Route the query and execute the corresponding model function.
        # fallback_fn: function to call if no model matches threshold
        # """
        # model_name = self.route(query)
        # if model_name is None:
        #     if fallback_fn:
        #         return fallback_fn(query)
        #     else:
        #         return "[No suitable model found]"
        # else:
        #     fn = self.model_functions[model_name]
        #     return fn(query)


#######################################################################

#                   utilisation du nom du meilleur modèle
#                   pour lui envoyer le prompt utilisateur

#######################################################################

# # Exemple de requêtes
# queries = [
#     "Peux-tu m'expliquer comment fonctionne une dérivée ?",
#     "Résume-moi ce paragraphe en 5 phrases.",
#     "Traduis ce texte en anglais.",
#     "Écris un script Python pour scraper un site.",
#     "Comment réparer une fuite d'eau ?"
# ]