# Techs Fatfood

## Backend

### Technologies

- **Langage :** Python
- **Framework :** FastAPI
- **Base de données :** PostgreSQL
- **Déploiement :** Docker

## Frontend

### Technologies

- **Framework JS :** NextJS
- **Librairie JS :** React
- **Librairie de Composants :** PrimeReact
- **Librairie CSS :** Aucunes
- **Pré-processeur CSS :** SCSS
- **Autre Techs :**
  - [Lottie](https://lottiefiles.com/) - Animations Assets
  - [Framer Motion](https://www.framer.com/motion) - Animations Components

## Classes

- **Classe User :**
  - `id: str`, *(UUID)*
  - `name: str`,
  - `email: str`, *(Nullable si inscrit via Discord / autre Provider ?)*
  - `discord_id: int`, *(Nullable si non-lié ?)*
  - `password: str`, *(Authentification passwordless ?)*
  - `created_at: date`,
  - `recipes: List[Recipe]`

- **Classe Ingredient :**
  - `name: str`,
  - `portion_size: float`,
  - `kcal: int`,
  - `proteins: float`,
  - `carbohydrate: float`,
  - `fats: float`

- **Classe Recipe :**
  - `name: str`,
  - `ingredients: List[Ingredient]`,
  - `type: Literal["Burger"]`, *(Par la suite on pourrait intégrer "Pizza")*
  - `owner_id: str`,
  - `likes: int`