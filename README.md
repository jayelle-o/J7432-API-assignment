# API assignment (April 14)

Your job is to use the Sunlight Foundation's [OpenStates API](https://sunlightlabs.github.io/openstates-api/) to do two things:

1. Loop over all the bills in Missouri this legislative session

2. Print out each bill's title and the name of its primary sponsor (you'll need to use the bill detail endpoint we discussed in class for this).

You can either sign up for your own API key on the website or use mine: 1f366e0712bd4ad6b079afe3bb993434

## Tips

- When you pass the bill number to the bill detail endpoint, you will need to process it to remove the space. When we looked at this in class, in our browsers, we didn't have to worry about it because modern browsers do that for us. Python doesn't. You'll see an example of this, which uses the `urllib.quote()` method in the `api_example.py` file in this directory.

- Remember that what comes back from these endpoints, once they're processed, is a combination of lists and dictionaries. You'll have to pay close attention as you process the output so that you know which lookup syntax to use (`output['whatever']` vs. `output[0]`).

The assignment is due next Friday, April 23.