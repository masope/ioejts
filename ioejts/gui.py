import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext


from .util import IoejtsCalculator
from .src import *


class IoejtsSurveyWindow(tk.Frame, IoejtsCalculator):

    def __init__(self, master=None, lang=EN, result_page=True):
        """ VARIABLE INITIALIZATION """
        self.result = []
        self._rp = result_page
        self.scaleValueList = [P_MEDIAN] * Q_QUANTITY
        self.isAboutTopLevelExist = False
        self.isResultTopLevelExist = False

        """ LOCALE SET """
        if lang == KR:
            self.QUESTIONS = QUESTIONS_KR
            self.UI_TXT = UI_TXT_KR
            self.UNDERLINE = UNDERLINE_DEFAULT
        else:
            self.QUESTIONS = QUESTIONS
            self.UI_TXT = UI_TXT_EN
            self.UNDERLINE = UNDERLINE_EN
        
        """ TOP-LEVEL FRAME CREATION """
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        
        """ SURVEY APPLICATION CREATION """
        self.RootCreation()
        self.SurveyWidgetCreation()


    # interfaces.
    def getResult(self):
        return self.result


    #
    # application creation functions.
    #
    def RootCreation(self):
        self.root = self.winfo_toplevel()
        self.root.title('OEJTS')
        self.root.minsize(*ROOT_WIN_MINSIZE)
        self.root.lift()
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        """ Keyboard Shortcut Bindings """
        self.root.bind("<KeyPress-a>", lambda e : self._AboutButtonUpdate(e))
        self.root.bind("<KeyPress-p>", lambda e : self._PreviousButtonUpdate(e))
        self.root.bind("<KeyPress-n>", lambda e : self._NextButtonUpdate(e))
        self.root.bind("<Right>", lambda e : self.widgetUserScale.set(self.widgetUserScale.get() + 1))
        self.root.bind("<Left>", lambda e : self.widgetUserScale.set(self.widgetUserScale.get() - 1))

    def SurveyWidgetCreation(self):
        """ Initializations """
        self.__SaveResult()


        """ Widget Control Variables """
        self.indexNumberInt = tk.IntVar()
        self.progressInt = tk.IntVar()
        self.userScaleInt = tk.IntVar()
        self.questionIndexString = tk.StringVar()
        self.leftQuestionString = tk.StringVar()
        self.rightQuestionString = tk.StringVar()


        """ Control Variable Initializations """
        self.indexNumberInt.set(0)
        self.progressInt.set(0)
        self.userScaleInt.set(3)
        self.questionIndexString.set(self.UI_TXT[HEADER](self.indexNumberInt.get() + 1))
        self.leftQuestionString.set(self.QUESTIONS[Q_INDEXES[0]][LEFT])
        self.rightQuestionString.set(self.QUESTIONS[Q_INDEXES[0]][RIGHT])


        """ Application Widget Grid Configurations """
        self.rowconfigure(0, minsize=30)
        self.rowconfigure(2, minsize=15)
        self.rowconfigure(4, minsize=15)
        self.rowconfigure(6, minsize=15)
        self.rowconfigure(7, weight=1, minsize=40)
        self.rowconfigure(8, minsize=15)
        self.rowconfigure(10, minsize=15)
        self.rowconfigure(12, minsize=30)

        self.columnconfigure(0, minsize=30)
        self.columnconfigure(2, minsize=30)
        self.columnconfigure(3, weight=1, minsize=100)
        self.columnconfigure(5, weight=1, minsize=100)
        self.columnconfigure(6, minsize=30)
        self.columnconfigure(8, minsize=30)


        """ Static Widgets """
        self.widgetTopSeparator = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.widgetMiddleSeparator = ttk.Separator(self, orient=tk.VERTICAL)
        self.widgetBottomSeparator = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.widgetTopSeparator.grid(row=5, column=1, columnspan=7, padx=5, sticky=tk.E+tk.W)
        self.widgetMiddleSeparator.grid(row=7, column=4, pady=5, sticky=tk.N+tk.S)
        self.widgetBottomSeparator.grid(row=9, column=1, columnspan=7, padx=5, sticky=tk.E+tk.W)


        """ Text Outputs """
        self.widgetQuestionIndex = tk.Label(self, font=('MS Serif', 14), 
                                                  textvariable=self.questionIndexString)
        self.widgetLeftQuestion = tk.Text(self, font=('Helvetica', 10), 
                                                wrap=tk.WORD, 
                                                state=tk.DISABLED, 
                                                width=15, 
                                                height=5, 
                                                relief=tk.FLAT, 
                                                bg=self.root.cget('bg'), 
                                                bd=0)
        self.widgetRightQuestion = tk.Text(self, font=('Helvetica', 10), 
                                                 wrap=tk.WORD, 
                                                 state=tk.DISABLED, 
                                                 width=15, 
                                                 height=5, 
                                                 relief=tk.FLAT, 
                                                 bg=self.root.cget('bg'), 
                                                 bd=0)
        
        self.widgetQuestionIndex.grid(row=0, rowspan=3, column=3, columnspan=3)
        self.widgetLeftQuestion.grid(row=7, column=2, columnspan=2, padx=15, sticky=tk.E+tk.W)
        self.widgetRightQuestion.grid(row=7, column=5, columnspan=2, padx=15, sticky=tk.E+tk.W)

        self.__TkStaticTextRewriter(self.widgetLeftQuestion, self.leftQuestionString.get())
        self.__TkStaticTextRewriter(self.widgetRightQuestion, self.rightQuestionString.get())
        
        
        """ Buttons """
        self.widgetAboutButton = ttk.Button(self, text=self.UI_TXT[ABOUT], 
                                                 underline=self.UNDERLINE, 
                                                 command=self._AboutButtonUpdate)
        self.widgetPreviousButton = ttk.Button(self, text=self.UI_TXT[PREV], 
                                                     underline=self.UNDERLINE, 
                                                     command=self._PreviousButtonUpdate)
        self.widgetNextButton = ttk.Button(self, text=self.UI_TXT[NEXT], 
                                                 underline=self.UNDERLINE, 
                                                 command=self._NextButtonUpdate)

        self.widgetAboutButton.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.widgetPreviousButton.grid(row=11, column=1)
        self.widgetNextButton.grid(row=11, column=7)


        """ Other Dynamic Widgets """
        self.widgetProgressbar = ttk.Progressbar(self, maximum=32, 
                                                       mode='determinate', 
                                                       orient=tk.HORIZONTAL, 
                                                       variable=self.progressInt)
        self.widgetUserScale = ttk.Scale(self, orient=tk.HORIZONTAL, 
                                               length=200, 
                                               from_=(P_MEDIAN-2), 
                                               to=(P_MEDIAN+2),
                                               variable=self.userScaleInt, 
                                               command=self._UserScaleUpdate)

        self.widgetProgressbar.grid(row=3, column=3, columnspan=3, sticky=tk.E+tk.W)
        self.widgetUserScale.grid(row=11, column=3, columnspan=3)


    #
    # widget command functions for application logics.
    #
    def _AboutButtonUpdate(self, e=None):
        if not self.isAboutTopLevelExist:
            self.isAboutTopLevelExist = True
            self.__AboutTopLevel()
            
    def _PreviousButtonUpdate(self, e=None):
        i = self.indexNumberInt.get()

        if i == 0:
            pass
        elif i in range(1, len(Q_INDEXES) + 1):
            self.__TkStaticTextRewriter(self.widgetLeftQuestion, self.QUESTIONS[Q_INDEXES[i - 1]][LEFT])
            self.__TkStaticTextRewriter(self.widgetRightQuestion, self.QUESTIONS[Q_INDEXES[i - 1]][RIGHT])

            self.indexNumberInt.set(i - 1)
            self.questionIndexString.set(self.UI_TXT[HEADER](self.indexNumberInt.get() + 1))

            self.userScaleInt.set(self.scaleValueList[i - 1])
        else:
            pass

    def _NextButtonUpdate(self, e=None):
        i = self.indexNumberInt.get()

        if i >= len(Q_INDEXES) - 1:
            self.__SaveResult()
            if self._rp:
                if not self.isResultTopLevelExist:
                    self.isResultTopLevelExist = True
                    self.__ResultTopLevel()
            else:
                self.__RootWindowTermination()
        elif i in range(len(Q_INDEXES) - 1):
            self.__TkStaticTextRewriter(self.widgetLeftQuestion, self.QUESTIONS[Q_INDEXES[i + 1]][LEFT])
            self.__TkStaticTextRewriter(self.widgetRightQuestion, self.QUESTIONS[Q_INDEXES[i + 1]][RIGHT])

            if i == self.progressInt.get():
                self.progressInt.set(self.progressInt.get() + 1)

            self.indexNumberInt.set(i + 1)
            self.questionIndexString.set(self.UI_TXT[HEADER](self.indexNumberInt.get() + 1))

            self.userScaleInt.set(self.scaleValueList[i + 1])
        else:
            pass

    def _UserScaleUpdate(self, e=None):
        self.__TtkScaleResolutionModifier(self.widgetUserScale)
        self.scaleValueList[self.indexNumberInt.get()] = self.userScaleInt.get()


    #
    # utility functions.
    #
    def __TkStaticTextRewriter(self, text, string):
        text.configure(state=tk.NORMAL)
        text.delete(0.0, tk.END)
        text.tag_configure("center", justify='center')
        text.insert("1.0", string)
        text.tag_add("center", "1.0", "end")
        text.configure(state=tk.DISABLED)

    def __TtkScaleResolutionModifier(self, scale):
        value = scale.get()
        if int(value) != value:
            scale.set(round(value))

    def __SaveResult(self):
        self.result = self.scaleValueList[::]

    def __RootWindowTermination(self):
        self.root.destroy()

    def __AboutTopLevel(self):
        """ Top-level Configuration """
        AboutTopLevel = tk.Toplevel()
        AboutTopLevel.title(self.UI_TXT[ABOUT_TITLE])
        AboutTopLevel.minsize(*ABOUT_WIN_MINSIZE)
        AboutTopLevel.transient(self)
        AboutTopLevel.focus_set()

        AboutTopLevel.rowconfigure(0, weight=1)
        AboutTopLevel.columnconfigure(0, weight=1)

        """ Textbox """
        infoTextBox = scrolledtext.ScrolledText(AboutTopLevel, font=('Helvetica', 10), 
                                                               wrap=tk.WORD, 
                                                               width=15, 
                                                               height=5,
                                                               state=tk.DISABLED,
                                                               relief=tk.SUNKEN, 
                                                               bg=AboutTopLevel.cget('bg'))
        infoTextBox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        self.__TkStaticTextRewriter(infoTextBox, self.UI_TXT[INFO])

        """ Ok Button """
        def closeTopLevel():
            AboutTopLevel.destroy()
            self.isAboutTopLevelExist = False

        AboutTopLevel.protocol("WM_DELETE_WINDOW", closeTopLevel)
        okayButton = ttk.Button(AboutTopLevel, text=self.UI_TXT[OKAY], 
                                                    underline=self.UNDERLINE, 
                                                    command=closeTopLevel)
        okayButton.grid(row=1, column=0, padx=15, pady= 15, sticky=tk.E)

        """ Keyboard Shortcut Bindings """        
        AboutTopLevel.bind("<KeyPress-o>", lambda e : closeTopLevel())
        AboutTopLevel.bind("<Escape>", lambda e : closeTopLevel())

    def __ResultTopLevel(self):
        """ Top-level Configuration """
        ResultTopLevel = tk.Toplevel()
        ResultTopLevel.title(self.UI_TXT[RESULT_TITLE])
        ResultTopLevel.minsize(*RESULT_WIN_MINSIZE)
        ResultTopLevel.transient(self)
        ResultTopLevel.grab_set()
        ResultTopLevel.focus_set()

        ResultTopLevel.rowconfigure(0, weight=1)
        ResultTopLevel.columnconfigure(0, weight=1)

        """ Textbox """
        infoTextBox = tk.Text(ResultTopLevel, font=('Helvetica', 10), 
                                              wrap=tk.WORD, 
                                              width=20, 
                                              height=7,
                                              state=tk.DISABLED,
                                              relief=tk.FLAT, 
                                              bg=ResultTopLevel.cget('bg'),
                                              bd=0)
        infoTextBox.grid(row=0, column=0, sticky=tk.E+tk.W)

        s = super().calc_p_s(self.getResult())
        self.__TkStaticTextRewriter(infoTextBox, self.UI_TXT[RESULT](*[*s.values()], "".join(super().calc_mbti(s))))

        """ Ok Button """
        def closeTopLevel():
            self.__RootWindowTermination()

        ResultTopLevel.protocol("WM_DELETE_WINDOW", closeTopLevel)
        okayButton = ttk.Button(ResultTopLevel, text=self.UI_TXT[OKAY], 
                                                     underline=self.UNDERLINE, 
                                                     command=closeTopLevel)
        okayButton.grid(row=1, column=0, padx=15, pady= 15, sticky=tk.E)

        """ Keyboard Shortcut Bindings """
        ResultTopLevel.bind("<KeyPress-o>", lambda e : closeTopLevel())
        ResultTopLevel.bind("<Escape>", lambda e : closeTopLevel())

