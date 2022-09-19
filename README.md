# Upload a file to Sharepoint via code

In this short tutorial, you'll learn how to upload a file to Sharepoint in a programmatic way. We will be using Microsoft Graph API for that.

Our sample code contained in this repo is based on python, but since we are basically calling Microsoft Graph API URLs you should be able to easily translate it to your language of choice.

## Create app registration

First, go to Azure Active Directory and create a new app registration. The name does not matter, and neither do all the parameters. The only two things you have to do are:

- create a `client_secret` and note it down. We will put it into `CLIENT_SECRET` shell variable, along with our `CLIENT_ID` variable; also note down your Azure Active Directory Tenant ID and put it in a variable (`AAD_TENANT_ID`)
- grant to the app registration the following API permissions under `Microsoft Graph` (see also image below): `Sites.Selected`

Remember to **Grant admin consent** for your directory after you have added permissions.

Take a note of the "Application (client) ID" of your app registration. You will need it later.

![API Permissions to grant to App Registration](/assets/permissions.png)

## Create your Sharepoint site

Now, go to your Office 365 Sharepoint tenant and create a new Sharepoint website. Take note of the following parameters:

- the name of your Office 365 tenant (`M365_TENANT_NAME`)
- the name of the Sharepoint site you have created (`SHP_SITE_NAME`)

and put them inside the proper shell variables.

## Grant permissions on Sharepoint site

Now it's time to grant permissions to our app registration on the Sharepoint site we have just created. For this, you will need a bit of PowerShell.

Open up a PowerShell window (with Administrator privileges) and run the following commands:

```powershell
Install-Module -Name "PnP.PowerShell"

Connect-PnPOnline -Url "https://<TENANT_NAME>.sharepoint.com" -PnPManagementShell
```

where `<TENANT_NAME>` is the name of your Office 365 tenant. You will need to login in a browser window and give specific permissions to grant the PnP Management Shell to run. Log-in via an **admin** of your Office 365 tenant, and remember to tick "on behalf of organization" checkbox:

![Grant permissions to PnP Management Shell](/assets/pnp-grant.png)

Then, in your PowerShell window, run the following commands:

```powershell
Grant-PnPAzureADAppSitePermission -AppId "<APP_ID>" -DisplayName "myappshp" -Permissions Write -Site https://<TENANT_NAME>.sharepoint.com/sites/<SHP_SITE_NAME>
```

where `<APP_ID>` is the Application (client) ID of your app registration and `<TENANT_NAME>` is the name of your Office 365 tenant, and `<SHP_SITE_NAME>` is the name of the Sharepoint site you have created and you want to grant (in our case, `SharepointUpload`)

## Run code

That's it. Run:

`python3 shp.py`

and in the following prompt take note of the `file_url` displayed, like in this image:

![Script output](/assets/output.png)

Connect to a browser, and you should be able to see a dummy PDF file uploaded.

![File is uploaded](/assets/file_uploaded.png)
