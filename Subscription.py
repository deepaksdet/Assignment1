import sys
try:
    total_amount = 0
    subscribe_plan = {"prime": 999, "zee5": 999, "sony liv": 999, "netflix": 1947}
    print('Please Enter your Budget:')
    budget = input()
    budget_int = int(budget)
    if budget_int < 999:
        print("Sorry... No Subscription available for Budget provided Rupees : {}".format(budget))
        print("Note: Minimum subscription starts from 999 or above.")
        sys.exit(1)

    print('Please Select Provider (Prime, zee5, sony liv, Netflix) to subscribe. (For more then one values please use comma ", "):')
    providers = input()
    providers = providers.lower().split(',')

    for provider in providers:

        amount = subscribe_plan[provider]
        total_amount = total_amount + amount
    if total_amount > budget_int:
        print(f"Sorry... Your budget is insufficient for {providers} subscription. Your Budget is : {budget_int} & Required Budget is :{total_amount}")
    else:
        print("Below subscription is/are in your budget, total cost is: {}".format(total_amount))
        for provider in providers:
            if provider=='prime':
                print("Prime Video 1x annual subscription - 999")
            elif provider =='zee5':
                print('Zee5 1x annual subscription - 999')
            elif provider == 'sony liv':
                print('Sony liv 1x annual subscription - 999')
            elif provider =='netflix':
                print('Netflix 3x standard monthly plan - 1947')

except KeyError:
    print("Invalid Input provided")
except ValueError:
    print("Invalid Input provided")