# US Open 2022 Data Cleanup & Win Probability Predictor

_**Data was taken from:** https://github.com/serve-and-volley/atp-world-tour-tennis-data_

**Overview**

This project uses Elo ratings and seed data to predict the winner of a tennis match between two players from the 2022 US Open. A logistic regression model was trained based on the Elo difference (explained below), as well as the seed difference. It provided both the model prediction and the baseline Elo win-estimate. Due to the dataset only having seeding data from 1-32, any players outside this ranking (ex., Sebastian Korda, 33rd), were automatically set to the 100 seed. This issue can be addressed through further development of the model.

**Elo Rating System**
- Initial Elo for every player started at 1500.
- EA = Expected Win Probability of Player A
- Elo_A = Elo of Player A (First Player in Output)
- Elo_A = Elo of Player B (Second Player in Output)
- Higher Elo = Higher Chance of Winning
- Elo Changes after every match, thus if Player A was the favorite and won, there would be a slight increase, in comparison to if Player B won.

_**Formula**: EA = %\dfrac{1}{1 + 10^(\dfrac{Elo_B-Elo_A}{400}%_

**Logistic Regression Model**
- Binary classification model used to estimate the probability that Player 1 wins a given match.
- Takes in ELO difference and seed difference between Player 1 and Player 2.
- W0 is the intercept, W1 and W2 are learned weights during training.
- Sigmoid function squashes the result into a probability between 0 and 1


_**Formula**_: P(Player 1 Wins) = σ(z) = 1/(1+e^-z)

**Quickstart**

**Step 1: Clone and Install**
git clone https://github.com/Anshuman-Roy-22/usopen2022-predictor.git
cd usopen2022-predictor
pip install -r requirements.txt

**Step 2: Predict a Match**
python predict.py --player1 "Carlos Alcaraz" --player2 "Casper Ruud"
python predict.py --player1 "Tommy Paul" --player2 "Sebastian Korda"

**Output**
<img width="978" height="181" alt="Image" src="https://github.com/user-attachments/assets/06126956-3ffe-4608-8dc2-8be1b3d95034" />
<img width="976" height="169" alt="Image" src="https://github.com/user-attachments/assets/f7d3b3a1-a9f2-4369-bd74-2944545d2cd6" />

**Future Improvements**
- As stated before, the automated seeding set to 100 outside of the top 32 seeds at the US Open 2022 may have skewed some of the results. Manipulating the data to fix this issue is necessary.
- Larger training dataset, specifically from recent tournaments within 1 year.
- Incorporating a functional frontend, such as an online dashboard, would be beneficial.

**Acknowledgements**
Inspired by AI Work at the US Open 
Data Source (once again): https://github.com/serve-and-volley/atp-world-tour-tennis-data

**Contact**
Made by Anshuman Roy, reach out via GitHub with any questions/concerns.

