/* Video formats shown in the gallery and the detail overlay.
   These describe the kinds of videos Abdelrhman makes — they are not client work. */
(function (YH) {
'use strict';
YH.PROJECTS = [
  {
    id: 'review', idx: '01',
    title: { en: 'Product review', ar: 'ريفيو للمنتج' },
    cat: { en: 'Format · TikTok, Reels, Shorts', ar: 'نوع الفيديو · تيك توك، ريلز، شورتس' },
    lead: {
      en: 'An honest, first-person take on your product: what it is, how it feels in real use, and why it\'s worth buying. The most trusted kind of UGC.',
      ar: 'رأي صادق من تجربة شخصية: المنتج إيه، إحساسه في الاستخدام الحقيقي، وليه يستاهل يتشترى. أكتر نوع UGC الناس بتثق فيه.',
    },
    best: { en: 'New products, launches', ar: 'المنتجات الجديدة والإطلاقات' },
    steps: {
      en: ['Hook — a bold first line that stops the scroll', 'Show — the product in my hands, up close', 'Proof — what I liked, honestly', 'CTA — where to get it'],
      ar: ['الهوك — جملة أولى قوية توقف السكرول', 'العرض — المنتج في إيدي وبالتفاصيل', 'الإثبات — اللي عجبني بصراحة', 'الدعوة — منين يشتروه'],
    },
    great: { en: ['Skincare', 'Gadgets', 'Food & drinks', 'Fashion', 'Apps'], ar: ['العناية بالبشرة', 'الأجهزة', 'الأكل والمشروبات', 'الموضة', 'التطبيقات'] },
    wa: { en: 'Hi Abdelrhman! I want a product review video.', ar: 'أهلاً عبدالرحمن! عايز فيديو ريفيو لمنتجي.' },
  },
  {
    id: 'unboxing', idx: '02',
    title: { en: 'Unboxing', ar: 'أنبوكسينج' },
    cat: { en: 'Format · First impressions', ar: 'نوع الفيديو · أول انطباع' },
    lead: {
      en: 'The excitement of opening it for the first time — the packaging, the details and a genuine first reaction that makes people want their own.',
      ar: 'حماس الفتح لأول مرة — التغليف والتفاصيل ورد فعل حقيقي يخلي الناس عايزة واحد زيه.',
    },
    best: { en: 'Premium packaging, gift items', ar: 'التغليف المميز والهدايا' },
    steps: {
      en: ['Hook — the box, and a reason to keep watching', 'Open — slow reveal of the packaging', 'React — real first impressions', 'CTA — where to get it'],
      ar: ['الهوك — العلبة وسبب يكمّل عشانه', 'الفتح — كشف التغليف بهدوء', 'رد الفعل — أول انطباع حقيقي', 'الدعوة — منين يشتروه'],
    },
    great: { en: ['Beauty boxes', 'Accessories', 'Electronics', 'Gifts'], ar: ['بوكسات التجميل', 'الإكسسوارات', 'الإلكترونيات', 'الهدايا'] },
    wa: { en: 'Hi Abdelrhman! I want an unboxing video.', ar: 'أهلاً عبدالرحمن! عايز فيديو أنبوكسينج.' },
  },
  {
    id: 'problem', idx: '03',
    title: { en: 'Problem → solution', ar: 'مشكلة ← حل' },
    cat: { en: 'Format · Hook-driven', ar: 'نوع الفيديو · بيعتمد على الهوك' },
    lead: {
      en: 'Start with a pain your customer already knows, then show your product fixing it. Simple, direct and made for ads.',
      ar: 'نبدأ بمشكلة العميل عارفها كويس، وبعدين نوري منتجك وهو بيحلها. بسيط ومباشر ومعمول للإعلانات.',
    },
    best: { en: 'Paid ads, problem-solving products', ar: 'الإعلانات الممولة والمنتجات اللي بتحل مشكلة' },
    steps: {
      en: ['Hook — "Do you also struggle with…?"', 'Problem — show the frustration', 'Solution — your product in action', 'Result + CTA'],
      ar: ['الهوك — "إنت كمان بتعاني من…؟"', 'المشكلة — نوري الإحباط', 'الحل — منتجك وهو شغال', 'النتيجة + الدعوة'],
    },
    great: { en: ['Home & cleaning', 'Health', 'Tech', 'Services'], ar: ['البيت والتنظيف', 'الصحة', 'التكنولوجيا', 'الخدمات'] },
    wa: { en: 'Hi Abdelrhman! I want a problem → solution video.', ar: 'أهلاً عبدالرحمن! عايز فيديو مشكلة وحل.' },
  },
  {
    id: 'testimonial', idx: '04',
    title: { en: 'Testimonial style', ar: 'تيستيمونيال' },
    cat: { en: 'Format · Talking head', ar: 'نوع الفيديو · كلام للكاميرا' },
    lead: {
      en: 'Straight to camera, like a real customer telling a friend why they love it. Warm, believable and great for retargeting.',
      ar: 'كلام مباشر للكاميرا، كأنه عميل حقيقي بيحكي لصاحبه ليه بيحب المنتج. دافي ومُقنع وممتاز لإعادة الاستهداف.',
    },
    best: { en: 'Building trust, retargeting ads', ar: 'بناء الثقة وإعلانات إعادة الاستهداف' },
    steps: {
      en: ['Hook — a personal opener', 'Story — before vs. after using it', 'Why it works — in plain words', 'CTA — recommend it'],
      ar: ['الهوك — بداية شخصية', 'الحكاية — قبل وبعد الاستخدام', 'ليه بينفع — بكلام بسيط', 'الدعوة — ترشيح المنتج'],
    },
    great: { en: ['Online stores', 'Courses', 'Restaurants', 'Brands'], ar: ['المتاجر الإلكترونية', 'الكورسات', 'المطاعم', 'البراندات'] },
    wa: { en: 'Hi Abdelrhman! I want a testimonial-style video.', ar: 'أهلاً عبدالرحمن! عايز فيديو تيستيمونيال.' },
  },
  {
    id: 'howto', idx: '05',
    title: { en: 'How-to / tutorial', ar: 'طريقة الاستخدام' },
    cat: { en: 'Format · Step by step', ar: 'نوع الفيديو · خطوة بخطوة' },
    lead: {
      en: 'Show people exactly how to use it in a few simple steps — so buying feels easy and obvious.',
      ar: 'نوري الناس بالظبط إزاي يستخدموه في كام خطوة بسيطة — عشان قرار الشراء يبقى سهل وواضح.',
    },
    best: { en: 'Products that need a demo', ar: 'المنتجات اللي محتاجة شرح' },
    steps: {
      en: ['Hook — the result first', 'Step 1, 2, 3 — clear and quick', 'Tip — the detail people miss', 'CTA — try it yourself'],
      ar: ['الهوك — النتيجة الأول', 'خطوة 1، 2، 3 — واضحة وسريعة', 'نصيحة — التفصيلة اللي الناس بتنساها', 'الدعوة — جرّبه بنفسك'],
    },
    great: { en: ['Beauty', 'Kitchen', 'Apps', 'Tools'], ar: ['التجميل', 'المطبخ', 'التطبيقات', 'الأدوات'] },
    wa: { en: 'Hi Abdelrhman! I want a how-to video.', ar: 'أهلاً عبدالرحمن! عايز فيديو طريقة استخدام.' },
  },
  {
    id: 'lifestyle', idx: '06',
    title: { en: 'Lifestyle', ar: 'لايف ستايل' },
    cat: { en: 'Format · Day in the life', ar: 'نوع الفيديو · يوم في حياتي' },
    lead: {
      en: 'Your product as a natural part of a real day — the most native-feeling kind of ad, made to blend into the feed.',
      ar: 'منتجك كجزء طبيعي من يوم حقيقي — أكتر نوع إعلان بيبان طبيعي وبيندمج مع الفيد.',
    },
    best: { en: 'Brand awareness, organic content', ar: 'الانتشار والمحتوى العضوي' },
    steps: {
      en: ['Hook — a relatable moment', 'Routine — the day unfolds', 'Product moment — naturally in frame', 'CTA — soft and friendly'],
      ar: ['الهوك — لحظة قريبة من الناس', 'الروتين — اليوم بيتحكي', 'لحظة المنتج — بشكل طبيعي في الكادر', 'الدعوة — خفيفة وودودة'],
    },
    great: { en: ['Drinks', 'Fashion', 'Fitness', 'Cafés'], ar: ['المشروبات', 'الموضة', 'الرياضة', 'الكافيهات'] },
    wa: { en: 'Hi Abdelrhman! I want a lifestyle video.', ar: 'أهلاً عبدالرحمن! عايز فيديو لايف ستايل.' },
  },
];
})(window.YH = window.YH || {});
