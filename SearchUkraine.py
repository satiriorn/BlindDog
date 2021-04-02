

romania_map = UndirectedGraph(dict(
    Kyiv=dict(Chernihiv=142, Zhytomyr=140, Cherkasy=192, Poltava=344, Vinnitsa=269),
    Chernihiv=dict(Sumy=307),
    Zhytomyr=dict(Vinnitsa=128, Rivne=188, Khmelnytsky=189),
    Khmelnytsky=dict(Vinnitsa=120, Ternopil=112, Rivne=194, Chernivtsi=188),
    Chernivtsi=dict(Ternopil=173, Vinnitsa=288, Ivano_Frankivsk=135),
    Ivano_Frankivsk=dict(Uzhhorod=293, Ternopil=136, Lviv=132),
    Rivne=dict(Lutsk=72, Lviv=211, Ternopil=159),
    Lviv=dict(Uzhhorod=250, Lutsk=150, Ternopil=134)))

romania_map.locations = dict(
    Kyiv=(100, 492), Chernihiv=(110, 634), Zhytomyr=(-49, 480), Cherkasy=(220, 300), Sumy=(445, 595),
    Poltava=(445, 450), Vinnitsa=(47, 223), Rivne=(-320, 510),
    Khmelnytsky=(-170, 250), Ternopil=(-270, 300), Chernivtsi=(-440, 100), Ivano_Frankivsk=(-495, 200),
    Uzhhorod=(-800, 135), Lviv=(-540, 340), Lutsk=(-400, 530))

romania_problem = GraphProblem('Kyiv', 'Bucharest', romania_map)
romania_locations = romania_map.locations
print(romania_locations)
# node colors, node positions and node label positions
node_colors = {node: 'white' for node in romania_map.locations.keys()}
node_positions = romania_map.locations
node_label_pos = {k: [v[0], v[1] - 10] for k, v in romania_map.locations.items()}
edge_weights = {(k, k2): v2 for k, v in romania_map.graph_dict.items() for k2, v2 in v.items()}

romania_graph_data = {'graph_dict': romania_map.graph_dict,
                      'node_colors': node_colors,
                      'node_positions': node_positions,
                      'node_label_positions': node_label_pos,
                      'edge_weights': edge_weights
                      }
show_map(romania_graph_data)