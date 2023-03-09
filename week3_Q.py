shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    s = 0
    for i in range(min(len(shop_prices), len(user_coupons))):
        s += shop_prices[i] * (100 - user_coupons[i]) / 100
    for i in range(min(len(shop_prices), len(user_coupons)), max(len(shop_prices), len(user_coupons))):
        s += shop_prices[i]
    return s


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.


s = "(())()"


def is_correct_parenthesis(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genre_total_play = {}
    genre_index_play = {}
    for i in range(len(genre_array)):
        if genre_array[i] not in genre_total_play:
            genre_total_play[genre_array[i]] = play_array[i]
            genre_index_play[genre_array[i]] = [[i, play_array[i]]]
        else:
            genre_total_play[genre_array[i]] += play_array[i]
            genre_index_play[genre_array[i]].append([i, play_array[i]])
    sgtp = sorted(genre_total_play.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, value in sgtp:
        index_play_array = genre_index_play[genre]
        sipa = sorted(index_play_array, key=lambda item: item[1], reverse= True)

        for i in range(len(sipa)):
            if i > 1:
                break
            result.append(sipa[i][0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!