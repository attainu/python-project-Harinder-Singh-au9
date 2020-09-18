import clx.xms
import requests

class Notification:
    
            
    def registration_confirmation(self,number,name,date):
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {"authorization":"Oz9Q5vLmERcX7MkbrVFK4UWianSxg1602A3IYwJHet8sdGTZhCVlXoBtgaFKJwxN3sAjYf8UCqv7O2nH","sender_id":"FSTSMS","message":"Hello "+name+" Your Registration has been approved and your username is"+number,"language":"english","route":"p","numbers":number}
        headers = {'cache-control': "no-cache"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        
    
        
    def order_placed_notification_to_user(self,restor_name,name,date,sum,time,number):
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {"authorization":"Oz9Q5vLmERcX7MkbrVFK4UWianSxg1602A3IYwJHet8sdGTZhCVlXoBtgaFKJwxN3sAjYf8UCqv7O2nH","sender_id":"FSTSMS","message":"Hello "+name+" Your Order has been Placed to "+restor_name+". Your total bill is " +sum+". It will take "+time+"min to dispatch.","language":"english","route":"p","numbers":number}
        headers = {'cache-control': "no-cache"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        
    def order_received_notification_to_restro(self,restor_name,name,date,sum,restro_number,address):
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {"authorization":"Oz9Q5vLmERcX7MkbrVFK4UWianSxg1602A3IYwJHet8sdGTZhCVlXoBtgaFKJwxN3sAjYf8UCqv7O2nH","sender_id":"FSTSMS","message":"Hello "+restor_name+" One order has been placed by Mr./Ms. "+name+" on date "+date+" and his total bill is " +sum+". Delivery Address is "+address,"language":"english","route":"p","numbers":restro_number}
        headers = {'cache-control': "no-cache"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        
            
#if __name__ == '__main__':
    #n=Notification()
    #n.registration_confirmation("7054538345","Rahul","17-8-20")
    #n.order_placed_notification_to_user("Khana Khazana","Rahul","18-09-20","400","40",9818706062)
    #n.order_received_notification_to_restro("Khana khazana","Rahul","17-2-19","400","9818706062","delhi","(Rajma Rice, Chole Bhature)")
    
    