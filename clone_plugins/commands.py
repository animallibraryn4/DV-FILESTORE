@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    # Handling the 'start' command button
    if query.data == "start":
        buttons = [[
            InlineKeyboardButton('/start', callback_data='start'),
            InlineKeyboardButton('/link', callback_data='link')
        ], [
            InlineKeyboardButton('/base_site', callback_data='base_site'),
            InlineKeyboardButton('/api', callback_data='api')
        ], [
            InlineKeyboardButton('/deletecloned', callback_data='deletecloned'),
            InlineKeyboardButton('/broadcast', callback_data='broadcast')
        ], [
            InlineKeyboardButton('💝 Support Group', url='https://t.me/+7ehnJA3aMb84OGNl'),
            InlineKeyboardButton('💁‍♀️ Help', callback_data='help')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id,
            query.message.id,
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.CLONE_START_TXT.format(query.from_user.mention, me2),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    # Handle /link command
    elif query.data == "link":
        buttons = [[
            InlineKeyboardButton('💻 Visit Link', url='http://examplelink.com')
        ], [
            InlineKeyboardButton('Back to Home', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="🔗 Here's your link to visit:",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    # Handle /base_site command
    elif query.data == "base_site":
        # Your base_site logic here
        buttons = [[
            InlineKeyboardButton('Back to Home', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="🔧 Configure your base site here.",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    # Handle /api command
    elif query.data == "api":
        buttons = [[
            InlineKeyboardButton('Back to Home', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="🛠 Configure your API settings.",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    # Handle /deletecloned command
    elif query.data == "deletecloned":
        buttons = [[
            InlineKeyboardButton('Back to Home', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="⚠️ Delete your cloned bot settings.",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    # Handle /broadcast command
    elif query.data == "broadcast":
        buttons = [[
            InlineKeyboardButton('Back to Home', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="📣 Broadcast your message to all users.",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    # Other callback queries
    elif query.data == "help":
        # Show help message
        buttons = [[
            InlineKeyboardButton('Home', callback_data='start'),
            InlineKeyboardButton('Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.CHELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
