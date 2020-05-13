def get_location(activity):
    location = {
        "biking" : "Shark Valley Trail, Everglades National Park",
        "skiing" : "Zermatt, Switzerland",
        "hiking" : "Mount Kilimanjaro, Tanzania",
        "surfing" : "Malibu, California",
        "cliffdiving" : "Waimea Bay, Hawaii",
        "rockclimbing" : "El Capitan, Yosemite National Park"
    }
    activity = activity.lower()
    activity = activity.replace(" ", "")
    return location[activity]