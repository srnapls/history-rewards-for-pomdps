import stormpy
import stormpy.core

import stormpy.examples
import stormpy.examples.files


def example_exploration():
    """
    Example to exploration of POMDPs.
    :return:
    """
    program = stormpy.parse_prism_program("prism/pomdp_e1.prism")

    prop = "Rmax=? [F \"end\"]"
    properties = stormpy.parse_properties(prop, program)
    print(properties[0])
    model = stormpy.build_model(program, properties)
    
    print(model)
    # Internally, POMDPs are just MDPs with additional observation information.
    # Thus, data structure exploration for MDPs can be applied as before.

    print(model.nr_observations)   
    for state in model.states:
        print("State {} has observation id {}".format(state.id, model.observations[state.id]))
    
    print("The model has {} observations".format(model.nr_observations))

    initial_state = model.initial_states[0]
    result = stormpy.model_checking(model, properties[0])
    #print("Result: {}".format(round(result.at(initial_state), 6)))


if __name__ == '__main__':
    example_exploration()
