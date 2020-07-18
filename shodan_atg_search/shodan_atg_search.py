import shodan

SHODAN_API_KEY = "YOUR API"

api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan
    results = api.search("apache")

    # Show results
    for result in results["matches"]:
        if result["location"]["country_name"] == "Brazil":
            print("IP: ", result["ip_str"])
            print(result["data"])

            print(result["location"]["country_name"])
            print("")

    print("Results found: ", results["total"])

except shodan.APIError as e:
    print("Error: ", e)
