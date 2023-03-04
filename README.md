# Cluster-OneNote-uuids
Python script for clustering OneNote ('.one'/'.onetoc2') files.

Microsoft has the habit of storing various UUIDs/GUIDs in generated files - [USING .NET GUIDS TO HELP
HUNT FOR MALWARE](https://www.virusbulletin.com/uploads/pdf/magazine/2015/vb201506-NET-GUIDs.pdf). 
For .NET files, the *typelib* GUID is unique to each Visual Studio project, while the *mvid* GUID identifies the specific build. Virustotal allows hunting for samples using these identifiers - [VirusTotal .NET GUIDs reference](https://developers.virustotal.com/reference/dot_net_guids).

In the case of OneNote, according to personal observations and [MS-ONESTORE](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/2b394c6b-8788-441f-b631-da1583d772fd), we have *guidFile* for each OneNote file (equivalent for *typelib* GUID) and *guidFileVersion* for each change to that file (equivalent for *mvid* GUID). Long story short, if we take an existing OneNote file and update it, the *guidFileVersion* will change but the *guidFile* will remain the same, allowing us to track different versions of a file.

The clustering uses the *guidFile* field of OneNote files. All files having the same GUID are added to the same cluster.

For detailed information in regards to a OneNote file, one can use [pyOneNote](https://github.com/DissectMalware/pyOneNote).

Quotes from Microsoft docs:
```
guidFile (16 bytes): A GUID, as specified by [MS-DTYP], that specifies the identity of this revision store file. SHOULD be globally unique.
(...)
guidFileVersion (16 bytes): A GUID, as specified by [MS-DTYP]. When either the value of cTransactionsInLog field or the guidDenyReadFileVersion field is being changed, guidFileVersion MUST be changed to a new GUID.
```

The *guidFile* is stored in 16 bytes starting from offset 16 relative to the start of the file.





## Case study
For testing, I looked at ['.one' files from MALWARE bazaar](https://bazaar.abuse.ch/browse.php?search=file_type%3Aone). Here are the results:


```
{
    "3247fcb0-e6ff-4260-b998-21ae329388ea": [
        "f61e6c906ba6429321dc8c1e8f89a6fd295cd4ee8bd21d394dd1679e226d4f3b.one",
        "a870d31caea7f6925f41b581b98c35b162738034d5d86c0c27c5a8d78404e860.one",
        "892e637a6c3909097d99972b8210947f4a228c49b9ad88ff802ce94f3c10b3cd.one",
        "00000f6dc506c0893973cde12e43be88be103b7f07c3f1f12dc97f4d157e29f8.one",
        "6c49b4d40b2925a4e5910e4157f7d302acf9203192187d3d1d178c258239f1c3.one",
        "ae410563d80ff196501e910682a5d2be987eb6370a805c291871d049b75e4133.one",
        "4b30e6ff64e1c2e8c1730778143489a6634c34705bdd2e5effa3e57cddf52907.one",
        "1fc609cb8e092b587826b300535cea12be24960dfa6ebab11c2104736cc3bd8e.one",
        "f2dc85ac9dec5cb21a57d86a83c777c9afd48ba76f89600e4cd3af1b381865eb.one",
        "13970db4675a4a91a4018eb53f104b6e2b2d84a168b4d2d1410c26e36b7c002b.one",
        "186d2972106079c8bf0c9e9000a15056161602dba947d0f85bc7141ef2066d5a.one",
        "add0650d6359a46fb81cf752a4d9e2b13b13e80d38d24c7bd5cee1029f400966.one",
        "b9080762697def380660f61a5f9dcdf0cce6aa4c62139f154cbbfefa18626930.one",
        "78632bbb0a21acb272a6238c54434b3df1e89bf95104a2ea6f0a7c880acf0d13.one",
        "9a279204e8f5e0a00753801d8568aeb12b44f9e5adbbc9af0b32f65d087b9253.one",
        "215c5b5c3b1ae20b73798732cd53039b6cf867e044e3e1ceba49191634434439.one",
        "9d6cb3b193447e11b2e309b249d07cf3f82a677812e478cec39e2d996d2e8944.one",
        "a285b419dff8e67bab8678441d670efb2ef573b8ccabad5dbb355c1ae805a6b4.one",
        "bbc994d3a91480e58678eea6c15baf8ceb136b8ad1493d38715e9d8a24921a43.one",
        "14872981701d4af9459d57a841a5691631c7e36b4af998fc52cfc5efcf1bf780.one"
    ],
    "f16e29d8-faa1-453d-9cfe-18e75f08e21b": [
        "60deac6ecb905441670f140e0cbdfbea2883e871b5458c84765db11ac86ffe17.one"
    ],
    "28a18a1a-7454-4d47-87fa-06fee06cf28b": [
        "bae645306145f5ca847e16add3371e197b1efbf32c8e63dbb3c14726446ca975.one",
        "aafc0ca9681c1f5c368b0f6da85b90e433f6d62fb34ed2e968e53f83981a800f.one",
        "fce64e01d94cb24d6de934910caa58fee08e921f1654b5b2c9069032adf718d3.one"
    ],
    "e15f0935-8bb7-4fa5-b392-86bd3713f99f": [
        "9019a31723e8dde778639cf5c1eb599bf250d7b6a3a92ba0e3c85b0043644d93.one",
        "62a0750ae87bd6445ebc202e442b0820c859507be37487e012b910660050929a.one",
        "8bfd499350dc36e9ad85f70e01249bb917dfe4002d07c8fca7a780a1a4b2c6c7.one",
        "9cd900111f019f32112eba2c1ce1ecd9345d05f5d9a8a617c4a609d77cf2f95b.one",
        "9ffaf97990d92c917884fe2faabee782cca284bec2571ee62ffb7b57d92e3352.one"
    ],
    "5cd4190c-bdd0-49a9-ba73-7a7dc6607bf0": [
        "c9098f9680174838236499bcbee0cf8b6ebd900bdd4cfa6045d0c2ee91f5f81a.one"
    ],
    "e5347422-1992-4f72-8525-c2174a1725a6": [
        "0e70937d4e126fb8449a48bb924d060071d90426a368b4e2d679d3fa2bca2c33.one",
        "37fe85dd17f7fb0aa206640c076a9fd795a6defa303efa40a361fd7760986e09.one"
    ],
    "306b6bbc-0543-417a-8f52-ebfd3e255e2b": [
        "e2b70c8552b38a6b8722d614254202c346190c6a187984a4450223eb536aaf4b.one"
    ],
    "0d2bbb43-3553-4fbd-9525-9fab989758af": [
        "ba208d1bae7ff8bcad7d9fbdc7298c2dc9b5a5d5d061f3037c7d0033951b5a41.one"
    ],
    "91a664a4-a164-40c6-bfa6-42831e81f95e": [
        "12f21e8b7d02f5f48dc6966ec41307f810ef92bf02f9fce4872839153081dd9c.one"
    ],
    "347132f5-19f9-4fa4-9faa-29613a1b3167": [
        "76ac1e659958f6a0ccecf6031c47a762787abb31a00a0807634437f1f79a1992.one",
        "0d781feece557451c861cf2b6eff3e121d7aaac9b156f17ae10d20702a1f962d.one",
        "319db59d8a4addfd6956413af7da48b33cd355cbeb9ca90a191ddf57f45e681d.one",
        "495e5b52716772099ac02c9476feabdd7d51856951d5e61f381c7016f90bb247.one"
    ],
    "94cd14ce-d6a9-4dad-9aaf-203ab6a32a44": [
        "db53c5052be26fbe49e0430fc1d60ab602d87918cad8dd7892974316c3eff0be.one"
    ],
    "4aa70454-7f06-4c9a-becb-9c51988acb37": [
        "3fe5b2887e5cc608b2b5264a51326a3ef7ee1fcf303f295eb550915289321979.one",
        "b58d332effebce32e00cc254be8561388082e2cdab140fe538bdc3d3ba7f5dcc.one",
        "c221e457eb1a69df5a715f77ed5071990246137948529cc0cac2d932419387f9.one",
        "59d4cf6a9c26bdb1fdfaf38135b591594b5a8f27b570f21d1676dcdf095ba32b.one",
        "b69ce5e5977885bb314aa26dd4a56052fdf4b030f1c66a8a52ad90e80bc39fac.one",
        "eca50ee3c2ed694bf8b42a4e0eb14555c70c0d6186cc2dc863af8265c25ba4f1.one"
    ],
    "7bf07f78-caa8-4779-9781-2e45de693c77": [
        "12967c80237e6d4eb19643cb8e365735e4ae6277f2457ea4e204a767d77704b5.one",
        "1c46a5d32059cae9a74821dfa020edcd6c900264996de3a5b004e832cc9bcead.one",
        "ea3de7e7f4c2b293a98e568251dd7f36c4e199586df33f3140164d347fd8f122.one",
        "d940138719adaa132763ad4839079f18dd051db278648248ac2b8a62e4f795f9.one"
    ],
    "b8e1ca72-1263-4fb6-b09a-d415272ca388": [
        "5aa30c40e7c57ad818881e70c431fc3e0477a7193ee33ad0ed53df89d5dc172d.one",
        "6a4fcd114e716464f67b36f3cc68d4eb21c1b17e7fb234eedb11f67c61877cfe.one"
    ],
    "477568a5-8ed4-4a03-ad31-78b1884505a5": [
        "db5fb14dd0b8227895f1c1f58ea72496913d6a186a37ab65ed8993943521a9ef.one",
        "997953548ccaf132f260b69dcd56dd56a2dc8028b4da3e6b99a2133ca2486039.one"
    ],
    "6ff79008-1ebe-42a1-a144-5a7e8d039fbe": [
        "b11b51ff96dc7a5f1cf9985087a6ad4f66980a2b2a9b1945acd43e39434c8dec.one"
    ],
    "24851a00-53dc-4694-be62-b699afde0819": [
        "15212428deeeabcd5b11a1b8383c654476a3ea1b19b804e4aca606fac285387f.one"
    ],
    "920d04ae-e39e-4ba1-ad21-3443383363e2": [
        "68ed66b62e1e6adf5a5e0baab0c1bbef63dc5d52c514ba7d8ff5b6295a498cb6.one",
        "bf8c7c35cb5b8f47ad7fe7e89322960e105efa754360953ca854925a6b914092.one",
        "58fd23e02ba5d6ae4b6662f427c047d62ed34eafc4e547aa62f059313de75397.one"
    ],
    "7362f44c-6bf0-4105-8bff-541e401c1858": [
        "9037e60b24cf0f56cc9e03ea0c2dc2f96180ac160b90c5836e80cc409e6611eb.one"
    ],
    "7d65c102-bb34-4135-b8ba-171e9248b5da": [
        "482a4763c8cf9c448fc851e6fe4554cc48abc563c49847ed040cdaee8a12003c.one"
    ],
    "8d514255-8cf4-4b86-9fc7-1565c80845cb": [
        "62072293339168c6296c56c17686172e4d3110c5ba25fe86c5cfa99765be8441.one"
    ],
    "4712d96b-2e84-4234-abe5-6c160cfe3f8f": [
        "7d84269a8ca5defbf09323180aca1ea7a26eea614fda04d3367c2fac2783a26c.one",
        "ec674e92a9d108d67d2cc0f1f2d20579a8ca8ba6e32af1fe0ed8a1067a426586.one"
    ],
    "e956c4e5-9a59-4207-bef3-62cd5a00b118": [
        "fe6d4c5fb28f7a3379322d4314d31d8227a3356c2992b2bd4b47922f97d3e315.one",
        "6778c59a29e25d722230163bea272ece58d2d3696fbce4347c20104e8fb735dc.one",
        "9e28cff8966bbacee0d1644f157ad3f6c96c7c1dbf04c993f868603db58ec34a.one"
    ],
    "ab4d549e-2e89-45c4-a935-0a854b7ad22c": [
        "cb0f982fc2d96123225527b79c44c85a630722284abb2a74c35c44fe2b8343bc.one",
        "2bbfc13c80c7c6e77478ec38d499447288adc78a2e4b3f8da6223db9e3ac2d75.one",
        "0d4ff412df66d9fb0f092920fd71c579f6e89f63972f2da024a19845870aa06a.one",
        "59537fddba3734be27b2637e2583a026e4cb5bceee222590b8a29ee9a928dcce.one",
        "02ab9be529e1ba28087cc2a3f2f1af3d1ea50e3c05cbf26b9c36eb1d942cf953.one",
        "ca9ed818a8decbefc8f9661b2e7995a9e1afb63a848a043963eec6ae54288a57.one"
    ],
    "0226cd67-7a2d-49e7-b72e-c17e7c00bb91": [
        "305d7962894c83ebfcc863fe129180f20e6144f1f59d70971249d14e6d178fa4.one"
    ],
    "53800758-70af-492a-bce4-4e37780eda13": [
        "17915f90eb7e41c7d6e27c1d01edb3b6affabdbc6d02afc0df55352c57b9c22d.one"
    ],
    "267a0a68-f391-427a-a478-808c6b66f538": [
        "6887cf122d9409d86f09bf8ea900844214c8c07f74daa680582b2b4c69cf35b8.one"
    ],
    "101f4b2a-0ef7-4aa7-81c8-89c7387a87f0": [
        "91da7c5ea5ab92ac99bb4e4c7da27fd840868c533eeee7804f3ed85394faa012.one"
    ],
    "NOT_ONE_FILE": [
        "660870c3f3e8ff105e5cc06b3b3d04436118fc67533c93d0df56bde359e335d0.one"
    ],
    "99a98a2e-3044-47bc-9499-3b00849222be": [
        "b77298a5018b33a4a78dee3a9fe8b869a761966004fb4a63af7fe1f13f7f5dfb.one"
    ],
    "efd78b3a-f6a0-474c-8ab7-ccfb5d4a10ed": [
        "002fe00bc429877ee2a786a1d40b80250fd66e341729c5718fc66f759387c88c.one",
        "bd040a74f99bd767652abc940a4939361d214ba6407781724fde55e48fa7aecf.one",
        "b45ace5a35914dcd4beb7486f3ddad4bbd84be245d403b9e6a3f1b907aa4ae03.one"
    ],
    "6e0af084-0f33-4089-9c18-2eb0f671745d": [
        "24a77f8bca1eb72556e1d9f1eeb2568a2d5c27a0a686d3c8e0635aefc7723144.one"
    ],
    "58bb3b5a-86a2-4672-99be-75eee5b97872": [
        "f8360776618ae88f15187275a0222863ad44565568a71e02626a0ff351e3ef9a.one"
    ],
    "5a75a424-b9c3-4de3-8ce7-bcb76f36efa5": [
        "1791dd7a7c7d0688fac3626d57221ada157c57572cf9ed46ad4cab3d28dbaf91.one"
    ],
    "0920f30b-2626-429b-802f-225b59628e74": [
        "0b77c4eda53491d8e97f4c444b30579850a6396a724eda28288fd8a54cdeafc3.one"
    ],
    "3ed31696-569b-4dd8-b576-5193be9ceb47": [
        "eb674dc2e3787de0948e0af5a50aa365b21eb2dd40c0ef9034e44ed1c46b11d1.one"
    ],
    "96d0c7ac-b832-4f43-b68e-0df8c5c97ee9": [
        "29d154eafeb75a7059fc164c70ae746c6f3eb83d29853b3856d0aa8f8df0adde.one"
    ],
    "1d65569f-29e9-4940-a33d-c4ee64b1053b": [
        "3f00a56cbf9a0e59309f395a6a0b3457c7675a657b3e091d1a9440bd17963f59.one"
    ],
    "9a8c0232-1520-4335-9bb1-29f7fd77db44": [
        "93fb9f37eb70c095e26cedc594ca55ab27710039d0f4e92878e6539975ae58aa.one"
    ],
    "eb862359-b5d3-4f7a-a6f0-d4e01749ce4c": [
        "b13c979dae8236f1e7f322712b774cedb05850c989fc08312a348e2385ed1b21.one"
    ],
    "ff1393ab-e25c-49fe-a4dd-02d7ee1f9011": [
        "a2c8a49dd9a92dcbaf44ee57f26f2c541eaee0b8c53de17d52e4892635f7b489.one"
    ],
    "6bb64d42-8535-4475-8cf7-b591dd7c09c7": [
        "907e1edfdd6879afe9edde05b7afda3ceae6cecbb99588c31dcd4035447837fd.one"
    ],
    "64b3bfed-73fd-445c-a075-ffdfe0c23a35": [
        "9c337d27dab65fc3f4b88666338e13416f218ab75c4b5e37cc396241c225efe8.one"
    ],
    "be925cbf-05cc-4de4-9f59-271b3824003c": [
        "849b413d49b5bb957f65dbcb91afafae46797a557ddab0dc0c0f98710ce1fcd0.one"
    ],
    "4a74120d-a062-463b-bca8-99fbbad23ae0": [
        "bdc5b1beeab60159cbaa9358d6da53cfce724923e28a745ef1df1edb480023d1.one"
    ],
    "578c5e4a-19c3-45d0-ab59-38c1c68724d9": [
        "046a0333f2957ca268168775b23ad4c467c7e76744887cc52f6aedd377888a95.one"
    ],
    "fd7d2c93-df41-459b-a83d-633ff30c564d": [
        "ef5996bf4698ace41405595a4d53a3515ca6041984d6e448c3368c8759837254.one"
    ],
    "ec79bb96-f666-4f54-a848-21b28c8c35cc": [
        "e061a4bf2a5310fc2b7f208129d2ec1e7ba9dbe41b3db253795205b0aeb1f5f3.one"
    ],
    "dcf5b03a-c476-408a-8881-41abbc26fc4e": [
        "f408ef3fa89546483ba63f58be3f27a98795655eb4b9b6217cbe302a5ba9d5f7.one"
    ],
    "41b9960c-b96e-4bb3-a72b-1c1767c110c3": [
        "1acfea4218390a872b340873b71343f6d360b5b9a9e300534e59a69fb4d9b924.one"
    ],
    "db7c1ddc-6bdc-4cdf-904c-44c7346923b6": [
        "4b464d744154fd80d4ea3b78eba5f87742acc82e136412f3b6431bd07ef7538d.one"
    ],
    "72dda358-74b3-4799-b552-d6b66b16219e": [
        "323ceb872e5f0256281968b5a2a3142986f2938a44b18f0d3d23ff2b1c9287a3.one"
    ],
    "95568ede-7a4c-4292-8eaf-dd81f3c967eb": [
        "1b553c8b161fd589ead6deb81fdbd98a71f6137b6e260c1faa4e1280b8bd5c40.one"
    ],
    "09384509-3db1-4dcb-a980-3bb8bb7aaed8": [
        "377fe4e55b6dde063c15c41389f3bb5aacf95443874bdcc0d02a44d6bd793780.one"
    ],
    "0f525d1e-fb94-499b-bb3a-dc26caea3510": [
        "e6da827d704493325f8d8719ff7e814c86b67f30677a82a6e2cf4efdddfbd2a1.one"
    ],
    "64469810-bd37-4477-b892-bf10610b8b45": [
        "e0d9f2a72d64108a93e0cfd8066c04ed8eabe2ed43b80b3f589b9b21e7f9a488.one"
    ]
}

```



## License
The MIT License (MIT)

Copyright (c) 2023 [0x1Avram](https://github.com/0x1Avram)

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
