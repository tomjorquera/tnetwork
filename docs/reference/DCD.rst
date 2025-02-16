*************************************
Dynamic Community Detection
*************************************

Dynamic community detection is the problem of discovering snapshot_communities in dynamic networks.

Currently, the following publsihed methods are implemented

* Rolling CPM
* Iterative match
* Survival graph



All of them are based on snapshots graphs. Iterative match and Survival graph are generic methods, since they can
be parameterized by the community detection method to use at each step, and by the community similarity function to
match snapshot_communities. They can even use a smoothed algorithm to discover snapshot_communities at each step.

Two other methods, yet unpublished, are proposed, track_communities and generate_multi_temporal_scale , respectively
to detect and generate communities at multiple temporal scale

.. currentmodule:: tnetwork

.. autosummary::
    :toctree: generated/

        iterative_match
        match_survival_graph
        rollingCPM
        track_communities
        generate_multi_temporal_scale