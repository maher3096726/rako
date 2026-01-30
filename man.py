from flet import *


def main(page:Page):
    page.window.width = 390
    page.window.height = 740
    page.window.top = 1
    page.window.left = 1290  
    page.title = "maher ahmed"
    is_national_id_valid = False
    def rout_change(e):
        nonlocal is_national_id_valid
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Text("\n \n"),
                    Row(
                        [
                        Image(
                        src='Secure login.gif',
                        width=350,
                        height=300)
                        ],alignment='center'),
                    Text("اهلاً بكم في تطبيقنا لتقديم افضل الخدمات لطلاب المعهد العالي للعلوم الإدارية ببلقاس \n",
                        width=390,
                        text_align='center',
                        weight='bold',
                        size=16,
                        color='black'
                        ),
                    Row([
                        ElevatedButton(
                        "تسجيل البيانات",
                        on_click=lambda _:page.go('/login'),
                        style=ButtonStyle(color='black',bgcolor='red',shape=RoundedRectangleBorder(radius=5)),
                        width=150,
                        tooltip='اضغط هنا لتسجيل بيانات الطالب'
                    ),
                        ElevatedButton(
                        'عرض معلومات المعهد',
                        on_click=lambda _:page.go('/sersh'),
                        style=ButtonStyle(color='black',bgcolor='red',shape=RoundedRectangleBorder(radius=5)),
                        width=150,
                        tooltip='اضغط هنا لعرض معلومات المعهد'
                    ),
                        ],alignment='center',
                        spacing=50,
                        ),
                    ElevatedButton(
                        'لــوكــيــشــن الــمــعــهــد',
                        on_click=lambda e:page.go('/location'),
                        style=ButtonStyle(color='black',bgcolor='red',shape=RoundedRectangleBorder(radius=5)),
                        width=200,
                        tooltip='اضغط هنا لعرض عنوان المعهد',
                        ),
                    AppBar(
                        title=Text('المعهد العالي للعلوم الإدارية ببلقاس',
                                   text_align='center',
                                   width=390,
                                   weight='bold'
                                   ),
                        color='black',
                        bgcolor='red',
                    )
                ],
                bgcolor='white'
            )
        )
        
        if page.route == '/login':
            # ... [الكود السابق لصفحة login يبقى كما هو] ...
            def validate_national_id(e):
                nonlocal is_national_id_valid
                national_id = e.control.value
                if national_id:
                    if len(national_id) != 14:
                        e.control.error_text = "الرقم القومي يجب أن يكون 14 رقمًا"
                        is_national_id_valid = False
                    elif not national_id.isdigit():
                        e.control.error_text = "الرقم القومي يجب أن يحتوي على أرقام فقط"
                        is_national_id_valid = False
                    else:
                        e.control.error_text = None
                        is_national_id_valid = True
                else:
                    e.control.error_text = "الرجاء إدخال الرقم القومي"
                    is_national_id_valid = False
                page.update()
            
            page.views.append(
            View(
                "/login",
                [
                    AppBar(
                        title=Text('المعهد العالي للعلوم الإدارية ببلقاس',weight='bold'),
                        color='black',
                        bgcolor='blue',
                        
                    ),
                    Text(""),
                    Text('الرجاء إدخال بيانات الطالب للتأكد من ظهور اسم المعهد في التنسيق',
                        width=390,
                        text_align='center',
                        size=20,
                        color='black'
                        ),
                    Text(''),
                    TextField(
                        label='اسم الطالب',
                        icon=Icons.PERSON_ADD_ALT_1,
                        color='black'
                        ),
                    Text(''' '''),
                    Row([TextField(
                        label='رقم الجلوس',
                        icon=Icons.PERSON,
                        color='black',
                        width=170
                        ),
                    TextField(
                        label='الرقم السري',
                        icon=Icons.LOCK,
                        width=185,
                        password=True,
                        can_reveal_password=True,
                        color='black'
                        )
                    ]),
                    Text(''' '''),
                    TextField(
                        label='الرقم القومي',
                        icon=Icons.BADGE,
                        password=True,
                        can_request_focus=True,
                        color='black',
                        keyboard_type=KeyboardType.NUMBER,
                        on_change=validate_national_id,
                        ),
                    Text(''),
                    Row([
                    ElevatedButton(
                        'ارسال البيانات',
                        on_click=lambda _: send_data(),
                        color='black',
                        bgcolor='blue',
                        width=150,
                        style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),
                    ),
                    ElevatedButton(
                        'اظهار البيانات',
                        color='black',
                        bgcolor='blue',
                        width=150,
                        style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)),
                    )],
                        alignment='center',
                        spacing=50,
                        )
                ],
                bgcolor='white'
            )
            )
            
            # دالة إرسال البيانات مع الشرط
            def send_data():
                if not is_national_id_valid:
                    # إظهار رسالة خطأ إذا كان الرقم القومي غير صالح
                    show_error_dialog("خطأ في الرقم القومي", "الرجاء إدخال رقم قومي صحيح (14 رقمًا فقط)")
                else:
                    page.go('/next')
            
            # دالة لعرض رسالة خطأ
            def show_error_dialog(title, message):
                def close_dlg(e):
                    dlg.open = False
                    page.update()
                
                dlg = AlertDialog(
                    title=Text(title),
                    content=Text(message),
                    actions=[
                        TextButton("موافق", on_click=close_dlg)
                    ]
                )
                
                page.dialog = dlg
                dlg.open = True
                page.update()
        if page.route == '/next':
            page.views.append(
            View(
                "/next",
                [
                    AppBar(
                        title=Text('المعهد العالي للعلوم الإدارية ببلقاس',weight='bold'),
                        color='black',
                        bgcolor='red',
                        
                    ),
                ]
            )
        )
        
        if page.route == '/sersh':
            # دالة لعرض/إخفاء الإجابة
            def toggle_answer(e):
                # إنشاء نافذة منبثقة لعرض الإجابة
                def close_dlg(e):
                    dlg.open = False
                    page.update()
                
                dlg = AlertDialog(
                    title=Text(e.control.data["question"]),
                    content=Container(
                        content=ListView(
                            controls=[
                                Text(e.control.data["answer"], size=16, text_align='center')
                            ],
                            height=200,
                            width=350
                        ),
                        padding=20,
                    ),
                    actions=[
                        TextButton("إغلاق", on_click=close_dlg)
                    ],
                    actions_alignment=MainAxisAlignment.END
                )
                
                page.dialog = dlg
                dlg.open = True
                page.update()
            
            # إنشاء واجهة الأسئلة الشائعة يدوياً بدون for loop
            faq_list = ListView(
                expand=True,
                spacing=10,
                padding=20
            )
            
            # إضافة كل سؤال يدوياً
            # 1. سؤال عن المعهد
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("عن المعهد", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "عن المعهد",
                            "answer": "المعهد العالي للعلوم الإدارية ببلقاس هو معهد متخصص في العلوم الإدارية والتجارية، يهدف إلى إعداد كوادر إدارية مؤهلة لسوق العمل."
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 2. سؤال الرؤية
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("الرؤية", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "الرؤية",
                            "answer": "الريادة في التعليم الإداري والمساهمة في تنمية المجتمع من خلال تخريج كوادر إدارية متميزة."
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 3. سؤال الرسالة
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("الرسالة", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "الرسالة",
                            "answer": "تقديم تعليم عالي الجودة في المجالات الإدارية، وتعزيز البحث العلمي، وخدمة المجتمع المحلي."
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 4. سؤال الأقسام
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("الأقسام", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "الأقسام",
                            "answer": ". قسم إدارة الأعمال\n2. قسم المحاسبة\n3. قسم نظم المعلومات الإدارية\n4."
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 5. سؤال الدرجات العلمية
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("الدرجات العلمية", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "الدرجات العلمية",
                            "answer": "• دبلوم إدارة أعمال\n• بكالوريوس في العلوم الإدارية\n• دورات تدريبية متخصصة"
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 6. سؤال مدة الدراسة
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("مدة الدراسة", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "مدة الدراسة",
                            "answer": "4 سنوات للحصول على درجة البكالوريوس في التخصصات المختلفة."
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 7. سؤال شروط القبول
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("شروط القبول", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "شروط القبول",
                            "answer": "• شهادة الثانوية العامة\n• اجتياز اختبار القبول\n• تقديم الأوراق المطلوبة"
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            # 8. سؤال الأنشطة الطلابية
            faq_list.controls.append(
                Container(
                    content=ElevatedButton(
                        content=Row([
                            Icon(Icons.INFO_OUTLINE, color='white'),
                            Text("الأنشطة الطلابية", 
                                 size=18, 
                                 weight='bold',
                                 color='white',
                                 expand=True,
                                 text_align='center')
                        ]),
                        on_click=toggle_answer,
                        data={
                            "question": "الأنشطة الطلابية",
                            "answer": "• نادي رياضي\n• نادي ثقافي\n• أنشطة تطوعية\n• ورش عمل تدريبية"
                        },
                        style=ButtonStyle(
                            bgcolor='blue',
                            shape=RoundedRectangleBorder(radius=10),
                            padding=15
                        ),
                        width=350
                    ),
                    margin=margin.only(bottom=10)
                )
            )
            
            page.views.append(
                View(
                    "/sersh",
                    [
                        AppBar(
                            title=Text('معلومات المعهد', weight='bold', size=20),
                            bgcolor='blue',
                            center_title=True,
                        ),
                        Container(
                            content=Column([
                                Container(
                                    content=Text(
                                        "المعهد العالي للعلوم الإدارية ببلقاس",
                                        size=22,
                                        weight='bold',
                                        color='blue',
                                        text_align='center'
                                    ),
                                    padding=padding.only(top=20, bottom=10),
                                    alignment=alignment.center
                                ),
                                Container(
                                    content=Text(
                                        "مرحباً بكم في صفحة معلومات المعهد",
                                        size=18,
                                        color='black',
                                        text_align='center'
                                    ),
                                    padding=padding.only(bottom=20)
                                ),
                                Divider(height=1, color='gray'),
                                Container(
                                    content=Text(
                                        "الأسئلة الشائعة",
                                        size=20,
                                        weight='bold',
                                        color='red',
                                        width=390,
                                        text_align='center'
                                    ),
                                    padding=padding.only(top=15, bottom=15)
                                ),
                                Container(
                                    content=faq_list,
                                    height=400,
                                    border=border.all(1, 'gray'),
                                    border_radius=10,
                                    padding=10
                                ),
                                Container(
                                    content=ElevatedButton(
                                        "العودة للصفحة الرئيسية",
                                        icon=Icons.HOME,
                                        on_click=lambda _: page.go('/'),
                                        style=ButtonStyle(
                                            bgcolor='green',
                                            color='white',
                                            shape=RoundedRectangleBorder(radius=8)
                                        ),
                                        width=200
                                    ),
                                    padding=padding.only(top=20),
                                    alignment=alignment.center
                                )
                            ], scroll='adaptive'),
                            padding=15,
                            expand=True
                        )
                    ],
                    bgcolor='white'
                )
            )
        
        if page.route == '/location':
            page.views.append(
                View(
                    "/location",
                    [
                        AppBar(
                            title=Text('موقع المعهد', weight='bold'),
                            bgcolor='green',
                            center_title=True,
                        ),
                        Container(
                            content=Column([
                                Container(
                                    content=Text(
                                        "عنوان المعهد:",
                                        size=22,
                                        weight='bold',
                                        color='green',
                                        text_align='center'
                                    ),
                                    padding=padding.only(top=20, bottom=10)
                                ),
                                Container(
                                    content=Text(
                                        "المعهد العالي للعلوم الإدارية\nبلقاس - محافظة الدقهلية\nجمهورية مصر العربية",
                                        size=18,
                                        text_align='center',
                                        weight='bold'
                                    ),
                                    padding=padding.only(bottom=20)
                                ),
                                Container(
                                    content=Icon(
                                        Icons.LOCATION_ON,
                                        size=100,
                                        color='red'
                                    ),
                                    padding=padding.only(bottom=20),
                                    alignment=alignment.center
                                ),
                                Container(
                                    content=Text(
                                        "للوصول إلى المعهد:\nيمكنك استخدام خرائط جوجل\nأو وسائل النقل العام المتاحة",
                                        size=16,
                                        text_align='center',
                                        color='gray'
                                    ),
                                    padding=padding.only(bottom=20)
                                ),
                                Container(
                                    content=ElevatedButton(
                                        "فتح خرائط جوجل",
                                        icon=Icons.MAP,
                                        on_click=lambda _: page.launch_url("https://www.google.com/maps/place/%D8%A7%D9%84%D9%85%D8%B9%D9%87%D8%AF+%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%8A+%D9%84%D9%84%D8%B9%D9%84%D9%88%D9%85+%D8%A7%D9%84%D8%A7%D8%AF%D8%A7%D8%B1%D9%8A%D8%A9+%D8%A8%D9%84%D9%82%D8%A7%D8%B3%E2%80%AD/@30.6935306,31.3061535,21z/data=!4m14!1m7!3m6!1s0x14f7eb7d43d39f85:0xf62eaddad31c011d!2z2KfZhNmF2LnZh9ivINin2YTYudin2YTZiiDZhNmE2LnZhNmI2YUg2KfZhNin2K_Yp9ix2YrYqSDYqNmE2YLYp9iz!8m2!3d30.6936377!4d31.3060921!16s%2Fg%2F11n09z0lkj!3m5!1s0x14f7eb7d43d39f85:0xf62eaddad31c011d!8m2!3d30.6936377!4d31.3060921!16s%2Fg%2F11n09z0lkj?entry=ttu&g_ep=EgoyMDI2MDEyNy.4wIKXMDSoASAFQAw%3D%3D"),
                                        style=ButtonStyle(
                                            bgcolor='blue',
                                            color='white',
                                            shape=RoundedRectangleBorder(radius=8)
                                        ),
                                        width=200
                                    ),
                                    padding=padding.only(bottom=10),
                                    alignment=alignment.center
                                ),
                                ElevatedButton(
                                    "العودة للصفحة الرئيسية",
                                    icon=Icons.ARROW_BACK,
                                    on_click=lambda _: page.go('/'),
                                    style=ButtonStyle(
                                        bgcolor='gray',
                                        color='white',
                                        shape=RoundedRectangleBorder(radius=8)
                                    ),
                                    width=200
                                )
                            ], 
                            horizontal_alignment='center',
                            spacing=10),
                            padding=30,
                            alignment=alignment.center
                        )
                    ],
                    bgcolor='white'
                )
            )
        
        page.update()
    
    page.on_route_change = rout_change
    page.go(page.route)

app(main)
