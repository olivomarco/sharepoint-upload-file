# Upload a file to Sharepoint via code

In this short tutorial, you'll learn how to upload a file to Sharepoint in a programmatic way. We will be using Microsoft Graph API for that.

Our sample code contained in this repo is based on python, but since we are basically calling Microsoft Graph API URLs you should be able to easily translate it to your language of choice.

## Create app registration

First, go to Azure Active Directory and create a new app registration. The name does not matter, and neither do all the parameters. The only two things you have to do are:

- create a `client_secret` and note it down. We will put it into `CLIENT_SECRET` shell variable, along with our `CLIENT_ID` variable; also note down your Azure Active Directory Tenant ID and put it in a variable (`AAD_TENANT_ID`)
- grant to the app registration the following API permissions under `Microsoft Graph` (see also the image):
`Sites.FullControl.All`
`Sites.Manage.All`
`Sites.Read.All`
`Sites.ReadWrite.All`
`Sites.Selected`

Remember to **grant admin consent** for your directory.

![API Permissions to grant to App Registration](/assets/permissions.png)

## Create your Sharepoint site

Now, go to your Office 365 Sharepoint tenant and create a new Sharepoint website. Take note of the following parameters:

- the name of your Office 365 tenant (`M365_TENANT_NAME`)
- the name of the Sharepoint site you have created (`SHP_SITE_NAME`)

and put them inside the proper shell variables.

## Run code

That's it. Run:

`python3 shp.py`

and in the following prompt take note of the file_url displayed, like in this image:

![Script output](/assets/output.png)

Connect to a browser, and you should be able to see a dummy PDF file uploaded.
