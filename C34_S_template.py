from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout


# --- Color Theme ---
Window.clearcolor = (0.01, 0.09, 0.17, 1)  # Dark Navy Blue

PRIMARY_COLOR = (0.2, 0.6, 0.8, 1)  # Teal Blue
SECONDARY_COLOR = (0.1, 0.4, 0.6, 1)
TEXT_COLOR = (1, 1, 1, 1)
BUTTON_TEXT_COLOR = (1, 1, 1, 1)


#####################################APP LAYOUT ###############################################################3
# --- Signup Screen ---
def build_signup_screen():
    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
    layout.add_widget(Label(text='[b]Signup[/b]', markup=True, font_size=36,
                            size_hint=(1, None), height=60, color=TEXT_COLOR))

    float_layout = FloatLayout(size_hint=(1, 1))

    name_input = TextInput(hint_text='Name', multiline=False,
                           size_hint=(0.6, None), height=50,
                           pos_hint={'center_x': 0.5, 'center_y': 0.85},
                           background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    email_input = TextInput(hint_text='Email', multiline=False,
                            size_hint=(0.6, None), height=50,
                            pos_hint={'center_x': 0.5, 'center_y': 0.70},
                            background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    password_input = TextInput(hint_text='Password', password=True, multiline=False,
                               size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.5, 'center_y': 0.55},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
    
    generate_otp_btn = Button(text='Generate OTP', size_hint=(0.4, None), height=40,
                              pos_hint={'center_x': 0.5, 'center_y': 0.40},
                              background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)

    otp_input = TextInput(hint_text='Enter OTP', multiline=False,
                          size_hint=(0.6, None), height=50,
                          pos_hint={'center_x': 0.5, 'center_y': 0.25},
                          background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

   

    verify_btn = Button(text='Verify OTP', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.10},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR)

    float_layout.add_widget(name_input)
    float_layout.add_widget(email_input)
    float_layout.add_widget(password_input)
    float_layout.add_widget(generate_otp_btn)
    float_layout.add_widget(otp_input)
    float_layout.add_widget(verify_btn)

    layout.add_widget(float_layout)

    switch_btn = Button(text='Already a user? Go to Login', size_hint=(1, None), height=50,
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    
    layout.add_widget(switch_btn)

    return layout

# --- Login Screen ---
def build_login_screen():
    global email_input,password_input
    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
    layout.add_widget(Label(text='[b]SPLITWISE APP[/b]', markup=True, font_size=36,
                            size_hint=(1, None), height=60, color="yellow"))

    float_layout = FloatLayout(size_hint=(1, 1))

    email_input = TextInput(hint_text='Email', multiline=False,
                            size_hint=(0.6, None), height=50,
                            pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    password_input = TextInput(hint_text='Password', password=True, multiline=False,
                               size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.5, 'center_y': 0.55},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    submit_btn = Button(text='Login', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR)
    

    float_layout.add_widget(email_input)
    float_layout.add_widget(password_input)
    float_layout.add_widget(submit_btn)

    layout.add_widget(float_layout)

    switch_btn = Button(text='New User? Go to Signup', size_hint=(1, None), height=50,
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
   
    layout.add_widget(switch_btn)

    return layout

def build_dashboard_screen():
    global owe_amount_label,other_owe_amount_label
    layout = FloatLayout(size_hint=(1, 1))

    welcome_label = Label(
        text='[b]WELCOME TO THE DASHBOARD![/b]',
        markup=True,
        font_size=28,
        size_hint=(None, None), size=(300, 30),
        pos_hint={'center_x': 0.5, 'top': 0.95},
        color="yellow"
    )
    layout.add_widget(welcome_label)

    # Info center box as FloatLayout
    info_float = FloatLayout(size_hint=(None, None), size=(600, 90),
                             pos_hint={'center_x': 0.5, 'top': 0.88})
  
    group_members_spinner = Spinner(
        text='[b]GROUP MEMBERS[/b]',
        values=group,
        size_hint=(None, None), size=(180, 40),
        pos_hint={'x': 0, 'center_y': 0.5},
        background_color=SECONDARY_COLOR,
        color="white",
        markup=True
    )
    info_float.add_widget(group_members_spinner)
    
   
   
    owe_float = FloatLayout(size_hint=(None, None), size=(120, 60),
                            pos_hint={'x': 0.35, 'center_y': 0.5})
    owe_label = Label(
        text='[b]YOU OWE[/b]', markup=True, font_size=18,
        size_hint=(1, None), height=25,
        pos_hint={'center_x': 0.5, 'top': 1},
        color="yellow"
    )

    owe_float.add_widget(owe_label)
    owe_amount_label = Label(
        text=str(0), font_size=24,
        size_hint=(1, None), height=35,
        pos_hint={'center_x': 0.5, 'y': 0},
        color=TEXT_COLOR
    )
    owe_float.add_widget(owe_amount_label)
    info_float.add_widget(owe_float)

    other_owe_float = FloatLayout(size_hint=(None, None), size=(150, 60),
                                  pos_hint={'x': 0.65, 'center_y': 0.5})
    other_owe_label = Label(
        text='[b]OTHERS OWE YOU[/b]', markup=True, font_size=18,
        size_hint=(1, None), height=25,
        pos_hint={'center_x': 0.5, 'top': 1},
        color="yellow"
    )
    other_owe_amount_label = Label(
        text=str(0), font_size=24,
        size_hint=(1, None), height=35,
        pos_hint={'center_x': 0.5, 'y': 0},
        color=TEXT_COLOR
    )
    other_owe_float.add_widget(other_owe_label)
    other_owe_float.add_widget(other_owe_amount_label)
    info_float.add_widget(other_owe_float)

    layout.add_widget(info_float)

    # Dummy label for spacing (optional)
    layout.add_widget(Label(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0}))

    group=["member1","member2","member3"]
    num_members = len(group)
    cols = 3 + num_members
    table = GridLayout(cols=cols, size_hint=(1, None),height=400)
   

    # Header row
    headers = ['DESCRIPTION', 'PAID BY', 'AMOUNT'] + group
    for col in headers:
        table.add_widget(Label(text=f"[b]{col}[/b]", markup=True, color="yellow", size_hint_y=None, height=40))

        layout.add_widget(table)

    btn_layout = BoxLayout(
        orientation='horizontal',
        size_hint=(1, None), height=60, spacing=20, padding=[0, 0, 0, 10]
    )
    add_expense_btn = Button(
        text='Add Expense',
        size_hint=(0.5, 1),
        background_color=SECONDARY_COLOR,
        color=(1, 1, 1, 1),
       
    )

    add_group_members_btn = Button(
        text='Add Group Members',
        size_hint=(0.5, 1),
        background_color=SECONDARY_COLOR,
        color=(1, 1, 1, 1),
      
    )

    btn_layout.add_widget(add_expense_btn)
    btn_layout.add_widget(add_group_members_btn)
    layout.add_widget(btn_layout)

    return layout

def build_add_group_screen():
        global member_name_input, member_email_input, contact_input
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(
            text='[b]ADD GROUP MEMBER[/b]', markup=True, font_size=36,
            size_hint=(1, None), height=60, color="yellow"
        ))

        float_layout = FloatLayout(size_hint=(1, 1))

        # Name
        name_label = Label(text='Name:', size_hint=(None, None), size=(100, 40),
                        pos_hint={'center_x': 0.2, 'center_y': 0.75}, color=TEXT_COLOR)
        member_name_input = TextInput(size_hint=(0.6, None), height=50,
                                    pos_hint={'center_x': 0.6, 'center_y': 0.75},
                                    background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

        # Email
        email_label = Label(text='Email:', size_hint=(None, None), size=(100, 40),
                            pos_hint={'center_x': 0.2, 'center_y': 0.6}, color=TEXT_COLOR)
        member_email_input = TextInput(size_hint=(0.6, None), height=50,
                                    pos_hint={'center_x': 0.6, 'center_y': 0.6},
                                    background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

        # Contact
        contact_label = Label(text='Contact (optional):', size_hint=(None, None), size=(150, 40),
                            pos_hint={'center_x': 0.2, 'center_y': 0.45}, color=TEXT_COLOR)
        contact_input = TextInput(size_hint=(0.6, None), height=50,
                                pos_hint={'center_x': 0.6, 'center_y': 0.45},
                                background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

        # Buttons
        add_btn = Button(text='Add Member', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.3},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR,
                        )

        back_btn = Button(text='Back to Dashboard', size_hint=(1, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.15},
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR,
                       )

        # Add to layout
        float_layout.add_widget(name_label)
        float_layout.add_widget(member_name_input)
        float_layout.add_widget(email_label)
        float_layout.add_widget(member_email_input)
        float_layout.add_widget(contact_label)
        float_layout.add_widget(contact_input)
        float_layout.add_widget(add_btn)
        float_layout.add_widget(back_btn)

        layout.add_widget(float_layout)
        return layout

#
def build_add_expense_screen():
    global who_paid_input, description_input, amount_input
    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

    layout.add_widget(Label(
        text='[b]ADD EXPENSE[/b]', markup=True, font_size=36,
        size_hint=(1, None), height=60, color="yellow"
    ))

    float_layout = FloatLayout(size_hint=(1, 1))

    # Who Paid
    who_paid_label = Label(text='Who Paid:', size_hint=(None, None), size=(120, 40),
                           pos_hint={'center_x': 0.18, 'center_y': 0.75}, color=TEXT_COLOR)
    who_paid_input = TextInput(size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.6, 'center_y': 0.75},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    # Description
    description_label = Label(text='Description:', size_hint=(None, None), size=(120, 40),
                              pos_hint={'center_x': 0.18, 'center_y': 0.6}, color=TEXT_COLOR)
    description_input = TextInput(size_hint=(0.6, None), height=50,
                                  pos_hint={'center_x': 0.6, 'center_y': 0.6},
                                  background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    # Amount
    amount_label = Label(text='Amount:', size_hint=(None, None), size=(120, 40),
                         pos_hint={'center_x': 0.18, 'center_y': 0.45}, color=TEXT_COLOR)
    amount_input = TextInput(size_hint=(0.6, None), height=50,
                             pos_hint={'center_x': 0.6, 'center_y': 0.45},
                             background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    # Buttons
    add_btn = Button(text='Add', size_hint=(0.4, None), height=50,
                     pos_hint={'center_x': 0.5, 'center_y': 0.28},
                     background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR,
                     )

    back_btn = Button(
        text='Back to Dashboard',
        size_hint=(1, None), height=50,
        pos_hint={'center_x': 0.5, 'center_y': 0.14},
        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR
    )

    # Call add_expense when the button is pressed, then go to dashboard
   
    # Add widgets
    float_layout.add_widget(who_paid_label)
    float_layout.add_widget(who_paid_input)
    float_layout.add_widget(description_label)
    float_layout.add_widget(description_input)
    float_layout.add_widget(amount_label)
    float_layout.add_widget(amount_input)
    float_layout.add_widget(add_btn)
    float_layout.add_widget(back_btn)

    layout.add_widget(float_layout)

    return layout

class MyApp(App):
    def build(self):
        return build_add_group_screen()

if __name__ == "__main__":
    MyApp().run()
