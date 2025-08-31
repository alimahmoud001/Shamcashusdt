
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام تحويل العملات الرقمية في سورية</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #1a365d;
            --secondary: #2c5282;
            --accent: #38a169;
            --light: #f7fafc;
            --dark: #1a202c;
            --danger: #e53e3e;
            --warning: #dd6b20;
            --light-blue: #e3f2fd;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Tajawal', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #f0f4f8, #d6e4f0);
            color: var(--dark);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.7;
        }
        
        .container {
            max-width: 280px;
            margin: 2 auto;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.18);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            padding: 30px 25px;
            text-align: center;
            position: relative;
        }
        
        header h1 {
            font-size: 2.1rem;
            margin-bottom: 12px;
            font-weight: 700; /* زيادة سمك خط العنوان */
            letter-spacing: -0.5px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        header p {
            font-size: 1.1rem;
            opacity: 0.9;
            font-weight: 500; /* زيادة سمك خط الوصف */
        }
        
        .logo {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 18px;
            margin-bottom: 15px;
        }
        
        .logo i {
            font-size: 3rem;
            background: rgba(255, 255, 255, 0.15);
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .form-container {
            padding: 30px;
        }
        
        .section {
            margin-bottom: 35px;
            padding-bottom: 25px;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .section-title {
            font-size: 1.5rem;
            color: var(--primary);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 15px;
            font-weight: 700; /* زيادة سمك خط العنوان */
            padding-bottom: 10px;
            border-bottom: 2px solid var(--light-blue);
        }
        
        .section-title i {
            background-color: #ebf8ff;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-size: 1.3rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.08);
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: 600; /* زيادة سمك خط التسميات */
            color: var(--dark);
            font-size: 1.05rem;
        }
        
        input, select, textarea {
            width: 100%;
            padding: 15px;
            border: 1px solid #cbd5e0;
            border-radius: 10px;
            font-size: 1.05rem;
            transition: all 0.3s;
            background-color: #f7fafc;
            font-weight: 500; /* زيادة سمك خط الإدخال */
        }
        
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--secondary);
            box-shadow: 0 0 0 4px rgba(66, 153, 225, 0.2);
            background-color: white;
        }
        
        .radio-group {
            display: flex;
            flex-wrap: wrap;
            gap: 18px;
            margin-top: 10px;
        }
        
        .radio-option {
            flex: 1;
            min-width: 140px;
        }
        
        .radio-option input {
            display: none;
        }
        
        .radio-option label {
            display: block;
            padding: 18px 15px;
            border: 2px solid #cbd5e0;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            background-color: #f7fafc;
            font-size: 1.1rem;
            font-weight: 600; /* زيادة سمك خط الخيارات */
        }
        
        .radio-option input:checked + label {
            border-color: var(--accent);
            background-color: #e6fffa;
            font-weight: 700; /* زيادة سمك الخط عند التحديد */
            box-shadow: 0 4px 10px rgba(56, 161, 105, 0.15);
            transform: translateY(-3px);
        }
        
        .info-box {
            background-color: #ebf8ff;
            border-left: 5px solid var(--secondary);
            padding: 20px;
            border-radius: 10px;
            margin-top: 25px;
            display: none;
        }
        
        .info-box.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }
        
        .info-box p {
            margin-bottom: 12px;
            line-height: 1.7;
            font-size: 1.05rem;
            font-weight: 500; /* زيادة سمك خط المعلومات */
        }
        
        .copy-field {
            background-color: white;
            border: 1px solid #cbd5e0;
            border-radius: 10px;
            padding: 14px;
            margin: 12px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .copy-field span {
            font-family: 'Courier New', monospace;
            word-break: break-all;
            font-size: 1.05rem;
            font-weight: 500; /* زيادة سمك خط النص القابل للنسخ */
        }
        
        .copy-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
            font-weight: 600; /* زيادة سمك نص زر النسخ */
            font-size: 1rem;
            min-width: 90px;
        }
        
        .copy-btn:hover {
            background: var(--secondary);
            transform: translateY(-2px);
            box-shadow: 0 3px 8px rgba(0,0,0,0.15);
        }
        
        .btn {
            display: block;
            width: 100%;
            padding: 18px;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.15rem;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 25px;
            font-weight: 700; /* زيادة سمك نص الأزرار */
            letter-spacing: 0.5px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.15);
        }
        
        .review-btn {
            background: linear-gradient(to right, var(--warning), #e67e22);
        }
        
        .submit-btn {
            background: linear-gradient(to right, var(--accent), #2ecc71);
            display: none;
        }
        
        .btn:hover {
            opacity: 0.95;
            transform: translateY(-3px);
            box-shadow: 0 7px 18px rgba(0,0,0,0.2);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .summary {
            display: none;
            background: #f0f7ff;
            border-radius: 12px;
            padding: 25px;
            margin-top: 25px;
            border: 2px solid #c5defa;
        }
        
        .summary-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 18px;
            padding-bottom: 18px;
            border-bottom: 1px dashed #cbd5e0;
            font-size: 1.1rem;
            font-weight: 500; /* زيادة سمك خط العناصر */
        }
        
        .summary-item span:first-child {
            font-weight: 600; /* زيادة سمك نص التصنيفات */
            color: var(--primary);
        }
        
        .summary-item:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
            font-weight: 700; /* زيادة سمك خط المجموع */
            font-size: 1.3rem;
            color: var(--primary);
            margin-top: 10px;
            padding-top: 10px;
            border-top: 2px dashed #cbd5e0;
        }
        
        .success-message {
            text-align: center;
            padding: 40px 30px;
            display: none;
            background: #f8fff8;
            border-radius: 12px;
            border: 2px solid #c5fad5;
            margin-top: 20px;
        }
        
        .success-message i {
            font-size: 4.5rem;
            color: var(--accent);
            margin-bottom: 25px;
        }
        
        .success-message h2 {
            color: var(--accent);
            margin-bottom: 25px;
            font-size: 2.2rem;
            font-weight: 800; /* زيادة سمك خط عنوان النجاح */
        }
        
        .success-message p {
            font-size: 1.15rem;
            margin-bottom: 25px;
            font-weight: 500; /* زيادة سمك خط النص */
            line-height: 1.8;
        }
        
        .fee-info {
            background: #fff8e1;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid var(--warning);
            font-size: 1.1rem;
            font-weight: 600; /* زيادة سمك خط معلومات العمولة */
            box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        }
        
        .fee-info i {
            color: var(--warning);
            margin-left: 8px;
        }
        
        #finalSummary {
            background: white;
            padding: 25px;
            border-radius: 12px;
            text-align: right;
            border: 1px solid #e2e8f0;
            margin-top: 20px;
            font-size: 1.1rem;
        }
        
        #finalSummary p {
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
            font-weight: 500; /* زيادة سمك خط الملخص النهائي */
        }
        
        #finalSummary p:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        
        #finalSummary strong {
            font-weight: 700; /* زيادة سمك الخط للكلمات البارزة */
            color: var(--primary);
            min-width: 160px;
            display: inline-block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @media (max-width: 768px) {
            .radio-group {
                flex-direction: column;
            }
            
            .radio-option {
                min-width: 100%;
            }
            
            .container {
                border-radius: 12px;
            }
            
            header {
                padding: 25px 20px;
            }
            
            header h1 {
                font-size: 1.8rem;
            }
            
            .form-container {
                padding: 20px;
            }
            
            .section-title {
                font-size: 1.35rem;
            }
            
            .btn {
                padding: 16px;
                font-size: 1.1rem;
            }
        }
    
        
        @media (max-width: 380px) {
            body {
                padding: 10px;
            }
            
            header {
                padding: 20px 15px;
            }
            
            header h1 {
                font-size: 1.6rem;
            }
            
            .logo i {
                width: 65px;
                height: 65px;
                font-size: 2.5rem;
            }
            
            .form-container {
                padding: 15px;
            }
            
            .section-title {
                font-size: 1.25rem;
            }
            
            .copy-btn {
                padding: 8px 12px;
                font-size: 0.9rem;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800&display=swap" rel="stylesheet">
   
         
</head>
<body>
    
    <div class="container">
        <header>
            <div class="logo">
                <i class="fas fa-coins"></i>
                <div>
                    <h1>نظام تحويل العملات الرقمية في سورية</h1>
                    <p>تحويل USDT بوسائل الدفع المحلية</p>
                </div>
            </div>
        </header>
        
        <div class="form-container">
            <div class="section">
                <h2 class="section-title"><i class="fas fa-user"></i> المعلومات الشخصية</h2>
                <div class="form-group">
                    <label for="fullname">الاسم الثلاثي</label>
                    <input type="text" id="fullname" placeholder="الاسم الكامل">
                </div>
                
                <div class="form-group">
                    <label for="phone">رقم الهاتف</label>
                    <input type="tel" id="phone" placeholder="09xxxxxxxx">
                </div>
                
                <div class="form-group">
                    <label for="city">المدينة</label>
                    <input type="text" id="city" placeholder="المدينة">
                </div>
            </div>
            
            <div class="fee-info">
                <i class="fas fa-info-circle"></i>
                <strong>نظام العمولة المحدث:</strong> 1 دولار ثابت + 0.5% من المبلغ الكامل
            </div>
            
            <div class="section">
                <h2 class="section-title"><i class="fas fa-exchange-alt"></i> نوع العملية</h2>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" id="buy" name="transactionType" value="buy" checked>
                        <label for="buy">شراء USDT</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" id="sell" name="transactionType" value="sell">
                        <label for="sell">بيع USDT</label>
                    </div>
                </div>
            </div>
            
            <!-- Buy Section -->
            <div id="buySection">
                <div class="section">
                    <h2 class="section-title"><i class="fas fa-shopping-cart"></i> تفاصيل الشراء</h2>
                    
                    <div class="form-group">
                        <label for="buyAmount">الكمية المطلوبة (USDT)</label>
                        <input type="number" id="buyAmount" placeholder="أدخل الكمية">
                    </div>
                    
                    <div class="form-group">
                        <label for="buyNetwork">اختر الشبكة</label>
                        <select id="buyNetwork">
                            <option value="bep20">BEP20</option>
                            <option value="trc20">TRC20</option>
                            <option value="erc20">ERC20</option>
                            <option value="binance">Binance Pay</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="buyAddress">العنوان (لإرسال USDT)</label>
                        <input type="text" id="buyAddress" placeholder="أدخل عنوان المحفظة">
                    </div>
                    
                    <div class="form-group">
                        <label for="buyNotes">ملاحظات (اختياري)</label>
                        <textarea id="buyNotes" rows="2" placeholder="أي ملاحظات إضافية"></textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="paymentMethod">طريقة الدفع</label>
                        <select id="paymentMethod">
                            <option value="">اختر طريقة الدفع</option>
                            <option value="sham">شام كاش</option>
                            <option value="syriatel">سيريتل كاش</option>
                            <option value="hawala">حوالة الهرم</option>
                            <option value="bimo">بنك بيمو</option>
                        </select>
                    </div>
                    
                    <div class="info-box" id="shamInfo">
                        <p>الدفع عبر شام كاش:</p>
                        <div class="copy-field">
                            <span>be456e0ea9392db4d68a7093ee317bc8</span>
                            <button class="copy-btn" data-clipboard-text="be456e0ea9392db4d68a7093ee317bc8">نسخ</button>
                        </div>
                        <p>رقم الحساب: 5991161126028260</p>
                    </div>
                    
                    <div class="info-box" id="syriatelInfo">
                        <p>الدفع عبر سيريتل كاش:</p>
                        <div class="copy-field">
                            <span>0934598967</span>
                            <button class="copy-btn" data-clipboard-text="0934598967">نسخ</button>
                        </div>
                    </div>
                    
                    <div class="info-box" id="hawalaInfo">
                        <p>الدفع عبر حوالة الهرم:</p>
                        <p>الاسم: علي ابراهيم محمود</p>
                        <p>رقم الهاتف: 0934598967</p>
                        <p>المدينة: اللاذقية</p>
                    </div>
                    
                    <div class="info-box" id="bimoInfo">
                        <p>الدفع عبر بنك بيمو:</p>
                        <div class="copy-field">
                            <span>060104947910013000000</span>
                            <button class="copy-btn" data-clipboard-text="060104947910013000000">نسخ</button>
                        </div>
                        <p>الاسم: علي ابراهيم محمود</p>
                    </div>
                </div>
            </div>
            
            <!-- Sell Section -->
            <div id="sellSection" style="display: none;">
                <div class="section">
                    <h2 class="section-title"><i class="fas fa-money-bill-wave"></i> تفاصيل البيع</h2>
                    
                    <div class="form-group">
                        <label for="sellAmount">الكمية المعروضة (USDT)</label>
                        <input type="number" id="sellAmount" placeholder="أدخل الكمية">
                    </div>
                    
                    <div class="form-group">
                        <label for="receiveMethod">طريقة الاستلام</label>
                        <select id="receiveMethod">
                            <option value="">اختر طريقة الاستلام</option>
                            <option value="syriatel">سيريتل كاش</option>
                            <option value="hawala">حوالة الهرم</option>
                            <option value="bimo">بنك بيمو</option>
                            <option value="sham">شام كاش</option>
                        </select>
                    </div>
                    
                    <div class="form-group" id="bimoAccountGroup" style="display: none;">
                        <label for="bimoAccount">رقم الحساب البنكي</label>
                        <input type="text" id="bimoAccount" placeholder="رقم الحساب">
                    </div>
                    
                    <div class="form-group" id="shamAccountGroup" style="display: none;">
                        <label for="shamAccount">رقم الحساب أو العنوان</label>
                        <input type="text" id="shamAccount" placeholder="رقم الحساب أو العنوان">
                    </div>
                    
                    <div class="form-group">
                        <label for="sellNotes">ملاحظات (اختياري)</label>
                        <textarea id="sellNotes" rows="2" placeholder="أي ملاحظات إضافية"></textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="sellNetwork">اختر الشبكة</label>
                        <select id="sellNetwork">
                            <option value="">اختر شبكة الاستلام</option>
                            <option value="bep20">BEP20</option>
                            <option value="trc20">TRC20</option>
                            <option value="erc20">ERC20</option>
                            <option value="binance">Binance Pay</option>
                        </select>
                    </div>
                    
                    <div class="info-box" id="bep20Info">
                        <p>العنوان BEP20:</p>
                        <div class="copy-field">
                            <span>0x21802218d8d661d66F2C7959347a6382E1cc614F</span>
                            <button class="copy-btn" data-clipboard-text="0x21802218d8d661d66F2C7959347a6382E1cc614F">نسخ</button>
                        </div>
                    </div>
                    
                    <div class="info-box" id="trc20Info">
                        <p>العنوان TRC20:</p>
                        <div class="copy-field">
                            <span>TD2LoErPRkVPBxDk72ZErtiyi6agirZQjX</span>
                            <button class="copy-btn" data-clipboard-text="TD2LoErPRkVPBxDk72ZErtiyi6agirZQjX">نسخ</button>
                        </div>
                    </div>
                    
                    <div class="info-box" id="erc20Info">
                        <p>العنوان ERC20:</p>
                        <div class="copy-field">
                            <span>0x21802218d8d661d66F2C7959347a6382E1cc614F</span>
                            <button class="copy-btn" data-clipboard-text="0x21802218d8d661d66F2C7959347a6382E1cc614F">نسخ</button>
                        </div>
                    </div>
                    
                    <div class="info-box" id="binanceInfo">
                        <p>Binance Pay:</p>
                        <div class="copy-field">
                            <span>969755964</span>
                            <button class="copy-btn" data-clipboard-text="969755964">نسخ</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <button id="reviewBtn" class="btn review-btn">مراجعة الطلب</button>
            
            <div class="summary" id="summarySection">
                <h2 class="section-title"><i class="fas fa-file-invoice"></i> ملخص الطلب</h2>
                <div class="summary-item">
                    <span>الاسم:</span>
                    <span id="summaryName"></span>
                </div>
                <div class="summary-item">
                    <span>رقم الهاتف:</span>
                    <span id="summaryPhone"></span>
                </div>
                <div class="summary-item">
                    <span>نوع العملية:</span>
                    <span id="summaryType"></span>
                </div>
                <div class="summary-item">
                    <span>الكمية (USDT):</span>
                    <span id="summaryAmount"></span>
                </div>
                <div class="summary-item">
                    <span>عمولة التحويل (1 دولار + 0.5%):</span>
                    <span id="summaryFee"></span>
                </div>
                <div class="summary-item">
                    <span>عمولة الشبكة:</span>
                    <span id="summaryNetworkFee"></span>
                </div>
                <div class="summary-item">
                    <span>المبلغ الإجمالي (SYP):</span>
                    <span id="summaryTotal"></span>
                </div>
                <div class="summary-item">
                    <span>ملاحظات:</span>
                    <span id="summaryNotes"></span>
                </div>
                <p style="margin-top: 20px; padding: 15px; background: #fff8f8; border-radius: 8px; font-weight: 600;">
                    <i class="fas fa-info-circle"></i> عمولة التسديد على طرق التحويل المختلفة بالليرة السورية تقع على المستخدم كما تحددها هذه الجهات
                </p>
            </div>
            
            <button id="submitBtn" class="btn submit-btn">إرسال الطلب</button>
            
            <div class="success-message" id="successMessage">
                <i class="fas fa-check-circle"></i>
                <h2>تم إرسال الطلب بنجاح!</h2>
                <p>تم إرسال تفاصيل طلبك إلى بريدنا الإلكتروني وسنتواصل معك قريبًا.</p>
                <p>تفاصيل الطلب:</p>
                <div id="finalSummary"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Constants
        const EXCHANGE_RATE = 9850; // SYP per USD
        const NETWORK_FEES = {
            'bep20': 0.15,
            'trc20': 2,
            'erc20': 0.3,
            'binance': 0
        };
        
        // DOM Elements
        const buySection = document.getElementById('buySection');
        const sellSection = document.getElementById('sellSection');
        const transactionTypeRadios = document.querySelectorAll('input[name="transactionType"]');
        const paymentMethod = document.getElementById('paymentMethod');
        const receiveMethod = document.getElementById('receiveMethod');
        const reviewBtn = document.getElementById('reviewBtn');
        const submitBtn = document.getElementById('submitBtn');
        const summarySection = document.getElementById('summarySection');
        const successMessage = document.getElementById('successMessage');
        
        // Toggle sections based on transaction type
        transactionTypeRadios.forEach(radio => {
            radio.addEventListener('change', () => {
                if (radio.value === 'buy') {
                    buySection.style.display = 'block';
                    sellSection.style.display = 'none';
                } else {
                    buySection.style.display = 'none';
                    sellSection.style.display = 'block';
                }
            });
        });
        
        // Show payment info based on selected method
        paymentMethod.addEventListener('change', () => {
            // Hide all info boxes first
            document.querySelectorAll('#buySection .info-box').forEach(box => {
                box.classList.remove('active');
            });
            
            // Show selected info box
            if (paymentMethod.value === 'sham') {
                document.getElementById('shamInfo').classList.add('active');
            } else if (paymentMethod.value === 'syriatel') {
                document.getElementById('syriatelInfo').classList.add('active');
            } else if (paymentMethod.value === 'hawala') {
                document.getElementById('hawalaInfo').classList.add('active');
            } else if (paymentMethod.value === 'bimo') {
                document.getElementById('bimoInfo').classList.add('active');
            }
        });
        
        // Show account fields for sell section
        receiveMethod.addEventListener('change', () => {
            document.getElementById('bimoAccountGroup').style.display = 'none';
            document.getElementById('shamAccountGroup').style.display = 'none';
            
            if (receiveMethod.value === 'bimo') {
                document.getElementById('bimoAccountGroup').style.display = 'block';
            } else if (receiveMethod.value === 'sham') {
                document.getElementById('shamAccountGroup').style.display = 'block';
            }
        });
        
        // Show network info for sell section
        document.getElementById('sellNetwork').addEventListener('change', function() {
            // Hide all info boxes first
            document.querySelectorAll('#sellSection .info-box').forEach(box => {
                box.classList.remove('active');
            });
            
            // Show selected info box
            if (this.value === 'bep20') {
                document.getElementById('bep20Info').classList.add('active');
            } else if (this.value === 'trc20') {
                document.getElementById('trc20Info').classList.add('active');
            } else if (this.value === 'erc20') {
                document.getElementById('erc20Info').classList.add('active');
            } else if (this.value === 'binance') {
                document.getElementById('binanceInfo').classList.add('active');
            }
        });
        
        // Copy functionality
        document.querySelectorAll('.copy-btn').forEach(button => {
            button.addEventListener('click', function() {
                const text = this.getAttribute('data-clipboard-text');
                navigator.clipboard.writeText(text).then(() => {
                    const originalText = this.textContent;
                    this.textContent = 'تم النسخ!';
                    setTimeout(() => {
                        this.textContent = originalText;
                    }, 2000);
                });
            });
        });
        
        // Calculate fees with new structure: $1 + 0.5% of total amount
        function calculateFees(amount, network) {
            // العمولة الجديدة: 1 دولار ثابت + 0.5% من المبلغ
            const transactionFee = 1 + (amount * 0.005);
            
            const networkFee = NETWORK_FEES[network] || 0;
            const totalFeeUSD = transactionFee + networkFee;
            const totalFeeSYP = totalFeeUSD * EXCHANGE_RATE;
            
            return {
                transactionFee,
                networkFee,
                totalFeeUSD,
                totalFeeSYP
            };
        }
        
        // Review button handler
        reviewBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get basic user info
            const fullName = document.getElementById('fullname').value;
            const phone = document.getElementById('phone').value;
            const city = document.getElementById('city').value;
            
            // Validate required fields
            if (!fullName || !phone || !city) {
                alert('الرجاء ملء جميع الحقول الإلزامية');
                return;
            }
            
            const transactionType = document.querySelector('input[name="transactionType"]:checked').value;
            
            // Transaction specific data
            let amount, network, notes;
            let methodDetails = '';
            
            if (transactionType === 'buy') {
                amount = parseFloat(document.getElementById('buyAmount').value);
                network = document.getElementById('buyNetwork').value;
                notes = document.getElementById('buyNotes').value;
                const method = document.getElementById('paymentMethod').value;
                
                if (!amount || amount <= 0 || !network || !method) {
                    alert('الرجاء ملء جميع الحقول الإلزامية في قسم الشراء');
                    return;
                }
                
                // Get method details
                switch(method) {
                    case 'sham':
                        methodDetails = 'شام كاش: be456e0ea9392db4d68a7093ee317bc8';
                        break;
                    case 'syriatel':
                        methodDetails = 'سيريتل كاش: 0934598967';
                        break;
                    case 'hawala':
                        methodDetails = 'حوالة الهرم: علي ابراهيم محمود - 0934598967 - اللاذقية';
                        break;
                    case 'bimo':
                        methodDetails = 'بنك بيمو: 060104947910013000000';
                        break;
                }
            } else {
                amount = parseFloat(document.getElementById('sellAmount').value);
                network = document.getElementById('sellNetwork').value;
                notes = document.getElementById('sellNotes').value;
                const method = document.getElementById('receiveMethod').value;
                
                if (!amount || amount <= 0 || !network || !method) {
                    alert('الرجاء ملء جميع الحقول الإلزامية في قسم البيع');
                    return;
                }
                
                // Get method details
                let accountInfo = '';
                if (method === 'bimo') {
                    accountInfo = document.getElementById('bimoAccount').value;
                } else if (method === 'sham') {
                    accountInfo = document.getElementById('shamAccount').value;
                }
                
                switch(method) {
                    case 'syriatel':
                        methodDetails = 'سيريتل كاش: ' + phone;
                        break;
                    case 'hawala':
                        methodDetails = 'حوالة الهرم: ' + fullName + ' - ' + phone + ' - ' + city;
                        break;
                    case 'bimo':
                        methodDetails = 'بنك بيمو: ' + accountInfo;
                        break;
                    case 'sham':
                        methodDetails = 'شام كاش: ' + accountInfo;
                        break;
                }
            }
            
            // Calculate fees
            const fees = calculateFees(amount, network);
            const totalAmountSYP = transactionType === 'buy' ? 
                (amount + fees.totalFeeUSD) * EXCHANGE_RATE : 
                (amount - fees.totalFeeUSD) * EXCHANGE_RATE;
            
            // Update summary
            document.getElementById('summaryName').textContent = fullName;
            document.getElementById('summaryPhone').textContent = phone;
            document.getElementById('summaryType').textContent = transactionType === 'buy' ? 'شراء' : 'بيع';
            document.getElementById('summaryAmount').textContent = amount + ' USDT';
            document.getElementById('summaryFee').textContent = fees.transactionFee.toFixed(2) + ' USD (' + (fees.transactionFee * EXCHANGE_RATE).toLocaleString() + ' SYP)';
            document.getElementById('summaryNetworkFee').textContent = fees.networkFee.toFixed(2) + ' USD (' + (fees.networkFee * EXCHANGE_RATE).toLocaleString() + ' SYP)';
            document.getElementById('summaryTotal').textContent = totalAmountSYP.toLocaleString() + ' SYP';
            document.getElementById('summaryNotes').textContent = notes || 'لا يوجد';
            
            // Store data for submission
            window.transactionData = {
                fullName,
                phone,
                city,
                transactionType,
                amount,
                network,
                notes,
                methodDetails,
                fees,
                totalAmountSYP
            };
            
            // Show summary and submit button
            summarySection.style.display = 'block';
            submitBtn.style.display = 'block';
            reviewBtn.style.display = 'none';
            
            // Scroll to summary
            summarySection.scrollIntoView({ behavior: 'smooth' });
        });
        
        // Submit button handler
        submitBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            const data = window.transactionData;
            
            // Prepare final summary for email
            const finalSummary = `
                <p><strong>الاسم:</strong> ${data.fullName}</p>
                <p><strong>رقم الهاتف:</strong> ${data.phone}</p>
                <p><strong>المدينة:</strong> ${data.city}</p>
                <p><strong>نوع العملية:</strong> ${data.transactionType === 'buy' ? 'شراء' : 'بيع'}</p>
                <p><strong>الكمية:</strong> ${data.amount} USDT</p>
                <p><strong>عمولة التحويل:</strong> ${data.fees.transactionFee.toFixed(2)} USD</p>
                <p><strong>عمولة الشبكة:</strong> ${data.fees.networkFee.toFixed(2)} USD</p>
                <p><strong>المبلغ الإجمالي:</strong> ${data.totalAmountSYP.toLocaleString()} SYP</p>
                <p><strong>تفاصيل الدفع/الاستلام:</strong> ${data.methodDetails}</p>
                <p><strong>ملاحظات:</strong> ${data.notes || 'لا يوجد'}</p>
            `;
            
            document.getElementById('finalSummary').innerHTML = finalSummary;
            
            // Prepare email content
            const subject = `طلب جديد: ${data.transactionType === 'buy' ? 'شراء' : 'بيع'} USDT`;
            const body = `تفاصيل الطلب الجديد:%0D%0A%0D%0A${finalSummary.replace(/<[^>]*>/g, '')}`;
            
            // Show success message
            summarySection.style.display = 'none';
            submitBtn.style.display = 'none';
            successMessage.style.display = 'block';
            
            // Create mailto link
            const mailtoLink = `mailto:alimahmoud001a@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            
            // Open email client
            window.location.href = mailtoLink;
        });
    </script>
</body>
</html>
