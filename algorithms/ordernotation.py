from manim import *
import numpy as np
import random
from manim_slides import Slide
import sys
sys.path.append('./src/')
from Util import Util


# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


class Introduction(MovingCameraScene,Slide):
    def construct(self):
        header = Text("Introduction", font = "Chalkboard",font_size=50, stroke_width=2)
        self.play(Write(header))
        self.next_slide()
        self.play(FadeOut(header))



        label1=Text("Vijay's \nAlgorithm", font = "Chalkboard",font_size=20, color=WHITE, stroke_width= 2)
        square1=Square(side_length=2,fill_color=GREEN, fill_opacity=1)
        arrow1 = Line(start = np.array([-2,0,0]), end = square1.get_left()).add_tip()
        arrow1.set_length(1)
        arrow2 = Line(start=square1.get_right(), end=np.array([2, 0, 0])).add_tip()
        arrow2.set_length(1)
        t1 = Text("Input", font="Chalkboard", font_size=15,stroke_width= 2)
        t1.set_color(WHITE)
        t1.move_to(np.array([-1.5, 0.4, 0]))
        t2 = Text("Output", font="Chalkboard", font_size=15,stroke_width= 2)
        t2.set_color(WHITE)
        t2.move_to(np.array([1.5, 0.4, 0]))
        newgroup1 = VGroup( square1,label1,arrow1,arrow2,t2,t1)

        self.play(Create(newgroup1), run_time=3)
        #self.next_slide()
        #self.play(self.camera.frame.animate.move_to(newgroup1).set(width=newgroup1.width))
        #self.next_slide()
        #self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))
        self.play(newgroup1.animate.shift(UP * 2 + 4 * LEFT))



        label2=Text("Ajay's \nAlgorithm", font = "Chalkboard",font_size=20, color=WHITE, stroke_width= 2)
        square2=Square(side_length=2,fill_color=GREEN, fill_opacity=1)
        arrow3 = Line(start = np.array([-2,0,0]), end = square2.get_left()).add_tip()
        arrow3.set_length(1)
        arrow4 = Line(start=square2.get_right(), end=np.array([2, 0, 0])).add_tip()
        arrow4.set_length(1)
        t3 = Text("Input", font="Chalkboard", font_size=15,stroke_width= 2)
        t3.set_color(WHITE)
        t3.move_to(np.array([-1.5, 0.4, 0]))
        t4 = Text("Output", font="Chalkboard", font_size=15,stroke_width= 2)
        t4.set_color(WHITE)
        t4.move_to(np.array([1.5, 0.4, 0]))
        newgroup2 = VGroup( square2,label2,arrow3,arrow4,t3,t4).shift(UP * 2 + 4 * RIGHT)

        self.play(TransformFromCopy(newgroup1, newgroup2),run_time=3)
        self.next_slide()

        q1 = Text("Which one will you choose?", color= RED, stroke_width=2, font_size=50 )
        self.play(Write(q1),run_time=2.0)
        self.next_slide()

        self.play(FadeOut(q1))

        a1 = Text("Correctness : The algorithm should give correct answer for every valid input.", font_size=30,stroke_width=2, t2c={"Correctness": GREEN}, t2s ={ "valid":ITALIC, "input":ITALIC})
        self.play(Write(a1))

        a2 = Text("Running Time : The algorithm should be fast.", font_size=30, stroke_width=2, t2c={"Running Time": GREEN}, t2s={ "fast": ITALIC})
        a2.align_to(a1,LEFT)
        a2.shift(DOWN)
        self.play(Write(a2))

        a3 = Text("Maintainence : The algorithm should be easy to maintain.", font_size=30, stroke_width=2, t2c={"Maintainence": GREEN}, t2s ={"maintain":ITALIC})
        a3.align_to(a2,LEFT)
        a3.shift(DOWN*2)
        self.play(Write(a3))

        self.next_slide()
        self.play(self.camera.frame.animate.move_to(a1.get_left()+1.5*RIGHT).set(width=a1.width*0.5))


        a4 = Text("Our focus \n in this \n course", font_size=20, color=ORANGE)
        a4.shift(a1.get_left() + LEFT + DOWN*0.4)
        br1 = BraceBetweenPoints(a1.get_left()+0.05*LEFT,a1.get_left() + DOWN +0.05*LEFT, direction= LEFT)
        self.play(Write(a4),FadeIn(br1))
        self.next_slide()
        self.play(FadeOut(a4,br1))
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))

class RunningTime(MovingCameraScene,Slide):
    def construct(self):

        header = Text("Running Time of An Algorithm", font = "Chalkboard",font_size=50, stroke_width=2)
        self.play(Write(header))
        self.next_slide()
        self.play(FadeOut(header))


        t1 = Tex(r"$min = A[0]$;", font_size=30, stroke_width=2 )
        t2 = Tex("for",r"$(i=1; i<n; i$", "++)\{", font_size=30, stroke_width=2 )
        t2.set_color_by_tex("for", RED)
        t2.align_to(t1,LEFT)
        t2.shift(0.4*DOWN)
        t3 = Tex("if", r"$(A[i] < min$",")", font_size=30, stroke_width=2 )
        t3.set_color_by_tex("if", RED)
        t3.align_to(t2,LEFT)
        t3.shift(DOWN*0.8+RIGHT*0.2)
        t4 = Tex(r"$min = A[i];$", font_size=30, stroke_width=2 )
        t4.align_to(t3,LEFT)
        t4.shift(DOWN*1.2+RIGHT*0.2)
        t5 = Text("}", font_size=30, stroke_width=2 )
        t5.align_to(t2,LEFT)
        t5.shift(DOWN*1.6)
        t6 = Tex(r"$return$",r"$\ min;$", font_size=30, stroke_width=2 )
        t6.set_color_by_tex("return", RED)
        t6.align_to(t5,LEFT)
        t6.shift(DOWN*2)

        newgroup1 = VGroup( t1,t2,t3,t4,t5,t6)

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.play(Write(t6))

        self.next_slide()

        self.play(newgroup1.animate.shift(UP * 3 + 5 * LEFT))

        q1 = Text("What is the running time of this algorithm?", color= RED, stroke_width=2, font_size=40 )
        q1.shift(1.5*LEFT)
        self.play(Write(q1),run_time=2.0)
        self.next_slide()

        q2 = Text("What do you mean by the running time of an algorithm?", color= RED, font_size=40, stroke_width=2)
        q2.align_to(q1,LEFT)
        q2.shift(DOWN)
        self.play(Write(q2),run_time=2.0)


        self.next_slide()
        self.play(FadeOut(q1,q2))
        self.next_slide()
        r1 = RoundedRectangle(color=GREEN,fill_opacity=0.5,height=0.3, width=3.5,corner_radius=0.1)
        r1.align_to(t1, LEFT+UP)
        r1.shift(LEFT*0.2)

        self.play(Create(r1))

        rect1 = Rectangle(width=5.0, height=0.5, grid_xstep=1.0, color=BLUE)
        rect1.shift(UR)
        arr = Tex(r"$A$",font_size=30, stroke_width=2 )
        arr.align_to(rect1,LEFT+UP)
        arr.shift(LEFT*0.4 + DOWN*0.1)


        n1 = Text("1", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*0.5+DOWN*0.15)
        n2 = Text("2", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*1.5+DOWN*0.15)
        n3 = Text("3", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*2.5+DOWN*0.15)
        n4 = Text("4", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*3.5+DOWN*0.15)
        n5 = Text("5", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*4.5+DOWN*0.15)

        self.play(GrowFromCenter(rect1), GrowFromCenter(arr))
        self.play(GrowFromCenter(n1),GrowFromCenter(n2),GrowFromCenter(n3),GrowFromCenter(n4),GrowFromCenter(n5))
        self.next_slide()

        t7 = Tex(r"$min = $",font_size=40, stroke_width=2).align_to(rect1, LEFT+UP).shift(RIGHT*1.5+ DOWN)
        t8 = Tex(r"$1$",font_size=40, stroke_width=2)
        t8.next_to(t7)
        self.play(Create(t7))
        self.play(TransformFromCopy(n1, t8),run_time=3)


        self.next_slide()
        r1.align_to(t2, LEFT+UP).shift(LEFT*0.2)
        r2 = Rectangle(width=1.0, height=0.5, fill_color=MAROON).align_to(rect1,LEFT+UP).shift(RIGHT).set_fill(ORANGE, opacity=0.7)
        arrow1 = Line(start = r2.get_top()+UP, end = r2.get_top()).add_tip()
        arrow1.set_length(1)
        i = Tex(r"$i$",font_size=40, stroke_width=2).align_to(arrow1,UP).shift(0.4*UP)
        newgroup2 = VGroup( r2,arrow1,i)
        self.play(GrowFromCenter(r2), GrowFromCenter(arrow1),GrowFromCenter(i), run_time=1)

        self.next_slide()
        self.play(r1.animate.align_to(t3, LEFT+UP).shift(LEFT*0.2))
        self.play(r1.animate.align_to(t2, LEFT+UP).shift(LEFT*0.2))
        self.play(newgroup2.animate.shift(RIGHT))
        self.next_slide()

        self.play(r1.animate.align_to(t3, LEFT+UP).shift(LEFT*0.2))
        self.play(r1.animate.align_to(t2, LEFT+UP).shift(LEFT*0.2))
        self.play(newgroup2.animate.shift(RIGHT))

        self.next_slide()
        self.play(r1.animate.align_to(t3, LEFT+UP).shift(LEFT*0.2))
        self.play(r1.animate.align_to(t2, LEFT+UP).shift(LEFT*0.2))
        self.play(newgroup2.animate.shift(RIGHT))

        self.next_slide()
        self.play(r1.animate.align_to(t3, LEFT+UP).shift(LEFT*0.2))
        self.play(r1.animate.align_to(t2, LEFT+UP).shift(LEFT*0.2))
        self.play(newgroup2.animate.shift(RIGHT))

        self.next_slide()
        self.play(r1.animate.align_to(t6, LEFT+UP).shift(LEFT*0.2))
        self.play(FadeOut(r2,t7,t8,arrow1,i))
        self.play(r1.animate.set_color(RED))
        self.play(r1.animate.align_to(t4, LEFT+UP).shift(LEFT*0.2))

        self.next_slide()
        t9 = Text("For our input, this line is never executed. \nSo, this is a good input for our algorithm"    , font_size=25).next_to(r1)
        self.play(Create(t9),run_time = 3)

        self.next_slide()
        self.play(FadeOut(rect1,r1,arr,t9,n1,n2,n3,n4,n5))

        q3 = Text("What is the worst case input for this algorithm?", color= RED, stroke_width=2, font_size=40 )
        self.play(Write(q3),run_time=2.0)
        self.next_slide()

        rect1.next_to(q3, DOWN)
        arr.align_to(rect1,LEFT+UP).shift(LEFT*0.4 + DOWN*0.1)
        n1 = Text("5", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*0.5+DOWN*0.15)
        n2 = Text("4", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*1.5+DOWN*0.15)
        n3 = Text("3", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*2.5+DOWN*0.15)
        n4 = Text("2", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*3.5+DOWN*0.15)
        n5 = Text("1", font_size=20, stroke_width=2).move_to(rect1,LEFT+UP).shift(RIGHT*4.5+DOWN*0.15)

        self.play(GrowFromCenter(rect1), GrowFromCenter(arr))
        self.play(GrowFromCenter(n1),GrowFromCenter(n2),GrowFromCenter(n3),GrowFromCenter(n4),GrowFromCenter(n5))
        self.next_slide()



class MeaningOfRunningTime(Slide):
    def construct(self):
        header = Text("What is the meaning of Running Time?", font = "Chalkboard",font_size=50, stroke_width=2)
        self.play(Write(header))
        self.next_slide()
        self.play(FadeOut(header))

        t1 = Text("All possible Inputs",font_size=30,stroke_width=2).shift(3*UP)
        self.play(Write(t1))
        self.next_slide()
        dotarray = []
        newgroup1 = VGroup()
        for i in range(0,200):
            x =  random.uniform(-7,7)
            y =  random.uniform(-3,2)
            dot = Dot(point = np.array([x, y, 0]))
            dotarray.append(dot)
            newgroup1.add(dot)
        dot1 = Dot(point = np.array([0, 0, 0]))
        self.play(GrowFromCenter(newgroup1), GrowFromCenter(dot1))
        self.next_slide()
        t2 = Text("Worst Case Input",font_size=30,stroke_width=2).align_to(dot1,DOWN).shift(0.6*DOWN)

        for dot in dotarray:
            dot.set_opacity(0.2)

        self.play(Write(t2), run_time=2.0)
        self.next_slide()
        self.play(FadeOut(newgroup1))

        t3 = Text("The running time of algorithm is its running time on the worst case input.",font_size=30,stroke_width=2).align_to(t2,DOWN).shift(0.6*DOWN)
        self.play(Write(t3), run_time =2.0)
        self.next_slide()

        self.play(FadeOut(dot1,t1,t2))
        self.play(t3.animate.set_opacity(0.5).scale(0.8).shift(RIGHT+2*UP))

        self.next_slide()

        ax = Axes(
            x_range=[0.1, 10], y_range=[0, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label=r"Year", y_label=r"Running Time")
        labels.set_opacity(0.5)
        t = ValueTracker(0.1)

        def func(x):
            return 1/x
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        newgroup = VGroup(ax,graph,dot,labels)

        self.play(Create(newgroup),rum_time=2)
        self.next_slide()
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=5)
        self.next_slide()

        t4 = Text("The running time changes over time.",font_size=30,stroke_width=2).align_to(t3,UP)
        self.play(Transform(t3, t4),run_time=3)
        self.next_slide()
        t5 = Text("Can we define a maching independent running time?",font_size=30,stroke_width=2,color=RED).align_to(t4,LEFT).shift(DOWN*0.5)
        self.play(TransformFromCopy(t4, t5),run_time=3)
        self.next_slide()

class MachineIndependentRunningTime(MovingCameraScene,Slide):
    def construct(self):
        header = Text("Machine Independent Running Time", font = "Chalkboard",font_size=50, stroke_width=2)
        self.play(Write(header))
        self.next_slide()
        self.play(FadeOut(header))


        t1 = Tex(r"$min = A[0]$;", font_size=30, stroke_width=2 )
        t2 = Tex("for",r"$(i=1; i<n; i$", "++)\{", font_size=30, stroke_width=2 )
        t2.set_color_by_tex("for", RED)
        t2.align_to(t1,LEFT)
        t2.shift(0.4*DOWN)
        t3 = Tex("if", r"$(A[i] < min$",")", font_size=30, stroke_width=2 )
        t3.set_color_by_tex("if", RED)
        t3.align_to(t2,LEFT)
        t3.shift(DOWN*0.8+RIGHT*0.2)
        t4 = Tex(r"$min = A[i];$", font_size=30, stroke_width=2 )
        t4.align_to(t3,LEFT)
        t4.shift(DOWN*1.2+RIGHT*0.2)
        t5 = Text("}", font_size=30, stroke_width=2 )
        t5.align_to(t2,LEFT)
        t5.shift(DOWN*1.6)
        t6 = Tex(r"$return$",r"$\ min;$", font_size=30, stroke_width=2 )
        t6.set_color_by_tex("return", RED)
        t6.align_to(t5,LEFT)
        t6.shift(DOWN*2)

        newgroup1 = VGroup(t1,t2,t3,t4,t5,t6).shift(UP*3+LEFT*5)

        self.play(Write(newgroup1))
        self.next_slide()
        rt = Text("Running Time",font_size=30, stroke_width=2).next_to(t1,RIGHT).shift(0.4*UP+2*RIGHT)
        self.play(Write(rt))
        self.next_slide()

        c1 = Tex(r"$c1$", font_size=30, stroke_width=2).next_to(t1,RIGHT).shift(2*RIGHT)
        self.play(Write(c1))
        self.next_slide()

        c2 = Tex(r"$c2$", font_size=30, stroke_width=2).move_to(c1,LEFT).shift(0.4*DOWN)
        self.play(Write(c2))
        self.next_slide()

        n2 = Tex(r"$(n-1)$", font_size=30, stroke_width=2).next_to(c2,RIGHT)
        self.play(Write(n2))
        self.next_slide()

        c3 = Tex(r"$c3$", font_size=30, stroke_width=2).move_to(c2,LEFT).shift(0.4*DOWN)
        self.play(Write(c3))
        n3 = Tex(r"$(n-1)$", font_size=30, stroke_width=2).next_to(c3,RIGHT)
        self.play(Write(n3))
        c4 = Tex(r"$c4$", font_size=30, stroke_width=2).move_to(c3,LEFT).shift(0.4*DOWN)
        self.play(Write(c4))
        n4 = Tex(r"$(n-1)$", font_size=30, stroke_width=2).next_to(c4,RIGHT)
        self.play(Write(n4))

        c5= Tex(r"$c5$", font_size=30, stroke_width=2).move_to(c4,LEFT).shift(0.8*DOWN)
        self.play(Write(c5))
        self.next_slide()

        c11 = Tex(r"$c$", font_size=30, stroke_width=2).move_to(c1)
        c12 = Tex(r"$c$", font_size=30, stroke_width=2).move_to(c2)
        c13 = Tex(r"$c$", font_size=30, stroke_width=2).move_to(c3)
        c14 = Tex(r"$c$", font_size=30, stroke_width=2).move_to(c4)
        c15 = Tex(r"$c$", font_size=30, stroke_width=2).move_to(c5)
        self.play(Transform(c1,c11),Transform(c2,c12),Transform(c3,c13),Transform(c4,c14),Transform(c5,c15), run_time=2)
        #self.play(FadeOut(c1,c2,c3,c4,c5))
        self.next_slide()


        self.play(c1.animate.move_to(np.array([-1,0,0])),c2.animate.move_to(np.array([0,0,0])),n2.animate.move_to((np.array([0.7,0,0]))),c3.animate.move_to(np.array([2,0,0])),n3.animate.move_to((np.array([2.7,0,0]))),c4.animate.move_to(np.array([4,0,0])),n4.animate.move_to((np.array([4.7,0,0]))),c5.animate.move_to(np.array([6,0,0])), run_time=2)
        plus1 = Tex(r"$+$", font_size=30, stroke_width=2).next_to(c1,RIGHT)
        plus2 = Tex(r"$+$", font_size=30, stroke_width=2).next_to(n2,RIGHT)
        plus3 = Tex(r"$+$", font_size=30, stroke_width=2).next_to(n3,RIGHT)
        plus4 = Tex(r"$+$", font_size=30, stroke_width=2).next_to(n4,RIGHT)
        self.play(Write(plus1),Write(plus2),Write(plus3),Write(plus4))
        self.next_slide()


        finalanswer1 = Tex(r"$3(n-1)$",font_size=30, stroke_width=2).align_to(c1,LEFT).shift(DOWN*0.5)
        finalanswer2 = Tex(r"$c$",font_size=30, stroke_width=2).next_to(finalanswer1,RIGHT)
        equal = Tex(r"$=$",font_size=30, stroke_width=2).next_to(finalanswer1,LEFT)
        self.play(Write(equal),Write(finalanswer1),Write(finalanswer2), run_time=2)
        self.next_slide()

        self.play(finalanswer1.animate.move_to(np.array([-3,-2,0])).scale(2), run_time=3)
        mi = Util.createSentence(self,"Machine Independent Running Time", finalanswer1,RIGHT,2)
        self.next_slide()

        self.play(finalanswer2.animate.move_to(np.array([-3,-3,0])).scale(2), run_time=3)
        mi2 = Text("Machine Dependent",font_size=30,stroke_width=2).next_to(finalanswer2,RIGHT).align_to(mi,LEFT)
        self.play(Create(mi2),run_time=2)
        self.next_slide()

        self.play(FadeOut(finalanswer2,mi,mi2,plus1,plus2,plus3,plus4,equal,c1,c2,c3,c4,c5,n2,n3,n4))


        al = Tex( r"$\alpha$",font_size=40, stroke_width=2)
        self.play(Create(al), rt.animate.next_to(al,LEFT), finalanswer1.animate.scale(0.5).next_to(al,RIGHT), run_time=4)
        self.next_slide()

        equal.move_to(al)
        self.play(Transform(al,equal), run_time=3)
        self.next_slide()

class OrderNotation(MovingCameraScene,Slide):
    def construct(self):
        Util.createWordThenFade(self,"The Order Notation")
        t = Tex( r"$3n^2-1$",font_size=40, stroke_width=2)

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 300, 10],
            x_length=10,
            tips=False,
        )
        labels = ax.get_axis_labels(x_label=r"n", y_label=r"\text{Running Time}")
        labels.set_opacity(0.5)
        t = ValueTracker(1/3)

        def func(x):
            return 2*(x**2) + 6*x -1

        def func2(x):
            return x**2
        graph = ax.plot(func, color=MAROON, x_range=[1/3, 10])
        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        label = ax.get_graph_label(
            graph, "2n^2+6n-1", x_val=10, direction=UP / 2
        )

        t1 = ValueTracker(1/3)
        graph1 = ax.plot(func2, color=GREEN, x_range=[0, 10])
        initial_point = [ax.coords_to_point(t1.get_value(), func2(t1.get_value()))]
        dot1 = Dot(point=initial_point)
        dot1.add_updater(lambda x: x.move_to(ax.c2p(t1.get_value(), func2(t1.get_value()))))
        label1 = ax.get_graph_label(
            graph1, "n^2", x_val=10, direction=UP / 2
        )

        newgroup = VGroup(ax,graph,dot,labels,graph1,dot1,label,label1)

        self.play(Create(newgroup),rum_time=8)
        
        self.play(t.animate.set_value(10), t1.animate.set_value(10),run_time=5)
        self.next_slide()

        w1 = Text("Both the functions have roughly same growth rate.",font_size=30,stroke_width=2).shift(UP)
        self.play(Create(w1),run_time=2)
        self.next_slide()

        self.play(FadeOut(ax,graph,dot,labels,graph1,dot1,label,label1,newgroup,w1))

        w2 = Tex(r"$n$",font_size=30,stroke_width=2).shift(UP*2+LEFT*4)
        w3 = Tex(r"$2n^2 + 6n -1$",font_size=30,stroke_width=2).next_to(w2).shift(RIGHT)
        w4 = Tex(r"$n^2$",font_size=30,stroke_width=2).next_to(w3).shift(RIGHT)

        self.play(Create(w2),Create(w3),Create(w4))
        self.next_slide()
        number = [None]*21
        t = [None]*6
        number[0] = Integer(0,font_size = 30).move_to(w2,LEFT).shift(DOWN*0.5)
        number[1] = Integer(0,font_size = 30).move_to(w3,LEFT).shift(DOWN*0.5)
        number[2] = Integer(0,font_size = 30).move_to(w4,LEFT).shift(DOWN*0.5)
        a = ValueTracker(0)
        number[0].add_updater(lambda m: m.set_value(a.get_value()))
        number[1].add_updater(lambda m: m.set_value(func(a.get_value())))
        number[2].add_updater(lambda m: m.set_value(func2(a.get_value())))
        self.add(number[0],number[1],number[2])

        for i in range(1,6):
            number[3*i] = Integer(0,font_size = 30).move_to(number[3*(i-1)],LEFT).shift(DOWN*0.5)
            number[3*i+1] = Integer(0,font_size = 30).move_to(number[3*(i-1)+1],LEFT).shift(DOWN*0.5)
            number[3*i+2] = Integer(0,font_size = 30).move_to(number[3*(i-1)+2],LEFT).shift(DOWN*0.5)
            self.add(number[3*i],number[3*i+1],number[3*i+2])

        b = ValueTracker(0)
        number[3].add_updater(lambda m: m.set_value(b.get_value()))
        number[4].add_updater(lambda m: m.set_value(func(b.get_value())))
        number[5].add_updater(lambda m: m.set_value(func2(b.get_value())))
        c = ValueTracker(0)
        number[6].add_updater(lambda m: m.set_value(c.get_value()))
        number[7].add_updater(lambda m: m.set_value(func(c.get_value())))
        number[8].add_updater(lambda m: m.set_value(func2(c.get_value())))
        d = ValueTracker(0)
        number[9].add_updater(lambda m: m.set_value(d.get_value()))
        number[10].add_updater(lambda m: m.set_value(func(d.get_value())))
        number[11].add_updater(lambda m: m.set_value(func2(d.get_value())))
        e = ValueTracker(0)
        number[12].add_updater(lambda m: m.set_value(e.get_value()))
        number[13].add_updater(lambda m: m.set_value(func(e.get_value())))
        number[14].add_updater(lambda m: m.set_value(func2(e.get_value())))
        f = ValueTracker(0)
        number[15].add_updater(lambda m: m.set_value(f.get_value()))
        number[16].add_updater(lambda m: m.set_value(func(f.get_value())))
        number[17].add_updater(lambda m: m.set_value(func2(f.get_value())))

        self.play(a.animate.set_value(2),b.animate.set_value(4),c.animate.set_value(8),d.animate.set_value(16),e.animate.set_value(32),f.animate.set_value(64), rum_time =8 )
        self.next_slide()

        l1 = Line(number[1].get_left(), number[1].get_right()).shift(DOWN*0.25).set_opacity(0.6).set_color(ORANGE)
        t1 = Tex(r" = 0.76", font_size=30, color = ORANGE).next_to(l1 )
        l2 = Line(number[5].get_left(), number[5].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t2 = Tex(r" = 0.25", font_size=30, color = ORANGE).next_to(l2 )
        self.play(Create(l1),Write(t1),Create(l2),Write(t2))
        self.next_slide()


        l3 = Line(number[7].get_left(), number[7].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t3 = Tex(r" = 0.31", font_size=30, color = ORANGE).next_to(l3)
        l4 = Line(number[8].get_left(), number[8].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t4 = Tex(r" = 0.25", font_size=30, color = ORANGE).next_to(l4 )
        self.play(Transform(l1,l3),Transform(t1,t3), Transform(l2,l4), Transform(t2,t4))
        self.next_slide()
        l3 = Line(number[10].get_left(), number[10].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t3 = Tex(r" = 0.28", font_size=30, color = ORANGE).next_to(l3 )
        l4 = Line(number[11].get_left(), number[11].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t4 = Tex(r" = 0.25", font_size=30, color = ORANGE).next_to(l4 )
        self.play(Transform(l1,l3),Transform(t1,t3), Transform(l2,l4), Transform(t2,t4))
        l3 = Line(number[13].get_left(), number[13].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t3 = Tex(r" = 0.27", font_size=30, color = ORANGE).next_to(l3 )
        l4 = Line(number[14].get_left(), number[14].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t4 = Tex(r" = 0.25", font_size=30, color = ORANGE).next_to(l4 )
        self.play(Transform(l1,l3),Transform(t1,t3), Transform(l2,l4), Transform(t2,t4))
        l3 = Line(number[16].get_left(), number[16].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t3 = Tex(r" = 0.26", font_size=30, color = ORANGE).next_to(l3 )
        l4 = Line(number[17].get_left(), number[17].get_right()).shift(UP*0.25).set_opacity(0.6).set_color(ORANGE)
        t4 = Tex(r" = 0.25", font_size=30, color = ORANGE).next_to(l4 )
        self.play(Transform(l1,l3),Transform(t1,t3), Transform(l2,l4), Transform(t2,t4))
        self.next_slide()

        w1 = Text("Both the functions have roughly same growth rate.",font_size=30,stroke_width=2).align_to(number[15], LEFT+UP).shift(DOWN*0.5)
        self.play(Write(w1),run_time=2)
        self.next_slide()
        w5 = Text("But Why?",font_size=30,stroke_width=2, color=RED).next_to(w1)
        self.play(Write(w5),run_time=2)
        self.next_slide()
        w6 = Tex(r"\text{The highest degree of} $n$ \text{is same.}",font_size=40,stroke_width=2, color=GREEN).align_to(w1, LEFT+UP).shift(DOWN*0.5)
        self.play(Write(w6),run_time=2)
        self.next_slide()

        self.play(FadeOut(w2,number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9],number[10],number[11],number[12],number[13],number[14],number[15],number[16],number[17],w1,w5,l1,l2,t1,t2))

        self.play(w3.animate.scale(2).shift(LEFT), w4.animate.scale(2).shift(RIGHT),w6.animate.scale(1.7).shift(UP))
        rect1 = Rectangle(width=0.2, height=0.4, color=MAROON).align_to(w3,LEFT+UP).shift(RIGHT*0.70)
        rect2 = Rectangle(width=0.2, height=0.4, color=MAROON).align_to(w4,LEFT+UP).shift(RIGHT*0.4)
        self.play(Create(rect1),Create(rect2))

        self.next_slide()
        self.play(FadeOut(w6,rect1,rect2,w3,w4))

        w1 = Tex("The growth rate of ", r"$n^2+6n$", " is less than the growith rate of ",  r"$n^3$").shift(UP*3)
        self.play(Write(w1), run_time=2)
        w2 = Tex(r"$n^2+6n = O(n^3)$").next_to(w1,DOWN)
        self.play(Write(w2), run_time=2)
        self.next_slide()
        w3 = Tex("Definition : ").align_to(w1,LEFT)
        w4 = Tex("If the growth rate of ", r"$f(n)$", " is less than or equal").next_to(w3)
        w5 = Tex("to the growth rate of ",r"$g(n),$", " then").align_to(w4,LEFT+UP ).shift(DOWN*0.5)
        newgroup = VGroup(w3,w4,w5)
        self.play(TransformFromCopy(w1,newgroup))
        self.next_slide()
        w6 = Tex(r"$f(n) = O(g(n))$").next_to(w5)
        self.play(TransformFromCopy(w2,w6))

        self.next_slide()
