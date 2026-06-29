from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str = ""
    raw_intention: str = ""
    desired_outcome: str = ""
    target_users: list[str] = Field(default_factory=list)
    environment: str = ""
    constraints: list[str] = Field(default_factory=list)


class Gap(BaseModel):
    failed_relation: str = ""
    present_arrangement: str = ""
    missing_possibility: str = ""
    affected_actors: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)


class LanguageGame(BaseModel):
    repeated_phrases: list[str] = Field(default_factory=list)
    workarounds: list[str] = Field(default_factory=list)
    roles: list[str] = Field(default_factory=list)
    tensions: list[str] = Field(default_factory=list)
    judgments: list[str] = Field(default_factory=list)


class HiddenVerb(BaseModel):
    id: str
    verb: str
    evidence: list[str] = Field(default_factory=list)
    accepted: bool = False
    source: str = ""


class Relation(BaseModel):
    id: str
    name: str
    source_entity: str = ""
    target_entity: str = ""
    constraint: str = ""
    traces_to_verbs: list[str] = Field(default_factory=list)


class Invariant(BaseModel):
    id: str
    statement: str
    must_remain_true_when: str = ""
    violated_by: str = ""
    traces_to_relations: list[str] = Field(default_factory=list)


class Genome(BaseModel):
    statement: str = ""
    must_sense: list[str] = Field(default_factory=list)
    must_remember: list[str] = Field(default_factory=list)
    must_transform: list[str] = Field(default_factory=list)
    must_connect: list[str] = Field(default_factory=list)
    must_protect: list[str] = Field(default_factory=list)
    must_expose: list[str] = Field(default_factory=list)
    must_repair: list[str] = Field(default_factory=list)
    must_decay: list[str] = Field(default_factory=list)
    traces_to_invariants: list[str] = Field(default_factory=list)


class Organism(BaseModel):
    model: str = ""
    boundary_inside: list[str] = Field(default_factory=list)
    boundary_outside: list[str] = Field(default_factory=list)
    reason: str = ""
    rejected_models: list[str] = Field(default_factory=list)


class Ontology(BaseModel):
    entities: list[str] = Field(default_factory=list)
    relations: list[str] = Field(default_factory=list)
    states: list[str] = Field(default_factory=list)
    boundaries: list[str] = Field(default_factory=list)


class SurvivalCondition(BaseModel):
    id: str
    condition: str
    test: str = ""
    evidence: list[str] = Field(default_factory=list)
    traces_to_invariants: list[str] = Field(default_factory=list)


class DeathCondition(BaseModel):
    id: str
    condition: str
    why_dead_even_if_running: str = ""
    traces_to_survival: list[str] = Field(default_factory=list)


class SelectedStack(BaseModel):
    name: str = ""
    language: str = ""
    storage: str = ""
    interface: str = ""
    services: list[str] = Field(default_factory=list)
    deployment: str = ""
    observability: str = ""
    tests: str = ""


class Stack(BaseModel):
    selected: SelectedStack = Field(default_factory=SelectedStack)
    alternatives: list[Any] = Field(default_factory=list)
    rationale: str = ""
    traces_to_genome: bool = True
    traces_to_survival: list[str] = Field(default_factory=list)


class ImplementationPhase(BaseModel):
    id: str
    phase: str
    purpose: str = ""
    files_to_create: list[str] = Field(default_factory=list)
    validation: list[str] = Field(default_factory=list)
    traces_to: list[str] = Field(default_factory=list)


class AgentContract(BaseModel):
    targets: list[str] = Field(default_factory=lambda: ["codex", "copilot", "claude"])
    instructions: str = ""
    forbidden_moves: list[str] = Field(default_factory=list)
    completion_definition: str = ""


class DesignSession(BaseModel):
    schema_version: Literal["1.0"] = "1.0"
    project: Project = Field(default_factory=Project)
    gap: Gap = Field(default_factory=Gap)
    language_game: LanguageGame = Field(default_factory=LanguageGame)
    hidden_verbs: list[HiddenVerb] = Field(default_factory=list)
    relations: list[Relation] = Field(default_factory=list)
    invariants: list[Invariant] = Field(default_factory=list)
    genome: Genome = Field(default_factory=Genome)
    organism: Organism = Field(default_factory=Organism)
    ontology: Ontology = Field(default_factory=Ontology)
    survival_conditions: list[SurvivalCondition] = Field(default_factory=list)
    death_conditions: list[DeathCondition] = Field(default_factory=list)
    stack: Stack = Field(default_factory=Stack)
    implementation_sequence: list[ImplementationPhase] = Field(default_factory=list)
    agent_contract: AgentContract = Field(default_factory=AgentContract)
