
import numpy as np

def gini(actual, pred):
    assert (len(actual) == len(pred))
    all = np.asarray(np.c_[actual, pred, np.arange(len(actual))], dtype=np.float)
    print(all, )
    all = all[np.lexsort((all[:, 2], -1 * all[:, 1]))]
    print("after sort", all)
    totalLosses = all[:, 0].sum()
    giniSum = all[:, 0].cumsum().sum() / totalLosses

    giniSum -= (len(actual) + 1) / 2.
    return giniSum / len(actual)

def gini_norm(actual, pred):
    return gini(actual, pred) / gini(actual, actual)


if __name__ == "__main__":
    n = 10
    predict = np.random.random(n)
    uniform = [i/n for i in range(n)]
    print(uniform)
    print(predict)
    gini(uniform, predict)
    # print(gini(uniform, predict), gini_norm(uniform, uniform), gini_norm(uniform, predict))
