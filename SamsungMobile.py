import random

class MobilePhone:
    def __init__(self, series, model, display_size, ram, rom):
        self.series = series
        self.model = model
        self.display_size = display_size
        self.ram = ram
        self.rom = rom

class SamsungFactory:
    def __init__(self):
        self.inventory = {}

    def manufacture_phones(self):
        for series in ['Note', 'S']:
            for model in ['10', '20'] if series == 'Note' else ['10', '20', '22']:
                phones = [MobilePhone(series, model, random.uniform(5.0, 7.0), random.choice([4, 6, 8]), random.choice([64, 128, 256])) for _ in range(1000)]
                self.inventory[f'{series}{model}'] = phones

    def get_phones(self, series, model):
        return self.inventory.get(f'{series}{model}', [])

# Create a Samsung factory and manufacture phones
factory = SamsungFactory()
factory.manufacture_phones()

# Get all Note20 phones
note20_phones = factory.get_phones('Note', '20')
print(f'Total Note20 phones: {len(note20_phones)}')
