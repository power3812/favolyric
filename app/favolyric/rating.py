import numpy as np
import os

# user1とuser2の間のピアソンスコアを計算する
def pearson_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')
    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    common_movies = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    num_ratings = len(common_movies)

    if num_ratings == 0:
        return 0

    user1_sum = np.sum([dataset[user1][item] for item in common_movies])
    user2_sum = np.sum([dataset[user2][item] for item in common_movies])

    user1_squared_sum = np.sum([np.square(dataset[user1][item])
                                    for item in common_movies])
    user2_squared_sum = np.sum([np.square(dataset[user2][item])
                                    for item in common_movies])
    sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item]
                                  for item in common_movies])
    Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings
    if Sxx * Syy == 0:
        return 0
    return Sxy / np.sqrt(Sxx * Syy)

# 入力ユーザに似たユーザをデータセットから検索する
def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError('Cannot find ' + user + ' in the dataset')

    scores = [[x, pearson_score(dataset, user, x)]
                  for x in dataset if x != user]
    scores.sort(key=lambda p: p[1], reverse=True)

    return scores[:num_users]

