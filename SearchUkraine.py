from search import *
from notebook import psource, heatmap, gaussian_kernel, show_map, final_path_colors, display_visual, plot_NQueens

Ukraine_map = UndirectedGraph(dict(
    Kyiv=dict(Chernihiv=142, Zhytomyr=140, Cherkasy=192, Poltava=344, Vinnitsa=269),
    Chernihiv=dict(Sumy=307),
    Zhytomyr=dict(Vinnitsa=128, Rivne=188, Khmelnytsky=189),
    Khmelnytsky=dict(Vinnitsa=120, Ternopil=112, Rivne=194, Chernivtsi=188),
    Chernivtsi=dict(Ternopil=173, Vinnitsa=288, Ivano_Frankivsk=135),
    Ivano_Frankivsk=dict(Uzhhorod=293, Ternopil=136, Lviv=132),
    Rivne=dict(Lutsk=72, Lviv=211, Ternopil=159),
    Lviv=dict(Uzhhorod=250, Lutsk=150, Ternopil=134),
    Vinnitsa=dict(Cherkasy=330, Kropyvnytskyi=322, Odessa=445),
    Odessa=dict(Kropyvnytskyi=317, Mykolayiv=140),
    Mykolayiv=dict(Kherson=71, Kropyvnytskyi=182, Dnipro=321),
    Kherson=dict(Simferopol=264, Dnipro=330, Zaporizhzhia=228),
    Simferopol=dict(Sevastopol=73, Kerch=203),
    Dnipro=dict(Kropyvnytskyi=250, Zaporizhzhia=85, Poltava=186, Kharkiv=218, Donetsk=263),
    Kharkiv=dict(Donetsk=314, Poltava=144, Sumy=184, Lugansk=338),
    Poltava=dict(Sumy=174, Kropyvnytskyi=249, Cherkasy=243, Chernihiv=403),
    Cherkasy=dict(Kropyvnytskyi=130),
    Donetsk=dict(Lugansk=168, Zaporizhzhia=232)))

Ukraine_map.locations = dict(
    Kyiv=(100, 492), Chernihiv=(110, 634), Zhytomyr=(-49, 480), Cherkasy=(220, 300), Sumy=(445, 595),
    Poltava=(445, 450), Vinnitsa=(-70, 223), Rivne=(-320, 510),
    Khmelnytsky=(-190, 250), Ternopil=(-310, 300), Chernivtsi=(-440, 100), Ivano_Frankivsk=(-495, 200),
    Uzhhorod=(-800, 135), Lviv=(-540, 340), Lutsk=(-400, 530), Kropyvnytskyi=(230, 170), Odessa=(80, -170),
    Mykolayiv=(220, -120), Kherson=(280, -150), Dnipro=(470, 170), Simferopol=(330, -300),
    Sevastopol=(260, -320), Kerch=(650, -270), Zaporizhzhia=(480, 80), Kharkiv=(650, 480),
    Donetsk=(800, 100), Lugansk=(900, 180)
)

Ukraine_locations = Ukraine_map.locations
print(Ukraine_locations)
# node colors, node positions and node label positions
node_colors = {node: 'white' for node in Ukraine_map.locations.keys()}
node_positions = Ukraine_map.locations
node_label_pos = {k: [v[0], v[1] - 10] for k, v in Ukraine_map.locations.items()}
edge_weights = {(k, k2): v2 for k, v in Ukraine_map.graph_dict.items() for k2, v2 in v.items()}

Ukraine_graph_data = {'graph_dict': Ukraine_map.graph_dict,
                      'node_colors': node_colors,
                      'node_positions': node_positions,
                      'node_label_positions': node_label_pos,
                      'edge_weights': edge_weights
                      }

def astar_search_graph(problem, h=None):
    h = memoize(h or problem.h, 'h')
    iterations, all_node_colors, node = best_first_graph_search_for_vis(problem, lambda n: n.path_cost + h(n))
    return(iterations, all_node_colors, node)
all_node_colors = []
Ukraine_problem = GraphProblem('Kyiv', 'Chernihiv', Ukraine_map)
display_visual(Ukraine_graph_data, user_input=False,
               algorithm=astar_search_graph,
               problem=Ukraine_problem)