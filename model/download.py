import lightkurve as lk
import pandas as pd
import pickle as pkl
import os


def downloadTarget(star):
    res = lk.search_lightcurve(star)[0].download()
    print(f"Downloaded target {star}")
    return res


def saveTarget(koi, data):
    print(f"Saving target {koi}")
    with open(f"lightcurve_downloads/{koi}", 'wb') as fh:
        pkl.dump(data, fh, protocol=pkl.HIGHEST_PROTOCOL)


def loadTarget(koi):
    with open(f"lightcurve_downloads/{koi}", 'rb') as fh:
        data = pkl.load(fh)
    return data


def download(targets):
    for idx, star in enumerate(targets):
        print(f"[{idx+1}/{len(targets)}] Downloading target {star} ...")
        data = downloadTarget(star)
        saveTarget(star, data)


def main():
    print("Loading Datset ...")
    df = pd.read_csv('dataset/kepler_koi_list.csv')
    koi = [str(i) for i in df.kepid]
    download(koi)


if __name__ == '__main__':
    if not os.path.exists('lightcurve_downloads'):
        os.makedirs('lightcurve_downloads')
    main()
