import bonobo
import requests

from time import Time

import xml.etree.ElementTree as ET

def extract_tree():
    tree = ET.parse('CustomerMgmt.xml')
    yield root from tree.getroot()

def addAcct():
for child in root:
        ActionType = child.attrib['ActionType']
        actionTime = child.attrib['ActionTS']
        Status = 'ACTIVE'
        for elem0 in child:
                CustomerID1 = elem0.attrib['C_ID']
                for elem1 in elem0.findall('Account'):
                        AccountID = elem1.attrib['CA_ID']
                        TaxStatus = elem1.attrib['CA_TAX_ST']
                        for elem2 in elem1.findall('CA_NAME'):
                                AccountDesc = elem2.text
                        for elem3 in elem1.findall('CA_B_ID'):
                                BrokerID1 = elem3.text
    SK_Broker_ID = (
    SELECT BrokerID FROM DimAccount, DimBroker
    WHERE BrokerID1 = DimBroker.BrokerID
    )
    SK_Customer_ID = (
    SELECT C_ID FROM DimAccount, DimCustomer
    WHERE CustomerID1 = DimCustomer.CustomerID
    AND actionTime IS BETWEEN  EffectiveDate AND EndDate #tbd
    )
def updAcct():

def closeAcct():

def updCust():

def inact():

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(
        extract_tree,
        bonobo.Limit(10),
        bonobo.CsvWriter('output.csv')
    )
    return graph


def get_services(**options):
    return {}


if __name__ == '__main__':
    start = time() #tbd
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(get_graph(**options), services=get_services(**options))
    stop = time() #tbd
    print("Time taken: ", stop - start, " seconds")
