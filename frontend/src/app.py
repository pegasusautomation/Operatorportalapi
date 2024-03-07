# from flask import Flask, render_template, jsonify
# import requests
# import json

# app = Flask(__name__)

# class GetLoginId:
#     def __init__(self):
#         pass
#     userdata = 'userData.json'
#     def get_login_id_api(self):
#         parsed_data = None
#         url = "https://operatorportal.dev.mr.tv3cloud.com/apiproxy/Subscriber/users"
#         auth_token = "oauth=refresh_token=0.AVAAHn5axl-Zm0mNpVaHTbXXyWbw77LR4C1Hrs-VWmlB5CW2AHU.AgABAAEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P-udtJUDK2OYlJKaw90lw2Ot8GN4yeCoylM9T0oEqFY2UfxXahN07dCiGVyQUgHN4w7omqPq-xVkAQDjYWRE_2pvkBsLJNkzxjieKerOBDiINe3lXuYUNBCOpqwkQ7sAL6T-Qjpt_4LlNABwQZaVONMwo041jHt96i6Hk6a5KG_LXqnBrh8Rt9gN1ekAInqE1NwfsmuuAPbhsVDXeU6gkvDnCVCy_RTqXlc0HGBl-Hb-muDvsccUE5Jt7Rn-qYnu1uXnW2_smKX0o1_v7MXXMDNa40bl9D0TMNjLuUvnVs5jHbrSXj8-QG3tHs0sMUkEtZMGjnSE3kx_0ped3Zeo6MRk60NEVUzZvMY9A57P4Nyjz5JN6NN-CZP-HdXazqi2C9MlGVI8sf8z22hthYAfaUZLyoAWjQBQMTcip-IOFgsZd_WGHQhJraSskCoDGz2X_X3mjqHT8SHxII7CnMqp_c8wZHX7OzCBWAJ_uLAG78SXVLc-1fwQEZa3s9GUapXWr7-VKUWuC5PB8G8kB3iO4HeEwktwIDShPRL9ggFsXpBwnJFE893aoQmAegjHfH1kLQm5ITehv2rNWMwn0xml4POVSp9Ss4ICtH1BGYCBuqIFQ7Iv-rp6mgq79qcRX-Dvw-4Ufo1YuSoOpTOvfbyGRZV3sPwhT2qIkcN1IqB0UdWWoSrfXkdVTC2RvSEnf-QG9a3o-vzIT8FKQN2FHptXJ_kHUXwXgZdymJSse_lCSN71M-q3dBBZFtpGQ; redirect_uri=https%3A%2F%2Freachclient.dev.mr.tv3cloud.com%2F%3Foauth%3DLIVEID%26tenant%3Ddefault%23p4518adg0r4; access-token=AuthToken1tVXbjqM4EP2azssokS-A4SEPBOgs3STpEHLpvIwImMQJt9iGXL5-TbZ7W1rtPIzUI0G5dHzqlFVUGbtJGS0TOjxIWYsnbD-hZ_Vwmt9Yua9jLm-DlLaDgg9ki5O8atJBUhWK0vOFaCj_T6CQ4lf8jvjFSw60iMXgWuSiiutBxfcKvQhlEAC6Wh6GpbSUTN6Um-QxK7r9Mi7okDLODsyQpj69XuzWfvXEfJofo1Wf7X5m2wgszlqfLY8_t0kvpHFeDAN_5fluL6JlXEo_HaY0i5tc9lzasoRGt5oO13TnHHhV0A9QsZI-hBbFJIH9LIZposdZH8dpBlNN34GenSRV85CTVMh-nBasjJOECvGkgTgdFPtCfhWipF26R9qloPw3op5pLBtOx7xqahWGTEggBr0Pld8pxpgrATGEpok04wmNdMNSFpoQQrPzMMQW1pSDNGCAbkW6-SB2r6bpsMOgZUHyiEOQYOUQHRtWF6ZZRLeMB6f7giMF9-w8ry40_Sy9-Kz9E3LkA4P_euj_26RgCa9ElcmPZvpsFLNrFOMXjcKrnA7LKvnxKPCfEG5U_b9bt6opj2X17bqi2YmEs933n_hL-YeqRzc4fzKDcrv5-O4Uatz-aRO7kYeKs3ssWVVOYnEaGtjQCSYaMoCmI8MC0NJN07QQIQYiFgaG6n5k6iY2CQZIjY0OiIkRVnumBTSEkaZB3YBECSCiCCbCEBqk511rxqmYlUNIgEUstUN6DlfDTtNPUIUocPbRFVF1ouWC7Ut1OzuUy-jQFLuas1IOLc0hrjqFATybIDWSlq3bhqF5noe0EbIIcVzX0Ua92ZsX2tEsXPjjqR0tQ2-4yycgDmdvby9p4Iok3OjSz1etGt_p-Jg3O-VcXUNa0t9GDr17sEOOtci12j8vQFq8vm3c-r453FLekvm19IxsMQHzZmyGivp8zrNGage73rQ-x-motZ_TILiH4r7xz5f73LHWr_dk75OFdwpu_ioPpwE455Fj5GyrUs3FRdnTIguUWHAbv0-rCS2280l2TKHm7o_BelzeT1c-5VrIE3t1psE8cM7Hxa2Z-JfcXbvF8pSp4NFfEbgsrweXxebJM9t3cJ9l7bvnFY3YdddWic6TlkxZvlc_pFHmvdyztbddh5CflwdvsnLTlRc6m-1UrPGmXaUiG5VRMnsz9EhfdRegH5gb3WeXskDFC_X9BbChDE84OPrR3QouT9hVz98"
#         # Prepare the request headers
#         headers = {
#             "Content-Type": "application/json; charset=UTF-8",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Cookie": auth_token
#         }
#         # Open the JSON file for reading
#         with open("C:\\user-datasubmission-react\\backend\\userData.json", "r") as file:
#             # Load the JSON data into a Python dictionary
#             body = json.load(file)
#         # # Prepare the request body
#         # body = {
#         #     "id": "9f60ce36b29666aiok8a3mvag000000003",
#         #     "accountid": "twohundredk.purch192831@outlook.com"
#         # }

#         try:
#             # Make the POST request
#             res = requests.post(url, json=body, headers=headers)
#             res.raise_for_status()  # Raise HTTPError for bad responses
#             parsed_data = res.json()
#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

#         return parsed_data

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/execute', methods=['GET'])
# def execute_request():
#     login_id_fetcher = GetLoginId()
#     login_data = login_id_fetcher.get_login_id_api()
#     app.logger.info('API Response: %s', login_data)
#     return jsonify(login_data)


# if __name__ == "__main__":
#     app.run(debug=True)


# import requests
# import json

# class UpdateUserData:
#     def __init__(self):
#         pass

#     def fetch_and_update(self):
#         # URL for fetching data from the API
#         url = "https://operatorportal.dev.mr.tv3cloud.com/apiproxy/Subscriber/users"
        
#         # Authentication token
#         auth_token = "oauth=refresh_token=0.AVAAHn5axl-Zm0mNpVaHTbXXyWbw77LR4C1Hrs-VWmlB5CW2AHU.AgABAAEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P-udtJUDK2OYlJKaw90lw2Ot8GN4yeCoylM9T0oEqFY2UfxXahN07dCiGVyQUgHN4w7omqPq-xVkAQDjYWRE_2pvkBsLJNkzxjieKerOBDiINe3lXuYUNBCOpqwkQ7sAL6T-Qjpt_4LlNABwQZaVONMwo041jHt96i6Hk6a5KG_LXqnBrh8Rt9gN1ekAInqE1NwfsmuuAPbhsVDXeU6gkvDnCVCy_RTqXlc0HGBl-Hb-muDvsccUE5Jt7Rn-qYnu1uXnW2_smKX0o1_v7MXXMDNa40bl9D0TMNjLuUvnVs5jHbrSXj8-QG3tHs0sMUkEtZMGjnSE3kx_0ped3Zeo6MRk60NEVUzZvMY9A57P4Nyjz5JN6NN-CZP-HdXazqi2C9MlGVI8sf8z22hthYAfaUZLyoAWjQBQMTcip-IOFgsZd_WGHQhJraSskCoDGz2X_X3mjqHT8SHxII7CnMqp_c8wZHX7OzCBWAJ_uLAG78SXVLc-1fwQEZa3s9GUapXWr7-VKUWuC5PB8G8kB3iO4HeEwktwIDShPRL9ggFsXpBwnJFE893aoQmAegjHfH1kLQm5ITehv2rNWMwn0xml4POVSp9Ss4ICtH1BGYCBuqIFQ7Iv-rp6mgq79qcRX-Dvw-4Ufo1YuSoOpTOvfbyGRZV3sPwhT2qIkcN1IqB0UdWWoSrfXkdVTC2RvSEnf-QG9a3o-vzIT8FKQN2FHptXJ_kHUXwXgZdymJSse_lCSN71M-q3dBBZFtpGQ; redirect_uri=https%3A%2F%2Freachclient.dev.mr.tv3cloud.com%2F%3Foauth%3DLIVEID%26tenant%3Ddefault%23p4518adg0r4; access-token=AuthToken1tVXbjqM4EP2azssokS-A4SEPBOgs3STpEHLpvIwImMQJt9iGXL5-TbZ7W1rtPIzUI0G5dHzqlFVUGbtJGS0TOjxIWYsnbD-hZ_Vwmt9Yua9jLm-DlLaDgg9ki5O8atJBUhWK0vOFaCj_T6CQ4lf8jvjFSw60iMXgWuSiiutBxfcKvQhlEAC6Wh6GpbSUTN6Um-QxK7r9Mi7okDLODsyQpj69XuzWfvXEfJofo1Wf7X5m2wgszlqfLY8_t0kvpHFeDAN_5fluL6JlXEo_HaY0i5tc9lzasoRGt5oO13TnHHhV0A9QsZI-hBbFJIH9LIZposdZH8dpBlNN34GenSRV85CTVMh-nBasjJOECvGkgTgdFPtCfhWipF26R9qloPw3op5pLBtOx7xqahWGTEggBr0Pld8pxpgrATGEpok04wmNdMNSFpoQQrPzMMQW1pSDNGCAbkW6-SB2r6bpsMOgZUHyiEOQYOUQHRtWF6ZZRLeMB6f7giMF9-w8ry40_Sy9-Kz9E3LkA4P_euj_26RgCa9ElcmPZvpsFLNrFOMXjcKrnA7LKvnxKPCfEG5U_b9bt6opj2X17bqi2YmEs933n_hL-YeqRzc4fzKDcrv5-O4Uatz-aRO7kYeKs3ssWVVOYnEaGtjQCSYaMoCmI8MC0NJN07QQIQYiFgaG6n5k6iY2CQZIjY0OiIkRVnumBTSEkaZB3YBECSCiCCbCEBqk511rxqmYlUNIgEUstUN6DlfDTtNPUIUocPbRFVF1ouWC7Ut1OzuUy-jQFLuas1IOLc0hrjqFATybIDWSlq3bhqF5noe0EbIIcVzX0Ua92ZsX2tEsXPjjqR0tQ2-4yycgDmdvby9p4Iok3OjSz1etGt_p-Jg3O-VcXUNa0t9GDr17sEOOtci12j8vQFq8vm3c-r453FLekvm19IxsMQHzZmyGivp8zrNGage73rQ-x-motZ_TILiH4r7xz5f73LHWr_dk75OFdwpu_ioPpwE455Fj5GyrUs3FRdnTIguUWHAbv0-rCS2280l2TKHm7o_BelzeT1c-5VrIE3t1psE8cM7Hxa2Z-JfcXbvF8pSp4NFfEbgsrweXxebJM9t3cJ9l7bvnFY3YdddWic6TlkxZvlc_pFHmvdyztbddh5CflwdvsnLTlRc6m-1UrPGmXaUiG5VRMnsz9EhfdRegH5gb3WeXskDFC_X9BbChDE84OPrR3QouT9hVz98"

#         # Prepare the request headers
#         headers = {
#             "Content-Type": "application/json; charset=UTF-8",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Cookie": auth_token
#         }

#         try:
#             # Make the GET request to fetch data from the API
#             response = requests.post(url, headers=headers)
#             response.raise_for_status()  # Raise HTTPError for bad responses
            
#             # Extract data from the response
#             api_data = response.json()

#             # Update the JSON file with the fetched data
#             with open('C:\\user-datasubmission-react\\backend\\userData.json', 'r') as file:
#                 json.dump(api_data, file, indent=2)

#             return {"status": "success", "message": "Data updated successfully"}
        
#         except requests.exceptions.RequestException as err:
#             return {"status": "error", "message": f"Request error: {err}"}
#         except Exception as e:
#             return {"status": "error", "message": f"An error occurred: {e}"}

# # Usage example
# if __name__ == "__main__":
#     updater = UpdateUserData()
#     result = updater.fetch_and_update()
#     print(result)






import requests
import json

class UpdateUserData:
    def __init__(self):
        pass

    def post_data_to_api(self, data):
        # URL for posting data to the API
        url = "https://operatorportal.dev.mr.tv3cloud.com/apiproxy/Subscriber/users"
        
        # Authentication token
        auth_token = "oauth=refresh_token=0.AVAAHn5axl-Zm0mNpVaHTbXXyWbw77LR4C1Hrs-VWmlB5CW2APQ.AgABAAEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P8BvE8OQ216AYtFI7Ll169uzkFM3BY5el6yJ7rid8JWyO9rittr4FFjf5ryk8cgqJZxqt8SmJ4KLwfLybEcQw3tF-ycLZBAkOMHiHrftYBBVBVeXENShxpYJuupdFJ0aLZIDyeOldioKO94_ZbchLFwPpQSrgRB3IhfNsEU6AsI7GezwmDv5Mc9L4CNlvsrmaWV3-_amjJJG5RgZogLjmAgdJgjN6aDxzkKW-Rm8n8VABpVRVzksbo1Pcksh0UeVBcM4e_Jsw11nx6hLN_ld053XqIM9N51mFQ4neSycD8krrdFSS-F48oIl6oqT8SzBUbKmkCGohByaSM1X4vz0GoVpguifHTJHfQloSNtEPicQe9HxGh_jD2gIxTl9WNxxSfqo95eOL8Vmw0p_KkrgTIMtVV1DnLMTU7-Ovv1vYvKOSmtmR8vFfhNlSj7bNHfuW0umnDbeMKO1Ng3kTx8UTI6Wde3CS2RqxhHkmFnghgFE6KxTxlKtF737hgd5FIK3HrUndBHDgMT35Z4MRH7Y2un4cPUWwzaAv0u5n5cJjDzULGD_34qRH9HE-Dxzh6x67BwJ-NvItWtQlfiXJUdqOVkZ6nkMDyz_XgYwXnvcEjWDcbpNxMZB91rYBU-tGFfVbdmJyx75I9XUoUmBAk9oEDaC2VzUVjvBkLVbz36gYRQT86sIJEQY5v3dArSBm8WNXN8aPe_tR-u586axwUNFdq2-_-RmNApx1OCCXaNosp30N2vaiHmXhv2FgijnouXrzXx3dF5WkutHf-ZH-T5cfz6mg6DCnSA49oSd3K_odxRvNx6nBcgGai7OsB6VQZuNfLG4opZ0kV9zxqQyLAROTJnaXJiqavLKSI98pj6eEYGP78mXg; access-token=AuthToken1rVNNk6o4FP01za4tEvJBFi4Q0GbUxla0tTevIkRFCWAIKv76iT2-maqpeYtXNRAul8u5h8o5F6_NclGmon_Qum5eHO8FDs1Soujycl9zpbteJi49qXr64qRF1Wa9tJIGYkVN0wr1r8ZGN7_CP4D_4NKDkLzp3WTRVLzuVWpvqtfGBGjb2Ny-Q56JUue6M2la8Fw-3pdciv4UQqJPjmfnPyJJdHpP5LGLMT-mbQuTEVmd7c3JpllwmlpzwQvZn0SrMAqsRJS81FHWz8SOt4W2AnHJU5F0teh_iq1_UJUUz6JBpa-UC0BA6rwylu2yHQGvzpaKbId3BFpemlbtN53i-wO_iDJTvLfnZcZLfuBFkf8QN_2CbCmynJ_y8lsNQ__97WUj1O-2Pnt-Z_8jVUdZ0weuCxF4gQPHXJhAE9nz6ZFDQAElyGQPDLExhc8cMwTxA-YCRDGwvKKoriL7qWTzt5T_6bDMU1U11U4_5-Cnx-7DY_ILj1VViH5VC8V1pf5v3qbdNqnKt0JZXqsPlcrvXOdVOeXNqQ-Yy6A5ESYMMEqw47hGAJs4LrMZg7YLKAKu7UCMEGOYAmTAkBKAISE2o8ilRi1KAUAORgQy7ALTgqzwVudKNHHZB9RmruvYhFi-ElyL7FmkjJjDip8bT6qTKBf5vjS_oi-UTg6t3NYqL3WfIZ8GLnaJHXoUwgFlHvYIQWEYQjSAjFI_CHw0sOJZOPeSeL6IRu9espyH_XWlUCgu2fnTvSbhEG8uizOireNutrO7dP2qiIrhEBxsKoJ9J44fRrd7e_GEP5zR69pehB81A_e_3AizT1uZ0Vh5dDnkNF0vgzWbjjt43c3PbTSCk-A4eJ9NYvrH8TTO6WTLUJJ0bEXG9cOZcJN_7A8el1mQ3H10fgNkFRg-L_ZRuIQxCMaOu_DHSuvAEzc5X5y7gb8J3r_udE1XG5Bu3dFqYX_xGV5epo8RkPoziIovf5p-T_XA6Zz3fZedj3Px4Tu-GqykqMZmuIdeeeLxF_gsVgY5xMUYzGSs35q8dtY4ehNdXMyP56t_l2IyOp7x4kG_LRs4ErfbNliUu3MznLZiMkDXsUyzWYmlnkZitle7S-DOwfXFCcz6Ew"
        # Prepare the request headers
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": auth_token
        }
        try:
            # Make the POST request to send data to the API
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses

            return {"status": "success", "message": "Data posted successfully"}
        
        except requests.exceptions.RequestException as err:
            return {"status": "error", "message": f"Request error: {err}"}
        except Exception as e:
            return {"status": "error", "message": f"An error occurred: {e}"}

# Usage example
if __name__ == "__main__":
    # Read JSON data from file
    with open('C:\\user-datasubmission-react\\backend\\userData.json', 'r') as file:
        data_to_post = json.load(file)

    updater = UpdateUserData()
    result = updater.post_data_to_api(data_to_post)
    print(result)
