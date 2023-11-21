from manim import *
from manim_slides import Slide
import networkx as nx

class BipartiteProperty(Slide):
    def construct(self):
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
        self.play(cycle5.vertices[1].animate.set_color(RED),Write(t1),FadeOut(text3))
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("Then its neighbour goes to", " set B")
        t1[1].set_color(BLUE)
        t1.shift(3 * DOWN)
        # print(cycle5.edges[(1,2)].animate.set_color_by_gradient(RED, BLUE))
        self.play(# cycle5.edges[(1,2)].animate.set_color(color=[RED, BLUE]),
                #   cycle5.edges[(5,1)].animate.set_color(color=[BLUE, RED]),
                  cycle5.vertices[2].animate.set_color(BLUE),
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
                  cycle5.vertices[3].animate.set_color(RED),
                  cycle5.vertices[4].animate.set_color(BLUE),
                  Write(t1)
                )
        self.next_slide()
        self.play(FadeOut(t1))
        t1 = Tex("Until ", "now",". Which set does this belong to?")
        t1[1].set_color(YELLOW)
        t1.shift(3 * DOWN)
        self.play(cycle5.vertices[5].animate.set_color(YELLOW),
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
        self.wait(2)

class CycleGraph(Scene):
    def construct(self):
        # Your graph creation code goes here
     
        nodes = [Dot(point=RIGHT*2*np.cos(i*np.pi/5) + UP*2*np.sin(i*np.pi/5), radius=0.1) for i in range(5)]
               # Create edges
        edges = [Line(nodes[i], nodes[(i + 1) % 5]) for i in range(5)]

        # Add nodes and edges to the sceCne
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(edge) for edge in edges])

        self.wait(2)

class LabelNodesAndCircles(Scene):
    def construct(self):
        # Create nodes
        nodes = [Dot(point=RIGHT*2*np.cos(i*np.pi/5) + UP*2*np.sin(i*np.pi/5), radius=0.1) for i in range(5)]

        # Create edges
        edges = [Line(nodes[i], nodes[(i + 1) % 5]) for i in range(5)]

        # Create circles for Set A and Set B
   #     circle_A = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
        circle_B = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)

        # Position the circles and labels
       # circle_A.move_to(nodes[1])  # Set A
        circle_B.move_to(nodes[4])  # Set B

#        label_A = Text("Set A").next_to(circle_A, UP)
        label_B = Text("Set A",font_size=20).next_to(circle_B, UP)

        # Add nodes, edges, circles, and labels to the scene
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(edge) for edge in edges])
      #  self.play(Create(circle_A), Create(circle_B), Write(label_A), Write(label_B))
        self.play( Create(circle_B))
        self.play( Write(label_B))

        self.wait(2)
class LabelNodesAndCircles1(Scene):
     def construct(self):
        # Create nodes
        nodes = [Dot(point=RIGHT*2*np.cos(i*np.pi/5) + UP*2*np.sin(i*np.pi/5), radius=0.1) for i in range(5)]

        # Create edges
        edges = [Line(nodes[i], nodes[(i + 1) % 5]) for i in range(5)]

        # Create circles for Set A and Set B
        circle_A = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
        circle_B = Circle(radius=0.3, color=RED, fill_opacity=0.3)

        # Position the circles and labels
        circle_A.move_to(nodes[4])  # Set A
        circle_B.move_to(nodes[3])  # Set B

        label_A = Text("Set A",font_size=20).next_to(circle_A, UP)
        label_B = Text("Set B",font_size=20).next_to(circle_B, UP)

        # Add nodes, edges, circles, and labels to the scene
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(edge) for edge in edges])
        self.play(Create(circle_A))
        self.play(Create(label_A))
        self.play(Create(circle_B))
        
        self.play(Create(label_B))
       
       # self.play( Create(circle_B), Write(label_B))

        self.wait(2)

class LabelNodesAndCircles2(Scene):
     def construct(self):
        # Create nodes
        nodes = [Dot(point=RIGHT*2*np.cos(i*np.pi/5) + UP*2*np.sin(i*np.pi/5), radius=0.1) for i in range(5)]

        # Create edges
        edges = [Line(nodes[i], nodes[(i + 1) % 5]) for i in range(5)]

        # Create circles for Set A and Set B
        circle_A = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
        circle_B = Circle(radius=0.3, color=RED, fill_opacity=0.3)
        circle_C = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
        circle_D = Circle(radius=0.3, color=RED, fill_opacity=0.3)
        circle_E = Circle(radius=0.3, color=WHITE, fill_opacity=0.3)

        # Position the circles and labels
        circle_A.move_to(nodes[4])  # Set A
        circle_B.move_to(nodes[3])  # Set B
        circle_C.move_to(nodes[2])
        circle_D.move_to(nodes[1])
        circle_E.move_to(nodes[0])
        

        label_A = Text("Set A",font_size=20).next_to(circle_A, UP)
        label_B = Text("Set B",font_size=20).next_to(circle_B, UP)
        label_C = Text("Set A",font_size=20).next_to(circle_C, UP)
        label_D = Text("Set B",font_size=20).next_to(circle_D, UP)
        label_E = Text("Set A ?",font_size=24).next_to(circle_E,DOWN)

        # Add nodes, edges, circles, and labels to the scene
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(edge) for edge in edges])
        self.play(Create(circle_A))
        self.play(Create(label_A))
        self.play(Create(circle_B))
        
        self.play(Create(label_B))
        self.play(Create(circle_C),Create(label_C),Create(circle_D), Write(label_D))
        self.play(Create(circle_E))
        self.play(Create(label_E))
        contradiction_text = Text("So, this is the contradiction").next_to(label_E, DOWN, buff=0.5)
        self.play(Write(contradiction_text))

        self.wait(2)



class ArgumentScene(Scene):
    def construct(self):
        # Create the text with the argument
        argument_text = Text("Argument : If a graph has no odd cycle, then it is Bipartite",font_size=30).move_to(UP*3)


        # Find the index of the word to underline
        word_to_underline = "Argument"
        index_to_underline = argument_text.text.index(word_to_underline)

        # Create an Underline object for the specified word
        underline = Underline(argument_text[index_to_underline:index_to_underline + len(word_to_underline)], color=WHITE)

        # Add the Text and Underline objects to the scene
        self.play(Write(argument_text))
        self.play(Create(underline))
        argument_text = (
            "To prove the above argument, we take a graph G with a set of vertices and edges. "
            "Divide the vertices into two sets in such a way that one endpoint of each edge belongs to set A "
            "and the other endpoint belongs to set B. There are no edges with both end points within a set."
        )

        # Split the text into lines with 10 words each
        words = argument_text.split()
        lines = [' '.join(words[i:i + 13]) for i in range(0, len(words), 13)]
      

        # Create Text objects for each line with small font size
        text_objects = [Text(line, font_size=24).to_edge(LEFT, buff=2.1).shift(i * 0.5 * DOWN) for i, line in enumerate(lines)]
        text_group=VGroup(*text_objects)
        
        # Add the Text objects to the scene
        self.play(*[Write(text_object) for text_object in text_objects])
        self.play(text_group.animate.move_to(DR*2.7).scale(0.6))
        

        vertices = [Tex(f"$a_{i}$") for i in range(1, 7)]
        edges = [
            (vertices[0], vertices[5]),
            (vertices[2], vertices[1]),
            (vertices[4], vertices[3]),
            (vertices[2], vertices[5]),
        ]
       
        # Position vertices in a line
        vertices_line = VGroup(*vertices).arrange(RIGHT).shift(UP)

        # Create ovals for sets A and B
       # oval_a = Circle(color=BLUE, radius=2).shift(LEFT * 4)
       # oval_b = Circle(color=RED, radius=2).shift(RIGHT * 4)
        oval_a = Ellipse(width=2.0, height=3.0, color=BLUE_B).shift(LEFT*4)
        oval_b = Ellipse(width=2.0, height=3.0, color=BLUE_B).shift(RIGHT*4)

        # Animate the appearance of vertices, ovals, and edges
        
        self.play(*[Write(vertex) for vertex in vertices])
        self.play(Create(vertices_line))
        self.wait(0.5)
        self.play(Create(oval_a), Create(oval_b))

        self.play(vertices_line[0].animate.move_to(oval_a.get_center() + UP))
        self.play(vertices_line[2].animate.move_to(oval_a.get_center()))
        self.play(vertices_line[4].animate.move_to(oval_a.get_center() + DOWN))

        self.play(vertices_line[1].animate.move_to(oval_b.get_center() + UP))
        self.play(vertices_line[3].animate.move_to(oval_b.get_center()))
        self.play(vertices_line[5].animate.move_to(oval_b.get_center() + DOWN))
        # Create edges between vertices and ovals
       # edges_a = [Line(vertices[i].get_center(), oval_a.get_center(), color=BLUE) for i in range(0,6,2)]
       # edges_b = [Line(vertices[i].get_center(), oval_b.get_center(), color=RED) for i in range(1,6,2)]

        edge = Line(oval_a.get_center()*0.881, oval_b.get_center()+UP+(LEFT*0.2), color=GREEN)
        self.play(Create(edge))
        edge1 = Line(oval_a.get_center()+UP+(RIGHT*0.2), oval_b.get_center()+DOWN+(LEFT*0.2), color=GREEN)
        self.play(Create(edge1))

        edge2 = Line(oval_a.get_center()*0.881, oval_b.get_center()+DOWN+(LEFT*0.2), color=GREEN)
        self.play(Create(edge2))
        edge3 = Line(oval_a.get_center()+DOWN+(RIGHT*0.2), oval_b.get_center()*0.881, color=GREEN)
        self.play(Create(edge3))



        self.wait()
      #  self.wait()



class Example(Scene):
    def construct(self):
        # Define the vertices and edges
        Vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        Edges = [(1, 2), (1, 3), (1, 5), (2, 6), (2, 4), (3, 7), (3, 4), (5, 6), (5, 7), (6, 8), (5, 7),(8,4)]

        # Create a NetworkX graph
        g_nx = nx.Graph()
        g_nx.add_nodes_from(Vertices)
        g_nx.add_edges_from(Edges)

        # Create a Manim Graph from the NetworkX graph
        g = Graph.from_networkx(g_nx, layout="circular", layout_scale=3, labels=True)

        # Display the initial state of the graph
       # self.play(Create(g))
        self.wait(1)

        # Manually adjust the positions of the vertices
        vertex_positions = {
            1: UL * 2,
            2: UR * 2,
            3: DL * 2,
            4: DR * 2,
            5: LEFT * 1 + UP * 1,
            6: UP * 1 + RIGHT * 1,
            8: RIGHT * 1 + DOWN * 1,
            7: DOWN * 1 + LEFT * 1,
        }

        for vertex, position in vertex_positions.items():
            g.vertices[vertex].move_to(position)

        # Apply animations to the graph (you can customize these animations)
        self.play(g.animate.scale(0.7).to_edge(UP))
        self.wait(1)

        # More animations if needed
        # ...

        self.wait()





class Ascene(Scene):
    def construct(self):
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
        BFS(v);
        If there exists an edge xy such that x and y are 
           at the same level in the BFS tree
        {
            We have found an Odd cycle
        =>      G is not Bipartite 
        }
        Else
        {
            We have found a bipartite graph
            A={L0,L2,L4,...}  even layer vertices
            B={L1,L3,L5,...}  odd layer vertices
        }
        """
        
        # Create a Text object
        algorithm_text_obj = Text(algorithm_text, font_size=25, line_spacing=0.5).to_edge(UL+(UP+0.2), buff=1)

        # Animate the text
        self.play(Write(algorithm_text_obj))
        self.wait(2)






