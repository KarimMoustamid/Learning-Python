"""
Python OOP 🏗️
- Classes without access modifiers, properties instead of get/set, and no `new`
- `self` is explicit where C# has an implicit `this`
- Dunder methods are the operator-overload / interface system
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/18_oop.py
"""

# ─── Your first class ────────────────────────────────────────
# C#:  public class User { public string Name { get; } public User(string n) {...} }
# Python: no access modifiers, no `new`, `self` is always the first parameter.
print("─── A class, no ceremony ─────────────────────────────────")


class User:
    """A user of the service."""

    def __init__(self, name, role="developer"):     # __init__ ≈ constructor
        self.name = name                            # self ≈ `this`, written out
        self.role = role
        self.jobs = 0

    def describe(self):
        return f"{self.name} ({self.role})"

    def run_job(self):
        self.jobs += 1
        return self.jobs


karim = User("Karim")                               # no `new` keyword
print(f"  describe()  → {karim.describe()}")
print(f"  run_job()   → {karim.run_job()}, then {karim.run_job()}")
print(f"  attributes  → name={karim.name!r} role={karim.role!r}")
print("  Calling the class builds the object; __init__ only fills it in.")

# ─── Instance vs class attributes ────────────────────────────
# ⚠ A mutable class attribute is shared by every instance. This is the
# Python equivalent of C# `static` — and a classic bug.
print("\n─── Instance vs class attributes ─────────────────────────")
print("""
  class Bad:
      tags = []              ← CLASS attribute: ONE list shared by all instances
      def add(self, t): self.tags.append(t)

  a, b = Bad(), Bad()
  a.add("x")                 → b.tags is ALSO ["x"]   ← surprise

  Fix: initialise per-instance state inside __init__.
""")

# ─── Methods: instance, class, static ────────────────────────
# C#: instance methods, `static`, and static factory methods.
print("─── Three kinds of method ────────────────────────────────")


class RetryPolicy:
    default_attempts = 3                            # class-level default

    def __init__(self, max_attempts=None, base_delay=0.5):
        self.max_attempts = max_attempts or self.default_attempts
        self.base_delay = base_delay

    def delay_for(self, attempt):                   # instance method — has self
        return min(self.base_delay * 2 ** attempt, 30.0)

    @classmethod
    def from_seconds(cls, seconds):                 # gets `cls`, not `self` → factory
        return cls(base_delay=float(seconds))

    @classmethod
    def aggressive(cls):
        return cls(max_attempts=1, base_delay=0)

    @staticmethod
    def describe_limits():                          # no self, no cls — plain function
        return "delay is capped at 30s and doubles each attempt"


policy = RetryPolicy()
print(f"  RetryPolicy()                 attempts={policy.max_attempts} delay={policy.base_delay}")
print(f"  .from_seconds(2)              → {RetryPolicy.from_seconds(2).base_delay}")
print(f"  .aggressive()                 → {RetryPolicy.aggressive().max_attempts} attempt")
print(f"  delay_for(0..3)               → {[policy.delay_for(i) for i in range(4)]}")
print(f"  RetryPolicy.describe_limits() → {RetryPolicy.describe_limits()}")

# ─── Properties — get/set without getX()/setX() ──────────────
# C#: `public int Age { get; set; }` with validation in the setter.
# Python: @property + @<name>.setter — the caller still writes obj.age.
print("\n─── @property: attribute syntax, method logic ───────────")


class ModelConfig:
    def __init__(self, deployment):
        self.deployment = deployment
        self._temperature = 0.7                     # underscore = backing field

    @property
    def temperature(self):                          # getter
        return self._temperature

    @temperature.setter
    def temperature(self, value):                   # setter — validates
        if not 0 <= value <= 2:
            raise ValueError(f"temperature must be 0–2, got {value}")
        self._temperature = value

    @property
    def is_deterministic(self):                     # computed, read-only
        return self._temperature == 0


config = ModelConfig("gpt-4o")
print(f"  config.temperature      → {config.temperature}")
config.temperature = 1.2
print(f"  after setting 1.2       → {config.temperature}")
print(f"  config.is_deterministic → {config.is_deterministic}")

try:
    config.temperature = 9
except ValueError as err:
    print(f"  setting 9               → ValueError: {err}")

# ─── Inheritance and super() ─────────────────────────────────
# C#: `class Derived : Base` and `base.Method()`. `super()` is base.
print("\n─── Inheritance ──────────────────────────────────────────")


class BaseClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint.rstrip("/")

    def request(self, path):
        return f"GET {self.endpoint}/{path}"


class FoundryClient(BaseClient):                    # syntax: class Child(Parent)
    def __init__(self, endpoint, api_key, api_version="2024-10-21"):
        super().__init__(endpoint)                  # C#: base(endpoint)
        self.api_key = api_key
        self.api_version = api_version

    def request(self, path):                        # override — needs no keyword
        return f"{super().request(path)}?api-version={self.api_version}"


client = FoundryClient("https://x.services.ai.azure.com/", "key123")
print(f"  {client.request('chat/completions')}")
print(f"  isinstance(client, BaseClient)  → {isinstance(client, BaseClient)}")
print(f"  issubclass(FoundryClient, BaseClient) → {issubclass(FoundryClient, BaseClient)}")
print("  ⚠ Python has no `virtual`/`override` keywords — every method is overridable.")

# ─── Dunder methods: how Python does interfaces & operators ──
# There is no IComparable / IEquatable / operator overloading syntax.
# You implement protocol methods whose NAMES are fixed double underscores.
print("\n─── Dunder methods ───────────────────────────────────────")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):                             # unambiguous, for developers
        return f"Vector(x={self.x}, y={self.y})"

    def __str__(self):                              # human-facing (print, f-string)
        return f"({self.x}, {self.y})"

    def __add__(self, other):                       # operator+ overload
        if not isinstance(other, Vector):
            return NotImplemented                   # the idiomatic "wrong type" signal
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):                        # == support
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):                             # needed once __eq__ is defined
        return hash((self.x, self.y))

    def __len__(self):                              # len(v)
        return 2

    def __iter__(self):                             # makes `for a in v` work
        yield self.x
        yield self.y


v1, v2 = Vector(1, 2), Vector(3, 4)
print(f"  repr(v1)        → {v1!r}")
print(f"  str(v1)         → {v1}")
print(f"  f-string        → {v1}")
print(f"  v1 + v2         → {v1 + v2}")
print(f"  v1 == Vector(1,2) → {v1 == Vector(1, 2)}")
print(f"  len(v1)         → {len(v1)}")
print(f"  list(v1)        → {list(v1)}   # __iter__")
print(f"  shown in a list → {[v1, v2]}   # uses __repr__, not __str__")
print("""
  ⚠ __repr__ is for developers (debuggers, lists, logs) — aim for something you
    could paste back into a REPL. __str__ is for end users. If you only write
    one, write __repr__.
""")

# ─── The context manager protocol ────────────────────────────
# __enter__ / __exit__ are what `with` calls — the C# `using`/IDisposable pair.
print("─── __enter__ / __exit__ (the `with` protocol) ────────────")


class Session:
    def __init__(self, name):
        self.name = name
        self.open = False

    def __enter__(self):
        self.open = True
        print(f"    ▶ session '{self.name}' opened")
        return self                                 # the value bound by `as`

    def __exit__(self, exc_type, exc_value, traceback):
        self.open = False
        print(f"    ■ session '{self.name}' closed (error={exc_type is not None})")
        return False                                # False = do not swallow the error


with Session("foundry") as session:
    print(f"    inside: open={session.open}")

try:
    with Session("boom") as session:
        raise RuntimeError("something failed inside the block")
except RuntimeError as err:
    print(f"    caught outside: {err}   ← __exit__ ran, then the error propagated")

# ─── Dataclasses — skip the boilerplate ──────────────────────
# C#: `public record ModelInfo(string Id, int Tokens);`
# Python: @dataclass generates __init__, __repr__, and __eq__ for you.
print("\n─── @dataclass — records, Python style ───────────────────")

from dataclasses import dataclass, field


@dataclass
class ModelInfo:
    model_id: str                                   # no `self.x = x` needed
    tokens: int
    tags: list = field(default_factory=list)        # ← the mutable-default fix
    api_version: str = "2024-10-21"                 # defaults must come last


info = ModelInfo("gpt-4o", 128)
print(f"  info           → {info}")
print(f"  == a fresh one → {info == ModelInfo('gpt-4o', 128)}   # __eq__ compares every field")

info.tags.append("chat")
print(f"  after tags.append('chat') → {info}")
print(f"  == a fresh one → {info == ModelInfo('gpt-4o', 128)}   # False: the lists now differ")
print(f"  tags are per-instance: {ModelInfo('x', 1).tags}   ← default_factory, not a shared default")


@dataclass(frozen=True)                             # immutable AND hashable
class EmbeddingRef:
    index: int
    model: str


ref = EmbeddingRef(0, "text-embedding-3-large")
print(f"\n  frozen ref    → {ref}")
print(f"  hashable      → usable as a dict key: {{ref: 'vector'}} → {{{ref}: 'vector'}}")

try:
    ref.index = 5
except Exception as err:
    print(f"  reassigning   → {type(err).__name__}: {err}")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


print(f"  frozen Point  → {Point(1, 2)}   (replaces the namedtuple from ch.15)")

# ─── Abstract base classes ───────────────────────────────────
# C#: `abstract class` / `interface`. abc.ABC gives you the same enforcement.
print("\n─── Abstract base classes ────────────────────────────────")

from abc import ABC, abstractmethod


class Embedder(ABC):
    """Contract every embedder must satisfy."""

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """Turn text into a vector."""

    def embed_batch(self, texts):
        """Concrete method — inherits for free, like a non-abstract base method."""
        return [self.embed(t) for t in texts]


try:
    Embedder()                                      # ← cannot instantiate the abstract
except TypeError as err:
    print(f"  Embedder() → TypeError: {err}")


class FakeEmbedder(Embedder):
    def embed(self, text: str) -> list[float]:
        return [float(len(text)), float(sum(map(ord, text)) % 97)]


embedder = FakeEmbedder()
print(f"  embed('hello')       → {embedder.embed('hello')}")
print(f"  embed_batch(['a','bb']) → {embedder.embed_batch(['a', 'bb'])}")

print("""
  ⚠ Python does NOT check that a subclass implements abstract members at the
    point you call them — it fails when you try to instantiate. And nothing
    stops a caller passing a non-Embedder: Python relies on duck typing
    ("if it has .embed(), it is one") unless you add runtime checks.
""")

# ─── Composition — usually better than inheritance ───────────
print("─── Composition over inheritance ─────────────────────────")
print("""
  Inheritance is for "is-a". For "has-a" — which is most of the time in
  API-client code — hold a collaborator instead of deriving from it:

      class ChatService:
          def __init__(self, client: FoundryClient, embedder: Embedder):
              self.client = client          ← has-a, testable, swappable
              self.embedder = embedder

  The C# advice is identical; Python just makes it easier to ignore because
  nothing forces you to declare a type.
""")

# ─── Practical: a miniature Foundry-shaped client ────────────
print("─── Practical: a small SDK-shaped class ──────────────────")

import os


@dataclass
class CallStats:
    calls: int = 0
    tokens: int = 0


class MiniFoundryClient:
    """Mirrors how the real Azure AI Foundry SDK is shaped:
    construct with endpoint + credential, expose intent-revealing methods,
    own a session via __enter__/__exit__, keep state private by convention."""

    default_api_version = "2024-10-21"              # class attribute: shared default

    def __init__(self, endpoint, api_key, api_version=None, policy=None):
        self.endpoint = endpoint.rstrip("/")
        self.api_version = api_version or self.default_api_version
        self.policy = policy or RetryPolicy()
        self._api_key = api_key                     # underscore = internal
        self._stats = CallStats()
        self._session_open = False

    # --- alternate constructor: read config from the environment -----------
    @classmethod
    def from_env(cls, env=None):
        # ⚠ NOT `env or os.environ` — an empty dict is falsy, so that would
        #   silently fall back to the real environment instead of erroring.
        env = os.environ if env is None else env
        try:
            return cls(endpoint=env["FOUNDRY_ENDPOINT"], api_key=env["FOUNDRY_API_KEY"])
        except KeyError as err:
            raise RuntimeError(f"missing environment variable {err}") from err

    # --- read-only views of internal state -------------------------------
    @property
    def host(self):
        return self.endpoint.split("//")[-1].split("/")[0]

    @property
    def stats(self):
        return self._stats

    # --- behaviour --------------------------------------------------------
    def chat(self, messages, temperature=0.7):
        if not self._session_open:
            raise RuntimeError("client used outside its `with` block")
        if not messages:
            raise ValueError("messages must not be empty")
        self._stats.calls += 1
        self._stats.tokens += sum(len(m["content"].split()) for m in messages)
        return {
            "model": "gpt-4o",
            "url": f"{self.endpoint}/chat/completions?api-version={self.api_version}",
            "temperature": temperature,
            "reply": messages[-1]["content"][::-1],   # stand-in for a real answer
        }

    # --- dunders ----------------------------------------------------------
    def __repr__(self):
        return f"MiniFoundryClient(host={self.host!r}, api_version={self.api_version!r})"

    def __str__(self):
        return f"Foundry client → {self.host} ({self.api_version})"

    def __enter__(self):
        self._session_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session_open = False
        return False


os.environ.setdefault("FOUNDRY_ENDPOINT", "https://demo.services.ai.azure.com")
os.environ.setdefault("FOUNDRY_API_KEY", "not-a-real-key")

client = MiniFoundryClient.from_env()
print(f"  {client}")
print(f"  repr: {client!r}")

with client as c:
    reply = c.chat([{"role": "user", "content": "explain embeddings"}])
    print(f"  reply → {reply['reply']}")
    print(f"  stats → calls={c.stats.calls} tokens={c.stats.tokens}")

try:
    client.chat([{"role": "user", "content": "hi"}])
except RuntimeError as err:
    print(f"  after the block → RuntimeError: {err}")

try:
    client.from_env(env={})
except RuntimeError as err:
    print(f"  missing config  → RuntimeError: {err}")

print("""
  ─── Summary ──────────────────────────────────────────────
  1. `self` is explicit; there is no `new`; access modifiers are convention
     (leading underscore = internal).
  2. Per-instance state goes in __init__. A mutable class attribute is shared.
  3. @classmethod = factory (gets cls); @staticmethod = plain function.
  4. @property gives attribute syntax over method logic — no getter/setter noise.
  5. Dunders ARE the operator/interface system: __eq__, __hash__, __add__,
     __iter__, __len__, __repr__, __str__, __enter__/__exit__.
  6. Define __repr__ over __str__. Define __hash__ whenever you define __eq__.
  7. @dataclass removes constructor/equality boilerplate; frozen=True makes it
     immutable and hashable.
  8. ABC enforces a contract; composition usually beats inheritance.
""")
