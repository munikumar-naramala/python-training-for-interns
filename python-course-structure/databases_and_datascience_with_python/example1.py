import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

log_data = """
Jul  1 09:00:55 calvisitor-10-105-160-95 kernel[0]: IOThunderboltSwitch<0>(0x0)::listenerCallback - Thunderbolt HPD packet for route = 0x0 port = 11 unplug = 0
Jul  1 09:01:05 calvisitor-10-105-160-95 com.apple.CDScheduler[43]: Thermal pressure state: 1 Memory pressure state: 0
Jul  1 09:01:06 calvisitor-10-105-160-95 QQ[10018]: FA||Url||taskID[2019352994] dealloc
Jul  1 09:02:26 calvisitor-10-105-160-95 kernel[0]: ARPT: 620701.011328: AirPort_Brcm43xx::syncPowerState: WWEN[enabled]
Jul  1 09:02:26 authorMacBook-Pro kernel[0]: ARPT: 620702.879952: AirPort_Brcm43xx::platformWoWEnable: WWEN[disable]
Jul  1 09:03:11 calvisitor-10-105-160-95 mDNSResponder[91]: mDNS_DeregisterInterface: Frequent transitions for interface awdl0 (FE80:0000:0000:0000:D8A5:90FF:FEF5:7FFF)
Jul  1 09:03:13 calvisitor-10-105-160-95 kernel[0]: ARPT: 620749.901374: IOPMPowerSource Information: onSleep,  SleepType: Normal Sleep,  'ExternalConnected': Yes, 'TimeRemaining': 0,
Jul  1 09:04:33 calvisitor-10-105-160-95 kernel[0]: ARPT: 620750.434035: wl0: wl_update_tcpkeep_seq: Original Seq: 3226
"""

pattern = r'(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2})\s(\S+)\s([\w.-]+)\[(\d+)\]:\s(.+)'

try:
    logs = re.findall(pattern, log_data)
except BaseException as error:
    print(error)
print(logs)
df = pd.DataFrame(logs, columns=['Timestamp', 'Hostname', 'Process', 'PID', 'Log_Message'])

try:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%b %d %H:%M:%S")
except BaseException as error:
    print(error)

print(df.head(2))

try:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, y='Process')
    plt.title('Count of Logs per Process')
    plt.xlabel('Count')
    plt.ylabel('Process')
    plt.show()

    df['Hour'] = df['Timestamp'].dt.hour
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x='Hour')
    plt.title('Count of Logs per Hour')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.show()

except BaseException as error:
    print('error is : {}'.format(error))
