from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.UpdateConnector import UpdateConnecting


class MainUpdateConnect(UpdateConnecting):
    def __init__(self, View, ViewModel: TemplateViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel
        self.PlainTextEdit = self.ViewerPlainTextEdit.getObjectByIndex(2)
        self.PlainTextEditCheckIP = self.ViewerPlainTextEdit.getObjectByIndex(3)
        self.PlainTextEditSubnets = self.ViewerPlainTextEdit.getObjectByIndex(1)
        self.widgetMapCheckIp = {}
        self.widgetMap = {}

    def mainUpdateConnect(self, data):
        """Связь виджетов и viewModel"""
        print('Вызов функции mainUpdateConnect  ', data, 'test')

        self.PlainTextEdit.setPlainText(f"{data}")

    def checkIPConnect(self):
        line_edit = self.ViewerLineEdit.getObjectByIndex(4)
        combo_box = self.ViewerComboBox.getObjectByIndex(3)
        print(line_edit.objectName())

        self.widgetMapCheckIp[str(1)] = {'line_edit': line_edit, 'combo_box': combo_box}

        line_edit.textChanged.connect(
            lambda text, name=line_edit.objectName(): self.createLineEditUpdateCallback('line_edit', text, name)
        )
        combo_box.currentTextChanged.connect(
            lambda text, name=combo_box.objectName(): self.createLineEditUpdateCallback('combo_box', text, name)
        )

    def createLineEditUpdateCallback(self, type_widget, text, name):
        self.viewModel.updateLineEditCheckIpData(self.widgetMapCheckIp, type_widget, name, text)

    def checkIpUpdateConnect(self, data):
        print('Вызов функции checkIpUpdateConnect  ', data, 'test')
        self.PlainTextEditCheckIP.setPlainText(f"{data}")

    def subNetConnect(self):
        le_ip = self.ViewerLineEdit.getObjectByIndex(1)
        le_subnets = self.ViewerLineEdit.getObjectByIndex(2)
        combo_box_ip_mask = self.ViewerComboBox.getObjectByIndex(2)
        combo_box_subnet_mask = self.ViewerComboBox.getObjectByIndex(1)
        print(le_ip.objectName())

        self.widgetMap[str(1)] = {'le_ip': le_ip, 'le_subnets': le_subnets, 'combo_box_subnet_mask': combo_box_subnet_mask, 'combo_box_ip_mask': combo_box_ip_mask}

        le_ip.textChanged.connect(
            lambda text, name=le_ip.objectName(): self.lineEditUpdateCallbackSubNet('le_ip', text, name)
        )
        le_subnets.textChanged.connect(
            lambda text, name=le_subnets.objectName(): self.lineEditUpdateCallbackSubNet('le_subnets', text, name)
        )
        combo_box_subnet_mask.currentTextChanged.connect(
            lambda text, name=combo_box_subnet_mask.objectName(): self.lineEditUpdateCallbackSubNet('combo_box_subnet_mask', text, name)
        )
        combo_box_ip_mask.currentTextChanged.connect(
            lambda text, name=combo_box_ip_mask.objectName(): self.lineEditUpdateCallbackSubNet('combo_box_ip_mask', text, name)
        )

    def lineEditUpdateCallbackSubNet(self, type_widget, text, name):
        self.viewModel.updateLineEditSubNetData(self.widgetMap, type_widget, name, text)

    def subNetUpdateConnect(self, data):
        print('Вызов функции subNetUpdateConnect  ', data, 'test')
        self.PlainTextEditSubnets.setPlainText(f"{data}")
