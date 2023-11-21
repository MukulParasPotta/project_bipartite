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
M_graph = Graph(vertices=[1,2,4,5,3],edges=M_graph_edge_list,layout="circular",layout_scale=0.6).set_color(GREEN)
A_graph_edge_list = [(1,2),(1,3),(2,3),(3,4),(1,5)]
A_graph = Graph(vertices=range(1,6),edges=A_graph_edge_list,layout="circular",layout_scale=0.6).set_color(RED)

def move_to_origin():
    M_graph.move_to(ORIGIN)
    A_graph.move_to(ORIGIN)

class BipartiteGraph(Slide):
    def construct(self):
        self.introduction()
        self.inspiration()
        self.definition()
        self.odd_cycle_property()
        self.no_odd_cycle_argument()
        self.how_to_decide()
        self.algorithm()
        self.conclusion()

    def introduction(self):
        heading = Tex("Bipartite Graphs", "\\\\and how to identify them").shift(UP)
        subheading = Tex("Presented by:\\\\Anshika Saxena (23210018)","\\\\Mukul Paras Potta (23210061)").scale(0.8).shift(3 * DOWN)
        # prof_name = Tex("Prof. Manoj Gupta").next_to(subheading, UP)
        self.play(Write(heading))
        self.play(Write(subheading))
        self.next_slide()
        Util.cleanUp(self)
    
    def inspiration(self):
        myBaseTemplate = TexTemplate(documentclass="\documentclass[preview]{standalone}")
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        myBaseTemplate.add_to_preamble(r"\usepackage{xcolor}")
        move_to_origin()
        answer = Tex("One of them is a Bipartite Graph! Any guesses?",font_size=50, stroke_width=2)
        self.play(Write(M_graph.shift(DOWN/2 + 2*LEFT)), run_time=2)
        A_graph.shift(DOWN/2 + 2*RIGHT)
        self.play(TransformFromCopy(M_graph, A_graph), run_time=2)
        
        graph_group = VGroup(M_graph, A_graph)
        question = Tex("What do you observe from these two graphs?",font_size=40, stroke_width=2).shift(UP)
        self.play(Write(question), run_time=2)
        self.next_slide()
        self.play(FadeOut(question))
        #self.next_slide()

        question2 = Tex("How is this graph different from this graph?",font_size=40, stroke_width=2).shift(UP)
        self.play(Write(question2), run_time=3)
        self.play(Indicate(M_graph))
        M_graph.save_state()
        self.play(Indicate(A_graph))
        A_graph.save_state()
        self.next_slide()
        self.play(FadeOut(question2, M_graph, A_graph))
        

        M_graph.restore()
        M_graph.shift(2.5*UP)
        A_graph.restore()
        A_graph.shift(DOWN)
        header_group = VGroup(answer, graph_group)
        self.play(Write(header_group))
        self.play(Indicate(graph_group))

        self.next_slide()
        self.play(FadeOut(answer))
        answer = Tex("This one is! But... why?")
        self.play(Write(answer), Indicate(M_graph))
        self.next_slide()
        Util.cleanUp(self)

    def definition(self):
        what = Tex(r"Before that, what does it mean for a graph $G$ to be bipartite?",
                   tex_environment=None,
                   tex_template=TexTemplateLibrary.threeb1b)
        what2 = Tex(r"If a graph $G$ is bipartite, vertices in $G$ can be split \\ \
                   into two sets $X$ and $Y$ such that:",
                   tex_environment=None,
                   tex_template=TexTemplateLibrary.threeb1b)
        what2.shift(1.1*LEFT)
        move_to_origin()
        self.play(Write(what), run_time=3)
        self.next_slide()
        self.play(FadeOut(what))
        self.play(Write(what2), run_time=3)
        self.next_slide()
        self.play(what2.animate.shift(3*UP))
        properties = Tex(
            "\item There are $some$ edges (possibly $none$) \\\\ connecting vertices in $X$ with those in $Y$.\item There are no edges connecting vertices within $X$ or $Y$.", 
            tex_environment="enumerate",
            tex_template=TexTemplateLibrary.threeb1b)
        self.play(Write(properties.align_on_border(LEFT).next_to(what2, DOWN)), run_time=4)
        self.next_slide()
        M_graph.shift(2 * DL)
        A_graph.change_layout(layout="circular",layout_scale=0.75).shift(2 * DR)
        self.play(Write(M_graph), Write(A_graph))
        self.next_slide()
        self.play( 
                M_graph.animate
                    .change_layout("partite", partitions=[[2,4],[1,5,3]], layout_scale=0.75).shift(2 * DL),
            run_time=3
        )
        self.next_slide()
        self.play(Wiggle(A_graph), run_time=2)
        self.next_slide()
        self.play(FadeOut(what2, properties))
        #self.play(VGroup(what, properties).animate.scale(0.45).shift(3 * LEFT + UP))
        question = Tex(r"Notice anything", r" else", " in this graph? \\ Why is this ", "$not$ ", "bipartite?",
                       tex_template=TexTemplateLibrary.threeb1b)
        question[1].set_color(RED)
        question[3].set_color(RED)
        question.shift(2 * UP)
        self.play(A_graph.animate.move_to(ORIGIN).scale(2), FadeOut(M_graph), run_time=2)
        self.play(Write(question), run_time=2)
        self.next_slide()
        self.play(FadeOut(question))
        self.next_slide()
        answer = Tex("Here, vertices cannot be split into two sets because it contains an ", "odd ", "cycle!").scale(0.85)
        answer[1].set_color(RED)
        answer.shift(2 * UP)
        cycle_group = VGroup(A_graph.edges[(1,2)],A_graph.edges[(1,3)],A_graph.edges[(2,3)],A_graph.vertices[1],A_graph.vertices[2],A_graph.vertices[3])
        self.play(Write(answer))
        self.play(Indicate(cycle_group, rate_func=rate_functions.there_and_back_with_pause))
        self.next_slide()
        Util.cleanUp(self)

    def odd_cycle_property(self):
        text = Tex("Property: ","If a graph G is Bipartite,then it cannot ").align_on_border(UL)
        # underline_1="Property"
        text2= Tex(" contain an odd cycle").next_to(text,DOWN)
        text1= Tex("Proof :      By Contradiction               ").next_to(text2, DOWN)
        text3= Tex("Let us assume that this graph is bipartite:").align_on_border(UP)
        #.next_to(text,LEFT,buff=1)
        # text1.move_to(LEFT*2.8)
        # text1.to_corner(LEFT*2.9)
        # text2.move_to(UL*1.2)
        # text3.move_to(DL*0.8)
        
        # index_to_underline = text.text.index(underline_1)

        # Create an Underline object for the specified word
        underline = Underline(text[0], color=WHITE)

        # Add the Text and Underline objects to the scene
        self.play(Write(text), Create(underline))
        self.play(Write(text2))
        self.next_slide()
        # text1.move_to(LEFT*2.3)
        self.play(Write(text1))
        self.next_slide()
        self.play(FadeOut(text,underline,text2,text1))

        self.play(Write(text3))
        cycle5 = Graph([1,2,3,4,5],[(1,2),(2,3),(3,4),(4,5),(5,1)],layout="circular",labels=True)
        self.play(Create(cycle5))
        self.next_slide()
        t1 = Tex("Pick a vertex, and assume it is in", " set A")
        t1[1].set_color(RED)
        t1.shift(3 * DOWN)
        self.play(cycle5.vertices[1].animate.set_color(RED, family=False),Write(t1),FadeOut(text3))
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("Then its neighbour goes to", " set B")
        t1[1].set_color(BLUE)
        t1.shift(3 * DOWN)
        # print(cycle5.edges[(1,2)].animate.set_color_by_gradient(RED, BLUE))
        self.play(# cycle5.edges[(1,2)].animate.set_color(color=[RED, BLUE]),
                #   cycle5.edges[(5,1)].animate.set_color(color=[BLUE, RED]),
                  cycle5.vertices[2].animate.set_color(BLUE, family=False),
                #   cycle5.vertices[5].animate.set_color(BLUE),
                  Write(t1)
                )
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("And so on...")
        t1.shift(3 * DOWN)
        # print(cycle5.edges[(1,2)].animate.set_color_by_gradient(RED, BLUE))
        self.play(# cycle5.edges[(2,3)].animate.set_color(color=[BLUE, RED]),
                #   cycle5.edges[(3,4)].animate.set_color(color=[RED, BLUE]),
                  cycle5.vertices[3].animate.set_color(RED, family=False),
                  cycle5.vertices[4].animate.set_color(BLUE, family=False),
                  Write(t1)
                )
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("Until ", "now",". Which set does this belong to?")
        t1[1].set_color(YELLOW)
        t1.shift(3 * DOWN)
        self.play(cycle5.vertices[5].animate.set_color(YELLOW, family=False),
                #   cycle5.vertices[4].animate.set_color(YELLOW),
                #   cycle5.edges[(3,4)].animate.set_color(YELLOW),
                #   cycle5.edges[(5,1)].animate.set_color(color=[RED,YELLOW]),
                #   cycle5.edges[(4,5)].animate.set_color(color=[BLUE,YELLOW]),
                  Write(t1)
                )
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("Can it be in ", "either", " set?")
        t1[1].set_color(GREEN)
        t1.shift(3 * DOWN)
        self.play(Write(t1))
        self.next_slide()
        t2 = Tex("No! This is a contradiction")
        t2.shift(3 * DOWN)
        self.play(Transform(t1,t2))
        self.play(FadeOut(t2))
        self.next_slide()
        self.wait(2)
        Util.cleanUp(self)

    def no_odd_cycle_argument(self):
        # Create the text with the argument
        argument_text = Tex("Argument",": If a graph has no odd cycle, then it is Bipartite").align_on_border(UP)


        # Find the index of the word to underline
        # word_to_underline = "Argument"
        # index_to_underline = argument_text.text.index(word_to_underline)

        # Create an Underline object for the specified word
        underline = Underline(argument_text[0], color=WHITE)

        # Add the Text and Underline objects to the scene
        self.play(Write(argument_text), Create(underline))
        self.next_slide()
        argument_text1 = Tex(
                "To prove the above argument, we take a graph G with a set of vertices and edges. "
                "Divide the vertices into two sets in such a way that one endpoint of each edge belongs to set A "
                "and the other endpoint belongs to set B. There are no edges with both end points within a set."
            ).scale(0.75)
        self.play(Write(argument_text1), run_time=3)
        t1 = Tex("Consider below two graphs:").next_to(argument_text, DOWN)
        self.next_slide()
        self.play(FadeOut(argument_text1))
        self.play(Write(t1))

        no_cycle_graph = Graph([1,2,3,4,5,6],[(1,2),(2,3),(3,4),(3,5),(2,6)],layout="circular",layout_scale=0.85).shift(4 * LEFT)
        even_cycle_graph = Graph([1,2,3,4,5,6],[(1,2),(2,3),(3,4),(3,5),(2,6),(1,4),(5,6)],layout="circular",layout_scale=0.85).shift(4 * RIGHT)

        self.play(Create(no_cycle_graph),Create(even_cycle_graph),FadeOut(t1))
        t1 = Tex("Is any one of these graphs bipartite?").shift(3 * DOWN)
        self.play(Write(t1))
        self.next_slide()
        self.play(FadeOut(t1),no_cycle_graph.animate.move_to(ORIGIN).scale(2),FadeOut(even_cycle_graph,target_position=8*RIGHT,scale=0.2))
        self.play(no_cycle_graph.animate.change_layout(layout="partite",partitions=[[1,3,6],[2,4,5]],layout_scale=2))
        self.next_slide()
        o_1 = Ellipse(width=1, height=4.5, color=GREEN_B).move_to(no_cycle_graph.vertices[3].get_center())
        o_2 = Ellipse(width=1, height=4.5, color=GREEN_B).move_to(no_cycle_graph.vertices[4].get_center())
        t1 = Tex("Observe there are no cycles in this graph").shift(3 * DOWN)
        self.play(Write(o_1),Write(o_2),Write(t1))
        self.next_slide()
        t2 = Tex("This one is bipartite!").shift(3 * DOWN)
        self.next_slide()
        self.play(Transform(t1,t2,replace_mobject_with_target_in_scene=True))
        self.next_slide()
        t3 = Tex("What about the other one?").shift(3 * DOWN)
        self.play(Transform(t2,t3,replace_mobject_with_target_in_scene=True),FadeOut(o_1,o_2),FadeOut(no_cycle_graph,target_position=8*LEFT,scale=0.2))
        self.play(even_cycle_graph.animate.move_to(ORIGIN).scale(2))
        self.next_slide()
        self.wait(2)
        t1 = Tex("This graph has only even length cycles").shift(3 * DOWN)
        self.play(Transform(t3,t1,replace_mobject_with_target_in_scene=True))
        self.play(Indicate(VGroup(
                even_cycle_graph.vertices[5],
                even_cycle_graph.vertices[2],
                even_cycle_graph.vertices[3],
                even_cycle_graph.vertices[6],
                even_cycle_graph.edges[(2,6)],
                even_cycle_graph.edges[(2,3)],
                even_cycle_graph.edges[(3,5)],
                even_cycle_graph.edges[(5,6)]),
                rate_func=rate_functions.there_and_back_with_pause
            )
        )
        self.play(Indicate(VGroup(
                even_cycle_graph.vertices[1],
                even_cycle_graph.vertices[2],
                even_cycle_graph.vertices[3],
                even_cycle_graph.vertices[4],
                even_cycle_graph.edges[(1,2)],
                even_cycle_graph.edges[(2,3)],
                even_cycle_graph.edges[(3,4)],
                even_cycle_graph.edges[(1,4)]),
                rate_func=rate_functions.there_and_back_with_pause
            )
        )
        self.play(Indicate(VGroup(
                even_cycle_graph.vertices[5],
                even_cycle_graph.vertices[2],
                even_cycle_graph.vertices[3],
                even_cycle_graph.vertices[6],
                even_cycle_graph.vertices[1],
                even_cycle_graph.vertices[4],
                even_cycle_graph.edges[(1,2)],
                even_cycle_graph.edges[(2,6)],
                even_cycle_graph.edges[(3,5)],
                even_cycle_graph.edges[(3,4)],
                even_cycle_graph.edges[(1,4)],
                even_cycle_graph.edges[(5,6)]),
                rate_func=rate_functions.there_and_back_with_pause
            )
        )
        self.next_slide()
        self.play(even_cycle_graph.animate.change_layout(layout="partite",partitions=[[1,3,6],[2,4,5]],layout_scale=2))
        o_1 = Ellipse(width=1, height=4.5, color=GREEN_B).move_to(even_cycle_graph.vertices[3].get_center())
        o_2 = Ellipse(width=1, height=4.5, color=GREEN_B).move_to(even_cycle_graph.vertices[4].get_center())
        t2 = Tex("This is bipartite as well!").shift(3 * DOWN)
        self.play(Transform(t1,t2,replace_mobject_with_target_in_scene=True),Write(o_1),Write(o_2))
        self.next_slide()
        Util.cleanUp(self)

    def how_to_decide(self):
        # Define the vertices and edges
        Vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        Edges = [(1, 2), (1, 3), (1, 5), (2, 6), (2, 4), (3, 7), (3, 4), (5, 6), (5, 7), (6, 8), (5, 7),(4,8)]

        t1 = Tex("How to decide whether a graph is bipartite?").align_on_border(UP)
        self.play(Write(t1))
        self.next_slide()
        t2 = Tex("Given what we know, we need to check for odd cycles!")
        self.play(Write(t2))
        self.next_slide()
        t3 = Tex("If odd cycles exist : graph is not bipartite.").next_to(t2,DOWN)
        t4 = Tex("Otherwise graph is bipartite.").next_to(t3,DOWN)
        self.play(FadeOut(t1), Write(t3),Write(t4))
        self.next_slide()
        Util.cleanUp(self)
        t1 = Tex("How to check for odd cycles?").align_on_border(UP)
        self.play(Write(t1))
        self.next_slide()
        t2 = Tex("We can use BFS to check for odd cycles!")
        self.play(Write(t2))
        self.next_slide()
        t3 = Tex("BFS traverses the graph in levels.")
        t4 = Tex("We can put vertices from even-numbered levels in set A,").next_to(t3,DOWN)
        t5 = Tex("and those from odd-numbered levels in set B.").next_to(t4,DOWN)
        text_group = VGroup(t3,t4,t5).shift(4 * LEFT + 2 * UP).scale(0.5)
        self.play(Transform(t2,t3))
        example_graph = Graph(Vertices, Edges, labels=True, layout="kamada_kawai")
        example_graph.shift(4*RIGHT).scale(0.85)
        self.play(FadeOut(t3),FadeIn(example_graph))
        self.next_slide()
        partitions = [[1],[2,3,5],[4,6,7],[8]]
        partitions.reverse()
        self.play(FadeIn(text_group[0]), example_graph.animate.change_layout(layout="partite",partitions=partitions,layout_config={'align':"horizontal"}).shift(4 * RIGHT))
        to_make_tree = [(3,4),(5,6),(5,7),(6,8)]
        self.play(example_graph.vertices[1].animate.set_color(GREEN, family=False))
        for edge in Edges:
            if edge not in to_make_tree:
                self.play(example_graph.edges[edge].animate.set_color(GREEN))
                self.play(example_graph.vertices[edge[1]].animate.set_color(GREEN, family=False))
        self.next_slide()
        l0 = Tex("L0").move_to(example_graph.vertices[1].get_center() + 1.75 * LEFT)
        l1 = Tex("L1").move_to(example_graph.vertices[5].get_center() + 0.75 * LEFT)
        l2 = Tex("L2").move_to(example_graph.vertices[7].get_center() + 0.75 * LEFT)
        l3 = Tex("L3").move_to(example_graph.vertices[8].get_center() + 1.75 * LEFT)
        self.play(FadeIn(text_group[1]), 
                  example_graph.vertices[1].animate.set_color(RED, family=False),
                  example_graph.vertices[4].animate.set_color(RED, family=False),
                  example_graph.vertices[6].animate.set_color(RED, family=False),
                  example_graph.vertices[7].animate.set_color(RED, family=False),
                  FadeIn(l0),
                  FadeIn(l2)
                )
        self.next_slide()
        self.play(FadeIn(text_group[2]), 
                  example_graph.vertices[2].animate.set_color(BLUE, family=False),
                  example_graph.vertices[3].animate.set_color(BLUE, family=False),
                  example_graph.vertices[5].animate.set_color(BLUE, family=False),
                  example_graph.vertices[8].animate.set_color(BLUE, family=False),
                  FadeIn(l1),
                  FadeIn(l3)
                )
        self.next_slide()
        t1 = Tex("Can such an edge", " exist","?").shift(3 * DOWN)
        t1[1].set_color(YELLOW)
        self.play(example_graph.animate.add_edges(*[(1,8)], edge_type=ArcBetweenPoints))
        self.play(example_graph.edges[(1,8)].animate.set_color(YELLOW),
                  Write(t1)
                )
        self.next_slide()
        t2 = Tex("Then that vertex would be part of L1!").shift(3 * DOWN)
        self.play(Transform(t1,t2))
        partitions1 = [[1],[2,3,5,8],[4,6,7]]
        partitions1.reverse()
        self.play(FadeOut(l3),example_graph.animate.change_layout(layout="partite",partitions=partitions1,layout_config={'align':"horizontal"}).shift(4 * RIGHT))
        self.next_slide()
        self.play(Transform(t2,t1,replace_mobject_with_target_in_scene=True),FadeIn(l3))
        self.play(example_graph.animate.remove_edges(*[(1,8)]),example_graph.animate.change_layout(layout="partite",partitions=partitions,layout_config={'align':"horizontal"}).shift(4 * RIGHT))
        self.play(example_graph.animate.add_edges(*[(4,6)], edge_type=ArcBetweenPoints))
        self.play(example_graph.edges[(4,6)].animate.set_color(YELLOW))
        t2 = Tex("This is an edge within a level, and creates an odd cycle!").shift(3 * DOWN)
        self.play(Transform(t1,t2))
        self.play(
            Indicate(
                VGroup(
                    example_graph.vertices[4],
                    example_graph.vertices[6],
                    example_graph.vertices[8],
                    example_graph.edges[(4,8)],
                    example_graph.edges[(4,6)],
                    example_graph.edges[(6,8)]
                ),
                rate_func=rate_functions.there_and_back_with_pause
            )
        )
        self.next_slide()
        self.play(Transform(t2,t1,replace_mobject_with_target_in_scene=True),example_graph.animate.remove_edges(*[(4,6)]))
        self.play(example_graph.animate.add_edges(*[(1,7)], edge_type=ArcBetweenPoints))
        self.play(example_graph.edges[(1,7)].animate.set_color(YELLOW))
        t2 = Tex("This is an edge across levels, which creates an odd cycle!").shift(3 * DOWN)
        self.play(Transform(t1,t2))
        self.play(
            Indicate(
                VGroup(
                    example_graph.vertices[1],
                    example_graph.vertices[5],
                    example_graph.vertices[7],
                    example_graph.edges[(1,5)],
                    example_graph.edges[(1,7)],
                    example_graph.edges[(5,7)]
                ),
                rate_func=rate_functions.there_and_back_with_pause
            )
        )
        self.next_slide()
        Util.cleanUp(self)

    def algorithm(self):
        # Text for the algorithm
        argument_text = Text("Algorithm",font_size=28).move_to(UP*3)


        # Find the index of the word to underline
        word_to_underline = "Algorithm"
        index_to_underline = argument_text.text.index(word_to_underline)

        # Create an Underline object for the specified word
        underline = Underline(argument_text[index_to_underline:index_to_underline + len(word_to_underline)], color=WHITE)

        # Add the Text and Underline objects to the scene
        self.play(Write(argument_text))
        self.play(Create(underline))

        algorithm_text = """
        Pick an arbitrary vertex v;
        L = BFS(v); // return layers of vertices
        If there exists an edge (x,y) such that x and y are 
           at the same level in the BFS tree
        {
            We have found an Odd cycle
        =>      G is not Bipartite 
        }
        Else
        {
            We have found a bipartite graph
            A={L[0],L[2],L[4],...}  even layer vertices
            B={L[1],L[3],L[5],...}  odd layer vertices
        }
        """
        
        # Create a Text object
        algorithm_text_obj = Text(algorithm_text, font_size=25, line_spacing=0.5).to_edge(UL+(UP+0.2), buff=1)

        # Animate the text
        self.play(Write(algorithm_text_obj))
        self.wait(2) 
        Util.cleanUp(self)

    def conclusion(self):
        self.play(Write(Tex("Thank You!")))
        self.next_slide()
        Util.cleanUp(self)
