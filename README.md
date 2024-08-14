## Rescorla-Wagner-Model

Vn+1 = Vn + α(Δt) * (Ln - Vn)

Where:

- Vn is the expected number of likes for post n
- Vn+1 is the expected number of likes for the next post
- α(Δt) is the learning rate as a function of the time between post n and the previous post
- Ln is the actual number of likes received for post n

The key assumptions of the Rescorla-Wagner model are:

- Learning occurs through prediction errors (the difference between expected and actual outcomes).
-  The associative strength (expectation of the outcome) is updated incrementally after each trial.
- The learning rate determines the speed of updating the associative strength.

These assumptions could apply to social media behavior - users may have expectations about how many likes they'll receive for a post, and they may update these expectations based on the actual likes they receive. Over time, they may learn to adapt their posting behavior to maximize likes.

This equation says that to calculate the user's new expectation for the next post, we start with their current expectation, and then we add to it the prediction error (the difference between actual and expected likes) multiplied by the learning rate (which depends on the time since the last post).
This equation represents a model of how a user's expectation of likes might be updated over time as they make posts and receive likes on a social media platform.

## Limitations
- The Rescorla-Wagner model assumes a single stimulus and outcome. In reality, social media behavior is more complex - users may learn associations for different types of posts, and likes may not be the only relevant outcome (e.g., comments, shares).
- The model assumes a linear relationship between the prediction error and the update to the associative strength. This may not hold for social media behavior - for example, there may be diminishing returns to increasing likes beyond a certain point.
- The model doesn't account for other factors that may influence posting behavior, such as a user's intrinsic motivation to share content or their social relationships with other users.
- The learning rate in the classical Rescorla-Wagner model is constant. In the social media context, it may make more sense for the learning rate to vary over time or across individuals.
