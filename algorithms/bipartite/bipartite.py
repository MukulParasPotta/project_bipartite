from pickle import TRUE
from manim import *
import numpy as np
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

M_graph_edge_list = [(1,2),(2,3),(3,4),(4,5)]
A_graph_edge_list = [(1,2),(1,3),(2,3),(3,4),(1,5)]

class BipartiteGraph1(Slide):
    def construct(self):
        myBaseTemplate = TexTemplate(documentclass="\documentclass[preview]{standalone}")
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        myBaseTemplate.add_to_preamble(r"\usepackage{xcolor}")
        answer = Tex("This is a Bipartite Graph, while this is not.",font_size=50, stroke_width=2)
        M_graph = Graph(vertices=[1,2,4,5,3],edges=M_graph_edge_list,layout="circular",layout_scale=0.6).set_color(GREEN)
        self.play(Write(M_graph.shift(DOWN/2 + 2*LEFT)))
        A_graph = Graph(vertices=range(1,6),edges=A_graph_edge_list,layout="circular",layout_scale=0.6).set_color(RED).shift(DOWN/2 + 2*RIGHT)
        self.play(TransformFromCopy(M_graph, A_graph),run_time=2)
        
        graph_group = VGroup(M_graph, A_graph)
        question = Tex("What do you observe from these two graphs?",font_size=40, stroke_width=2).shift(0.5*UP)
        self.play(Write(question))
        self.next_slide()
        self.play(FadeOut(question))
        self.next_slide()

        question2 = Tex("How is this graph different from this graph?",font_size=40, stroke_width=2).shift(0.5*UP)
        self.play(Write(question2), run_time=3)
        self.play(Indicate(M_graph))
        M_graph.save_state()
        self.play(Indicate(A_graph))
        A_graph.save_state()
        self.next_slide()
        self.play(FadeOut(question2, M_graph, A_graph))
        

        M_graph.restore()
        M_graph.shift(2*UP)
        A_graph.restore()
        A_graph.shift(DOWN)
        header_group = VGroup(answer, graph_group)
        self.play(Write(header_group))
        self.play(Indicate(M_graph,color=GREEN))
        self.play(Indicate(A_graph,color=RED))

        self.next_slide()
        self.play(FadeOut(header_group))
        self.next_slide()

class IntervalScheduling2(Slide):
    def construct(self):
        l0 = NumberLine(
            x_range=[0, 48, 1],
            length=12,
            color=BLUE,
        )
        l0.align_to(np.array([-6,-1,0]),LEFT+UP)
        self.play(Create(l0))

        startingx=[-5.5,-4,-1.25,1.1,-6,-3.75,-1.5,1.3,3.15]
        startingy=[0,0,0,0,1,1,1,1,1]
        wid=[1,2,2,1.5,1.75,2,2.25,1.5,0.5]
        textinsideRectangle = [None]*9
        r = [None]*22
        for i in range(4):
            r[i] = Rectangle(height=0.4, width=wid[i], color=GREEN)
            r[i].align_to(np.array([startingx[i],startingy[i],0]),LEFT+UP)
            textinsideRectangle[i] = Tex("{$a_" + str(i+1) + "$", font_size=30, stroke_width=2).shift(r[i].get_center())
            self.play(Create(r[i]), Write(textinsideRectangle[i]))

        ourAnswer = Text("Our Answer", font_size=25, color=GREEN ).next_to(r[3]).shift(RIGHT)
        self.play(Write(ourAnswer))

        optimalAnswer = Text("Optimal Answer", font_size=25, color=RED).align_to(ourAnswer,LEFT).align_to(np.array([0,1,0]),UP)
        self.play(Create(optimalAnswer))
        r[4] = Rectangle(height=0.4, width=wid[4], color=RED)
        r[4].align_to(np.array([startingx[4],startingy[4],0]),LEFT+UP)
        textinsideRectangle[4] = Tex("{$o_1$", font_size=25,stroke_width=2).shift(r[4].get_center())

        self.play(Create(r[4]), Write(textinsideRectangle[4]))
        textinsideRectangle[4].add_updater(lambda x: x.move_to(r[4].get_center()))
        self.next_slide()
        q1 = Text("Can this happen?", font_size=25, color=RED).next_to(r[4], UP)
        r4copy = r[4].copy()
        self.play(Create(q1),r[4].animate.become(Rectangle(height=0.4,width=1, color=RED).align_to(np.array([startingx[4],startingy[4],0]),LEFT+UP)))
        self.next_slide()
        self.play(q1.animate.become(Text("No", font_size=25, color=GREEN)).next_to(r[4], UP))

        self.next_slide()
        self.play(FadeOut(q1),r[4].animate.become(r4copy))

        greenDashed = DashedLine(start=np.array([startingx[0]+wid[0],-1,0]), end=np.array([startingx[0]+wid[0],4,0]),color=GREEN )
        redDashed = DashedLine(start=np.array([startingx[4]+wid[4],-1,0]), end=np.array([startingx[4]+wid[4],4,0]),color=RED )
        self.play(GrowFromEdge(greenDashed,DOWN))
        self.play(GrowFromEdge(redDashed,DOWN))
        self.next_slide()
        better = Tex(r"$end(a_1) \le end(o_1)$",font_size=30).next_to(greenDashed, DOWN)
        self.play(Write(better))


        r[5] = Rectangle(height=0.4, width=wid[5], color=RED)
        r[5].align_to(np.array([startingx[5],startingy[5],0]),LEFT+UP)
        textinsideRectangle[5] = Tex("{$o_2$", font_size=25,stroke_width=2).shift(r[5].get_center())
        self.play(Create(r[5]), Write(textinsideRectangle[5]))
        textinsideRectangle[5].add_updater(lambda x: x.move_to(r[5].get_center()))
        self.next_slide()
        q1 = Text("Can this happen?", font_size=25, color=RED).next_to(r[5], UP)
        r5copy = r[5].copy()
        self.play(Create(q1),r[5].animate.become(Rectangle(height=0.4,width=1, color=RED).align_to(np.array([startingx[5],startingy[5],0]),LEFT+UP)))
        self.next_slide()
        self.play(q1.animate.become(Text("No", font_size=25, color=GREEN)).next_to(r[5], UP))
        self.next_slide()
        self.play(FadeOut(q1),r[5].animate.become(r5copy))
        self.play(redDashed.animate.shift(RIGHT*(startingx[5]+wid[5]-startingx[4]-wid[4])),greenDashed.animate.shift(RIGHT*(startingx[1]+wid[1]-startingx[0]-wid[0])))
        self.play(better.animate.become(Tex(r"$end(a_2) \le end(o_2)$",font_size=30).next_to(greenDashed, DOWN)))

        r[6] = Rectangle(height=0.4, width=wid[6], color=RED)
        r[6].align_to(np.array([startingx[6],startingy[6],0]),LEFT+UP)
        textinsideRectangle[6] = Tex("{$o_3$", font_size=25,stroke_width=2).shift(r[6].get_center())
        self.play(Create(r[6]), Write(textinsideRectangle[6]))
        textinsideRectangle[6].add_updater(lambda x: x.move_to(r[6].get_center()))
        self.next_slide()
        self.play(redDashed.animate.shift(RIGHT*(startingx[6]+wid[6]-startingx[5]-wid[5])),greenDashed.animate.shift(RIGHT*(startingx[2]+wid[2]-startingx[1]-wid[1])))
        self.play(better.animate.become(Tex(r"$end(a_3) \le end(o_3)$",font_size=30).next_to(greenDashed, DOWN)))
        self.next_slide()

        r[7] = Rectangle(height=0.4, width=wid[7], color=RED)
        r[7].align_to(np.array([startingx[7],startingy[7],0]),LEFT+UP)
        textinsideRectangle[7] = Tex("{$o_4$", font_size=25,stroke_width=2).shift(r[7].get_center())
        self.play(Create(r[7]), Write(textinsideRectangle[7]))
        textinsideRectangle[7].add_updater(lambda x: x.move_to(r[7].get_center()))
        self.next_slide()
        self.play(redDashed.animate.shift(RIGHT*(startingx[7]+wid[7]-startingx[6]-wid[6])),greenDashed.animate.shift(RIGHT*(startingx[3]+wid[3]-startingx[2]-wid[2])))
        self.play(better.animate.become(Tex(r"$end(a_4) \le end(o_4)$",font_size=30).next_to(greenDashed, DOWN)))
        self.next_slide()

        r[8] = Rectangle(height=0.4, width=wid[8], color=RED)
        r[8].align_to(np.array([startingx[8],startingy[8],0]),LEFT+UP)
        textinsideRectangle[8] = Tex("{$o_5$", font_size=25,stroke_width=2).shift(r[8].get_center())
        self.play(Create(r[8]), Write(textinsideRectangle[8]))
        q1 = Tex(r"Can $o_5$ exists?", font_size=35, color=RED).next_to(r[8], UP)
        self.play(Write(q1))
        self.next_slide()
        self.play(q1.animate.become(Text("No", font_size=25, color=GREEN)).next_to(r[8], UP))
        self.next_slide()
        self.play(FadeOut(q1),FadeOut(r[8]),FadeOut(textinsideRectangle[8]))
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )


class IntervalScheduling3(Slide):
    def construct(self):
        title = Title("Proof Strategy: Greedy is always better than Optimum", include_underline=TRUE)
        self.play(Write(title))
        self.next_slide()
        Util.cleanUp(self)

        lemma=Tex( "Lemma: ", "Let $a_1,a_2,\dots,a_k$ ", "be the the answer of our algorithm and ", "$o_1,o_2,\dots,o_{\ell}$ ", "be the optimum. Then, ", "$end(a_i) \le end(o_i)$ ", "for all ","$1 \le i \le k$.").set_height(0.6)
        lemma.set_color_by_tex_to_color_map({"Lemma":BLUE})
        lemma.align_to(np.array([-6.5,3,0]),LEFT+UP)
        line = Line(start = lemma.get_left(), end=lemma.get_right()).next_to(lemma, DOWN*0.5).set_opacity(0.5).set_color(BLUE)
        self.play(Write(lemma), GrowFromCenter(line), run_time=3)
        self.next_slide()
        proof = Tex("Proof: ", "By Induction on the number of classes in our answer.").set_height(0.3).next_to(lemma,DOWN).align_to(lemma,LEFT)
        proof[0].set_color(BLUE)
        line1 = Line(start = line.get_left(), end=line.get_right()).align_to(proof,LEFT+DOWN).shift(DOWN*0.2).set_opacity(0.5).set_color(BLUE)
        self.play(Write(proof),GrowFromCenter(line1))
        self.next_slide()
        base = Tex( "Base Case: ", "$i = 1$.").set_height(0.25).next_to(proof,DOWN).align_to(proof,LEFT)
        base[0].set_color(BLUE)
        self.play(Write(base))
        line2 = DashedLine(start = np.array([0,-4,0]), end=np.array([0,4,0]),color=RED).move_to(line1.get_right()).shift(RIGHT*0.1)
        self.play(GrowFromEdge(line2,DOWN))

        l0 = NumberLine(
            x_range=[0, 12, 1],
            length=3,
            color=BLUE,
        )
        l0.next_to(line1).shift(DOWN*2)
        r1 = Rectangle(height=0.25, width=1).set_color(GREEN)
        r1.align_to(l0.get_left(),LEFT+UP).shift(0.25*RIGHT+UP*0.5)
        textinsideRectangle1 = Tex("{$a_1$", font_size=25,stroke_width=2).shift(r1.get_center())

        r2 = Rectangle(height=0.25, width=1.25).set_color(RED)
        r2.align_to(l0.get_left(),LEFT+UP).shift(0.75*RIGHT+UP)
        textinsideRectangle2 = Tex("{$o_1$", font_size=25,stroke_width=2).shift(r2.get_center())

        self.play(Create(l0),Create(r2),Create(r1),Create(textinsideRectangle1),Create(textinsideRectangle2))
        self.next_slide()

        base1 = Tex("Since our algorithm chooses the first interval with least ending time, $end(o_1) \le end(a_1)$").set_height(0.6).next_to(base,DOWN).align_to(base,LEFT)
        line3 = Line(start = line.get_left(), end=line.get_right()).align_to(base1,LEFT+DOWN).shift(DOWN*0.2).set_opacity(0.5).set_color(BLUE)
        self.play(Create(base1),GrowFromCenter(line3))
        self.next_slide()

        induction = Tex("Induction hypothesis: ", "$end(a_i) \le end(o_i)$ ", "for all ", "$i < {\ell}$.").set_height(0.3).next_to(base1,DOWN).align_to(base1,LEFT)
        induction[0].set_color(BLUE)
        self.play(Write(induction))
        copytextinsideRectangle1 = Tex("{$a_{i}$", font_size=25,stroke_width=2).shift(r1.get_center())
        copytextinsideRectangle2 = Tex("{$o_{i}$", font_size=25,stroke_width=2).shift(r2.get_center())

        self.play(Rotate(l0,PI),Rotate(r1,PI), Rotate(r2,PI),textinsideRectangle1.animate.become(copytextinsideRectangle1), textinsideRectangle2.animate.become(copytextinsideRectangle2))

        r3 = Rectangle(height=0.25, width=0.75).set_color(RED)
        r3.align_to(r2,LEFT+UP).shift(1.5*RIGHT)
        textinsideRectangle3 = Tex("{$o_{i+1}$", font_size=25,stroke_width=2).shift(r3.get_center())
        self.next_slide()

        induction1 = Tex("This implies that ", "$start(o_{i+1}) > end(a_{i})$.").set_height(0.3).next_to(induction,DOWN).align_to(induction,LEFT)
        induction2 = Tex("Thus, our algorithm could also have choosen $o_{i+1}$ as the next interval. Thus, $end(a_{i+1}) \le end(o_{i+1})$").set_height(0.6).next_to(induction1,DOWN).align_to(induction1,LEFT)

        self.play(Create(r3),Write(textinsideRectangle3))
        self.play(Write(induction1))
        self.next_slide()

        line4 = Line(start = line.get_left(), end=line.get_right()).align_to(induction2,LEFT+DOWN).shift(DOWN*0.2).set_opacity(0.5).set_color(BLUE)
        r4 = Rectangle(height=0.25, width=0.75).set_color(GREEN)
        r4.align_to(r1,LEFT+UP).shift(1.5*RIGHT)
        textinsideRectangle4 = Tex("{$a_{i+1}$", font_size=25,stroke_width=2).shift(r4.get_center())
        self.play(Write(induction2),GrowFromCenter(line4),Create(r4),Create(textinsideRectangle4))

        self.next_slide()
        corollary = Tex("Corollary: ", "Let $a_1,a_2,\dots,a_k$ ", "be the the answer of our algorithm and ", "$o_1,o_2,\dots,o_{\ell}$ ", "be the optimum. Then, $k = \ell$." )
        corollary.set_color_by_tex_to_color_map({"Corollary":BLUE}).set_height(0.6).next_to(induction2,DOWN).align_to(induction2,LEFT)

        self.play(Write(corollary))

class IntervalScheduling4(Slide):
    def construct(self):
        title = Title("Proof Strategy: The Exchange Argument")
        self.play(Write(title))
        self.next_slide()
        Util.cleanUp(self)
        l0 = NumberLine(
            x_range=[0, 48, 1],
            length=12,
            color=BLUE,
        )
        l0.align_to(np.array([-6,-1,0]),LEFT+UP)
        self.play(Create(l0))

        startingx=[-5.5,-4,-1.25,1.1,-6,-3.75,-1.5,1.3,3.15]
        startingy=[0,0,0,0,1,1,1,1,1]
        wid=[1,2,2,1.5,1.75,2,2.25,1.5,0.5]
        textinsideRectangle = [None]*9
        r = [None]*22
        for i in range(4):
            r[i] = Rectangle(height=0.4, width=wid[i], color=GREEN)
            r[i].align_to(np.array([startingx[i],startingy[i],0]),LEFT+UP)
            textinsideRectangle[i] = Tex("{$a_" + str(i+1) + "$", font_size=30, stroke_width=2).shift(r[i].get_center())
            self.play(Create(r[i]), Write(textinsideRectangle[i]))

        textinsideRectangle[0].add_updater(lambda x: x.move_to(r[0].get_center()))
        textinsideRectangle[1].add_updater(lambda x: x.move_to(r[1].get_center()))
        textinsideRectangle[2].add_updater(lambda x: x.move_to(r[2].get_center()))
        textinsideRectangle[3].add_updater(lambda x: x.move_to(r[3].get_center()))

        ourAnswer = Text("Our Answer", font_size=25, color=GREEN ).next_to(r[3]).shift(RIGHT)
        self.play(Write(ourAnswer))

        optimalAnswer = Text("Optimal Answer", font_size=25, color=RED).align_to(ourAnswer,LEFT).align_to(np.array([0,1,0]),UP)
        self.play(Create(optimalAnswer))
        r[4] = Rectangle(height=0.4, width=wid[4], color=RED)
        r[4].align_to(np.array([startingx[4],startingy[4],0]),LEFT+UP)
        textinsideRectangle[4] = Tex("{$o_1$", font_size=25,stroke_width=2).shift(r[4].get_center())

        self.play(Create(r[4]), Write(textinsideRectangle[4]))
        textinsideRectangle[4].add_updater(lambda x: x.move_to(r[4].get_center()))
        greenDashed = DashedLine(start=np.array([startingx[0]+wid[0],-1,0]), end=np.array([startingx[0]+wid[0],4,0]),color=GREEN )
        redDashed = DashedLine(start=np.array([startingx[4]+wid[4],-1,0]), end=np.array([startingx[4]+wid[4],4,0]),color=RED )
        self.play(GrowFromEdge(greenDashed,DOWN))
        self.play(GrowFromEdge(redDashed,DOWN))

        better = Tex(r"$end(a_1) \le end(o_1)$",font_size=30).next_to(greenDashed, DOWN)
        self.play(Write(better))
        self.next_slide()

        self.play(r[4].animate.set_opacity(0.2),textinsideRectangle[4].animate.set_opacity(0.2),r[0].animate.shift(UP))
        observation = Tex("Observation: ", "There is an optimum that starts wiith $a_1$.").align_to(l0, LEFT+UP).shift(DOWN).set_height(0.3)
        observation[0].set_color(BLUE)
        self.play(Write(observation))
        self.next_slide()

        r[5] = Rectangle(height=0.4, width=wid[5], color=RED)
        r[5].align_to(np.array([startingx[5],startingy[5],0]),LEFT+UP)
        textinsideRectangle[5] = Tex("{$o_2$", font_size=25,stroke_width=2).shift(r[5].get_center())
        self.play(Create(r[5]), Write(textinsideRectangle[5]))
        textinsideRectangle[5].add_updater(lambda x: x.move_to(r[5].get_center()))

        self.play(redDashed.animate.shift(RIGHT*(startingx[5]+wid[5]-startingx[4]-wid[4])),greenDashed.animate.shift(RIGHT*(startingx[1]+wid[1]-startingx[0]-wid[0])))
        self.play(better.animate.become(Tex(r"$end(a_2) \le end(o_2)$",font_size=30).next_to(greenDashed, DOWN)))
        self.next_slide()

        self.play(r[5].animate.set_opacity(0.2),textinsideRectangle[5].animate.set_opacity(0.2),r[1].animate.shift(UP))
        observationcopy = Tex("Observation: ", "There is an optimum that starts wiith $a_1,a_2$.").align_to(l0, LEFT+UP).shift(DOWN).set_height(0.3)
        observationcopy[0].set_color(BLUE)
        self.play(observation.animate.become(observationcopy))
        self.next_slide()

        r[6] = Rectangle(height=0.4, width=wid[6], color=RED)
        r[6].align_to(np.array([startingx[6],startingy[6],0]),LEFT+UP)
        textinsideRectangle[6] = Tex("{$o_3$", font_size=25,stroke_width=2).shift(r[6].get_center())
        self.play(Create(r[6]), Write(textinsideRectangle[6]))
        textinsideRectangle[6].add_updater(lambda x: x.move_to(r[6].get_center()))
        self.next_slide()
        self.play(redDashed.animate.shift(RIGHT*(startingx[6]+wid[6]-startingx[5]-wid[5])),greenDashed.animate.shift(RIGHT*(startingx[2]+wid[2]-startingx[1]-wid[1])))
        self.play(better.animate.become(Tex(r"$end(a_3) \le end(o_3)$",font_size=30).next_to(greenDashed, DOWN)))
        self.next_slide()
        self.play(r[6].animate.set_opacity(0.2),textinsideRectangle[6].animate.set_opacity(0.2),r[2].animate.shift(UP))
        observationcopy = Tex("Observation: ", "There is an optimum that starts wiith $a_1,a_2,a_3$.").align_to(l0, LEFT+UP).shift(DOWN).set_height(0.3)
        observationcopy[0].set_color(BLUE)
        self.play(observation.animate.become(observationcopy))

        r[7] = Rectangle(height=0.4, width=wid[7], color=RED)
        r[7].align_to(np.array([startingx[7],startingy[7],0]),LEFT+UP)
        textinsideRectangle[7] = Tex("{$o_4$", font_size=25,stroke_width=2).shift(r[7].get_center())
        self.play(Create(r[7]), Write(textinsideRectangle[7]))
        textinsideRectangle[7].add_updater(lambda x: x.move_to(r[7].get_center()))
        self.next_slide()
        self.play(redDashed.animate.shift(RIGHT*(startingx[7]+wid[7]-startingx[6]-wid[6])),greenDashed.animate.shift(RIGHT*(startingx[3]+wid[3]-startingx[2]-wid[2])))
        self.play(better.animate.become(Tex(r"$end(a_4) \le end(o_4)$",font_size=30).next_to(greenDashed, DOWN)))
        self.next_slide()
        self.play(r[7].animate.set_opacity(0.2),textinsideRectangle[7].animate.set_opacity(0.2),r[3].animate.shift(UP))
        observationcopy = Tex("Observation: ", "There is an optimum that starts wiith $a_1,a_2,a_3,a_4$.").align_to(l0, LEFT+UP).shift(DOWN).set_height(0.3)
        observationcopy[0].set_color(BLUE)
        self.play(observation.animate.become(observationcopy))
        self.next_slide()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        title = Title("Homework: Try to write in your own words.")
        lemma = Tex("Lemma: ", "Let $a_1,a_2,\dots,a_{\ell}$ be the our answer, then for all $1 \le i \le \ell$, there is an optimum that starts with $a_1,a_2, \dots, a_i$.").move_to(np.array([0,2,0])).set_height(0.8)
        lemma[0].set_color(BLUE)
        self.play(Write(title),Write(lemma))

        corollary = Tex("Corollary: ", "Let $a_1,a_2,\dots,a_k$ ", "be the the answer of our algorithm and ", "$o_1,o_2,\dots,o_{\ell}$ ", "be the optimum. Then, $k = \ell$." )
        corollary.set_color_by_tex_to_color_map({"Corollary":BLUE}).set_height(0.8).next_to(lemma,DOWN).align_to(lemma,LEFT)
        self.play(Write(corollary))

class IntervalScheduling5(Slide):
    def construct(self):
        title = Title("Implementing the Greedy Algorithm")
        self.play(Write(title))
        self.next_slide()
        Util.cleanUp(self)
        code_scale = 0.8
        buffer=0.5
        map = {"$\le$": GREEN, "$n$":GOLD,"$S$": GOLD, "$\leftarrow$":GREEN,";":RED, "$i$":GOLD, "\{":ORANGE,"\}":ORANGE,"\cup":GREEN,"while":RED_D,"if":RED_D}
        code = []
        code.append(("\\text{Sort the interval based on their end times}",";"))
        code.append(("$S$", "$\leftarrow$", "First interval in the sorted order",";"))
        code.append(("$i$", "$\leftarrow$", "\\text{2}",";"))
        code.append(("while ","(","$i$", "$\le$", "$n$",")"))
        code.append(("","$\{$"))
        code.append(("if","(","$i$", "\\text{-th interval does not overlap with the last interval in} ", "$S$",")"))
        code.append(("$S$", "$\leftarrow$", "$S$", "$\cup$", "$\{$", "$i$", "\\text{-th interval}", "$\}$", ";"))
        code.append(("","$\}$"))
        line = [None]*8
        linenumber = [None]*8
        surround = [None]*8
        for i in range(len(line)):
            line[i] = Tex(*[x for x in code[i]])
            line[i].scale(code_scale)
            line[i].set_color_by_tex_to_color_map(map)
            linenumber[i] = Tex(str(i+1))
            linenumber[i].scale(code_scale*0.7)

            if i == 0:
                linenumber[i].shift(np.array([-4,3,0])).to_edge(LEFT)
                line[i].shift(np.array([-4,3,0])).to_edge(LEFT).shift(RIGHT*0.5)
            elif i==5:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],LEFT+DOWN).shift(DOWN*buffer).shift(RIGHT*0.5)
            elif i==6:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],LEFT+DOWN).shift(DOWN*buffer).shift(RIGHT)
            elif i==7:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],DOWN).align_to(line[0],LEFT).shift(DOWN*buffer)
            else:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],LEFT+DOWN).shift(DOWN*buffer)
            surround[i]=SurroundingRectangle(linenumber[i],corner_radius=0.1,color=MAROON)

        self.play(*[Write(x) for x in line],*[Create(x) for x in linenumber],*[Create(x) for x in surround] )
        self.next_slide()
        q1 = Text("What is the running time of the algorithm?", color=RED, font_size=30).align_to(linenumber[7], LEFT+DOWN).shift(DOWN)
        self.play(Write(q1))
        self.next_slide()
        ans = Text("Dominated by sorting in the first line.", color=GREEN, font_size=30).align_to(q1, LEFT+DOWN).shift(DOWN*0.5)
        s = surround[0].copy().move_to(surround[0].get_center()).set_color(YELLOW_E).set(stroke_width=7)
        self.play( Write(ans),Create(s))
        self.next_slide()
        ans1 = Tex("$O(n \log n)$", color=GREEN, font_size=30).align_to(q1, LEFT+DOWN).shift(DOWN*0.5)
        self.play(ans.animate.become(ans1))
        self.play(Uncreate(s))
        self.next_slide()
