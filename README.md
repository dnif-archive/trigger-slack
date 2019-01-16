# Slack
https://www.slack.com

### Overview
Slack is the collaboration hub that brings the right people together with all the right information and tools to get work done. Millions of people around the world use Slack to connect their teams, unify their systems, and drive their business forward. Slack brings all of an organisation communication together, a single place for messaging, tools and files it helps in saving time and communicating better.  

### PRE-REQUISITES to use Slack and DNIF  
Install slackclient python library for this Integration  
` pip install slackclient `

Outbound access required for github to clone the plugin

| Protocol   | Source IP  | Source Port  | DNIF FW	| Microsoft-AD FW | Destination Domain | Destination Port  |  
|:------------- |:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|  
| TCP | DS,CR,A10 | Any | Egress	| Ingress | github.com | 443 |
| TCP | DS,CR,A10 | Any | Egress	| Ingress | slack domain | 443 |

#### `*`The above rule assumes both request and response is enabled

### Slack trigger plugin functions  
Details of the function that can be used with the Slack trigger plugin is given in this section.   

### chan_write 
This function allows to send a custom message against an observerd event to specified slack channel.

#### Input  
- Slack channel name 
- The custom message to be sent for the event(The message must be written between double quotes(""))     
#### Example
```
_fetch $SrcIP, $ViolationField , $IntelRef from event where $Intel=True limit 1
>>_trigger api slack chan_write securityteam "Source IP _SrcIP_ found positive in Intel check against Intel feed _IntelRef_"
```
> **Note**  
- In the above example `_SrcIP_` and `_IntelRef_` are `_Field_` which get replaced by their respective values `$SrcIP` and `$IntelRef` which are `$Field`  present in data stack.   
- `_Field_` can be any field present in the DNIF data stack and will be replaced by its corresponding `$Field` value.    
#### Output as in DNIF

![dnifconsole](https://user-images.githubusercontent.com/37173181/50637323-8f3e5180-0f7f-11e9-9bff-90da07eabed9.jpg)  

#### Output as in Slack  

![slack](https://user-images.githubusercontent.com/37173181/50637354-bac13c00-0f7f-11e9-8f94-1bc4d00af30e.jpg)


The output of the lookup call has the following structure (for the available data)
    
|     Field     |             Description              |
|---------------|--------------------------------------|
| Channel    | Name of channel message is being sent to |
| Message    | Message sent to slack channel  |


### Using the Slack API and DNIF  
The Slack API is found on github at   
https://github.com/dnif/trigger-slack
### Getting started with Slack API and DNIF

1. ####    Login to your Data Store, Correlator, and A10 containers.  
   [ACCESS DNIF CONTAINER VIA SSH](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. ####    Move to the `‘/dnif/<Deployment-key>/trigger_plugins’` folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/trigger_plugins/
```
3. ####   Clone using the following command  
```  
git clone https://github.com/dnif/trigger-slack.git slack
```  
4. ####   Move to the `‘/dnif/<Deployment-key>/trigger_plugins/slack/’` folder path and open dnifconfig.yml configuration file     
    
   Replace the tag: <ADD_Your_Slack_Bot_User_OAuth_Access_Token> with your Slack credentials
```
trigger_plugins:
   SLACK_TOKEN: <ADD_Your_Slack_Bot_User_OAuth_Access_Token>
```
