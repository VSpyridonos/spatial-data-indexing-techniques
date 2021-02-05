import sys
import csv
import math


def range_intersection_query(query_filename):

    with open(query_filename, 'r') as qf:
        query_reader = csv.reader(qf, delimiter = '\t')

        # The root
        check_node = len(R_tree) - 1
        node_accesses = 0
        number_of_results = 0

        # Recursive function that is called for every intermediate node
        def func(c_node, q_rec):
            nonlocal node_accesses
            nonlocal number_of_results

            # For each entry in the node
            for entry in R_tree[c_node]:
                node_accesses += 1


                # Check if the rectangles are intersecting
                x_intersect_cond1 = (float(entry[1]) >= float(q_rec[1]) and float(entry[1]) <= float(q_rec[2]))
                x_intersect_cond2 = (float(entry[2]) >= float(q_rec[1]) and float(entry[2]) <= float(q_rec[2]))
                x_intersect_cond3 = (float(entry[1]) < float(q_rec[1]) and float(entry[2]) > float(q_rec[2]))
                y_intersect_cond1 = (float(entry[3]) >= float(q_rec[3]) and float(entry[3]) <= float(q_rec[4]))
                y_intersect_cond2 = (float(entry[4]) >= float(q_rec[3]) and float(entry[4]) <= float(q_rec[4]))
                y_intersect_cond3 = (float(entry[3]) < float(q_rec[3]) and float(entry[4]) > float(q_rec[4]))
                x_intersect = x_intersect_cond1 or x_intersect_cond2 or x_intersect_cond3
                y_intersect = y_intersect_cond1 or y_intersect_cond2 or y_intersect_cond3
                is_intersecting = x_intersect and y_intersect


                # Check if the query rectangle is inside the tree rectangle
                query_x_inside_cond1 = (float(q_rec[1]) >= float(entry[1])) and (float(q_rec[1]) <= float(entry[2]))
                query_x_inside_cond2 = (float(q_rec[2]) >= float(entry[1])) and (float(q_rec[2]) <= float(entry[2]))
                query_y_inside_cond1 = (float(q_rec[3]) >= float(entry[3])) and (float(q_rec[3]) <= float(entry[4]))
                query_y_inside_cond2 = (float(q_rec[4]) >= float(entry[3])) and (float(q_rec[4]) <= float(entry[4]))
                query_x_inside = query_x_inside_cond1 or query_x_inside_cond2
                query_y_inside = query_y_inside_cond1 or query_y_inside_cond2
                query_is_inside = query_x_inside and query_y_inside


                # If the query rectangle intersects or is inside of a MBR of the node
                if is_intersecting or query_is_inside:


                    # If the node is intermediate, call the function recursively with the node's id
                    if R_tree.index(R_tree[c_node]) > L - 1:
                        func(int(entry[0]), q_rec)

                    # If the node is a leaf, for each rectangle that it contains, check if 
                    # it intersects with the query rectangle. If it does, increment the counter.
                    else:
                        if is_intersecting:
                            number_of_results += 1


        while True:
            try:
                # Read the query rectangles one by one
                query_rec = next(query_reader)
                node_accesses = 0
                number_of_results = 0

                # Call function for each rectangle with the tree's root as a parameter
                func(check_node, query_rec)

                # Print results for each query rectangle
                print("Range intersection query gia to orthogwnio: " + str(query_rec))
                print("Arithmos apotelesmatwn : " + str(number_of_results))
                print("Node accesses: " + str(node_accesses) + '\n')
            except StopIteration:
                print("Telos range_intersection_query\n\n")
                break




def range_inside_query(query_filename):

    with open(query_filename, 'r') as qf:
        query_reader = csv.reader(qf, delimiter = '\t')

        # The root
        check_node = len(R_tree) - 1
        node_accesses = 0
        number_of_results = 0

        # I anadromiki synartisi pou kaleitai gia kathe endiameso komvo
        def func(c_node, q_rec):
            nonlocal node_accesses
            nonlocal number_of_results

            # For each entry in the node
            for entry in R_tree[c_node]:
                node_accesses += 1

                # Check if the rectangles are intersecting
                x_intersect_cond1 = (float(entry[1]) >= float(q_rec[1]) and float(entry[1]) <= float(q_rec[2]))
                x_intersect_cond2 = (float(entry[2]) >= float(q_rec[1]) and float(entry[2]) <= float(q_rec[2]))
                x_intersect_cond3 = (float(entry[1]) < float(q_rec[1]) and float(entry[2]) > float(q_rec[2]))
                y_intersect_cond1 = (float(entry[3]) >= float(q_rec[3]) and float(entry[3]) <= float(q_rec[4]))
                y_intersect_cond2 = (float(entry[4]) >= float(q_rec[3]) and float(entry[4]) <= float(q_rec[4]))
                y_intersect_cond3 = (float(entry[3]) < float(q_rec[3]) and float(entry[4]) > float(q_rec[4]))
                x_intersect = x_intersect_cond1 or x_intersect_cond2 or x_intersect_cond3
                y_intersect = y_intersect_cond1 or y_intersect_cond2 or y_intersect_cond3
                is_intersecting = x_intersect and y_intersect


                # Check if the tree's rectangle is inside the query rectangle
                x_inside_cond1 = (float(entry[1]) >= float(q_rec[1])) and (float(entry[1]) <= float(q_rec[2]))
                x_inside_cond2 = (float(entry[2]) >= float(q_rec[1])) and (float(entry[2]) <= float(q_rec[2]))
                y_inside_cond1 = (float(entry[3]) >= float(q_rec[3])) and (float(entry[3]) <= float(q_rec[4]))
                y_inside_cond2 = (float(entry[4]) >= float(q_rec[3])) and (float(entry[4]) <= float(q_rec[4]))
                x_inside = x_inside_cond1 or x_inside_cond2
                y_inside = y_inside_cond1 or y_inside_cond2
                is_inside = x_inside and y_inside


                # Check if the query rectangle is inside the tree rectangle
                query_x_inside_cond1 = (float(q_rec[1]) >= float(entry[1])) and (float(q_rec[1]) <= float(entry[2]))
                query_x_inside_cond2 = (float(q_rec[2]) >= float(entry[1])) and (float(q_rec[2]) <= float(entry[2]))
                query_y_inside_cond1 = (float(q_rec[3]) >= float(entry[3])) and (float(q_rec[3]) <= float(entry[4]))
                query_y_inside_cond2 = (float(q_rec[4]) >= float(entry[3])) and (float(q_rec[4]) <= float(entry[4]))
                query_x_inside = query_x_inside_cond1 or query_x_inside_cond2
                query_y_inside = query_y_inside_cond1 or query_y_inside_cond2
                query_is_inside = query_x_inside and query_y_inside


                # An to orthogwnio tis erwtisis temnei i vrisketai mesa se kapoio MBR tou komvou
                # If the query rectangle intersects or is inside of a MBR of the node
                if is_intersecting or query_is_inside:

                    # If the node is intermediate, call the function recursively with the node's id as a parameter
                    if R_tree.index(R_tree[c_node]) > L - 1:
                        func(int(entry[0]), q_rec)

                    # If the node is a leaf, for each rectangle that it contains, check if 
                    # it intersects with the query rectangle. If it does, increment the counter.
                    else:
                        if is_inside:
                            number_of_results += 1

        while True:
            try:
                # Read the query rectangles one by one
                query_rec = next(query_reader)
                node_accesses = 0
                number_of_results = 0

                # Call function for each rectangle with the tree's root as a parameter
                func(check_node, query_rec)

                # Print results for each query rectangle
                print("Range inside query gia to orthogwnio: " + str(query_rec))
                print("Arithmos apotelesmatwn : " + str(number_of_results))
                print("Node accesses: " + str(node_accesses) + '\n')
            except StopIteration:
                print("Telos range_inside_query\n\n")
                break



def containment_query(query_filename):

    with open(query_filename, 'r') as qf:
        query_reader = csv.reader(qf, delimiter = '\t')

        # The root
        check_node = len(R_tree) - 1
        node_accesses = 0
        number_of_results = 0

        # Recursive function that is called for every intermediate node
        def func(c_node, q_rec):
            nonlocal node_accesses
            nonlocal number_of_results

            # For each entry in the node
            for entry in R_tree[c_node]:
                node_accesses += 1

                # Check if the query rectangle is inside the tree's rectangle
                query_x_inside_cond1 = (float(q_rec[1]) >= float(entry[1])) and (float(q_rec[1]) <= float(entry[2]))
                query_x_inside_cond2 = (float(q_rec[2]) >= float(entry[1])) and (float(q_rec[2]) <= float(entry[2]))
                query_y_inside_cond1 = (float(q_rec[3]) >= float(entry[3])) and (float(q_rec[3]) <= float(entry[4]))
                query_y_inside_cond2 = (float(q_rec[4]) >= float(entry[3])) and (float(q_rec[4]) <= float(entry[4]))
                query_x_inside = query_x_inside_cond1 or query_x_inside_cond2
                query_y_inside = query_y_inside_cond1 or query_y_inside_cond2
                query_is_inside = query_x_inside and query_y_inside

                # If the query rectangle is inside of a MBR of the node
                if query_is_inside:

                    # If the node is intermediate, call the function recursively with the node's id as a parameter
                    if R_tree.index(R_tree[c_node]) > L - 1:
                        func(int(entry[0]), q_rec)

                    # If the node is a leaf, increment the result counter
                    else:
                        number_of_results += 1

        while True:
            try:
                # Read the query rectangles one by one
                query_rec = next(query_reader)
                node_accesses = 0
                number_of_results = 0

                # Call function for each rectangle with the tree's root as a parameter
                func(check_node, query_rec)

                # Print results for each query rectangle
                print("Containment query gia to orthogwnio: " + str(query_rec))
                print("Arithmos apotelesmatwn : " + str(number_of_results))
                print("Node accesses: " + str(node_accesses) + '\n')
            except StopIteration:
                print("Telos containment_query\n\n")
                break




# Gets the file name from the command line
rectangle_file = sys.argv[1]


# Reads files with rectangle coordinates
with open(rectangle_file, 'r') as rf:
    tsv_reader = csv.reader(rf, delimiter = '\t')

    # List with all the rectangles and their coordinates
    rectangles_list = []
    # List with all the rectangles sorted by their x-low
    x_low_sorted_list = []
    # List with all the rectangles sorted by their y-low
    y_low_sorted_list = []

    # The R-tree
    R_tree = []



    # Filling rectangles_list
    while True:
        try:
            rec = next(tsv_reader)
            rectangles_list.append(rec)
        except StopIteration:
            break


    # The list that contains the rectangles sorted by their x-low is created
    x_low_sorted_list = sorted(rectangles_list, key = lambda rectangle: rectangle[1])




    N = len(x_low_sorted_list)  # Total number of rectangles
    f = math.floor(1024/36)     # Node capacity (fixed)
    L = math.ceil(N/f)          # Number of leaves


    # Calculate tree height and number of nodes on every level
    tree_height = 0
    temp = N
    nodes_in_levels = []
    total_number_of_nodes = 0

    # Calculate tree height, number of nodes on every level and total number of nodes
    while temp != 1:
        tree_height += 1
        temp = math.ceil(temp/f)
        nodes_in_levels.append(temp)
        total_number_of_nodes += temp


    first_node = []
    node_id = 0
    remaining_rectangles = N
    number_of_recs_in_list = 0
    counter = 0
    number_of_elements = 0

    # Inside following while conditions, leaves are inserted into the tree
    # While condition checks if there are remaining rectangles in the list
    while remaining_rectangles > 0:

        # If there are less rectangles than *node_capacity times square root of number leaves* inside the list
        if len(x_low_sorted_list) < f * math.ceil(math.sqrt(L)):
            x = remaining_rectangles

            for i in range(x):
            
                # Every element in x_low_sorted_list is inserted in y_low_sorted_list
                y_low_sorted_list.append(x_low_sorted_list[i])

                number_of_recs_in_list += 1
                remaining_rectangles -= 1

            # Delete the elements that were inserted from x_low_sorted_list
            x_low_sorted_list = x_low_sorted_list[x:]

            # Sort inserted elements by their y-low
            y_low_sorted_list = sorted(y_low_sorted_list, key = lambda rectangle: rectangle[3])

            # For each element inside the sorted list, insert it into the leaves 
            for i in range(number_of_recs_in_list):
                first_node.append(y_low_sorted_list[i])
                number_of_elements = len(y_low_sorted_list)
                number_of_recs_in_list -= 1
                counter += 1

                if number_of_recs_in_list == 0:
                    R_tree.insert(node_id, first_node)
                    node_id += 1
                    first_node = []
                    counter = 0

                if counter == f:
                    R_tree.insert(node_id, first_node)
                    node_id += 1
                    first_node = []
                    counter = 0
            number_of_elements = 0
            y_low_sorted_list = []



        else:
            # Reads *node_capacity times square root of number_of_leaves* rectangles
            for i in range(f * math.ceil(math.sqrt(L))):
                # Kathe stoixeio tis x_low_sorted_list to vazw stin y_low_sorted_list
                # Insert each element inside x_low_sorted_list into y_low_sorted_list
                y_low_sorted_list.append(x_low_sorted_list[i])

                remaining_rectangles -= 1

            # Delete the elements that were inserted from x_low_sorted_list
            x_low_sorted_list = x_low_sorted_list[f * math.ceil(math.sqrt(L)):]


            # Sort inserted elements by their y-low
            y_low_sorted_list = sorted(y_low_sorted_list, key = lambda rectangle: rectangle[3])


            # For each element inside the sorted list, insert it into the leaves
            for i in range(f * math.ceil(math.sqrt(L))):
                first_node.append(y_low_sorted_list[i])
                counter += 1
                if counter == f:
                    R_tree.insert(node_id, first_node)
                    node_id += 1
                    first_node = []
                    counter = 0
            y_low_sorted_list = []


    # At this point, all leaves have been inserted into the tree
    # The remaining nodes will now be created

    nodes_visited = 0
    parent_node_index = 0
    child_node_index = 0
    a_child_node_MBR = []
    a_child_node = []
    parent_node = []
    stop_num = 0
    records_of_node = 0



    # For each node inside the R-tree
    for node in R_tree:

        stop_num += 1
        records_of_node = len(node)
        nodes_visited += 1
        node_x_low = 1
        node_x_high = 0
        node_y_low = 1
        node_y_high = 0

	# For each record in the node
        for record in node:

            # Find the smallest x-lows and y-lows and the largest x-highs and y-highs in every node
            # This way, the MBR that covers its records will be calculated
            if float(record[1]) < node_x_low:
                node_x_low = float(record[1])
            if float(record[2]) > node_x_high:
                node_x_high = float(record[2])
            if float(record[3]) < node_y_low:
                node_y_low = float(record[3])
            if float(record[4]) > node_y_high:
                node_y_high = float(record[4])


        a_child_node_MBR = [str(node_x_low), str(node_x_high), str(node_y_low), str(node_y_high)]

        # a_child_node list contains the node's id and the MBR's coordinates
        a_child_node.append([str(child_node_index), a_child_node_MBR[0], a_child_node_MBR[1], a_child_node_MBR[2], a_child_node_MBR[3]])
        child_node_index += 1


        # if *node_capacity* nodes have been visited or a node's records are less than *node_capacity*
        if nodes_visited == f or records_of_node < f :
            nodes_visited = 0
            parent_node += a_child_node

            # Insert the nodes into the R-tree
            R_tree.insert(node_id + parent_node_index, parent_node)
            node_id += 1
            parent_node_index += 1
            a_child_node = []
            parent_node = []


        # Stop when the last node has been inserted into the R-tree
        if stop_num == total_number_of_nodes:
            break;





#####################################
######### Area Calculation ##########
#####################################
    node_counter = 0
    k = 0

    # Always remove an element from the R-tree as the above code creates an extra node above the root
    R_tree.pop()
    average_level_area = []

    base = 0
    height = 0
    area = 0
    avg_area = 0
    avg_level_area = []
    all_node_areas = []
    test_area = 0
    ns = 0


    # For each node in the R-tree
    for node in R_tree:
        node_counter +=1

        # For every node, save its number of records inside ns
        ns = len(node)

        # For each record inside the node
        for record in node:

            # Calculate each record's area and add it to area variable
            base = float(record[2]) - float(record[1])
            height = float(record[4]) - float(record[3])
            area += (base * height)


        # Add the node's average area inside avg_area
        avg_area += (area / ns)
        base = 0
        height = 0
        area = 0


        # Calculate area for every R-tree level
        if node_counter == nodes_in_levels[k]:

            avg_area = avg_area / nodes_in_levels[k]

            # In the end, avg_level_area will contain the area of every R-tree level
            avg_level_area.append(avg_area)

            base = 0
            height = 0
            area = 0
            avg_area = 0

            k += 1
            node_counter = 0





    # Print tree stats
    
    a = 0

    node_id -= 1
    print('Ypsos denrou: ' + str(tree_height))
    b = 0
    c = 0
    for el in nodes_in_levels:
        print('Arithmos komvwn sto epipedo ' + str(b) + ' = ' + str(el))
        print('Meso emvado MBRs sto epipedo ' + str(b) + ' = ' + str("{:.10f}".format(avg_level_area[b])) + '\n')
        b += 1


    # Writing in file
    tf = open("rtree.txt", "w+")
    tf.write('node-id rizas: ' + str(len(R_tree) - 1) + '\n')
    tf.write('arithmos epipedwn: ' + str(tree_height) + '\n\n')
    a = 0
    for el in R_tree:
        tf.write("node-id = " + str(a) + ", arithmos eggrafwn = " + str(len(el)) + ", " + str(el) + '\n\n')
        a += 1

    print('\n\n\nERWTISEIS STO R-DENTRO:\n\n\n')


    # Call range query functions
    range_intersection_query('query_rectangles.txt')
    range_inside_query('query_rectangles.txt')
    containment_query('query_rectangles.txt')
