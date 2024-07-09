# Diamond Price Prediction App

This repository contains a Streamlit web application that predicts the price of diamonds based on various features. The model is trained using Gradient Boosting and other machine learning techniques.

## Table of Contents

- [Features](#features)
- [Data](#data)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)


## Features

- **Price Prediction**: Predict the price of a diamond based on its features.
- **User Input**: Enter diamond features such as carat, cut, color, clarity, size, etc.
- **Visualizations**: Visualize the distribution of diamond prices using violin plots.

## Data

The data used in this project is a cleaned version of the diamond dataset. The main features include:

- `price`: Price in US dollars ($326–$18,823)
- `carat`: Weight of the diamond (0.2–5.01)
- `cut`: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- `color`: Diamond color, from J (worst) to D (best)
- `clarity`: Measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- `x`: Length in mm (0–10.74)
- `y`: Width in mm (0–58.9)
- `z`: Depth in mm (0–31.8)
- `size`: Volume of the diamond (x * y * z)
- `depth`: Total depth percentage (43–79)
- `table`: Width of top of diamond relative to widest point (43–95)

## Model

The app uses a Gradient Boosting model for predicting diamond prices. The model was trained using various machine learning techniques, including cross-validation and hyperparameter tuning.

- **Best Parameters**: 
  - `learning_rate`: 0.2
  - `min_samples_leaf`: 4
  - `n_estimators`: 300

- **Performance**:
  - Best cross-validation score: 0.98
  - Test score: 0.98

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, improvements, or bug fixes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
