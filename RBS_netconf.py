# This code is referenced to Cisco python netconf development course

from ncclient import manager
import xmltodict

import xml.dom.minidom


# Create an XML filter for targeted NETCONF queries
netconf_filter_All="""
<filter type="subtree">
  <ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
  </ManagedElement>
</filter>


"""

netconf_filter_MO_PM= """
<filter type="subtree">
  <ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
    <managedElementId>TLAB06X</managedElementId>
      <SystemFunctions>
        <systemFunctionsId>1</systemFunctionsId>
        <Pm/>
      </SystemFunctions>
  </ManagedElement>
</filter>
"""

netconf_filter_FM= """
<filter type="subtree">
  <ManagedElement>
    <managedElementId>1</managedElementId>
    <SystemFunctions>
      <systemFunctionsId>1</systemFunctionsId>
      <Fm>
        <fmId>1</fmId>
          <FmAlarmModel/>
      </Fm>
    </SystemFunctions>
  </ManagedElement>
</filter>
"""

netconf_filter_eNBInfo="""
<filter type="subtree">
  <ManagedElement>
    <managedElementId>1</managedElementId>
      <networkManagedElementId>TLAB06X</networkManagedElementId>
        <SystemFunctions/>
  </ManagedElement>
</filter>

"""

netconf_filter_eNBInfo_ANR="""
<filter type="subtree">
  <ManagedElement>
    <managedElementId>1</managedElementId>
      <ENodeBFunction>
        <AnrFunction>
          <AnrFunctionEUtran/>
        </AnrFunction>
      </ENodeBFunction>
  </ManagedElement>
</filter>

"""

netconf_filter_eNBInfo4="""
<filter type="subtree">
  <ManagedElement>
    <managedElementId>1</managedElementId>
      <networkManagedElementId>TLAB06X</networkManagedElementId>
        <ENodeBFunction>
          <eNBId/>
        </ENodeBFunction>
  </ManagedElement>
</filter>

"""

# Open a connection to the network device using ncclient
with manager.connect(
        host="169.254.2.2",
        port=830,
        username="rbs",
        password="Roger$RN567x",
        hostkey_verify=False
        ) as m:

  netconf_reply = m.get_config(source='running', filter=netconf_filter_All).data_xml

"""   with open("%s.xml" % "netconf_filter_All", 'w') as f:
    f.write(netconf_reply) """

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned

# Processing XML object 



print(xml.dom.minidom.parseString(netconf_reply).toprettyxml())
print("")

