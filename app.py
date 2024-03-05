from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

class GetLoginId:
    def __init__(self):
        pass

    def get_login_id_api(self):
        parsed_data = None
        url = "https://operatorportal.dev.mr.tv3cloud.com/apiproxy/Subscriber/users"
        auth_token = "oauth=refresh_token=0.AVAAHn5axl-Zm0mNpVaHTbXXyWbw77LR4C1Hrs-VWmlB5CW2AHU.AgABAAEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P86J7VxM_6NuD04LGWeBDdcls_XjfqDFdWDZRiidu3vhIehPxhWJQ3zUE93s4_mOPJ3GRQO16O48mbh85zuJBVHuotwkDTzVlOY1xU9wYgEe8rwS0obCoXjTeyyqmXi0jBE1B2yPKoYc5AoYASalU-DCG-LCLUmoQtFxbARCgG6C2SD4qreKPMo2x2Rt_lJi9iOnl3rb5lAhOVr52u6SeB7i51yunkxMoBx9oxoYoF6038ZvDmlZUvwUTBVwL8blfDrqVDj90SbS0kby8g3v7MLB1hqOiXNw7qsRNcQ7ZvnO3v2FdCFBaL8MnowDG5FlTq0pBYeneZH8K5vW_TChSCX2DT-as-JExFJxGX6T48Koc50MjUhO2bSgy2OSE6SE1oBmHZtDObwl9IirIRcsAFSywRwmF705gyAWkxHJtydJasAWQntzSfdR3x1AdqU51kWhhKFRN5xVi5olHcovJAHjX_2v3zWEw3BSZLHkhctgqwWiHyN7juCCaOGWk3cRb9hBd1pWkCtptba7pbsHexvFuAFy-l8SazhIJomMuiu4WHw8khnwjNrNo0GNP03Q65QiHjcwIqEKcnd3WPiCPhMB6KuU5jelQx84QOQCGKaf8rIv0ft_WMk9mlHPBNFw5Lmz_QOmPP6LTj5mA0Kn6wjML8h-D-VVwuqFfu_VcOetc332uMQGX6Ub3SY7KC8alBWEnzZySQ9SpLXLsq8vAA4RaPcX4w3ilB8CyfxtHPSobvRL0MUikucTg; redirect_uri=https%3A%2F%2Freachclient.dev.mr.tv3cloud.com%2F%3Foauth%3DLIVEID%26tenant%3Ddefault%23eyvfx6yxyz4; access-token=AuthToken1tVTLjuI6EP0a2IxA8SN2smARIHDpaR4N4bkZOYlDAnm17QTorx8n031burqzGKlHcuxK1akqq3yqnCpMeB7wQaxUKTvI6cCJXoKnjyQ_l0yoRz_kdT8TfVWjIC2qsB8UmYZ0Z1JWXPzHUSr5O3wD_MQFMc-Y7N-zVBas7BfirLU3qTdoGKY-2i0Jea4S9dBikLIka-w5y_iAJyKJE6Isc3G_ObXz3ZUvi_Ti7XqJ_yM6ecbmFfeS7eXHKeiuOUuzwfNs587GXY_nLFezcBDyiFWp6o55nQTce5R8sOf-KBZFxt-VGhX0ALA5ogHoRQyEgcmiHmJhBEJs-kbXCYKiasMpLlWPhVmSsyDgUnawwcJ-ds7UZyFy3qRr024lF3_gNeFMVYJPRVGV2g1agAJkdN-j_EkxpkIHkANgWRCTDhyaxNY7sAAAViMhgGyEtQCxQYzmhKbVApsPYxM0OmDbgLZ-EFCkBWoiYjdu2KamTVpM84JDre46aVrcePhRevlR-w4cqVYH_pXg_9MkSwJRyCJS72T6IIrVEIX8hiiiSPkgL4JvbYH_RuBK1_-r4xYlF0wVXx5XVr4MROJ__Y0_I3_T9Wga529m0GLTH1-dQrfbL5o4lYoLkbwxlRT5nMnrgCBiUkQxJAY2IbENYJuWZdmQUgKpjQyi2Q8t00IWRQbUbWMa1EIQaZtlGxgiiDEwCaA6AKQaYEEEAKFd914mgstlPgDUsAmysU26I6GbnYfvStNE2tJdvrPCK6483yTnXE_nERfKi6vML0WSq4GNR3Ssb0EM16FQt6TtmA4h2HVdiIfQpnQ0Ho_wsLtcuWvHW643s-nC8bZrd-C-TcClcrahm1ByDbyoLlweGffFy9wBzkSs6pvYzZdzAPPVvXSfc93Yb5Pw9e6hdb5H9mko1fHXS-zDoXWZGmX7N1wvoHs4HY6x98A3Y1ZWTIyS3QROKdhrs8Pj04qKZrL496fdJVi9rdhpa28mZLOpogPfaNMNPKImnysXktRaMtDLbWipSxwiedxI_ziODmkG613ODjXDeNW87irO2etQxoTH89l6ursc_vFPpypePy2H3_262s0TH5LZnLKyPq25LLNltp1ET6JaDg8X17su7fJanevj7vm1wEteNkPOqyx83FrmY96OxtexQPx2ToSf31i4n-3vsdb6i-f59WAWLwU_HJk8ncqWiQYbG3l6GZXPu1tsnF86aKzXTw"
        # Prepare the request headers
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": auth_token
        }
        
        # Prepare the request body
        body = {
            "id": "9f60ce36b29666aiok8a3mvag000000003",
            "accountid": "twohundredk.purch192831@outlook.com"
        }

        try:
            # Make the POST request
            res = requests.post(url, json=body, headers=headers)
            res.raise_for_status()  # Raise HTTPError for bad responses
            parsed_data = res.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return parsed_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['GET'])
def execute_request():
    login_id_fetcher = GetLoginId()
    login_data = login_id_fetcher.get_login_id_api()
    app.logger.info('API Response: %s', login_data)
    return jsonify(login_data)


if __name__ == "__main__":
    app.run(debug=True)