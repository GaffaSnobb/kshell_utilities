from dataclasses import dataclass

@dataclass
class OrbitalOrder:
    """
    For storing information about the general classification of the
    shell model orbitals.
    """
    idx: int    # NOTE: Indices are in the "standard shell model order", not the order of the interaction file.
    # idx_snt: None | int # Index of the orbital as listed in the interaction file.
    major_shell_idx: int
    major_shell_name: str

@dataclass
class OrbitalParameters:
    """
    For storing parameters of the model space orbitals.
    """
    idx: int        # Index of the orbital from the partition file.
    n: int
    l: int          # Orbital angular momentum.
    j: int          # Total angular momentum.
    tz: int         # Isospin.
    nucleon: str    # Proton or neutron
    name: str       # Ex: p 0d5/2.
    parity: int
    order: OrbitalOrder

    def __str__(self):
        return self.name

@dataclass
class ModelSpace:
    orbitals: list[OrbitalParameters]
    n_major_shells: int
    major_shell_names: set[str]
    n_orbitals: int
    n_valence_nucleons: int
    # n_proton_orbitals: int
    # n_neutron_orbitals: int

@dataclass
class Interaction:
    model_space: ModelSpace
    model_space_proton: ModelSpace
    model_space_neutron: ModelSpace
    name: str
    n_core_protons: int
    n_core_neutrons: int


@dataclass
class ConfigurationParameters:
    idx: int
    parity: int
    configuration: list[int]