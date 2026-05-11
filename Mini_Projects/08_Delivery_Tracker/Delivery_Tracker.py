class Parcel:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class DeliveryTracker:
    def __init__(self):
        self.parcels = []

    def add_parcel(self, parcel):
        self.parcels.append(parcel)

    def update_status(self, name, status):
        allowed_statuses = ['New', 'Shipped', 'Delivered']

        if status not in allowed_statuses:
            print(f'\nStatus "{status}" not found (available statuses: New, Shipped, Delivered).')
            return

        for parcel in self.parcels:

            if parcel.name == name:
                parcel.status = status
                print(f'\nParcel "{name}" updated status to "{status}".')
                return

        print(f'\nParcel "{name}" not found.')

    def show_all_parcels(self):
        print(13 * '=', 'All parcels', 13 * '=', sep='\n')
        for parcel in self.parcels:
            print(f'Name: {parcel.name} \n Status: {parcel.status}')

delivery_tracker = DeliveryTracker()

delivery_tracker.add_parcel(Parcel('Nvidia RTX 3060', 'New'))
delivery_tracker.add_parcel(Parcel('Samsung Galaxy A17', 'New'))
delivery_tracker.add_parcel(Parcel('LG 43', 'New'))

delivery_tracker.show_all_parcels()

delivery_tracker.update_status('Nvidia RTX 3060', 'Shipped')
delivery_tracker.update_status('LG 43', 'Delivered')

delivery_tracker.show_all_parcels()
