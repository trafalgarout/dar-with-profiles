/* ai-tools/tools-logic.js */

const datasets = {
    usernames: ["المغامر", "الذكي", "الفنان", "الملك", "الأسطورة", "البرنس", "الصقر", "النجم", "البطل", "المبدع"],
    hobbies: ["الرسم", "الرياضة", "السفر", "القراءة", "التصوير", "الطبخ", "البرمجة", "الألعاب", "الموسيقى", "التصميم"],
    businessPrefixes: ["مؤسسة", "شركة", "مجموعة", "مكتب", "مركز", "وكالة", "ستوديو", "بيت", "رواد", "نخبة"],
    businessSuffixes: ["للابتكار", "للحلول", "التقنية", "العالمية", "الحديثة", "المتطورة", "الإبداعية", "المستدامة", "المتميزة", "الأولى"],
    hashtags: ["#ذكاء_اصطناعي", "#تقنية", "#أدوات_مجانية", "#تطوير_الذات", "#ريادة_أعمال", "#تسويق_رقمي", "#إبداع", "#نجاح", "#عمل_حر", "#تطوير_مواقع"],
    startupIndustries: ["التعليم", "الصحة", "التجارة الإلكترونية", "النقل", "السياحة", "الفن", "العقارات", "الزراعة", "الطاقة", "الأمن السيبراني"],
};

const generators = {
    username: (name, hobby) => {
        const randomSuffix = Math.floor(Math.random() * 9999);
        const prefix = name || datasets.usernames[Math.floor(Math.random() * datasets.usernames.length)];
        const suffix = hobby || datasets.hobbies[Math.floor(Math.random() * datasets.hobbies.length)];
        return [`${prefix}_${suffix}_${randomSuffix}`, `${suffix}_${prefix}`, `${prefix}99`, `The_${prefix}`];
    },
    businessName: (keyword) => {
        const results = [];
        for (let i = 0; i < 5; i++) {
            const p = datasets.businessPrefixes[Math.floor(Math.random() * datasets.businessPrefixes.length)];
            const s = datasets.businessSuffixes[Math.floor(Math.random() * datasets.businessSuffixes.length)];
            results.push(`${p} ${keyword || "المستقبل"} ${s}`);
        }
        return results;
    },
    instagramBio: (job, hobby) => {
        return [
            `✨ ${job || "شخص مبدع"} | 🎨 محب لـ ${hobby || "الحياة"}\n📍 دبي | 🏹 أطمح للأفضل\n📩 للتواصل عبر الخاص`,
            `🚀 شغوف بالـ ${hobby || "تطوير"}\n💼 ${job || "رائد أعمال"}\n⭐ عش حياتك كما تحب`,
            `🌙 ${job || "فنان"}\n🌊 هدوء وسلام\n✨ ${hobby || "القراءة"} هي عالمي`
        ];
    },
    hashtags: (topic) => {
        let results = [...datasets.hashtags];
        if (topic) results = results.map(h => `#${topic}_${h.substring(1)}`);
        return results.slice(0, 10);
    },
    password: (length = 12) => {
        const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
        let retVal = "";
        for (let i = 0, n = charset.length; i < length; ++i) {
            retVal += charset.charAt(Math.floor(Math.random() * n));
        }
        return [retVal];
    },
    startupIdea: (industry) => {
        const ind = industry || datasets.startupIndustries[Math.floor(Math.random() * datasets.startupIndustries.length)];
        return [
            `منصة تعتمد على الذكاء الاصطناعي لتطوير ${ind}`,
            `تطبيق موبايل يسهل عمليات ${ind} للأفراد`,
            `شركة ناشئة متخصصة في حلول ${ind} المستدامة`,
            `أداة سحابية لإدارة مشاريع ${ind}`
        ];
    },
    studyPlan: (days, subject) => {
        const plan = [];
        for (let i = 1; i <= parseInt(days || 5); i++) {
            plan.push(`اليوم ${i}: مراجعة أساسيات ${subject || "المادة"} والتركيز على القسم ${i}`);
        }
        return plan;
    },
    blogTitle: (topic) => {
        return [
            `أفضل 10 نصائح للنجاح في ${topic || "مجالك"}`,
            `كيف تبدأ رحلتك في ${topic || "هذا المجال"} من الصفر`,
            `دليلك الشامل لـ ${topic || "تعلم مهارة جديدة"} في 2026`,
            `أسرار لا يعرفها الكثيرون عن ${topic || "هذا الموضوع"}`
        ];
    },
    youtubeTitle: (topic) => {
        return [
            `تجربتي مع ${topic || "هذا الشيء"} (لن تصدق النتيجة!)`,
            `كيف تربح من ${topic || "اليوتيوب"} في 5 خطوات فقط`,
            `أفضل فيديو عن ${topic || "هذا الموضوع"} ستشاهده اليوم`,
            `لماذا فشل الجميع في ${topic || "هذا التحدي"}؟`
        ];
    },
    resumeSummary: (job) => {
        return [
            `${job || "محترف"} طموح يمتلك خبرة واسعة في إدارة المشاريع وتحقيق النتائج المرجوة.`,
            `خبير في ${job || "هذا المجال"} يسعى للانضمام لفريق عمل مبدع للمساهمة في تحقيق أهداف الشركة.`,
            `${job || "مختص"} شغوف بالتعلم المستمر وتطوير المهارات القيادية والتقنية.`
        ];
    }
};

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert("تم النسخ بنجاح!");
    });
}

function displayResults(results) {
    const container = document.getElementById("results");
    container.innerHTML = "";
    results.forEach(res => {
        const div = document.createElement("div");
        div.className = "result-item";
        div.innerHTML = `
            <span>${res}</span>
            <button class="copy-btn" onclick="copyToClipboard('${res}')">نسخ</button>
        `;
        container.appendChild(div);
    });
}
