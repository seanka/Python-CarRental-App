import random

carDictionary = {
    1000: [
        {
            "carId": 1000,
            "carName": "Ayla",
            "carBrand": "Daihatsu",
            "rentalPrice": 200000,
            "totalPassengers": 4,
            "availability": True,
        },
        {
            "carId": 1000,
            "carName": "Brio",
            "carBrand": "Honda",
            "rentalPrice": 240000,
            "totalPassengers": 4,
            "availability": False,
        },
        {
            "carId": 1000,
            "carName": "Calya",
            "carBrand": "Toyota",
            "rentalPrice": 215000,
            "totalPassengers": 6,
            "availability": True,
        },
    ],
    1500: [
        {
            "carId": 1500,
            "carName": "HR-V",
            "carBrand": "Honda",
            "rentalPrice": 380000,
            "totalPassengers": 4,
            "availability": True,
        },
        {
            "carId": 1500,
            "carName": "Xenia",
            "carBrand": "Daihatsu",
            "rentalPrice": 330000,
            "totalPassengers": 6,
            "availability": False,
        },
        {
            "carId": 1500,
            "carName": "Cortez",
            "carBrand": "Wuling",
            "rentalPrice": 350000,
            "totalPassengers": 6,
            "availability": True,
        },
    ],
    2000: [
        {
            "carId": 2000,
            "carName": "Santa Fe",
            "carBrand": "Hyundai",
            "rentalPrice": 475000,
            "totalPassengers": 6,
            "availability": True,
        },
        {
            "carId": 2000,
            "carName": "CX-5",
            "carBrand": "Mazda",
            "rentalPrice": 430000,
            "totalPassengers": 4,
            "availability": False,
        },
        {
            "carId": 2000,
            "carName": "Innova",
            "carBrand": "Toyota",
            "rentalPrice": 450000,
            "totalPassengers": 6,
            "availability": True,
        },
    ],
}


def initRandomCarIdDictionary():
    for engineCapacity, carEngineList in carDictionary.items():
        for car in carEngineList:
            car["carId"] = generateRandomCarId(engineCapacity)


def generateRandomCarId(engineCapacity):
    # 2 first string : 10, 15, 20 | 2 last number : random number
    carList = carDictionary[engineCapacity].copy()

    existingCarId = set()

    for car in carList:
        existingCarId.add(car["carId"])

    while True:
        randomId = random.randint(10, 99)
        randomId = f"{str(engineCapacity)[:2]}{randomId}"

        if int(randomId) not in existingCarId:
            existingCarId.add(int(randomId))
            return int(randomId)


# CAR FILTERS METHOD
def getFilteredCars(dictionary, filterDictionary):
    filteredCars = dictionary.copy()

    # Loop through filterDictionary, get filterKey and filterValue for the filtering
    for filterKey, filterValue in filterDictionary.items():

        # Get car list for filterValue
        if filterKey == "engineCapacity":
            if filterValue != "any":
                filteredCars = filteredCars[filterValue]
            else:
                filteredCars = []
                for carEngine in dictionary.keys():
                    filteredCars.extend(dictionary[carEngine])

            # Filter car list based on availability
        elif filterKey == "availability":
            if filterValue != "any":
                filteredCars = list(
                    filter(lambda car: car["availability"] == filterValue, filteredCars)
                )

        # Filter car list based on priceRange
        elif filterKey == "priceRange":
            filteredCars = list(
                filter(
                    lambda car: (car["rentalPrice"] >= filterValue[0])
                    and (car["rentalPrice"] <= filterValue[1]),
                    filteredCars,
                )
            )

        # Filter car list based on carSeats
        elif filterKey == "carSeats":
            if filterValue != "any":
                filteredCars = list(
                    filter(
                        lambda car: car["totalPassengers"] >= filterValue,
                        filteredCars,
                    )
                )

        # Filter car list based on carId
        elif filterKey == "carId":
            filteredCars = list(
                filter(lambda car: car["carId"] == filterValue, filteredCars)
            )

        elif filterKey == "carBrand":
            if filterValue != "any":
                filteredCars = list(
                    filter(
                        lambda car: car["carBrand"] == filterValue.title(), filteredCars
                    )
                )

    return filteredCars


def presentCarList(filteredCarList, sortBy=None):
    print("Car ID\t| Car Name\t| Car Brand\t| Rental Price\t| Seats\t| Availability")
    print(
        "=============================================================================="
    )

    sortedList = filteredCarList.copy()

    if sortBy is not None:
        if sortBy == "carname":
            sortBy = "carName"
        elif sortBy == "carbrand":
            sortBy = "carBrand"
        elif sortBy == "rentalprice":
            sortBy = "rentalPrice"
        elif sortBy == "totalpassengers":
            sortBy = "totalPassengers"
        elif sortBy == "carid":
            sortBy = "carId"

        sortedList = sorted(filteredCarList, key=lambda car: car[sortBy])

    for car in sortedList:
        print(
            f"{car["carId"]}\t| {car["carName"]}{"\t\t" if len(car["carName"]) <= 5 else "\t"}| {car["carBrand"]}{"\t\t" if len(car["carBrand"]) <= 5 else "\t"}| {getRupiahFormat(car["rentalPrice"])}\t| {car["totalPassengers"]}\t| {car["availability"]}"
        )


# UTILS METHOD
def getRupiahFormat(value):
    return "Rp.{:,}".format(value)


# INPUT METHODS
def presentSortByInput():
    sortKeyList = ["carId", "carName", "carBrand", "rentalPrice", "totalPassengers"]

    def presentIsAgreeToSort():
        while True:
            isAgreeToSortInput = input(
                """
Do You Want to Sort The Result:
yes | no
    """
            ).lower()

            if isAgreeToSortInput in ["yes", "no"]:
                return isAgreeToSortInput == "yes"

            print("Please Provide Valid Input!")

    isAgreeToSortInput = presentIsAgreeToSort()

    if not isAgreeToSortInput:
        return None

    while True:
        sortByInput = input(
            f"""
Please Provide Sort By Key
{" | ".join(sortKeyList)}
    """
        ).lower()

        if sortByInput in list(map(lambda key: key.lower(), sortKeyList)):
            return sortByInput

        print("Please Provide Valid Input!")


def presentEngineCapacityInput(isSearch):
    while True:
        engineCapacityInput = input(
            f"""
Please Provide Engine Capacity:
1000 | 1500 | 2000{" | Any" if isSearch else ""}
    """
        ).lower()

        if engineCapacityInput in ["1000", "1500", "2000"]:
            return int(engineCapacityInput)
        elif isSearch and engineCapacityInput == "any":
            return engineCapacityInput

        print("Please Check Your Engine Capacity Input")


def presentCarNameInput():
    carName = input("\nPlease Provide Car Name: ")

    return carName.title()


def presentCarIdInput(dictionary={}, list=[]):
    existingCarId = set()

    if len(dictionary) > 0:
        for carList in dictionary.values():
            for car in carList:
                existingCarId.add(car["carId"])
    elif len(list) > 0:
        for car in list:
            existingCarId.add(car["carId"])

    while True:
        carIdInput = input(
            f"""
Please Provide Car ID:
{' | '.join(map(str, sorted(existingCarId)))}
    """
        )

        try:
            carIdInput = int(carIdInput)
            if carIdInput in existingCarId:
                return carIdInput
            else:
                print("Please Provide Valid Car ID")
        except:
            print("Please Provide Valid Input")


def presentCarRentalPriceInput():
    while True:
        rentalPriceInput = input("Please Provide Car Rental Price: ")

        try:
            if int(rentalPriceInput) >= 0:
                return int(rentalPriceInput)
            else:
                print("Please Provide Number Bigger than 0")
        except:
            print("Please Provide Valid Input")


def presentCarSeatsInput():
    while True:
        seatsInput = input("Please Provide Number of Passengers: ")

        try:
            if int(seatsInput) >= 0:
                return int(seatsInput)
            else:
                print("Please Provide Number Bigger than 0")
        except:
            print("Please Provide Valid Input")


def presentBrandInput(isSearchForExistingBrand):
    if isSearchForExistingBrand:
        existingCarBrands = set()

        for carList in carDictionary.values():
            for car in carList:
                existingCarBrands.add(car["carBrand"].lower())

        existingCarBrands.add("any")

    while True:
        if isSearchForExistingBrand:
            brandInput = input(
                f"""
Please Provide Car Brand:
{" | ".join(existingCarBrands).title()}
    """
            ).lower()

            if brandInput in existingCarBrands:
                return brandInput

            print("Please Provide Valid Input!")

        elif not isSearchForExistingBrand:
            brandInput = input("\nPlease Provide Car Brand: ")

            return brandInput.title()


def presentAvailabilityInput():
    while True:
        availabilityInput = input(
            """
Please Provide Car Availability:
True | False | Any
    """
        ).lower()

        if availabilityInput in ["true", "false"]:
            return availabilityInput == "true"
        elif availabilityInput == "any":
            return "any"

        print("Please Provide Valid Input")


def presentFilterInputMenu(filterKeyList, isForceAvailabilityToTrue=False):
    def presentPriceRangeInput():
        while True:
            priceRangeCapacityInput = input(
                """
Please Provide price range:
Minimum-Maximum
    """
            )

            priceRangeList = priceRangeCapacityInput.split("-")

            if len(priceRangeList) != 2:
                print("Please Check Your Price Range Format Input")
            elif not priceRangeList[0].isdigit() and not priceRangeList[1].isdigit():
                print("Make sure to only input number")
            elif int(priceRangeList[0]) >= int(priceRangeList[1]):
                print("First Input Should be Lower than Second Input")
            else:
                return [int(priceRangeList[0]), int(priceRangeList[1])]

    filterDictionary = {}

    for filterKey in filterKeyList:
        if filterKey == "engineCapacity":
            filterDictionary[filterKey] = presentEngineCapacityInput(True)
        elif filterKey == "availability":
            filterDictionary[filterKey] = presentAvailabilityInput()
        elif filterKey == "carBrand":
            filterDictionary[filterKey] = presentBrandInput(True)
        elif filterKey == "priceRange":
            filterDictionary[filterKey] = presentPriceRangeInput()
        elif filterKey == "carSeats":
            filterDictionary[filterKey] = presentCarSeatsInput()

    if isForceAvailabilityToTrue:
        filterDictionary["availability"] = True

    return filterDictionary


# MAIN MENU METHOD
def presentLoginInput():
    while True:
        loginInput = input(
            """
Please Provide Your Login Detail: 
admin | user | exit
    """
        ).lower()

        if loginInput in ["admin", "user", "exit"]:
            return loginInput
        else:
            print("Please Provide Valid Login!")


def presentUserMenu():
    def presentUserMenuChoices():
        print(
            """
          Welcome User
================================
1. Rent a Car
2. Return a Car
0. Back to Main Menu
================================
"""
        )

        while True:
            adminMenuInput = input("Please Provide User Menu: ")

            if adminMenuInput in ["1", "2", "0"]:
                return int(adminMenuInput)

            print("Please Provide Number Based on Menu\n")

    def presentUserMenuRent():
        userFilterInput = presentFilterInputMenu(
            ["engineCapacity", "priceRange", "carSeats"], True
        )

        filteredCars = getFilteredCars(carDictionary, userFilterInput)

        if filteredCars is None or len(filteredCars) <= 0:
            print("\033[H\033[J", end="")
            print("\nSorry We couldn't Find any Cars Match with Your Preferences")
            input("\nPress Any Key to Continue ...")
            return

        sortByInput = presentSortByInput()

        print("\033[H\033[J", end="")
        print(f"\nWe Found {len(filteredCars)} cars Match with Your Preferences:\n")
        presentCarList(filteredCars, sortByInput)

        carIdInput = presentCarIdInput(list=filteredCars)
        selectedCar = getFilteredCars(filteredCars, {"carId": carIdInput})

        rentalDuration = input("Please Provide Rental Duration: ")
        totalRentalPayment = int(rentalDuration) * selectedCar[0]["rentalPrice"]

        print(
            f"\nYour Total Payment is {getRupiahFormat(totalRentalPayment)}, Please Pay Down Payment with Minimum of 30%: {getRupiahFormat(0.3*totalRentalPayment)}"
        )

        # Update Car Dictionary
        selectedCar[0]["availability"] = False

        input("\nPress Any Key to Continue ...")

    def presentUserMenuReturn():
        carListWithFalseAvailability = []

        for carEngineList in carDictionary.values():
            for car in carEngineList:
                if not car["availability"]:
                    carListWithFalseAvailability.append(car)

        carIdInput = presentCarIdInput(list=carListWithFalseAvailability)
        selectedCar = getFilteredCars(
            carListWithFalseAvailability, {"carId": carIdInput}
        )[0]

        print(
            f"\nCar ID {selectedCar["carId"]} with Car Name {selectedCar["carName"]} has been Successfully Returned, Thank You for Choosing our Services."
        )

        selectedCar["availability"] = True

        input("\nPress Any Key to Continue ...")

    while True:
        print("\033[H\033[J", end="")
        userMenuInput = presentUserMenuChoices()

        if userMenuInput == 1:
            print("\033[H\033[J", end="")
            presentUserMenuRent()
        elif userMenuInput == 2:
            print("\033[H\033[J", end="")
            presentUserMenuReturn()
        elif userMenuInput == 0:
            break


def presentAdminMenu():
    def presentAdminMenuChoices():
        print(
            """
          Welcome Admin
================================
1. Display Cars
2. Insert Car
3. Delete Car
4. Update Car
0. Back to Main Menu
================================
"""
        )

        while True:
            adminMenuInput = input("Please Provide Admin Menu: ")

            if adminMenuInput in ["1", "2", "3", "4", "0"]:
                return int(adminMenuInput)

            print("Please Provide Number Based on Menu\n")

    def presentAdminDisplayMenu():
        def presentDisplayIsFiltered():
            while True:
                isFilteredInput = input(
                    """
Do You Want to Filter the Cars:
yes | no
    """
                ).lower()

                if isFilteredInput in ["yes", "no"]:
                    return isFilteredInput == "yes"

                print("Please Provide Valid Answer")

        isFilteredInput = presentDisplayIsFiltered()

        if isFilteredInput:
            adminFilterInput = presentFilterInputMenu(
                ["engineCapacity", "availability", "carBrand"]
            )
            filteredCars = getFilteredCars(carDictionary, adminFilterInput)

            if filteredCars is None or len(filteredCars) <= 0:
                print("\nSorry We couldn't Find any Cars Match with Your Preferences")
                input("\nPress Any Key to Continue ...")
                return

            sortByInput = presentSortByInput()

            print("\033[H\033[J", end="")
            presentCarList(filteredCars, sortByInput)

        elif not isFilteredInput:
            sortByInput = presentSortByInput()

            print("\033[H\033[J", end="")
            for engineCapacity, carLists in carDictionary.items():
                print(f"\nCars with {engineCapacity} CC :::")
                presentCarList(carLists, sortByInput)

        input("\nPress Any Key to Continue ...")

    def presentAdminInsertCarMenu():
        carDictionaryToBeAdded = {}

        engineCapacityInput = presentEngineCapacityInput(False)

        carDictionaryToBeAdded["availability"] = True
        carDictionaryToBeAdded["carId"] = generateRandomCarId(engineCapacityInput)
        carDictionaryToBeAdded["carName"] = presentCarNameInput()
        carDictionaryToBeAdded["carBrand"] = presentBrandInput(False)
        carDictionaryToBeAdded["rentalPrice"] = presentCarRentalPriceInput()
        carDictionaryToBeAdded["totalPassengers"] = presentCarSeatsInput()

        carDictionary[engineCapacityInput].append(carDictionaryToBeAdded)

        print("\nCar Has Been Successfully Added Into the Car Dictionary")
        input("\nPress Any Key to Continue ...")

    def presentAdminDeleteCarMenu():
        for engineCapacity, carLists in carDictionary.items():
            print(f"\nCars with {engineCapacity} CC :::")
            presentCarList(carLists, "carid")

        carIdInput = presentCarIdInput(dictionary=carDictionary)

        engineCapacity = 0
        if str(carIdInput)[:2] == "10":
            engineCapacity = 1000
        elif str(carIdInput)[:2] == "15":
            engineCapacity = 1500
        elif str(carIdInput)[:2] == "20":
            engineCapacity = 2000

        carEngineList = carDictionary[engineCapacity]
        carToBeDeleted = getFilteredCars(carEngineList, {"carId": int(carIdInput)})[0]

        if not carToBeDeleted["availability"]:
            print(
                "\nSorry, Car isn't available for delete now since it's currently being rented"
            )
        else:
            carEngineList.remove(carToBeDeleted)

            print(
                f"\nCar ID {carIdInput} with Car Name {carToBeDeleted["carName"]} Successfully Deleted from the Dictionary"
            )

        input("\nPress Any Key to Continue ...")

    def presentAdminUpdateCarMenu():
        for engineCapacity, carLists in carDictionary.items():
            print(f"\nCars with {engineCapacity} CC :::")
            presentCarList(carLists, "carid")

        carIdInput = presentCarIdInput(dictionary=carDictionary)

        engineCapacity = 0
        if str(carIdInput)[:2] == "10":
            engineCapacity = 1000
        elif str(carIdInput)[:2] == "15":
            engineCapacity = 1500
        elif str(carIdInput)[:2] == "20":
            engineCapacity = 2000

        carEngineList = carDictionary[engineCapacity]
        carToBeUpdated = getFilteredCars(carEngineList, {"carId": int(carIdInput)})[0]

        updateKey = [
            "carName",
            "carBrand",
            "rentalPrice",
            "availability",
            "carSeats",
            "exit",
        ]

        while True:
            updateKeyInput = input(
                f"""
Please Provide Car Properties You Want to Update
{" | ".join(updateKey)}
    """
            ).lower()

            if updateKeyInput == "exit":
                print(f"\nCar Properties has Successfully Updated")
                input("\nPress Any Key to Continue ...")
                return
            elif updateKeyInput in list(map(lambda key: key.lower(), updateKey)):
                if updateKeyInput == "carname":
                    carToBeUpdated["carName"] = presentCarNameInput()
                elif updateKeyInput == "carbrand":
                    carToBeUpdated["carBrand"] = presentBrandInput(False)
                elif updateKeyInput == "rentalprice":
                    carToBeUpdated["rentalPrice"] = presentCarRentalPriceInput()
                elif updateKeyInput == "availability":
                    carToBeUpdated["availability"] = presentAvailabilityInput()
                elif updateKeyInput == "carseats":
                    carToBeUpdated["carSeats"] = presentCarSeatsInput()
            else:
                print("Please Provide Valid Input!")

    while True:
        print("\033[H\033[J", end="")
        adminMenuInput = presentAdminMenuChoices()

        if adminMenuInput == 1:
            print("\033[H\033[J", end="")
            presentAdminDisplayMenu()
        elif adminMenuInput == 2:
            print("\033[H\033[J", end="")
            presentAdminInsertCarMenu()
        elif adminMenuInput == 3:
            print("\033[H\033[J", end="")
            presentAdminDeleteCarMenu()
        elif adminMenuInput == 4:
            print("\033[H\033[J", end="")
            presentAdminUpdateCarMenu()
        elif adminMenuInput == 0:
            break


def main():
    initRandomCarIdDictionary()

    while True:
        print("\033[H\033[J", end="")
        loginInput = presentLoginInput()

        if loginInput == "admin":
            presentAdminMenu()

        elif loginInput == "user":
            print("\033[H\033[J", end="")
            presentUserMenu()

        elif loginInput == "exit":
            break


main()
