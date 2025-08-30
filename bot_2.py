#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, ConversationHandler
from telegram.error import TelegramError
import json
import os
from datetime import datetime

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# معلومات البوت والإعدادات
BOT_TOKEN = "8126453870:AAHKpVDTFA5R5SHcYQVldkNlQp83PKlxeio"
ADMIN_ID = 910021564
GROUP_USERNAME = "@shamcashusdt1"
SHAMCASH_ADDRESS = "be456e0ea9392db4d68a7093ee317bc8"
USDT_ADDRESS = "0x2F1A184B6abBb49De547D539eDC3b5eAdc3E01F9"
SUPPORT_USERNAME = "@ali0619000"
REPORT_GROUP = "@shamcashusdt1"

# حالات المحادثة
(WAITING_FOR_BUY_AMOUNT, WAITING_FOR_BUY_ADDRESS, WAITING_FOR_BUY_CURRENCY,
 WAITING_FOR_SELL_AMOUNT, WAITING_FOR_SELL_ADDRESS, WAITING_FOR_SELL_CURRENCY) = range(6)

# قاعدة بيانات بسيطة في الذاكرة
user_data = {}
transactions = []  # قائمة المعاملات
daily_stats = {"buy_count": 0, "sell_count": 0, "total_commission": 0.0}

def get_admin_keyboard():
    """إنشاء لوحة مفاتيح الأدمن"""
    keyboard = [
        [KeyboardButton("📊 الإحصائيات"), KeyboardButton("📋 المعاملات")],
        [KeyboardButton("💰 العمولات"), KeyboardButton("👥 المستخدمين")],
        [KeyboardButton("🔙 العودة للقائمة الرئيسية")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_main_keyboard():
    """إنشاء لوحة المفاتيح الرئيسية"""
    keyboard = [
        [KeyboardButton("🟢 شراء USDT"), KeyboardButton("🔴 بيع USDT")],
        [KeyboardButton("📊 حالة الطلبات"), KeyboardButton("ℹ️ معلومات")],
        [KeyboardButton("🔙 القائمة الرئيسية")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_currency_keyboard():
    """إنشاء لوحة اختيار العملة"""
    keyboard = [
        [KeyboardButton("💵 دولار أمريكي"), KeyboardButton("🇸🇾 ليرة سورية")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def check_group_membership(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool:
    """التحقق من انضمام المستخدم للمجموعة"""
    try:
        member = await context.bot.get_chat_member(GROUP_USERNAME, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except TelegramError:
        return False

def calculate_commission(amount: float) -> float:
    """حساب العمولة: 1$ + 0.5% من المبلغ"""
    return 1.0 + (amount * 0.005)

def format_transaction_report(user_id: int, username: str, transaction_type: str, amount: float, currency: str, address: str = None) -> str:
    """تنسيق تقرير المعاملة وحفظها"""
    commission = calculate_commission(amount)
    total_amount = amount + commission if transaction_type == "شراء" else amount - commission
    
    # حفظ المعاملة
    transaction = {
        "id": len(transactions) + 1,
        "user_id": user_id,
        "username": username,
        "type": transaction_type,
        "amount": amount,
        "currency": currency,
        "commission": commission,
        "total": total_amount,
        "address": address,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    transactions.append(transaction)
    
    # تحديث الإحصائيات
    if transaction_type == "شراء":
        daily_stats["buy_count"] += 1
    else:
        daily_stats["sell_count"] += 1
    daily_stats["total_commission"] += commission
    
    report = f"""
📊 تقرير معاملة جديدة

👤 المستخدم: @{username} (ID: {user_id})
🔄 نوع المعاملة: {transaction_type}
💰 المبلغ: {amount:.2f} USDT
💳 العملة: {currency}
💸 العمولة: {commission:.2f} $
📈 المبلغ الإجمالي: {total_amount:.2f}
🕐 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    if address:
        if transaction_type == "شراء":
            report += f"📍 عنوان BEP20: {address}\n"
        else:
            report += f"📍 عنوان شام كاش: {address}\n"
    
    report += "\n⚠️ عند تحويل المبلغ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي"
    
    return report

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """معالج أمر البدء"""
    user = update.effective_user
    user_id = user.id
    
    # التحقق من كون المستخدم أدمن
    if user_id == ADMIN_ID:
        welcome_text = f"""
مرحباً {user.first_name}! 👋

🔧 لوحة تحكم الأدمن

اختر من القائمة أدناه:
"""
        await update.message.reply_text(welcome_text, reply_markup=get_admin_keyboard())
        return
    
    # التحقق من الانضمام للمجموعة
    is_member = await check_group_membership(context, user_id)
    
    if not is_member:
        keyboard = [[InlineKeyboardButton("انضم للمجموعة", url=f"https://t.me/{GROUP_USERNAME[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"مرحباً {user.first_name}! 👋\n\n"
            "للاستفادة من خدمات البوت، يجب عليك الانضمام إلى مجموعتنا أولاً:\n"
            f"{GROUP_USERNAME}\n\n"
            "بعد الانضمام، اضغط /start مرة أخرى.",
            reply_markup=reply_markup
        )
        return
    
    # إذا كان المستخدم منضماً للمجموعة
    welcome_text = f"""
مرحباً {user.first_name}! 🎉

أهلاً بك في بوت تداول USDT عبر شام كاش

💰 خدماتنا:
• شراء USDT بالليرة السورية أو الدولار
• بيع USDT واستلام الأموال عبر شام كاش

💸 العمولة: 1$ + 0.5% من المبلغ الإجمالي

📞 للدعم: {SUPPORT_USERNAME}

اختر الخدمة المطلوبة من القائمة أدناه:
"""
    
    await update.message.reply_text(welcome_text, reply_markup=get_main_keyboard())

async def buy_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """بدء عملية شراء USDT"""
    user_id = update.effective_user.id
    
    # التحقق من الانضمام للمجموعة
    is_member = await check_group_membership(context, user_id)
    if not is_member:
        await update.message.reply_text("يجب عليك الانضمام للمجموعة أولاً. اضغط /start")
        return ConversationHandler.END
    
    await update.message.reply_text(
        "🟢 شراء USDT\n\n"
        "كم مبلغ USDT تريد شراءه؟\n"
        "مثال: 100"
    )
    
    return WAITING_FOR_BUY_AMOUNT

async def buy_amount_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام مبلغ الشراء"""
    try:
        amount = float(update.message.text)
        if amount <= 0:
            await update.message.reply_text("يرجى إدخال مبلغ صحيح أكبر من الصفر.")
            return WAITING_FOR_BUY_AMOUNT
        
        context.user_data['buy_amount'] = amount
        commission = calculate_commission(amount)
        total = amount + commission
        
        await update.message.reply_text(
            f"💰 المبلغ: {amount} USDT\n"
            f"💸 العمولة: {commission:.2f} $\n"
            f"📈 المبلغ الإجمالي: {total:.2f} $\n\n"
            "الآن أرسل عنوان محفظتك على شبكة BEP20:"
        )
        
        return WAITING_FOR_BUY_ADDRESS
        
    except ValueError:
        await update.message.reply_text("يرجى إدخال رقم صحيح.")
        return WAITING_FOR_BUY_AMOUNT

async def buy_address_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام عنوان المحفظة للشراء"""
    address = update.message.text.strip()
    
    # التحقق الأساسي من العنوان (يبدأ بـ 0x ويحتوي على 42 حرف)
    if not address.startswith('0x') or len(address) != 42:
        await update.message.reply_text(
            "عنوان المحفظة غير صحيح. يجب أن يبدأ بـ 0x ويحتوي على 42 حرف.\n"
            "يرجى إدخال عنوان صحيح:"
        )
        return WAITING_FOR_BUY_ADDRESS
    
    context.user_data['buy_address'] = address
    
    await update.message.reply_text(
        "اختر العملة التي تريد الدفع بها:",
        reply_markup=get_currency_keyboard()
    )
    
    return WAITING_FOR_BUY_CURRENCY

async def buy_currency_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام اختيار العملة للشراء"""
    currency_text = update.message.text
    
    if "دولار" in currency_text:
        currency = "دولار أمريكي"
    elif "ليرة" in currency_text:
        currency = "ليرة سورية"
    else:
        await update.message.reply_text(
            "يرجى اختيار العملة من الأزرار المتاحة:",
            reply_markup=get_currency_keyboard()
        )
        return WAITING_FOR_BUY_CURRENCY
    
    context.user_data['buy_currency'] = currency
    
    # إنشاء ملخص الطلب
    amount = context.user_data['buy_amount']
    address = context.user_data['buy_address']
    commission = calculate_commission(amount)
    total = amount + commission
    
    summary = f"""
✅ ملخص طلب الشراء:

💰 المبلغ: {amount} USDT
📍 عنوان BEP20: {address}
💳 العملة: {currency}
💸 العمولة: {commission:.2f} $
📈 المبلغ الإجمالي: {total:.2f}

💳 عنوان شام كاش للدفع:
{SHAMCASH_ADDRESS}

📸 يرجى إرسال لقطة شاشة للتحويل إلى الدعم:
{SUPPORT_USERNAME}

⏳ سيتم إرسال USDT خلال دقائق من تأكيد الدفع.

⚠️ عند تحويل المبلغ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي
"""
    
    await update.message.reply_text(summary, reply_markup=get_main_keyboard())
    
    # إرسال التقرير للمجموعة
    user = update.effective_user
    report = format_transaction_report(
        user.id, user.username or user.first_name, 
        "شراء", amount, currency, address
    )
    
    try:
        await context.bot.send_message(REPORT_GROUP, report)
    except Exception as e:
        logger.error(f"خطأ في إرسال التقرير: {e}")
    
    return ConversationHandler.END

async def sell_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """بدء عملية بيع USDT"""
    user_id = update.effective_user.id
    
    # التحقق من الانضمام للمجموعة
    is_member = await check_group_membership(context, user_id)
    if not is_member:
        await update.message.reply_text("يجب عليك الانضمام للمجموعة أولاً. اضغط /start")
        return ConversationHandler.END
    
    await update.message.reply_text(
        "🔴 بيع USDT\n\n"
        "كم مبلغ USDT تريد بيعه؟\n"
        "مثال: 100"
    )
    
    return WAITING_FOR_SELL_AMOUNT

async def sell_amount_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام مبلغ البيع"""
    try:
        amount = float(update.message.text)
        if amount <= 0:
            await update.message.reply_text("يرجى إدخال مبلغ صحيح أكبر من الصفر.")
            return WAITING_FOR_SELL_AMOUNT
        
        context.user_data['sell_amount'] = amount
        commission = calculate_commission(amount)
        total = amount - commission
        
        await update.message.reply_text(
            f"💰 المبلغ: {amount} USDT\n"
            f"💸 العمولة: {commission:.2f} $\n"
            f"📉 المبلغ الذي ستستلمه: {total:.2f} $\n\n"
            "الآن أرسل عنوان شام كاش الخاص بك:"
        )
        
        return WAITING_FOR_SELL_ADDRESS
        
    except ValueError:
        await update.message.reply_text("يرجى إدخال رقم صحيح.")
        return WAITING_FOR_SELL_AMOUNT

async def sell_address_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام عنوان شام كاش للبيع"""
    address = update.message.text.strip()
    
    context.user_data['sell_address'] = address
    
    await update.message.reply_text(
        "اختر العملة التي تريد استلامها:",
        reply_markup=get_currency_keyboard()
    )
    
    return WAITING_FOR_SELL_CURRENCY

async def sell_currency_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """استلام اختيار العملة للبيع"""
    currency_text = update.message.text
    
    if "دولار" in currency_text:
        currency = "دولار أمريكي"
    elif "ليرة" in currency_text:
        currency = "ليرة سورية"
    else:
        await update.message.reply_text(
            "يرجى اختيار العملة من الأزرار المتاحة:",
            reply_markup=get_currency_keyboard()
        )
        return WAITING_FOR_SELL_CURRENCY
    
    context.user_data['sell_currency'] = currency
    
    # إنشاء ملخص الطلب
    amount = context.user_data['sell_amount']
    address = context.user_data['sell_address']
    commission = calculate_commission(amount)
    total = amount - commission
    
    summary = f"""
✅ ملخص طلب البيع:

💰 المبلغ: {amount} USDT
📍 عنوان شام كاش: {address}
💳 العملة: {currency}
💸 العمولة: {commission:.2f} $
📉 المبلغ الذي ستستلمه: {total:.2f}

💳 أرسل USDT إلى العنوان التالي (شبكة BEP20):
{USDT_ADDRESS}

📸 يرجى إرسال لقطة شاشة للتحويل إلى الدعم:
{SUPPORT_USERNAME}

⏳ سيتم إرسال الأموال خلال دقائق من تأكيد الاستلام.

⚠️ عند تحويل المبلغ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي
"""
    
    await update.message.reply_text(summary, reply_markup=get_main_keyboard())
    
    # إرسال التقرير للمجموعة
    user = update.effective_user
    report = format_transaction_report(
        user.id, user.username or user.first_name, 
        "بيع", amount, currency, address
    )
    
    try:
        await context.bot.send_message(REPORT_GROUP, report)
    except Exception as e:
        logger.error(f"خطأ في إرسال التقرير: {e}")
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """إلغاء المحادثة"""
    await update.message.reply_text(
        "تم إلغاء العملية.", 
        reply_markup=get_main_keyboard()
    )
    return ConversationHandler.END

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """معلومات البوت"""
    info_text = f"""
ℹ️ معلومات البوت

🤖 بوت تداول USDT عبر شام كاش

💰 الخدمات:
• شراء USDT بالليرة السورية أو الدولار
• بيع USDT واستلام الأموال عبر شام كاش

💸 العمولة: 1$ + 0.5% من المبلغ الإجمالي

🔒 الأمان:
• جميع المعاملات محمية
• دعم فني متاح 24/7

📞 للدعم: {SUPPORT_USERNAME}
👥 المجموعة: {GROUP_USERNAME}

⚠️ عند تحويل المبلغ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي
"""
    
    await update.message.reply_text(info_text)

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """إحصائيات الأدمن"""
    if update.effective_user.id != ADMIN_ID:
        return
    
    total_transactions = len(transactions)
    total_users = len(set(t["user_id"] for t in transactions))
    
    stats_text = f"""
📊 إحصائيات البوت

📈 إجمالي المعاملات: {total_transactions}
👥 عدد المستخدمين: {total_users}
🟢 عمليات الشراء اليوم: {daily_stats['buy_count']}
🔴 عمليات البيع اليوم: {daily_stats['sell_count']}
💰 إجمالي العمولات اليوم: {daily_stats['total_commission']:.2f} $

📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    await update.message.reply_text(stats_text)

async def admin_transactions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """عرض آخر المعاملات"""
    if update.effective_user.id != ADMIN_ID:
        return
    
    if not transactions:
        await update.message.reply_text("لا توجد معاملات حتى الآن.")
        return
    
    # عرض آخر 10 معاملات
    recent_transactions = transactions[-10:]
    
    text = "📋 آخر المعاملات:\n\n"
    
    for t in reversed(recent_transactions):
        text += f"""
🆔 #{t['id']} - {t['type']}
👤 @{t['username']} (ID: {t['user_id']})
💰 {t['amount']:.2f} USDT
💳 {t['currency']}
💸 عمولة: {t['commission']:.2f} $
🕐 {t['timestamp']}
{'─' * 30}
"""
    
    if len(text) > 4000:  # تقليل النص إذا كان طويلاً
        text = text[:4000] + "..."
    
    await update.message.reply_text(text)

async def admin_commissions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """تقرير العمولات"""
    if update.effective_user.id != ADMIN_ID:
        return
    
    if not transactions:
        await update.message.reply_text("لا توجد معاملات حتى الآن.")
        return
    
    total_commission = sum(t["commission"] for t in transactions)
    buy_commission = sum(t["commission"] for t in transactions if t["type"] == "شراء")
    sell_commission = sum(t["commission"] for t in transactions if t["type"] == "بيع")
    
    commission_text = f"""
💰 تقرير العمولات

📈 إجمالي العمولات: {total_commission:.2f} $
🟢 عمولات الشراء: {buy_commission:.2f} $
🔴 عمولات البيع: {sell_commission:.2f} $
📊 العمولات اليوم: {daily_stats['total_commission']:.2f} $

📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    await update.message.reply_text(commission_text)

async def admin_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """إحصائيات المستخدمين"""
    if update.effective_user.id != ADMIN_ID:
        return
    
    if not transactions:
        await update.message.reply_text("لا توجد معاملات حتى الآن.")
        return
    
    # تجميع إحصائيات المستخدمين
    user_stats = {}
    for t in transactions:
        user_id = t["user_id"]
        if user_id not in user_stats:
            user_stats[user_id] = {
                "username": t["username"],
                "buy_count": 0,
                "sell_count": 0,
                "total_amount": 0,
                "total_commission": 0
            }
        
        if t["type"] == "شراء":
            user_stats[user_id]["buy_count"] += 1
        else:
            user_stats[user_id]["sell_count"] += 1
        
        user_stats[user_id]["total_amount"] += t["amount"]
        user_stats[user_id]["total_commission"] += t["commission"]
    
    # ترتيب المستخدمين حسب إجمالي المبلغ
    sorted_users = sorted(user_stats.items(), key=lambda x: x[1]["total_amount"], reverse=True)
    
    text = f"👥 إحصائيات المستخدمين (أعلى {min(10, len(sorted_users))}):\n\n"
    
    for user_id, stats in sorted_users[:10]:
        text += f"""
👤 @{stats['username']} (ID: {user_id})
🟢 شراء: {stats['buy_count']} | 🔴 بيع: {stats['sell_count']}
💰 إجمالي: {stats['total_amount']:.2f} USDT
💸 عمولات: {stats['total_commission']:.2f} $
{'─' * 30}
"""
    
    if len(text) > 4000:
        text = text[:4000] + "..."
    
    await update.message.reply_text(text)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """معالج الرسائل النصية"""
    text = update.message.text
    user_id = update.effective_user.id
    
    # وظائف الأدمن
    if user_id == ADMIN_ID:
        if text == "📊 الإحصائيات":
            await admin_stats(update, context)
            return
        elif text == "📋 المعاملات":
            await admin_transactions(update, context)
            return
        elif text == "💰 العمولات":
            await admin_commissions(update, context)
            return
        elif text == "👥 المستخدمين":
            await admin_users(update, context)
            return
        elif text == "🔙 العودة للقائمة الرئيسية":
            await update.message.reply_text(
                "تم العودة للقائمة الرئيسية.",
                reply_markup=get_main_keyboard()
            )
            return
    
    # وظائف المستخدمين العاديين
    if text == "🟢 شراء USDT":
        await buy_usdt(update, context)
    elif text == "🔴 بيع USDT":
        await sell_usdt(update, context)
    elif text == "ℹ️ معلومات":
        await info(update, context)
    elif text == "📊 حالة الطلبات":
        await update.message.reply_text(
            "📊 حالة الطلبات\n\n"
            "لمتابعة حالة طلباتك، يرجى التواصل مع الدعم:\n"
            f"{SUPPORT_USERNAME}"
        )
    elif text == "🔙 القائمة الرئيسية":
        await update.message.reply_text(
            "تم العودة إلى القائمة الرئيسية.",
            reply_markup=get_main_keyboard()
        )
    else:
        await update.message.reply_text(
            "يرجى استخدام الأزرار المتاحة أو كتابة /start للبدء."
        )


def main():
    """تشغيل البوت"""
    # إنشاء التطبيق
    application = Application.builder().token(BOT_TOKEN).build()
    
    # معالج المحادثات للشراء
    buy_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🟢 شراء USDT$"), buy_usdt)],
        states={
            WAITING_FOR_BUY_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, buy_amount_received)],
            WAITING_FOR_BUY_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, buy_address_received)],
            WAITING_FOR_BUY_CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, buy_currency_received)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    # معالج المحادثات للبيع
    sell_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🔴 بيع USDT$"), sell_usdt)],
        states={
            WAITING_FOR_SELL_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, sell_amount_received)],
            WAITING_FOR_SELL_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, sell_address_received)],
            WAITING_FOR_SELL_CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, sell_currency_received)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    # إضافة المعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(buy_handler)
    application.add_handler(sell_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex("^🟢 شراء USDT$") & ~filters.Regex("^🔴 بيع USDT$") & ~filters.Regex("^💵 دولار أمريكي$") & ~filters.Regex("^🇸🇾 ليرة سورية$") & ~filters.Regex("^📊 الإحصائيات$") & ~filters.Regex("^📋 المعاملات$") & ~filters.Regex("^💰 العمولات$") & ~filters.Regex("^👥 المستخدمين$") & ~filters.Regex("^🔙 العودة للقائمة الرئيسية$"), handle_text))
    
    # تشغيل البوت
    print("🤖 البوت يعمل الآن...")
    application.run_polling()

if __name__ == '__main__':
    main()

