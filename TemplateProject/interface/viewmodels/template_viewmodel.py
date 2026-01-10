from PySide6.QtCore import Signal, QObject

# from TemplateProject.models.mdReaderModel import IPModel


class TemplateViewModel(QObject):
    # dataChanged = Signal(str)  # Вы можете использовать это для уведомления View об изменении данных
    # dataChanged1 = Signal(str)  # Вы можете использовать это для уведомления View об изменении данных
    # dataChanged2 = Signal(str)  # Вы можете использовать это для уведомления View об изменении данных
    Model = None
    # aggregateWidget = None
    # g_cidrArray = None
    # lineEditData = {}
    # lineEditCheckIpData = {}
    # cidrArray = []
    # ipsArray = []

    def __init__(self, View):
        super().__init__()
        self.view = View
        self.initModel()

    def initModel(self):
        pass
        # self.Model = IPModel()

    def setAggregateWidget(self, widget):
        self.aggregateWidget = widget

    def getCIDRArray(self):
        self.g_cidrArray = []
        for _ in range(0, 33):
            self.g_cidrArray.append(str(_))
        return self.g_cidrArray

    def updateLineEditCheckIpData(self, widgetMap, type_widget, name, text):
        print(f"Обновление: {type_widget}, {name}, значение: {text}")

        # Находим индекс виджета по имени
        x = None
        index = None
        for key, value in widgetMap.items():
            if value[type_widget].objectName() == name:
                if type_widget == 'combo_box':
                    x = 1
                else:
                    x = 0
                index = key
                print(value[type_widget].objectName(), key, value)
                break

        if index is None:
            print(f"Виджет с именем {name} не найден.")
            return

        # Получаем текущее значение IP и CIDR для данного индекса
        current_ip = widgetMap[index]['line_edit'].text() if type_widget == 'combo_box' else text
        current_cidr = widgetMap[index]['combo_box'].currentText() if type_widget == 'line_edit' else text

        # Формируем строку IP/CIDR и обновляем lineEditData
        combined_value = None
        if x == 0:
            combined_value = f"{current_ip}"
            name = "0"
        else:
            combined_value = f"{current_cidr}"
            name = "1"

        self.lineEditCheckIpData[name] = combined_value

        self.dataChanged1.emit(str(self.Model.check_ip(self.lineEditCheckIpData)))

    def updateLineEditSubNetData(self, widgetMap, type_widget, name, text):
        print(f"Обновление: {type_widget}, {name}, значение: {text}")

        # Находим индекс виджета по имени
        index = None
        for key, value in widgetMap.items():
            if value[type_widget].objectName() == name:
                index = key
                break

        if index is None:
            print(f"Виджет с именем {name} не найден.")
            return

        # Получаем значения из виджетов
        ip = widgetMap[index]['le_ip'].text()
        subnets = widgetMap[index]['le_subnets'].text()
        ip_mask = widgetMap[index]['combo_box_ip_mask'].currentText()
        subnet_mask = widgetMap[index]['combo_box_subnet_mask'].currentText()

        # Проверка наличия IP-адреса и маски
        if not ip or not ip_mask:
            result = "Ошибка: Укажите IP-адрес и начальную маску."
            self.dataChanged2.emit(result)
            return

        # Проверка корректности IP-адреса
        try:
            octets = list(map(int, ip.split('.')))
            if len(octets) != 4 or not all(0 <= o < 256 for o in octets):
                raise ValueError
        except ValueError:
            result = "Ошибка: Неверный формат IP-адреса."
            self.dataChanged2.emit(result)
            return

        # Преобразование IP в целое число
        network = sum(octets[i] << (24 - 8 * i) for i in range(4))
        # Преобразование IP в целое число
        ip_int = sum(octets[i] << (24 - 8 * i) for i in range(4))

        def calculate_broadcast(network, subnet_mask):
            mask = (0xFFFFFFFF << (32 - subnet_mask)) & 0xFFFFFFFF
            broadcast = network | ~mask & 0xFFFFFFFF
            return broadcast

        def calculate_network_address(ip, mask):
            mask_bits = (0xFFFFFFFF << (32 - mask)) & 0xFFFFFFFF
            network1 = ip & mask_bits
            return network1

        def ip_to_str(ip):
            return '.'.join(str((ip >> (24 - 8 * i)) & 0xFF) for i in range(4))

        # Сценарий 1: Указана целевая маска
        if subnet_mask and not subnets:
            subnet_mask = int(subnet_mask)
            ip_mask = int(ip_mask)
            if subnet_mask < ip_mask:
                result = f"Ошибка: Целевая маска {subnet_mask} меньше начальной маски {ip_mask}."
            else:
                network_address = calculate_network_address(ip_int, subnet_mask)
                total_subnets = 2 ** (subnet_mask - ip_mask)
                hosts_per_subnet = (2 ** (32 - subnet_mask)) - 2  # Минус 2 для учета сетевого и широковещательного

                broadcast_address = calculate_broadcast(network, subnet_mask)
                start_address = network_address + 1
                end_address = broadcast_address - 1

                result = (f"Номер подсети: 1\n"
                          f"Требуемый размер: {hosts_per_subnet} + 2\n"
                          f"Выделено адресов: {hosts_per_subnet + 2}\n"
                          f"Остаток свободных адресов: 0\n"
                          f"IP адрес подсети: {ip_to_str(network_address)}\n"
                          f"Маска подсети: {subnet_mask}\n"
                          f"Диапазон адресов: {ip_to_str(start_address)} - {ip_to_str(end_address)}\n"
                          f"Широковещательный адрес: {ip_to_str(broadcast_address)}")

        # Сценарий 2: Указано количество узлов
        elif subnets and not subnet_mask:
            required_hosts = int(subnets) + 2
            required_mask = 32
            while required_hosts > (2 ** (32 - required_mask)):
                required_mask -= 1

            ip_mask = int(ip_mask)
            if required_mask < ip_mask:
                result = f"Ошибка: Маска для {subnets} узлов меньше начальной маски {ip_mask}."
            else:
                network_address = calculate_network_address(ip_int, required_mask)
                hosts_per_subnet = (2 ** (32 - required_mask)) - 2
                total_subnets = 2 ** (required_mask - ip_mask)
                free_addresses = hosts_per_subnet - int(subnets)

                broadcast_address = calculate_broadcast(network, required_mask)
                start_address = network_address + 1
                end_address = start_address + int(subnets) - 1

                result = (f"Номер подсети: 1\n"
                          f"Требуемый размер: {subnets} + 2\n"
                          f"Выделено адресов: {hosts_per_subnet + 2}\n"
                          f"Остаток свободных адресов: {free_addresses}\n"
                          f"IP адрес подсети: {ip_to_str(network_address)}\n"
                          f"Маска подсети: {required_mask}\n"
                          f"Диапазон адресов: {ip_to_str(start_address)} - {ip_to_str(broadcast_address-1)}\n"
                          f"Широковещательный адрес: {ip_to_str(broadcast_address)}\n"
                          f"Всего подсетей: {total_subnets}\n"
                          f"Кол-во узлов в каждой подсети: {hosts_per_subnet}")
        else:
            result = "Ошибка: Укажите либо целевую маску, либо количество подсетей."

        self.dataChanged2.emit(result)

    def updateLineEditData(self, widgetMap, type_widget, name, text):
        """
        Обновляет данные, связывая QLineEdit и QComboBox в строку формата IP/CIDR.
        :param widgetMap: словарь, связывающий виджеты
        :param type_widget: тип виджета (line_edit или combo_box)
        :param name: имя виджета
        :param text: новое значение текста
        """
        print(f"Обновление: {type_widget}, {name}, значение: {text}")

        # Находим индекс виджета по имени
        index = None
        for key, value in widgetMap.items():
            if value[type_widget].objectName() == name:
                if type_widget == 'combo_box':
                    name = value["line_edit"].objectName()
                index = key
                print(value[type_widget].objectName(), key, value)
                break

        if index is None:
            print(f"Виджет с именем {name} не найден.")
            return

        # Получаем текущее значение IP и CIDR для данного индекса
        current_ip = widgetMap[index]['line_edit'].text() if type_widget == 'combo_box' else text
        current_cidr = widgetMap[index]['combo_box'].currentText() if type_widget == 'line_edit' else text

        # Формируем строку IP/CIDR и обновляем lineEditData
        combined_value = f"{current_ip}/{current_cidr}"
        self.lineEditData[name] = combined_value
        aggregate_date = [value for value in self.lineEditData.values()]

        print(f"Обновлено значение: {name} = {combined_value}")
        print("Текущее состояние:", self.lineEditData)
        print("Полное значение: ", self.lineEditData.values(), self.lineEditData.keys())
        print("Только передаваемое значение: ", aggregate_date)

        # Если нужно уведомить View об изменении, можно вызвать dataChanged.emit()
        self.dataChanged.emit(str(self.Model.aggregate_networks(aggregate_date)))
