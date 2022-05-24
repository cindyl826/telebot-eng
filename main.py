import telebot
import time

TOKEN = "1849596311:AAFMAJxmA37W85Zyraqz-jRNBZTfBwHSr-o"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['faq'])
def FAQ(message):
  bot.reply_to(message, "Frequently Asked Questions: \
  \n 1./What_is_ATTA \
  \n 2./What_are_ATTA_main_functions  \
  \n 3./What_makes_ATTA_Streaming_Platform_unique \
  \n 4./How_does_the_content_curation_work \
  \n 5./ATTA_investors_and_partners \
  \n 6./How_does_the_NFT_marketplace_work \
  \n 7./Who_are_going_to_use_ATTA \
  \n 8./How_should_I_participate_in_the_ATTA_governance \
  \n 9./Roadmap \
  \n 10./What_is_the_Scout_Project \
  \n 11./When_is_ATTA_TGE \
  \n 12./I_hold_ATTA_NFT_and_airdrops_What_to_do_next \
  \n 13./Social_Media_Links \
  \n 14./Local_Language_Community_Groups\
  \n 15./Contact_Admin_for_Proposal_and_Suggestions" )

@bot.message_handler(commands = ['What_is_ATTA'])
def ATTA(message):
  bot.reply_to(message," ATTA is a Web3 OGC+PUGC content protocol. We aim to build the next-generation content ecosystem with a Web3-native model to financialize OGC and PUGC content flow. We strive to supercharge content creators for the continued generation of hitting ideas while maximizing their business value. \nWe give users a simple product experience with three major functions at launch: video streaming, content curation, and an NFT Marketplace. ATTA will be governed under the power of ATTA DAO and veToken model.")


@bot.message_handler(commands = ['What_are_ATTA_main_functions'])
def function(message):
  bot.reply_to(message, "We give users a simple product experience with three major functions at launch: video streaming, content curation, and the NFT Marketplace.The DAO-empowered Video streaming platform enables users to stream videos in a Web3 way with DAO-based decentralized rating, reviewing and incentive mechanisms. The content curation function makes it possible for decentralized fundraising and content curation for creators.The marketplace is a trading marketplace for OGC content-related NFTs  and derivatives.")

@bot.message_handler(commands = ['What_makes_ATTA_Streaming_Platform_unique'])
def unique(message):
  bot.reply_to(message, "We provide users with a Web3 video streaming platform with decentralized rating, reviewing, and incentive mechanisms. The DAO-based rating gives community members chances and options for rating all the contents while being rewarded by the ATTA token. All the contents on ATTA are pre-evaluated by the ATTA committee for humanity and political bottom lines. The DAO-based reviewing enables ATTA users to get high-quality reviews of the content beforehand while being able to participate in the reviewing process. Highlight cuts and unlicensed adaptation are also eliminated on ATTA. At the same time, ATTA community members can enjoy juicy token incentives by participating in the governance and staking pool, OGC creators also get a high percentage of the box office.")

@bot.message_handler(commands = ['How_does_the_content_curation_work'])
def curation(message):
  bot.reply_to(message, "The content curation function enables decentralized fundraising and content curation for creators. ATTA provides equal chances for creators and promotes diversity. Creators can get feedback through the community’s evaluation and voting on the project’s ideology then better modify the content and develop the business potential. ATTA also makes it possible for decentralized IP discovery and gem hunting.")

@bot.message_handler(commands = ['How_does_the_NFT_marketplace_work'])
def nftMarketplace(message):
   bot.reply_to(message, "In the Web2 world, users pay and watch based on the content consumption model. In Web3, direct ownership and adaptation rights are reserved for content-related NFT holders.We want to create a marketplace for trading OGC content-related NFTs  and derivatives.Viewers can not only own the uncut OGC content for collection purposes, but also trade adaptation rights, direct liquidity uptick, to PUGC creators.")

@bot.message_handler(commands = ['Who_are_going_to_use_ATTA'])
def nftMarketplace(message):
   bot.reply_to(message, "ATTA is an inclusive platform, we welcome all the users searching for entertainment. To be more specific, OGC creators can meet funding needs and distribution needs (especially content that can't fit web2 criteria); for content consumers, they can add liquidity by tokenizing paid content (NFT) for collection and copyrights in web3, in addition to consumption; for degens, we provide financial incentives through NFT trading, collection, and tokenomics; for PUGC creators, ATTA provides Licensed adaptation with legal protection and potential fan token for further monetization. We are creating a protocol that empowers the creation and monetization of paid video content in a web3 way. We want to create a token economy that incentivizes all stakeholders of protocol-from content producers, distributors, film critics, and adaptors.")

@bot.message_handler(commands = ['Roadmap'])
def nftMarketplace(message):
   bot.reply_to(message, "We will publicly launch our product in Q3, 2022 along with the Web3 movie festival.To be more specific about our roadmap: \n\nQ2 2022: \n-Complete alpha version for internal testing\n-Testnet launch with DAO governance and rating, reviewing and streaming functions\n-Beta testing with targeted institutions, creators and partners\n\nQ3 2022:\n-Public launch with 1st Web3 Movie Festival \n-TGE \n-Continued content lineup\n\nQ4 2022:\n-Royalty program launch\n-Marketplace launch\n-Continued content lineup\n\n2023:\n-Continued product update and content curation\n-Pivot to OGC and OGC IP-based PUGC\n-Develop and launch PUGC and fan tokens related products")

@bot.message_handler(commands = ['How_should_I_participate_in_the_ATTA_governance'])
def nftMarketplace(message):
   bot.reply_to(message, "ATTA will be governed under the power of ATTA DAO and veATTA token.$ATTA holders will vote on all major proposals after ATTA moves to DAO-based governance.1 ATTA equals 1 vote. There will be a staking contract which allows stakers to vote on DAO proposals.A CRV/veToken model is proposed for Snapshot voting. For the first year, two Snapshot strategies will be employed. For vested tokens, the erc20-balance-of strategy gets each participant’s ATTA balance; for unvested tokens, the contract-call strategy is a call to our custom readonly smart contract. This contract returns voting weight for the team, advisors, investors, as well as DAO partners when called. Voting weight is based on the number of unvested tokens for each stakeholder.")

@bot.message_handler(commands = ['Social_Media_Links'])
def social(message):
  bot.reply_to(message, "Official website: https://www.atta.zone/ \n\nTelegram English:https://t.me/attaofficialeng1\n\nTelegram Announcement: https://t.me/ATTA_Announcements\n\nTwitter: https://twitter.com/ATTA_Protocol\n\nInstagram:https://www.instagram.com/atta_protocol/\n\nDiscord:https://discord.com/invite/PqjaWaD6Y9\n\nMedium: https://medium.com/atta-protocol\n")

@bot.message_handler(commands = ['Local_Language_Community_Groups'])
def social(message):
  bot.reply_to(message, "Indonesia: https://t.me/attaofficial_Indonesia\n\nBrazil: https://t.me/attaofficial_Brazil\n\nPhilippines: https://t.me/attaofficial_philippines\n\nVietnam: https://t.me/attaofficial_vietnam\n\nIndia: https://t.me/attaofficial_India\n\nChina:https://t.me/attaofficialcn1\n\nAfrica :https://t.me/attaofficial_africa")

@bot.message_handler(commands = ['ATTA_investors_and_partners'])
def ama(message):
  bot.reply_to(message,"A handful of well-known institutions and individual investors participated in our Angel round, including (in no particular order): Zonff Partners, SHIMA Capital, Hash Global, Altonomy Ventures, Winkrypto, Youbi Capital, LD Capital, Oasis Capital and Weblock. Outstanding individual investors are management of top projects in the industry, including MASK, HECO and YAO Capital CEO Eric Zhang.\nATTA is also proud to be the official partner of a list of well-regarded projects on the market, including Binance NFT, Binance Charity, FLOW, CertiK, Treasureland, Element, and Poizon App etc. ")

@bot.message_handler(commands = ['What_is_the_Scout_Project'])
def events(message):
  bot.reply_to(message, "The Scout Project is a community BUIDL project (aka Ambassador Program) that is open to members from all regions around the globe. It aims to recruit a group of “scouts' ' who have in-depth knowledge on Metaverse and are passionate about participating in the construction of the ATTA Metaverse ecosystem.\n\nIf you think you’re qualified and can actively contribute to the ATTA Metaverse, then join us now!\n\nFill out the application form here: https://forms.gle/Qkd5p5QycNjQqwEPA\n\nRead more here: \nhttps://medium.com/atta-official/introducing-atta-ambassador-program-the-scout-project-79b0ab872036")

@bot.message_handler(commands= ['When_is_ATTA_TGE'])
def smileangel(message):
   bot.reply_to(message, "Around 2022 Q3 - Q4")

@bot.message_handler(commands = ['Contact_Admin_for_Proposal_and_Suggestions'])
def links(message):
  bot.reply_to(message, "Please send an email to info@atta.zone or contact @zoeywang502, thank you!")

@bot.message_handler(commands = ['I_hold_ATTA_NFT_and_airdrops_What_to_do_next'])
def airdrop(message):
  bot.reply_to(message, "Thank you for being a HODLer of ATTA NFT products! Please feel free to hold or trade ATTA NFTs on the marketplaces that we work closely with, such as Binance NFT or Treasureland. \n\nIn light of ATTA’s upcoming IDO, holders and traders of ATTA NFTs and airdrops are entitled to receive priority subscription rights or even direct airdrop of the ATTA token. More details will be provided in the upcoming weeks.")


while True:
  try:
    bot.polling()
  except:
    time.sleep(5)
