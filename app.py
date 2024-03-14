from flask import Flask, render_template, jsonify, request
import requests
 
app = Flask(__name__)
 
class GetLoginId:
    def __init__(self):
        pass
 
    def get_login_id_api(self, user_id, account_id):
        parsed_data = None
        url = "https://operatorportal.dev.mr.tv3cloud.com/apiproxy/Subscriber/users"
        auth_token = "oauth=refresh_token=0.AVAAHn5axl-Zm0mNpVaHTbXXyWbw77LR4C1Hrs-VWmlB5CW2APQ.AgABAAEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P8OujMqLlC1dSbLjsz2Mcidwnj5Nv9oarl-nUgB9RUCfk2Ly85QwSuNSXqBQAMt9jSQuMmVBR07FPhOrGsXbxsU5olrR2EhtnUIRFPfpdFglRagNwB9Cs7DAm__0mEJ9aBBXcu1UtP53iIdN-x3sVxGCJr8xYuN8OUVA0UUg1_TuvF3lfbOCqGm5PcbctdMeImSmn4jKYlv3HfEnsFOJmSEdy6R_itBTguyKpsUImibqDHbYj0SPon3OLEzeU9ePJCla5xGRSl1ndBncOVkhLrBx-nEAmdjm1bRz12We4wD9evCNUF-HZTKXrVfjgDobrUbToFOa8c-SWvH7vgoFStC9138gOYWPTyIyCBychWbudpUZ-Sgvty92pQHvN5kX1ct7RDH_B59efph69KIof91i3n6z2XjGnGfNDf42WwbmOI0B61pToLI7LQJSAy6SrFrrMn5OkEVD271O-PO7S4Nz4OMaAjz9F_jKrJ-w-P1WcGBV6n3HYgDmp4y77j_4IY5Rtttdt4VJ1FHy_08Z5b3twaHiamLCT-k0hX9h2Ra3nWAUtCg9gB13RLBglEyYuskFyoXHaEGvnxN6qZcWZAnOC095Vy3pMbF_s88j_cnjpMdMqaU1c6UuR21m-AKHKsNGH0Q0O-_4Lu8ABnZNi3Wsw0N3zqWqb3cDpT1wkz1BB5zwgWjSEXyZr83e2_qMbL67MkCjLmJ6Swdaj-SyfreKs6ckBScK_vLsRepobNEv8AOKo6HxIlMiht325-cbp7KYaD-dIIZ2ulK_fupxOjl07eHd6G3dPvrKX6N89F6A_RevrtVRxc81wBAZB9CJ8W7qptDfuf1-4AJAnB-WThtDSSwwIQvCjr3A9ykLEj6; redirect_uri=https%3A%2F%2Freachclient.dev.mr.tv3cloud.com%2F%3Foauth%3DLIVEID%26tenant%3Ddefault%23o814i16n44w; access-token=AuthToken1rVRdk6o4EP01-jZWCIGEBx4Q0MFx5KLgqC-3AkTNyNckwa9fv3HKu1u1tffhVm0ROp3O6U7l9AGvLzlrCuYelerkwPQGcKKHYNWNN4eOCnUblew8qsVInc2iavtyVLS1hgwjKXsm_pUolfwd_gH8B1ccWU3l6FpXsqXdqBUHHb1IbSAAlp6-DS9Zo7i6abeoKK8f-w2tmfsOoa1Opgf4z6i2VXFP689bbNHPou9hOrXXX2B7ArgMTu_DJaNV7c6jdRgFw5Q1tFFR6ZZsT_tKDQN25gVLbx1zP1juH0Vbs2dQo4oXSEFeGAS8UIYKhkH-YuaOiQobg2LoFUXbf5cT9HCkZ9aUgo4OtClpQ4-0qvhPdlUDBGpWcnrizTcbuvz32Zlk4k9Tnzl_cv-p6KJSugYhEBkDODb1a9lQW-e5evjQwAa2kfYeGBtYGD59y0HQesCIgbBlDL2qai-s_MWk_JvK_-xwzQvRynavnjr41WPy6LH9mx6LtmJu2zFBVSv-77qyz2UheM7E0OvVsRX8ThVvm3cqT67hEAfqB1m2YzjYtkyTaAKAbRIHOA4ExMBIy8GEFkKOY2EDaTDEtmFB2wYORgRrtjA2DGRayIaORQydgobhteOCybhxNdMAEWiYZOgLRhUrn0FT19PB-HnxtD2xZsUPjf4UfSZUeuzrvBO8Ua6DfBwQi9gg9DCEY-x4lmfbKAxDiMbQwdgPAh-Nh_GPcOml8XIVTRdemi1Dd4FL--qbq37WZB8mno2ZJmYLd875MQfrKYnXOJXiTe1m9CvaqWu-zMzZ9vjxkV2qLFkWJpkLducHQyg0Odyj7oJgxd-Nzy6Mz3Gf6DpBHy0e-jknJo1VMw3wYrGFR5IXaNOApVyKSbzcsK8g6t8sw5_00zLNZbLy512Wn9Tcn502On2xgGf-FWeITcKvdUIs_C2CsfIOZ2jMAr26V1X4ts-DamNSXpLTTLwmeZ9NtvdKgn3wkVkw6LvdYRFcssq-RFrhE3KqmlSOyf5V9e9KWJ_9ahW-JXiXvEZ3_d8Z76e3cE_Beb_a8ltnb9vNzr80-ZykbdLDvGUEbIWZ7NAxSWWxJT_uRhXifj0Fi40vIMpxwrbewAz0-As"
        # Prepare the request headers
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": auth_token
        }
       
        # Prepare the request body
        body = {
            "id": user_id,
            "accountid": account_id
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
    user_id = request.args.get('id')
    account_id = request.args.get('accountid')
    login_id_fetcher = GetLoginId()
    login_data = login_id_fetcher.get_login_id_api(user_id, account_id)
    app.logger.info('API Response: %s', login_data)
    return jsonify(login_data)
 
if __name__ == "__main__":
    app.run(debug=True)