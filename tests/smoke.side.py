{
  "id": "e1666318-4808-496f-b6ff-73d2db1503ba",
  "version": "2.0",
  "name": "Smoke Test",
  "url": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
  "tests": [{
    "id": "5789e1e0-01f7-4b41-b53d-d04da317dd5c",
    "name": "Name and Logo Test",
    "commands": [{
      "id": "a4859e10-57a3-4f63-8c68-317a4cf41bc0",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "1380424d-fd11-4588-b75f-30f1b76d84f7",
      "comment": "",
      "command": "setWindowSize",
      "target": "1200x800",
      "targets": [],
      "value": ""
    }, {
      "id": "6a22ad29-e9fe-4126-a8ef-02f3aa63f1a8",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.header-logo img",
      "targets": [
        ["css=.header-logo img", "css:finder"],
        ["xpath=//img[@alt='Teton Chamber of Commerce Logo']", "xpath:img"],
        ["xpath=//div[@id='content']/header/div/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a2b31704-97e1-474e-bb5f-10aa920413a1",
      "comment": "",
      "command": "verifyText",
      "target": "css=.header-title > h1",
      "targets": [
        ["css=.header-title > h1", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h1", "xpath:idRelative"],
        ["xpath=//h1", "xpath:position"],
        ["xpath=//h1[contains(.,'Teton Idaho')]", "xpath:innerText"]
      ],
      "value": "Teton Idaho"
    }, {
      "id": "5191cc4e-694d-4691-ac03-e60618dd1144",
      "comment": "",
      "command": "verifyText",
      "target": "css=.header-title > h2",
      "targets": [
        ["css=.header-title > h2", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h2", "xpath:idRelative"],
        ["xpath=//h2", "xpath:position"],
        ["xpath=//h2[contains(.,'Chamber of Commerce')]", "xpath:innerText"]
      ],
      "value": "Chamber of Commerce"
    }, {
      "id": "bc902274-3b6a-468c-9517-6976e03e4795",
      "comment": "",
      "command": "verifyTitle",
      "target": "Teton Idaho CoC",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "85f289e1-3a2a-4352-b30f-896a6884b789",
    "name": "Home Page Test",
    "commands": [{
      "id": "a428e6e6-2464-4f7e-9056-6feed99e1039",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "372a7c2c-c437-4b7c-af3d-9a29653418d9",
      "comment": "",
      "command": "setWindowSize",
      "target": "1200x800",
      "targets": [],
      "value": ""
    }, {
      "id": "4b42c95d-e88b-420b-a47f-04ee505737d6",
      "comment": "",
      "command": "click",
      "target": "linkText=Home",
      "targets": [
        ["linkText=Home", "linkText"],
        ["css=.active", "css:finder"],
        ["xpath=//a[contains(text(),'Home')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'index.html')])[2]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Home')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "30c1e57b-499a-4369-bacc-c290e8b366f1",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 img",
      "targets": [
        ["css=.spotlight1 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p/a/img", "xpath:idRelative"],
        ["xpath=//p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2633c2f4-62d5-4d8c-8331-35c519be2358",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 img",
      "targets": [
        ["css=.spotlight2 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p/a/img", "xpath:idRelative"],
        ["xpath=//div[2]/p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "214b90e8-9a2f-4092-bdb0-f0f5d6f01fc1",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "linkText=Join Us",
      "targets": [
        ["linkText=Join Us", "linkText"],
        ["css=.a-button:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us')]", "xpath:link"],
        ["xpath=//section[@id='nopad']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[2]", "xpath:href"],
        ["xpath=//section/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b43210a0-1742-49c2-ab51-7b8d205f3312",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us",
      "targets": [
        ["linkText=Join Us", "linkText"],
        ["css=.a-button:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us')]", "xpath:link"],
        ["xpath=//section[@id='nopad']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[2]", "xpath:href"],
        ["xpath=//section/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "d8d14715-889a-4fd2-ae30-fc574e4a5a28",
    "name": "Directory Page Test",
    "commands": [{
      "id": "62a120e9-4b00-4a4d-9c5d-678519ace4de",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "6125245c-7d5f-4e6f-ae2d-4b6a26ceed4f",
      "comment": "",
      "command": "setWindowSize",
      "target": "1200x800",
      "targets": [],
      "value": ""
    }, {
      "id": "bc8610c3-f692-4412-991d-241c23edf739",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "502dbeef-e2a1-43e2-91e3-2b1c85dcebb5",
      "comment": "",
      "command": "click",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "627c0807-19d9-4414-be17-85bfb124332b",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }, {
      "id": "955f17df-6683-4e06-aa11-4d3b1b0bf1ee",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d3627621-4661-42a9-9622-31301b9715ec",
      "comment": "",
      "command": "click",
      "target": "css=.gold-member:nth-child(9)",
      "targets": [
        ["css=.gold-member:nth-child(9)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]", "xpath:idRelative"],
        ["xpath=//section[9]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d9c062bd-a476-4a0a-a15b-40fee2728f62",
      "comment": "",
      "command": "click",
      "target": "css=.gold-member:nth-child(9)",
      "targets": [
        ["css=.gold-member:nth-child(9)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]", "xpath:idRelative"],
        ["xpath=//section[9]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "87b72706-c741-4d67-a966-0b80c8323bbc",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }]
  }, {
    "id": "0d2b6f4e-5cd5-4ef2-b193-d465c1049d84",
    "name": "Join Page Test",
    "commands": [{
      "id": "48e52ad3-dc70-432d-a40b-6d116d2b1636",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "26e28d98-5da6-4d52-82b6-1ff8d0305cde",
      "comment": "",
      "command": "setWindowSize",
      "target": "1200x800",
      "targets": [],
      "value": ""
    }, {
      "id": "c88b20ca-3c7b-4d05-9491-d02013ea495a",
      "comment": "",
      "command": "click",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "e0064213-b732-473a-9e51-b1e08ccc71b3",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a4b3f060-763a-45fa-9784-d4ec0f6c45a3",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5a090ebd-fbfb-4e3c-83f7-0a7056a6dbc9",
      "comment": "",
      "command": "waitForElementVisible",
      "target": "name=fname",
      "targets": [],
      "value": "30000"
    }, {
      "id": "cdc58700-f36b-4e0c-adc7-50eae53eb9bc",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [],
      "value": ""
    }, {
      "id": "5480bee5-9442-49f9-a17d-d2e6634596a1",
      "comment": "",
      "command": "executeScript",
      "target": "document.getElementsByName('fname')[0].value='Alex';",
      "targets": [],
      "value": "Alex"
    }, {
      "id": "81598f17-23b2-433c-b2ca-027ce622c565",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "df3d48b1-24a3-4a21-85f9-f7249a03d197",
      "comment": "",
      "command": "executeScript",
      "target": "document.getElementsByName('lname')[0].value='Smith';",
      "targets": [],
      "value": "Giraldo"
    }, {
      "id": "6a25ae55-9791-4b1e-985e-9dd52df5b6eb",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "10be3709-3008-4b8a-9428-adb670a2838a",
      "comment": "",
      "command": "executeScript",
      "target": "var el=document.getElementsByName('bizname')[0]; el.value='My business'; el.dispatchEvent(new Event('input',{bubbles:true}));",
      "targets": [],
      "value": ""
    }, {
      "id": "46192361-5d73-44e9-b586-b83f4bc93d2a",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [],
      "value": ""
    }, {
      "id": "786e289e-a88f-4752-a750-b7a99c2a8a7e",
      "comment": "",
      "command": "executeScript",
      "target": "document.getElementsByName('biztitle')[0].value='Technician';",
      "targets": [],
      "value": ""
    }, {
      "id": "2357e7b3-ed01-42ff-ab60-5be0a0c5c9b9",
      "comment": "",
      "command": "click",
      "target": "css=.myinput:nth-child(5)",
      "targets": [
        ["css=.myinput:nth-child(5)", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]", "xpath:idRelative"],
        ["xpath=//label[4]", "xpath:position"],
        ["xpath=//label[contains(.,'Title or Position')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "3c42def2-2e30-44d6-b777-11d374389f6b",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5bf24bb0-edc1-4776-8a3c-427331b9698d",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "f870bc5f-a369-47f3-a6f8-1437454f24f9",
    "name": "Admin Page Test",
    "commands": [{
      "id": "38d5b172-c8f8-4ce0-838d-751e62e3f9d5",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "4a111d4d-cbe0-4bf0-b329-3abbd44d6bc0",
      "comment": "",
      "command": "setWindowSize",
      "target": "1200x800",
      "targets": [],
      "value": ""
    }, {
      "id": "0ce0a744-1c1e-4fb7-bdf2-a1d3f3921f69",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "54e9c79d-92b7-4323-9f50-65cde1a6e1b2",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "8005fe43-7994-405f-95e4-b89feea283dd",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ba58c841-fe1c-4e58-8ec3-12dff0fc81bb",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b1e43f62-ac1a-4c2f-88d3-1bd3a9707112",
      "comment": "",
      "command": "executeScript",
      "target": "document.getElementById('username').value='asdfmajja';",
      "targets": [],
      "value": ""
    }, {
      "id": "04cefd6d-3fc8-411f-9a0e-c766b1bb2ce8",
      "comment": "",
      "command": "executeScript",
      "target": "document.getElementById('password').value='aklalalaklskjdekfjdlkd';",
      "targets": [],
      "value": ""
    }, {
      "id": "f5e24a0d-376c-449c-9c9d-9821aabf59ee",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "8cd40bb4-419e-4bea-bd49-9c7cf67da2ec",
      "comment": "",
      "command": "click",
      "target": "css=form > div",
      "targets": [
        ["css=form > div", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/div", "xpath:idRelative"],
        ["xpath=//form/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "65c14f9b-3ff8-408b-af26-7e04538a51ca",
      "comment": "",
      "command": "verifyText",
      "target": "css=.errorMessage",
      "targets": [
        ["css=.errorMessage", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/div/span", "xpath:idRelative"],
        ["xpath=//div/span", "xpath:position"],
        ["xpath=//span[contains(.,'Invalid username and password.')]", "xpath:innerText"]
      ],
      "value": "Invalid username and password."
    }]
  }],
  "suites": [{
    "id": "aa82a66e-7f6f-49d2-a597-508f9f4c1888",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["5789e1e0-01f7-4b41-b53d-d04da317dd5c", "85f289e1-3a2a-4352-b30f-896a6884b789", "d8d14715-889a-4fd2-ae30-fc574e4a5a28", "0d2b6f4e-5cd5-4ef2-b193-d465c1049d84", "f870bc5f-a369-47f3-a6f8-1437454f24f9"]
  }],
  "urls": ["http://127.0.0.1:5500/week_12/cse270-v16/cse270/teton/1.6/index.html"],
  "plugins": []
}