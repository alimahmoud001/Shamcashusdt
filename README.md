<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام بيع وشراء USDT - شام كاش</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --success-color: #27ae60;
            --warning-color: #f39c12;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
            padding: 0;
            margin: 0;
        }
        
        .container {
            max-width: 380px;
            margin: 0 auto;
            padding: 10px;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), #1a2530);
            color: white;
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        h1, h2, h3 {
            margin-bottom: 10px;
        }
        
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            padding: 15px;
            margin-bottom: 15px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: var(--dark-color);
            font-size: 14px;
        }
        
        input[type="text"],
        input[type="number"],
        input[type="email"],
        input[type="tel"],
        select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border 0.3s;
        }
        
        input:focus, select:focus {
            border-color: var(--secondary-color);
            outline: none;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }
        
        button {
            background: linear-gradient(135deg, var(--secondary-color), #2980b9);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: all 0.3s;
            font-weight: bold;
        }
        
        button:hover {
            background: linear-gradient(135deg, #2980b9, var(--secondary-color));
        }
        
        button:disabled {
            background: #cccccc;
            cursor: not-allowed;
        }
        
        .result {
            display: none;
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border-right: 4px solid var(--secondary-color);
            animation: fadeIn 0.5s ease-in;
        }
        
        .info-box {
            background-color: #e8f4fd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            border-right: 4px solid var(--secondary-color);
        }
        
        .address-box {
            background-color: #f9f9f9;
            padding: 12px;
            border-radius: 8px;
            margin: 10px 0;
            word-break: break-all;
            font-family: monospace;
            font-size: 12px;
            border: 1px dashed #ccc;
        }
        
        .tab {
            overflow: hidden;
            border: 1px solid #ccc;
            background-color: #f1f1f1;
            border-radius: 8px 8px 0 0;
            display: flex;
        }
        
        .tab button {
            background-color: inherit;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 12px;
            transition: 0.3s;
            color: var(--dark-color);
            flex: 1;
            font-size: 14px;
            font-weight: bold;
        }
        
        .tab button:hover {
            background-color: #ddd;
        }
        
        .tab button.active {
            background: linear-gradient(135deg, var(--secondary-color), #2980b9);
            color: white;
        }
        
        .tabcontent {
            display: none;
            padding: 15px;
            border: 1px solid #ccc;
            border-top: none;
            border-radius: 0 0 8px 8px;
            background-color: white;
        }
        
        footer {
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px;
            padding: 15px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }
        
        .telegram-link {
            color: var(--secondary-color);
            text-decoration: none;
            font-weight: bold;
        }
        
        .telegram-link:hover {
            text-decoration: underline;
        }
        
        .final-notice {
            margin-top: 15px;
            padding: 12px;
            background-color: #fff3cd;
            border-radius: 8px;
            border-right: 4px solid #ffc107;
            font-size: 14px;
            text-align: center;
        }
        
        .loader {
            display: none;
            border: 4px solid #f3f3f3;
            border-radius: 50%;
            border-top: 4px solid var(--secondary-color);
            width: 40px;
            height: 40px;
            margin: 15px auto;
            animation: spin 1s linear infinite;
        }
        
        .success-message {
            display: none;
            color: var(--success-color);
            text-align: center;
            margin-top: 12px;
            font-weight: bold;
            font-size: 14px;
        }
        
        .error-message {
            display: none;
            color: var(--accent-color);
            text-align: center;
            margin-top: 12px;
            font-weight: bold;
            font-size: 14px;
        }
        
        .timer-message {
            display: none;
            color: var(--warning-color);
            text-align: center;
            margin-top: 12px;
            font-weight: bold;
            font-size: 14px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .copy-btn {
            background: linear-gradient(135deg, #7d7d7d, #5d5d5d);
            padding: 8px;
            font-size: 12px;
            margin-top: 8px;
            width: auto;
            display: inline-block;
        }
        
        .user-info {
            display: grid;
            grid-template-columns: 1fr;
            gap: 15px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 8px;
            border-right: 4px solid #ddd;
        }
        
        /* تحسينات للجوال */
        @media (max-width: 480px) {
            .container {
                padding: 8px;
            }
            
            header {
                padding: 12px;
            }
            
            h1 {
                font-size: 18px;
            }
            
            .card {
                padding: 12px;
            }
            
            input[type="text"],
            input[type="number"],
            input[type="email"],
            input[type="tel"],
            select {
                padding: 10px;
                font-size: 14px;
            }
            
            button {
                padding: 12px;
                font-size: 14px;
            }
            
            .tab button {
                padding: 10px;
                font-size: 12px;
            }
            
            .address-box {
                font-size: 11px;
                padding: 10px;
            }
            
            .info-box {
                padding: 12px;
            }
            
            .user-info {
                grid-template-columns: 1fr;
                padding: 12px;
            }
        }
        
        @media (min-width: 768px) {
            .user-info {
                grid-template-columns: 1fr 1fr;
            }
            
            .user-info .form-group:last-child {
                grid-column: span 2;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-exchange-alt"></i> نظام بيع وشراء USDT عبر شام كاش</h1>
        </header>
        
        <div class="card">
            <div class="info-box">
                <h3><i class="fas fa-info-circle"></i> معلومات مهمة</h3>
                <p><i class="fas fa-dollar-sign"></i> سعر صرف الدولار: <strong>11000</strong> ليرة سورية</p>
                <p><i class="fas fa-percentage"></i> العمولة: 1$ + 0.5% من المبلغ الإجمالي</p>
            </div>
            
            <div class="user-info">
                <div class="form-group">
                    <label for="userName"><i class="fas fa-user"></i> الاسم الكامل:</label>
                    <input type="text" id="userName" required placeholder="أدخل اسمك الكامل">
                </div>
                
                <div class="form-group">
                    <label for="userPhone"><i class="fas fa-phone"></i> رقم الهاتف:</label>
                    <input type="tel" id="userPhone" required placeholder="أدخل رقم هاتفك">
                </div>
                
                <div class="form-group">
                    <label for="userEmail"><i class="fas fa-envelope"></i> البريد الإلكتروني:</label>
                    <input type="email" id="userEmail" required placeholder="أدخل بريدك الإلكتروني">
                </div>
            </div>
            
            <div class="tab">
                <button class="tablinks active" onclick="openTab(event, 'Buy')"><i class="fas fa-shopping-cart"></i> شراء USDT</button>
                <button class="tablinks" onclick="openTab(event, 'Sell')"><i class="fas fa-coins"></i> بيع USDT</button>
            </div>
            
            <div id="Buy" class="tabcontent" style="display: block;">
                <h3><i class="fas fa-shopping-cart"></i> شراء USDT</h3>
                <form id="buyForm">
                    <div class="form-group">
                        <label for="buyAmount"><i class="fas fa-money-bill-wave"></i> المبلغ المراد شراءه (USDT):</label>
                        <input type="number" id="buyAmount" step="0.01" min="1" required placeholder="أدخل المبلغ بالـ USDT">
                    </div>
                    
                    <div class="form-group">
                        <label for="networkAddress"><i class="fas fa-wallet"></i> عنوان الشبكة (BEP20 فقط):</label>
                        <input type="text" id="networkAddress" required placeholder="أدخل عنوان المحفظة BEP20">
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-money-check"></i> طريقة الدفع:</label>
                        <select id="buyCurrency">
                            <option value="usd">الدولار الأمريكي ($)</option>
                            <option value="syp">الليرة السورية (SYP)</option>
                        </select>
                    </div>
                    
                    <button type="submit"><i class="fas fa-calculator"></i> احسب المبلغ المستحق</button>
                </form>
                
                <div id="buyResult" class="result">
                    <h3><i class="fas fa-file-invoice-dollar"></i> تفاصيل عملية الشراء</h3>
                    <p>المبلغ المراد شراءه: <span id="resultBuyAmount"></span> USDT</p>
                    <p>العمولة: <span id="buyCommission"></span></p>
                    <p>المبلغ الإجمالي المستحق: <span id="totalBuyAmount"></span></p>
                    
                    <div class="info-box">
                        <p><i class="fas fa-info-circle"></i> يرجى تحويل المبلغ إلى عنوان شام كاش التالي:</p>
                        <div class="address-box">be456e0ea9392db4d68a7093ee317bc8</div>
                        <button class="copy-btn" onclick="copyToClipboard('be456e0ea9392db4d68a7093ee317bc8')"><i class="fas fa-copy"></i> نسخ العنوان</button>
                        
                        <p style="margin-top: 12px;">
                            <i class="fas fa-comment"></i> بعد التحويل، يرجى إرسال صورة لقطة الشاشة إلى الدعم على Telegram: 
                            <a href="https://t.me/ali0619000" class="telegram-link" target="_blank">@ali0619000</a>
                        </p>
                    </div>
                    
                    <button id="sendBuyButton" onclick="sendToTelegram('buy')" style="margin-top: 12px; background: linear-gradient(135deg, #0088cc, #005c8a);">
                        <i class="fab fa-telegram"></i> إرسال الطلب إلى Telegram
                    </button>
                </div>
            </div>
            
            <div id="Sell" class="tabcontent">
                <h3><i class="fas fa-coins"></i> بيع USDT</h3>
                <form id="sellForm">
                    <div class="form-group">
                        <label for="sellAmount"><i class="fas fa-money-bill-wave"></i> المبلغ المراد بيعه (USDT):</label>
                        <input type="number" id="sellAmount" step="0.01" min="1" required placeholder="أدخل المبلغ بالـ USDT">
                    </div>
                    
                    <div class="form-group">
                        <label for="shamCashAddress"><i class="fas fa-wallet"></i> عنوان شام كاش الخاص بك:</label>
                        <input type="text" id="shamCashAddress" required placeholder="أدخل عنوان شام كاش">
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-money-check"></i> طريقة الاستلام:</label>
                        <select id="receiveCurrency">
                            <option value="syp">الليرة السورية (SYP)</option>
                            <option value="usd">الدولار الأمريكي ($)</option>
                        </select>
                    </div>
                    
                    <button type="submit"><i class="fas fa-calculator"></i> احسب المبلغ المستلم</button>
                </form>
                
                <div id="sellResult" class="result">
                    <h3><i class="fas fa-file-invoice-dollar"></i> تفاصيل عملية البيع</h3>
                    <p>المبلغ المراد بيعه: <span id="resultSellAmount"></span> USDT</p>
                    <p>العمولة: <span id="sellCommission"></span></p>
                    <p>المبلغ الإجمالي المستلم: <span id="totalSellAmount"></span></p>
                    
                    <div class="info-box">
                        <p><i class="fas fa-info-circle"></i> يرجى تحويل USDT إلى العنوان التالي:</p>
                        <div class="address-box">0x2F1A184B6abBb49De547D539eDC3b5eAdc3E01F9</div>
                        <button class="copy-btn" onclick="copyToClipboard('0x2F1A184B6abBb49De547D539eDC3b5eAdc3E01F9')"><i class="fas fa-copy"></i> نسخ العنوان</button>
                        
                        <p style="margin-top: 12px;">
                            <i class="fas fa-comment"></i> بعد التحويل، يرجى إرسال صورة لقطة الشاشة إلى الدعم على Telegram: 
                            <a href="https://t.me/ali0619000" class="telegram-link" target="_blank">@ali0619000</a>
                        </p>
                        <p><i class="fas fa-clock"></i> سيتم إرسال المبلغ خلال عدة دقائق بعد التأكد من التحويل.</p>
                    </div>
                    
                    <button id="sendSellButton" onclick="sendToTelegram('sell')" style="margin-top: 12px; background: linear-gradient(135deg, #0088cc, #005c8a);">
                        <i class="fab fa-telegram"></i> إرسال الطلب إلى Telegram
                    </button>
                </div>
            </div>
        </div>
        
        <div class="final-notice">
            <i class="fas fa-exclamation-circle"></i> عند تحويل المبلغ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي.
        </div>
        
        <div class="loader" id="loader"></div>
        <div class="success-message" id="successMessage">
            <i class="fas fa-check-circle"></i> تم إرسال الطلب بنجاح إلى المجموعة!
        </div>
        
        <div class="error-message" id="errorMessage">
            <i class="fas fa-exclamation-triangle"></i> حدث خطأ في الإرسال. يرجى المحاولة مرة أخرى.
        </div>
        
        <div class="timer-message" id="timerMessage">
            <i class="fas fa-clock"></i> يجب الانتظار <span id="countdown">10:00</span> دقائق قبل إرسال طلب جديد.
        </div>
        
        <footer>
            <p><i class="fas fa-headset"></i> لأي استفسار، يرجى التواصل مع الدعم على Telegram: <a href="https://t.me/ali0619000" class="telegram-link" target="_blank">@ali0619000</a></p>
            <p><i class="fab fa-telegram"></i> سيتم إرسال التفاصيل إلى مجموعة Telegram: <a href="https://t.me/shamcashusdt1" class="telegram-link" target="_blank">@shamcashusdt1</a></p>
        </footer>
    </div>

    <script>
        // سعر الصرف الثابت
        const exchangeRate = 11000; // 1 USD = 11000 SYP
        const botToken = "8126453870:AAHKpVDTFA5R5SHcYQVldkNlQp83PKlxeio";
        const chatId = "@shamcashusdt1"; // مجموعة التلجرام
        const cooldownPeriod = 10 * 60 * 1000; // 10 دقائق بالميلي ثانية
        
        // فتح التبويبات
        function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
        }
        
        // حساب العمولة
        function calculateCommission(amount) {
            const fixedFee = 1; // 1$ ثابت
            const percentageFee = 0.005; // 0.5%
            return fixedFee + (amount * percentageFee);
        }
        
        // نسخ النص إلى الحافظة
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                alert("تم نسخ العنوان: " + text);
            }, function() {
                // Fallback for older browsers
                const textArea = document.createElement("textarea");
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert("تم نسخ العنوان: " + text);
            });
        }
        
        // التحقق من صحة البريد الإلكتروني
        function isValidEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }
        
        // التحقق من صحة رقم الهاتف
        function isValidPhone(phone) {
            const re = /^[+\d][\d\s\-()]{8,}$/;
            return re.test(phone);
        }
        
        // التحقق من إمكانية الإرسال (عدم تجاوز المهلة)
        function canSendMessage() {
            const lastSendTime = localStorage.getItem('lastSendTime');
            if (!lastSendTime) return true;
            
            const currentTime = new Date().getTime();
            return (currentTime - parseInt(lastSendTime)) > cooldownPeriod;
        }
        
        // تحديث وقت الإرسال الأخير
        function updateLastSendTime() {
            localStorage.setItem('lastSendTime', new Date().getTime());
        }
        
        // عرض مؤقت العد التنازلي
        function showCooldownTimer() {
            const lastSendTime = localStorage.getItem('lastSendTime');
            if (!lastSendTime) return;
            
            const timerMessage = document.getElementById('timerMessage');
            const countdownElement = document.getElementById('countdown');
            timerMessage.style.display = 'block';
            
            const interval = setInterval(() => {
                const currentTime = new Date().getTime();
                const elapsedTime = currentTime - parseInt(lastSendTime);
                const remainingTime = cooldownPeriod - elapsedTime;
                
                if (remainingTime <= 0) {
                    clearInterval(interval);
                    timerMessage.style.display = 'none';
                    document.getElementById('sendBuyButton').disabled = false;
                    document.getElementById('sendSellButton').disabled = false;
                    return;
                }
                
                const minutes = Math.floor(remainingTime / 60000);
                const seconds = Math.floor((remainingTime % 60000) / 1000);
                countdownElement.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
                
                // تعطيل أزرار الإرسال أثناء الانتظار
                document.getElementById('sendBuyButton').disabled = true;
                document.getElementById('sendSellButton').disabled = true;
            }, 1000);
        }
        
        // معالجة نموذج الشراء
        document.getElementById('buyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // التحقق من صحة البيانات المدخلة
            const userName = document.getElementById('userName').value;
            const userPhone = document.getElementById('userPhone').value;
            const userEmail = document.getElementById('userEmail').value;
            
            if (!userName || !userPhone || !userEmail) {
                alert('يرجى ملء جميع الحقول الشخصية');
                return;
            }
            
            if (!isValidPhone(userPhone)) {
                alert('يرجى إدخال رقم هاتف صحيح');
                return;
            }
            
            if (!isValidEmail(userEmail)) {
                alert('يرجى إدخال بريد إلكتروني صحيح');
                return;
            }
            
            const amount = parseFloat(document.getElementById('buyAmount').value);
            const currency = document.getElementById('buyCurrency').value;
            const address = document.getElementById('networkAddress').value;
            const commission = calculateCommission(amount);
            
            let totalAmount;
            let commissionText;
            let totalText;
            
            if (currency === 'usd') {
                totalAmount = amount + commission;
                commissionText = commission.toFixed(2) + " $";
                totalText = totalAmount.toFixed(2) + " $";
            } else {
                totalAmount = (amount + commission) * exchangeRate;
                commissionText = (commission * exchangeRate).toFixed(0) + " SYP (" + commission.toFixed(2) + " $)";
                totalText = totalAmount.toFixed(0) + " SYP";
            }
            
            document.getElementById('resultBuyAmount').textContent = amount.toFixed(2);
            document.getElementById('buyCommission').textContent = commissionText;
            document.getElementById('totalBuyAmount').textContent = totalText;
            document.getElementById('buyResult').style.display = 'block';
            
            // حفظ البيانات في localStorage لإرسالها لاحقًا
            const transactionData = {
                type: 'شراء',
                amount: amount,
                currency: currency,
                address: address,
                commission: commission,
                total: totalAmount,
                userName: userName,
                userPhone: userPhone,
                userEmail: userEmail,
                timestamp: new Date().toLocaleString()
            };
            localStorage.setItem('currentTransaction', JSON.stringify(transactionData));
            
            // التحقق من إمكانية الإرسال
            if (!canSendMessage()) {
                showCooldownTimer();
            }
        });
        
        // معالجة نموذج البيع
        document.getElementById('sellForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // التحقق من صحة البيانات المدخلة
            const userName = document.getElementById('userName').value;
            const userPhone = document.getElementById('userPhone').value;
            const userEmail = document.getElementById('userEmail').value;
            
            if (!userName || !userPhone || !userEmail) {
                alert('يرجى ملء جميع الحقول الشخصية');
                return;
            }
            
            if (!isValidPhone(userPhone)) {
                alert('يرجى إدخال رقم هاتف صحيح');
                return;
            }
            
            if (!isValidEmail(userEmail)) {
                alert('يرجى إدخال بريد إلكتروني صحيح');
                return;
            }
            
            const amount = parseFloat(document.getElementById('sellAmount').value);
            const currency = document.getElementById('receiveCurrency').value;
            const address = document.getElementById('shamCashAddress').value;
            const commission = calculateCommission(amount);
            
            let netAmount;
            let commissionText;
            let totalText;
            
            if (currency === 'usd') {
                netAmount = amount - commission;
                commissionText = commission.toFixed(2) + " $";
                totalText = netAmount.toFixed(2) + " $";
            } else {
                netAmount = (amount - commission) * exchangeRate;
                commissionText = (commission * exchangeRate).toFixed(0) + " SYP (" + commission.toFixed(2) + " $)";
                totalText = netAmount.toFixed(0) + " SYP";
            }
            
            document.getElementById('resultSellAmount').textContent = amount.toFixed(2);
            document.getElementById('sellCommission').textContent = commissionText;
            document.getElementById('totalSellAmount').textContent = totalText;
            document.getElementById('sellResult').style.display = 'block';
            
            // حفظ البيانات في localStorage لإرسالها لاحقًا
            const transactionData = {
                type: 'بيع',
                amount: amount,
                currency: currency,
                address: address,
                commission: commission,
                total: netAmount,
                userName: userName,
                userPhone: userPhone,
                userEmail: userEmail,
                timestamp: new Date().toLocaleString()
            };
            localStorage.setItem('currentTransaction', JSON.stringify(transactionData));
            
            // التحقق من إمكانية الإرسال
            if (!canSendMessage()) {
                showCooldownTimer();
            }
        });
        
        // إرسال البيانات إلى Telegram باستخدام التوكن المباشر
        async function sendToTelegram(type) {
            // التحقق من إمكانية الإرسال
            if (!canSendMessage()) {
                showCooldownTimer();
                return;
            }
            
            const transactionData = JSON.parse(localStorage.getItem('currentTransaction'));
            if (!transactionData) {
                alert('لا يوجد بيانات لإرسالها. يرجى تعبئة النموذج أولاً.');
                return;
            }
            
            // التحقق من صحة البيانات المدخلة
            const userName = document.getElementById('userName').value;
            const userPhone = document.getElementById('userPhone').value;
            const userEmail = document.getElementById('userEmail').value;
            
            if (!userName || !userPhone || !userEmail) {
                alert('يرجى ملء جميع الحقول الشخصية');
                return;
            }
            
            if (!isValidPhone(userPhone)) {
                alert('يرجى إدخال رقم هاتف صحيح');
                return;
            }
            
            if (!isValidEmail(userEmail)) {
                alert('يرجى إدخال بريد إلكتروني صحيح');
                return;
            }
            
            // عرض تحميل
            document.getElementById('loader').style.display = 'block';
            document.getElementById('successMessage').style.display = 'none';
            document.getElementById('errorMessage').style.display = 'none';
            document.getElementById('timerMessage').style.display = 'none';
            
            // نص الرسالة
            let message = `*طلب ${transactionData.type} USDT عبر شام كاش*%0A%0A`;
            message += `*الاسم:* ${userName}%0A`;
            message += `*الهاتف:* ${userPhone}%0A`;
            message += `*البريد الإلكتروني:* ${userEmail}%0A`;
            message += `*نوع المعاملة:* ${transactionData.type}%0A`;
            message += `*المبلغ:* ${transactionData.amount} USDT%0A`;
            message += `*طريقة الدفع/الاستلام:* ${transactionData.currency === 'usd' ? 'دولار أمريكي' : 'ليرة سورية'}%0A`;
            message += `*العمولة:* ${transactionData.commission.toFixed(2)} $%0A`;
            message += `*المبلغ الإجمالي:* ${transactionData.total} ${transactionData.currency === 'usd' ? '$' : 'ليرة سورية'}%0A`;
            message += `*العنوان:* ${transactionData.address}%0A`;
            message += `*الوقت:* ${transactionData.timestamp}%0A%0A`;
            message += `*لأي اسفسار التواصل مع الدعم @ali0619000.`;
            
            try {
                // إرسال الطلب إلى مجموعة التلجرام باستخدام API
                const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatId}&text=${message}&parse_mode=Markdown`);
                const data = await response.json();
                
                if (data.ok) {
                    document.getElementById('loader').style.display = 'none';
                    document.getElementById('successMessage').style.display = 'block';
                    updateLastSendTime();
                    showCooldownTimer();
                } else {
                    throw new Error('فشل في الإرسال');
                }
            } catch (error) {
                document.getElementById('loader').style.display = 'none';
                document.getElementById('errorMessage').style.display = 'block';
                console.error('Error sending to Telegram:', error);
                
                // فتح رابط التلجرام مع نص الرسالة كحل بديل
                window.open(`https://t.me/share/url?url=&text=${message}`, '_blank');
            }
        }
        
        // التحقق من وقت الإرسال الأخير عند تحميل الصفحة
        window.addEventListener('load', function() {
            if (!canSendMessage()) {
                showCooldownTimer();
            }
        });
    </script>
</body>
</html>
