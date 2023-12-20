import asyncio
import pyautogui

async def main():

    print("""Crafting Macro by Lxghtend
Instructions:
- Type in the name of the item you want to craft, so it is the only item on screen.
Notes:
- If something goes wrong, check the github page for an updated version, then message me (@Lxghtend) and I will look at it for you.
      """)

    # Creating a varible to act as a counter for the amount crafted
    amount_crafted = 0

    # Sets the function to loop indefintely
    while True:

        # Adds 1 to the crafted amount every time the loop is ran
        amount_crafted = amount_crafted + 1
        
        # Defining variable for timing and clicking
        build_coords = pyautogui. locateCenterOnScreen("build.png", confidence=0.7)

        # Waiting for an item to appear on the screen in the foundry
        while build_coords is None:
            await asyncio.sleep(0.1)
            build_coords = pyautogui. locateCenterOnScreen("build.png", confidence=0.7)

        pyautogui.moveTo(build_coords)

        # Click the item to craft multiples times
        for i in range(3):
            await asyncio.sleep(1)
            pyautogui.mouseDown()
            await asyncio.sleep(0.2)
            pyautogui.mouseUp()

        # Defining variable for timing and clicking
        ok_coords = pyautogui. locateCenterOnScreen("ok.png", confidence=0.7)

        # Press ok multiple times to pass the "are you sure?" screen
        while ok_coords is None:
            await asyncio.sleep(0.1)
            ok_coords = pyautogui. locateCenterOnScreen("ok.png", confidence=0.7)

        pyautogui.moveTo(ok_coords)

        # Click the button multiples times
        for i in range(3):
            await asyncio.sleep(1)
            pyautogui.mouseDown()
            await asyncio.sleep(0.2)
            pyautogui.mouseUp()

        # Defining variable for timing and clicking
        completion_coords = pyautogui. locateCenterOnScreen("completion.png", confidence=0.7)

        # Wait for the item to finish crafting
        while completion_coords is None:
            await asyncio.sleep(0.1)
            completion_coords = pyautogui. locateCenterOnScreen("completion.png", confidence=0.7)

        pyautogui.moveTo(completion_coords)

        # Click the item to collect it
        for i in range(3):
            await asyncio.sleep(1)
            pyautogui.mouseDown()
            await asyncio.sleep(0.2)
            pyautogui.mouseUp()

        # Prints amount crafted variable at the end of every loop
        print (f"Amount Crafted:{amount_crafted}")

        await asyncio.sleep(1)

asyncio.run(main())