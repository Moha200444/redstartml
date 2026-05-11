import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import math
    import numpy.linalg as la

    return math, np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constantes Physiques

    On définit les trois constantes fondamentales du problème. Ces variables
    interviendront dans l'ensemble des développements analytiques et des simulations
    numériques ultérieurs.

    $$\boxed{g = 1\;\text{m}\,\text{s}^{-2}, \quad M = 1\;\text{kg}, \quad \ell = 2\;\text{m}}$$
    """)
    return


@app.function
def constantes():
    g = 1.0    # accélération de la gravité (m/s²)
    M = 1.0    # masse du booster (kg)
    l = 2.0    # longueur totale du booster (m)

    print(f"g = {g},  M = {M},  ℓ = {l}")
    return g, M, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Composantes Cartésiennes de la Poussée

    ###  Détermination analytique

    La force de poussée $\mathbf{F}_p$ a pour amplitude $f$ et fait un angle
    $\phi$ avec l'axe du booster. En notant $\mathbf{e}_b = (-\sin\theta,\,
    \cos\theta)^\top$ le vecteur unitaire de l'axe du booster et
    $\mathbf{n}_b = (\cos\theta,\, \sin\theta)^\top$ le vecteur normal (obtenu
    par rotation de $+\frac{\pi}{2}$ de $\mathbf{e}_b$), la force se décompose
    naturellement selon ces deux directions :

    $$\mathbf{F}_p = f\cos\phi\;\mathbf{e}_b - f\sin\phi\;\mathbf{n}_b$$

    En coordonnées cartésiennes, cela donne les **composantes** :

    $$\boxed{F_x = -f\,\sin(\theta + \phi) \qquad \text{et} \qquad F_y = f\,\cos(\theta + \phi)}$$

    ### Cas particuliers de vérification

    - **Poussée axiale** ($\phi = 0$, $\theta = 0$) : $F_x = 0$, $F_y = f$.
      La poussée est purement verticale ascendante, ce qui correspond au
      comportement attendu d'un réacteur aligné avec l'axe d'un booster vertical.

    - **Poussée latérale** ($\phi = \frac{\pi}{2}$, $\theta = 0$) :
      $F_x = -f$, $F_y = 0$. La poussée est purement horizontale vers la gauche,
      ce qui est cohérent avec le décalage angulaire de $90°$.

    - **Poussée anti-gravité** ($\phi = 0$, $\theta = 0$, $f = Mg$) :
      $F_y = Mg$, ce qui compense exactement le poids.
    """)
    return


@app.cell
def _(np):
    def forces(f, theta, phi):
        """
        Composantes cartésiennes (Fx, Fy) de la force de poussée du réacteur.

        Paramètres
        ----------
        f : float
            Amplitude de la poussée (N), avec f >= 0
        theta : float
            Angle d'inclinaison du booster (rad)
        phi : float
            Angle de gîrage de la poussée (rad)

        Retour
        ------
        tuple(float, float)
            (Fx, Fy) : composantes cartésiennes de la poussée (N)
        """

        Fx = -f * np.sin(theta + phi)
        Fy =  f * np.cos(theta + phi)

        return Fx, Fy

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Équations du Mouvement du Centre de Masse

    ### Principe fondamental de la dynamique

    En appliquant le **théorème du centre d'inertie** (deuxième loi de Newton) au
    booster assimilé à un solide indéformable de masse $M$, on a, dans le référentiel
    galiléen $(Oxy)$ supposé lié au sol :

    $$M\,\mathbf{a}_G = \sum \mathbf{F}_{\text{ext}}$$

    où $\mathbf{a}_G = (\ddot{x},\, \ddot{y})^\top$ désigne le vecteur
    accélération du centre de masse $G$.

    ### Projection sur les axes

    En projetant sur l'axe $Ox$ :

    $$\boxed{M\,\ddot{x}(t) = -f(t)\,\sin\!\bigl(\theta(t) + \phi(t)\bigr)}$$

    En projetant sur l'axe $Oy$ :

    $$\boxed{M\,\ddot{y}(t) = f(t)\,\cos\!\bigl(\theta(t) + \phi(t)\bigr) - Mg}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩  Moment d'Inertie

    ###  Calcul pour une tige uniforme

    Le moment d'inertie d'une tige homogène de masse $M$ et de longueur $\ell$ par
    rapport à un axe perpendiculaire à la tige et passant par son **centre de
    masse** est donné par la relation classique :

    $$\boxed{J_G = \frac{1}{12}\,M\,\ell^2}$$


    ###  Application numérique

    Pour $M = 1\;\text{kg}$ et $\ell = 2\;\text{m}$ :

    $$\boxed{J_G= \frac{1 \times 2^2}{12} = \frac{4}{12} = \frac{1}{3} \approx 0{,}333\;\text{kg}\,\text{m}^2}$$
    """)
    return


@app.cell
def _():
    # Moment d'inertie du booster par rapport à son centre de masse
    g, M, l = constantes()
    J = M * l**2 / 12.0
    print(f"J = M*l²/12 = {M} × {l}² / 12 = {J:.6f} kg·m²")

    return J, M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Équation de Rotation (Inclinaison)

    ### Calcul du couple résultant en $G$

    Le couple par rapport au centre de masse $G$ ne provient **que** de la force de
    poussée $\mathbf{F}_p$ appliquée en $B$. En effet, le poids $\mathbf{P}$
    s'appliquant en $G$ ne crée aucun moment :

    $$\boldsymbol{\tau}_G(\mathbf{P}) = \overrightarrow{GP} \times \mathbf{P} = \mathbf{0} \times \mathbf{P} = \mathbf{0}$$

    Le vecteur position de la base $B$ par rapport à $G$ vaut :

    $$\overrightarrow{GB} = -\frac{\ell}{2}\,\mathbf{e}_b(\theta) = \begin{pmatrix} \dfrac{\ell}{2}\sin\theta \\[6pt] -\dfrac{\ell}{2}\cos\theta \end{pmatrix}$$

    Le couple de la poussée est le **produit vectoriel 2D** :

    $$\tau_G = \det\begin{pmatrix} GB_x & GB_y \\ F_{p,x} & F_{p,y} \end{pmatrix} = GB_x \cdot F_{p,y} - GB_y \cdot F_{p,x}$$

    Après substitution et simplification trigonométrique utilisant
    $\cos\alpha\sin\beta - \sin\alpha\cos\beta = \sin(\beta - \alpha)$, on obtient
    le résultat remarquablement simple :

    $$\boxed{\tau_G = -\frac{\ell\,f}{2}\,\sin\phi}$$

    On constate que le couple ne dépend **que** de $\phi$ et de $f$, et non de
    $\theta$ : c'est une conséquence directe de la symétrie du problème.

    ### Équation différentielle de rotation

    Le théorème du moment cinétique en $G$ donne :

    $$\boxed{J_G\,\ddot{\theta}(t) = -\frac{\ell\,f(t)}{2}\,\sin\!\bigl(\phi(t)\bigr)}$$

    soit encore, en explicitant $J_G$ :

    $$\frac{M\ell^2}{12}\,\ddot{\theta} = -\frac{\ell\,f}{2}\,\sin\phi \quad\Longleftrightarrow\quad \ddot{\theta} = -\frac{6\,f}{M\ell}\,\sin\phi$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Formulation Cauchy et Champ de Vecteurs

    ### Vecteur d'état

    On introduit les variables de vitesse $v_x = \dot{x}$, $v_y = \dot{y}$ et
    $\omega = \dot{\theta}$. Le **vecteur d'état** du système est alors :

    $$\boxed{\mathbf{s}(t) = \begin{pmatrix} x(t) \\ v_x(t) \\ y(t) \\ v_y(t) \\ \theta(t) \\ \omega(t) \end{pmatrix} \in \mathbb{R}^6}$$

    **La dimension de l'espace d'état est $n = 6$.**

    ### Formulation sous forme de Cauchy

    Le système d'équations différentielles se met sous la **forme de Cauchy**
    standard $\dot{\mathbf{s}} = F(\mathbf{s},\, f,\, \phi)$ avec le champ de
    vecteurs $F : \mathbb{R}^{6+2} \to \mathbb{R}^6$ défini par :

    $$\boxed{F(\mathbf{s},\, f,\, \phi) = \begin{pmatrix}
    v_x \\[8pt]
    -\dfrac{f}{M}\,\sin(\theta + \phi) \\[10pt]
    v_y \\[8pt]
    \dfrac{f}{M}\,\cos(\theta + \phi) - g \\[10pt]
    \omega \\[8pt]
    -\dfrac{\ell\,f}{2\,J_G}\,\sin\phi
    \end{pmatrix}}$$

    ###  Structure du système

    Le système est **non linéaire** (les fonctions trigonométriques et les produits
    $f\sin\phi$, $f\cos(\theta+\phi)$ le rendent non affine en l'état). Il possède
    deux **entrées de commande** — l'amplitude $f$ et l'angle de gîrage $\phi$ — et
    six **variables d'état**. Les équations de translation et de rotation sont
    découplées dans le cas particulier $\phi = 0$ (poussée axiale).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simulation Numérique

    ### Problème de Cauchy

    On souhaite résoudre numériquement le **problème de Cauchy** associé au système
    différentiel :

    $$\begin{cases}
    \dot{\mathbf{s}}(t) = F\bigl(\mathbf{s}(t),\; f(t),\; \phi(t)\bigr) \\[6pt]
    \mathbf{s}(t_0) = \mathbf{s}_0
    \end{cases}$$

    sur l'intervalle de temps $[t_0,\, t_f]$.

    ###  Méthode d'intégration

    On utilise la méthode **Runge-Kutta-Fehlberg d'ordre 5(4)** (RK45) implémentée
    dans `scipy.integrate.solve_ivp`. Cette méthode à pas adaptatif offre un
    excellent compromis entre précision et efficacité computationnelle. Le paramètre
    `dense_output=True` permet de construire une approximation continue
    $\tilde{\mathbf{s}}(t)$ de la solution, évaluable en tout instant $t$ (et non
    uniquement aux instants de pas internes).

    ###  Paramètres de précision

    | Paramètre | Valeur | Signification |
    |-----------|:------:|---------------|
    | `rtol` | $10^{-10}$ | Tolérance relative par composante |
    | `atol` | $10^{-12}$ | Tolérance absolue par composante |
    | `max_step` | $0{,}01\;\text{s}$ | Pas de temps maximum |

    Ces tolérances très strictes garantissent une excellente fidélité de la solution
    numérique par rapport à la solution exacte.
    """)
    return


@app.cell
def _(J, M, g, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):
        """
        Résout le problème de Cauchy du booster par la méthode RK45.

        Paramètres
        ----------
        t_span : list[float]
            Intervalle d'intégration [t0, tf] (s)

        y0 : list[float]
            État initial [x0, vx0, y0, vy0, theta0, omega0]

        f_phi : callable
            Fonction (t, y) -> [f, phi]

        Retour
        ------
        callable
            Fonction sol(t) donnant l'état du système.
        """

        def rhs(t, y):
            f_val, phi_val = f_phi(t, y)

            return np.array([
                y[1],                                      # dx/dt
                -f_val / M * np.sin(y[4] + phi_val),      # dvx/dt
                y[3],                                      # dy/dt
                 f_val / M * np.cos(y[4] + phi_val) - g,  # dvy/dt
                y[5],                                      # dtheta/dt
                -l * f_val * np.sin(phi_val) / (2.0 * J)  # domega/dt
            ])

        result = sci.solve_ivp(
            rhs,
            t_span,
            y0,
            method="RK45",
            dense_output=True,
            max_step=0.01,
            rtol=1e-10,
            atol=1e-12
        )

        def sol(t):
            return result.sol(t)

        return sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Validation : Scénario de Chute Libre

    ### Conditions initiales

    On considère le booster initialement au repos à l'altitude $y(0) = 10\;\text{m}$,
    sans vitesse initiale ni inclinaison :

    $$\mathbf{s}_0 = \begin{pmatrix} 0 \\ 0 \\ 10 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \qquad f(t) \equiv 0, \qquad \phi(t) \equiv 0$$

    ###Solution analytique

    En chute libre ($f = 0$), les équations de translation se réduisent à :

    $$\ddot{x} = 0, \qquad \ddot{y} = -g$$

    L'intégration successive donne :

    $$\dot{y}(t) = \dot{y}_0 - gt = -t, \qquad y(t) = y_0 + \dot{y}_0 t - \frac{1}{2}gt^2 = 10 - \frac{t^2}{2}$$

    Le centre de masse franchit l'altitude $y = \ell$ lorsque :

    $$10 - \frac{t^\star{}^2}{2} = 2 \;\Longleftrightarrow\; \frac{t^\star{}^2}{2} = 8 \;\Longleftrightarrow\; \boxed{t^\star = \sqrt{16} = 4\;\text{s}}$$

    (On ne retient que la racine positive, l'instant $t = -4\;\text{s}$ n'ayant pas
    de sens physique dans ce problème.)

    ###  Vérification numérique et graphique

    Le graphique ci-dessous représente $y(t)$ simulé numériquement par `redstart_solve`
    ainsi que les droites $y = \ell$ et $t = 4\;\text{s}$, permettant de vérifier
    visuellement la concordance entre la solution analytique et la solution
    numérique.
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def test_chute_libre():
        """Simulation et représentation graphique de la chute libre."""

        t_span = [0.0, 5.0]

        # [x, vx, y, vy, theta, omega]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # réacteur éteint

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 10000)

        y_t = sol(t)[2]
        y_theo = 10.0 - 0.5 * g * t**2

        plt.figure(figsize=(9, 5))

        plt.plot(
            t,
            y_t,
            'b-',
            lw=2,
            label=r"$y(t)$ simulé (RK45)"
        )

        plt.plot(
            t,
            y_theo,
            'k--',
            lw=1,
            alpha=0.5,
            label=r"$y(t)=10-\frac{1}{2}gt^2$"
        )

        plt.axhline(
            y=l,
            color="grey",
            ls="--",
            label=rf"$y=\ell={l}$ m"
        )

        plt.axvline(
            x=4.0,
            color="red",
            ls=":",
            label=r"$t^\star=4$ s"
        )

        plt.plot(
            4.0,
            l,
            'ro',
            ms=8,
            zorder=5,
            label=r"Intersection"
        )

        plt.title("Chute Libre — Altitude du Centre de Masse")
        plt.xlabel(r"Temps $t$ (s)")
        plt.ylabel(r"Altitude $y$ (m)")

        plt.grid(True, alpha=0.3)
        plt.legend(loc="best")
        plt.tight_layout()

        return plt.gcf()


    test_chute_libre()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Atterrissage Contrôlé

    ### Position du problème

    On cherche à déterminer une loi de commande $f(t)$ permettant au booster
    d'effectuer un atterrissage en douceur à l'instant $t_f = 5\;\text{s}$.

    **Conditions initiales** ($t = 0$) :

    $$x(0) = 0, \quad \dot{x}(0) = 0, \quad y(0) = 10\;\text{m}, \quad \dot{y}(0) = -2\;\text{m/s}, \quad \theta(0) = 0, \quad \dot{\theta}(0) = 0$$

    **Conditions finales** ($t = 5\;\text{s}$) :

    $$y(5) = \frac{\ell}{2} = 1\;\text{m} \quad \text{(base au niveau du sol)}, \qquad \dot{y}(5) = 0\;\text{m/s} \quad \text{(atterrissage doux)}$$

    On impose en outre $\phi(t) \equiv 0$ (poussée axiale), ce qui découple le
    mouvement vertical du mouvement de rotation.

    ### Formulation variationnelle

    Avec $\phi = 0$ et $\theta = 0$, l'équation verticale se réduit à :

    $$M\ddot{y} = f(t) - Mg \quad\Longleftrightarrow\quad \boxed{f(t) = M\bigl(\ddot{y}(t) + g\bigr)}$$

    Le problème se ramène donc à la recherche d'une trajectoire $y(t)$ vérifiant
    quatre conditions aux limites, d'où l'idée naturelle d'un **polynôme de degré 3**
    possédant exactement quatre coefficients libres :

    $$y(t) = a\,t^3 + b\,t^2 + c\,t + d$$

    ###  Détermination des coefficients

    Les conditions aux limites conduisent au système linéaire :

    $$\begin{cases}
    y(0) = 10        &\Longrightarrow\; d = 10 \\[4pt]
    \dot{y}(0) = -2   &\Longrightarrow\; c = -2 \\[4pt]
    y(5) = 1          &\Longrightarrow\; 125a + 25b = -9 \\[4pt]
    \dot{y}(5) = 0    &\Longrightarrow\; 75a + 10b = 2
    \end{cases}$$

    Les deux dernières équations forment le système $2 \times 2$ :

    $$\begin{pmatrix} 125 & 25 \\ 75 & 10 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} -9 \\ 2 \end{pmatrix}$$

    dont le déterminant vaut $\Delta = 125 \times 10 - 75 \times 25 = 1250 - 1875 = -625 \neq 0$,
    garantissant l'existence et l'unicité de la solution. Par la méthode de Cramer :

    $$a = \frac{\det\begin{pmatrix} -9 & 25 \\ 2 & 10 \end{pmatrix}}{-625} = \frac{-90 - 50}{-625} = \frac{-140}{-625} = \boxed{\frac{8}{125} = 0{,}064}$$

    $$b = \frac{\det\begin{pmatrix} 125 & -9 \\ 75 & 2 \end{pmatrix}}{-625} = \frac{250 + 675}{-625} = \frac{925}{-625} = \boxed{-\frac{7}{25} = -0{,}28}$$

    ### Trajectoire et loi de commande

    La trajectoire polynomiale s'écrit donc :

    $$\boxed{y(t) = \frac{8}{125}\,t^3 - \frac{7}{25}\,t^2 - 2\,t + 10}$$

    La dérivée seconde $\ddot{y}(t) = 6at + 2b$ permet d'exprimer la loi de commande :

    $$\boxed{f(t) = M\bigl(6at + 2b + g\bigr) = \frac{48}{125}\,t + \frac{11}{25}}$$

    **Vérification de réalisabilité** : $f(0) = \frac{11}{25} = 0{,}44\;\text{N} > 0$ et
    $f(5) = \frac{48}{25} + \frac{11}{25} = \frac{59}{25} = 2{,}36\;\text{N} > 0$.
    La force reste positive pour tout $t \in [0, 5]$, ce qui garantit la
    **réalisabilité physique** de cette loi de commande.

    ### Simulation et validation
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):

    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.collections import LineCollection
    from mpl_toolkits.mplot3d.art3d import Line3DCollection


    def atterrissage_controle_3d():
        """Simulation et visualisation 3D de l'atterrissage contrôlé."""

        # --- Coefficients du polynôme y(t) = a*t³ + b*t² + c*t + d ---
        d = 10.0
        c = -2.0
        a = 8.0  / 125.0
        b = -7.0  / 25.0

        def y_theorique(t):
            return a * t**3 + b * t**2 + c * t + d

        def f_commande(t, y_state):
            """Loi de commande avec phi = 0."""
            ddy = 6.0 * a * t + 2.0 * b
            return np.array([M * (ddy + g), 0.0])

        # --- Temps et état initial ---
        t0, tf = 0.0, 5.0
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        # --- Résolution numérique ---
        sol = redstart_solve([t0, tf], y0, f_commande)
        t = np.linspace(t0, tf, 500)
        etat = sol(t)
        x_t     = etat[0]
        vx_t    = etat[1]
        y_t     = etat[2]
        vy_t    = etat[3]
        theta_t = etat[4]
        omega_t = etat[5]

        # ============================================================
        # FIGURE 1 : Graphes 2D (3 sous-graphes)
        # ============================================================
        fig1, axes = plt.subplots(2, 2, figsize=(13, 9))

        # --- Altitude ---
        axes[0, 0].plot(t, y_t, 'b-', lw=2, label=r"$y(t)$ simulé")
        axes[0, 0].plot(t, y_theorique(t), 'r--', lw=1.5, label=r"$y(t)$ théorique")
        axes[0, 0].axhline(y=l/2, color='grey', ls=':', label=rf"$y=\ell/2={l/2}$ m")
        axes[0, 0].set_title("Altitude")
        axes[0, 0].set_xlabel("t (s)"); axes[0, 0].set_ylabel("y (m)")
        axes[0, 0].legend(); axes[0, 0].grid(True)

        # --- Vitesse verticale ---
        axes[0, 1].plot(t, vy_t, 'g-', lw=2, label=r"$\dot y(t)$")
        axes[0, 1].axhline(y=0, color='grey', ls=':')
        axes[0, 1].set_title("Vitesse verticale")
        axes[0, 1].set_xlabel("t (s)"); axes[0, 1].set_ylabel("vy (m/s)")
        axes[0, 1].legend(); axes[0, 1].grid(True)

        # --- Force de poussée ---
        f_vals = np.array([f_commande(ti, None)[0] for ti in t])
        axes[1, 0].plot(t, f_vals, 'r-', lw=2, label=r"$f(t)$")
        axes[1, 0].axhline(y=M*g, color='grey', ls=':', label=rf"$Mg={M*g}$ N")
        axes[1, 0].set_title("Force de poussée")
        axes[1, 0].set_xlabel("t (s)"); axes[1, 0].set_ylabel("f (N)")
        axes[1, 0].legend(); axes[1, 0].grid(True)

        # --- Angle theta ---
        axes[1, 1].plot(t, np.degrees(theta_t), 'm-', lw=2, label=r"$\theta(t)$")
        axes[1, 1].set_title("Angle d'inclinaison")
        axes[1, 1].set_xlabel("t (s)"); axes[1, 1].set_ylabel(r"$\theta$ (°)")
        axes[1, 1].legend(); axes[1, 1].grid(True)

        fig1.suptitle("Atterrissage contrôlé du booster — Diagnostics 2D", fontsize=14)
        plt.tight_layout()
    

        # ============================================================
        # FIGURE 2 : Trajectoire 3D
        # ============================================================
        fig2 = plt.figure(figsize=(14, 10))
        ax3d = fig2.add_subplot(111, projection='3d')

        # --- Trajectoire colorée par le temps ---
        N = len(t)
        for i in range(N - 1):
            frac = t[i] / tf
            color = plt.cm.plasma(frac)
            ax3d.plot(x_t[i:i+2], y_t[i:i+2], t[i:i+2],
                      color=color, lw=2.5, alpha=0.9)

        # --- Colorbar ---
        sm = plt.cm.ScalarMappable(cmap='plasma',
                                    norm=plt.Normalize(vmin=t0, vmax=tf))
        sm.set_array([])
        cbar = fig2.colorbar(sm, ax=ax3d, shrink=0.6, pad=0.1)
        cbar.set_label("Temps (s)", fontsize=11)

        # --- Points de départ et d'arrivée ---
        ax3d.scatter(*[x_t[0]], *[y_t[0]], *[t[0]],
                     color='limegreen', s=120, edgecolors='k', zorder=5,
                     label="Départ  (t=0 s)")
        ax3d.scatter(*[x_t[-1]], *[y_t[-1]], *[t[-1]],
                     color='red', s=120, edgecolors='k', marker='s', zorder=5,
                     label="Arrivée  (t=5 s)")

        # --- Sol (plan y = l/2 = 1 m) ---
        xx = np.linspace(min(x_t) - 1, max(x_t) + 1, 5)
        tt = np.linspace(t0, tf, 5)
        XX, TT = np.meshgrid(xx, tt)
        YY_ground = np.full_like(XX, l / 2)
        ax3d.plot_surface(XX, YY_ground, TT, alpha=0.08, color='brown')

        # --- Dessiner le booster à plusieurs instants ---
        n_snapshots = 8
        idx_snap = np.linspace(0, N - 1, n_snapshots, dtype=int)
        for idx in idx_snap:
            xc = x_t[idx]
            yc = y_t[idx]
            tc = t[idx]
            th = theta_t[idx]
            # Extrémités du booster (demi-longueur dans chaque direction)
            half = l / 2
            dx = half * np.sin(th)
            dy = half * np.cos(th)
            ax3d.plot([xc - dx, xc + dx],
                      [yc - dy, yc + dy],
                      [tc, tc],
                      color='navy', lw=4, solid_capstyle='round', alpha=0.7)
            # Petite flèche pour la poussée (vers le haut le long de l'axe du booster)
            arrow_len = 0.4
            ax3d.quiver(xc, yc, tc,
                        arrow_len * np.sin(th),
                        arrow_len * np.cos(th),
                        0,
                        color='orange', arrow_length_ratio=0.3, lw=1.5)

        # --- Étiquettes et style ---
        ax3d.set_xlabel("x  (m)", fontsize=11, labelpad=10)
        ax3d.set_ylabel("y  (m)", fontsize=11, labelpad=10)
        ax3d.set_zlabel("Temps  (s)", fontsize=11, labelpad=10)
        ax3d.set_title("Trajectoire 3D du booster — Atterrissage contrôlé",
                       fontsize=14, pad=20)
        ax3d.legend(loc='upper left', fontsize=10)

        # Angle de vue agréable
        ax3d.view_init(elev=25, azim=-50)

        fig2.tight_layout()
    

        # ============================================================
        # FIGURE 3 : Vue 3D alternative — booster en 3D avec Z fictif
        # ============================================================
        fig3 = plt.figure(figsize=(14, 10))
        ax3b = fig3.add_subplot(111, projection='3d')

        # On crée un axe Z fictif = theta (inclinaison) pour donner de la profondeur
        z_t = np.zeros_like(t)  # plan z=0 car le mouvement est 2D

        # Trajectoire principale
        points = np.array([x_t, y_t, z_t]).T.reshape(-1, 1, 3)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        norm = plt.Normalize(t0, tf)
        lc = Line3DCollection(segments, cmap='plasma', norm=norm, linewidths=3)
        lc.set_array(t[:-1])
        ax3b.add_collection3d(lc)

        # Booster à chaque snapshot — cette fois orienté dans le plan XY avec Z = 0
        for idx in idx_snap:
            xc = x_t[idx]
            yc = y_t[idx]
            th = theta_t[idx]
            half = l / 2
            dx = half * np.sin(th)
            dy = half * np.cos(th)

            # Corps du booster (ligne épaisse)
            ax3b.plot([xc - dx, xc + dx],
                      [yc - dy, yc + dy],
                      [0, 0],
                      color='navy', lw=5, solid_capstyle='round', alpha=0.8)

            # Flamme / poussée (triangle approximatif)
            flame_len = 0.6 * (f_commande(t[idx], None)[0] / (M * g))  # échelle avec la force
            fx_dir = -np.sin(th)  # direction opposée à l'axe
            fy_dir = -np.cos(th)
            ax3b.quiver(xc - dx, yc - dy, 0,
                        fx_dir * flame_len, fy_dir * flame_len, 0,
                        color='orangered', arrow_length_ratio=0.4, lw=2)

            # Label du temps
            ax3b.text(xc, yc, 0.3, f"t={t[idx]:.1f}s",
                      fontsize=7, ha='center', color='black')

        # Sol
        sol_x = np.linspace(min(x_t) - 2, max(x_t) + 2, 10)
        sol_y = np.array([l / 2] * 10)
        sol_z = np.array([0] * 10)
        sol_xx, sol_yy = np.meshgrid(sol_x, sol_y)
        sol_zz = np.zeros_like(sol_xx)
        ax3b.plot_surface(sol_xx, sol_yy, sol_zz, alpha=0.1, color='saddlebrown')

        # Sol vertical (mur de gauche)
        wall_yy, wall_zz = np.meshgrid(np.linspace(l/2 - 1, 12, 5), np.linspace(-0.5, 0.5, 5))
        wall_xx = np.full_like(wall_yy, min(x_t) - 2)
        ax3b.plot_surface(wall_xx, wall_yy, wall_zz, alpha=0.04, color='grey')

        # Points départ/arrivée
        ax3b.scatter(x_t[0], y_t[0], 0, color='limegreen', s=150,
                     edgecolors='k', zorder=5, label="Départ (t=0)")
        ax3b.scatter(x_t[-1], y_t[-1], 0, color='red', s=150,
                     edgecolors='k', marker='s', zorder=5, label="Arrivée (t=5)")

        ax3b.set_xlabel("x  (m)", fontsize=11, labelpad=10)
        ax3b.set_ylabel("y  (m)", fontsize=11, labelpad=10)
        ax3b.set_zlabel("z  (m)", fontsize=11, labelpad=10)
        ax3b.set_title("Vue 3D — Booster avec orientation et poussée",
                       fontsize=14, pad=20)
        ax3b.legend(loc='upper right', fontsize=10)
        ax3b.set_zlim(-0.5, 0.5)
        ax3b.view_init(elev=20, azim=-60)

        fig3.tight_layout()
    

        plt.show()

        # ============================================================
        # Vérification finale
        # ============================================================
        final = sol(tf)
        print("=" * 55)
        print("  Conditions finales")
        print("=" * 55)
        print(f"  y(5)    = {final[2]:.12f} m")
        print(f"  vy(5)   = {final[3]:.2e} m/s")
        print(f"  θ(5)    = {np.degrees(final[4]):.2e}°")
        print(f"  ω(5)    = {final[5]:.2e} rad/s")
        print("=" * 55)

        return fig1, fig2, fig3, sol


    fig_2d, fig_3d_traj, fig_3d_booster, sol_cl = atterrissage_controle_3d()
    print("\n✓ Figures sauvegardées :")
    print("  1. atterrissage_controle_2d.png")
    print("  2. atterrissage_controle_3d.png")
    print("  3. atterrissage_controle_booster_3d.png")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(l):
    import random as _random


    # Compteur global pour les identifiants SVG uniques
    _world_uid = [0]

    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        W, H = x_max - x_min, y_max - y_min
        _world_uid[0] += 1
        uid = _world_uid[0]

        # --- Définitions SVG (gradients, filtres) ---
        defs = (
            f'<defs>'
            # Ciel gradient
            f'<linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0%" stop-color="#0c1445"/>'
            f'<stop offset="30%" stop-color="#1b3a6b"/>'
            f'<stop offset="65%" stop-color="#4a90d9"/>'
            f'<stop offset="100%" stop-color="#87ceeb"/>'
            f'</linearGradient>'
            # Sol gradient
            f'<linearGradient id="gnd{uid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0%" stop-color="#4caf50"/>'
            f'<stop offset="4%" stop-color="#388e3c"/>'
            f'<stop offset="100%" stop-color="#5d4037"/>'
            f'</linearGradient>'
            # Grille
            f'<pattern id="grid{uid}" width="1" height="1" patternUnits="userSpaceOnUse">'
            f'<path d="M 1 0 L 0 0 0 1" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.015"/>'
            f'</pattern>'
            # Filtre lueur
            f'<filter id="glow{uid}" x="-50%" y="-50%" width="200%" height="200%">'
            f'<feGaussianBlur stdDeviation="0.12" result="b"/>'
            f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
            f'</filter>'
            f'</defs>'
        )

        # --- Éléments statiques (coordonnées SVG, y inversé) ---
        sky = (f'<rect x="{x_min}" y="{-y_max}" width="{W}" '
               f'height="{y_max}" fill="url(#sky{uid})"/>')
        grid = (f'<rect x="{x_min}" y="{-y_max}" width="{W}" '
                f'height="{y_max}" fill="url(#grid{uid})"/>')

        # Étoiles
        rng = _random.Random(42)
        stars = ""
        for _ in range(40):
            sx = rng.uniform(x_min + 0.2, x_max - 0.2)
            sy = rng.uniform(-y_max + 0.2, -y_max * 0.3)
            sr = rng.uniform(0.015, 0.05)
            so = rng.uniform(0.3, 0.85)
            stars += (f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="{sr:.3f}" '
                      f'fill="white" opacity="{so:.2f}"/>')

        # Sol
        ground = (f'<rect x="{x_min}" y="0" width="{W}" '
                  f'height="{-y_min}" fill="url(#gnd{uid})"/>')

        # Plateforme d'atterrissage
        pw = l  # largeur = longueur du booster
        ph = 0.10
        pad_bg = (f'<rect x="{-pw/2}" y="{-ph}" width="{pw}" height="{ph}" '
                  f'fill="#616161" rx="0.015"/>')
        pad_mark_v = (f'<line x1="0" y1="{-ph}" x2="0" y2="0" '
                      f'stroke="#ffd700" stroke-width="0.025"/>')
        pad_mark_h = (f'<line x1="{-pw/2 + 0.05}" y1="{-ph/2}" '
                      f'x2="{pw/2 - 0.05}" y2="{-ph/2}" '
                      f'stroke="#ffd700" stroke-width="0.018"/>')
        pad_border = (f'<rect x="{-pw/2}" y="{-ph}" width="{pw}" height="{ph}" '
                      f'fill="none" stroke="#ffc107" stroke-width="0.012" rx="0.015"/>')

        # Ligne d'horizon
        horizon = (f'<line x1="{x_min}" y1="0" x2="{x_max}" y2="0" '
                   f'stroke="#2e7d32" stroke-width="0.025"/>')

        # Marqueurs d'altitude
        alt_marks = ""
        for a in range(2, int(y_max) + 1, 2):
            alt_marks += (f'<line x1="{x_min + 0.05}" y1="{-a}" '
                          f'x2="{x_min + 0.25}" y2="{-a}" '
                          f'stroke="rgba(255,255,255,0.2)" stroke-width="0.01"/>')
            alt_marks += (f'<text x="{x_min + 0.3}" y="{-a + 0.06}" '
                          f'fill="rgba(255,255,255,0.25)" font-size="0.16" '
                          f'font-family="monospace">{a}</text>')

        # --- Objets dynamiques (coordonnées cartésiennes, y inversé par scale) ---
        objs = "\n    ".join(objects) if objects else ""

        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{x_min} {-y_max} {W} {H}" '
            f'style="width:100%;height:auto;border-radius:8px;overflow:hidden;'
            f'box-shadow:0 4px 16px rgba(0,0,0,0.25);background:#0c1445">'
            f'{defs}'
            f'{sky}{stars}{grid}{ground}'
            f'{pad_bg}{pad_mark_v}{pad_mark_h}{pad_border}{horizon}{alt_marks}'
            f'<g transform="scale(1, -1)">'
            f'{objs}'
            f'</g></svg>'
        )


    return (world,)


@app.cell
def _(mo, world):
    mo.hstack(
        [
            mo.Html(world([-3, 3, -2, 4])),

            mo.Html(world(
                [-3, 3, -2, 4],
                '<rect x="-1" y="0" width="2" height="2" fill="black"/>',
            )),

            mo.Html(world(
                [-3, 3, -2, 4],
                '<rect x="-3" y="2" width="2" height="2" fill="red"/>',
                '<rect x="1" y="2" width="2" height="2" fill="blue"/>',
            )),
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, math):
    def booster(x, y, theta, f, phi):
        td = math.degrees(theta)
        hw = 0.09  # demi-largeur du corps

        # --- Corps du booster ---
        body = (f'<rect x="{-hw}" y="{-l/2}" width="{2*hw}" height="{l}" '
                f'fill="#78909c" rx="0.04"/>')
        # Bande d'accent
        band = (f'<rect x="{-hw}" y="{-l*0.05}" width="{2*hw}" height="{l*0.10}" '
                f'fill="#e53935" rx="0.01"/>')
        # Fenêtre
        window = (f'<circle cx="0" cy="{l*0.20}" r="{hw*0.40}" fill="#b3e5fc" '
                  f'stroke="#546e7a" stroke-width="0.015"/>')
        # Ogive (courbe)
        nose = (f'<path d="M{-hw},{l/2} Q{-hw},{l/2+0.22} 0,{l/2+0.28} '
                f'Q{hw},{l/2+0.22} {hw},{l/2} Z" fill="#90a4ae"/>')
        # Ailerons
        fin_l = (f'<polygon points="{-hw},{-l/2+0.22} {-hw-0.10},{-l/2} '
                 f'{-hw},{-l/2}" fill="#546e7a"/>')
        fin_r = (f'<polygon points="{hw},{-l/2+0.22} {hw+0.10},{-l/2} '
                 f'{hw},{-l/2}" fill="#546e7a"/>')
        # Tuyère
        nozzle = (f'<rect x="{-hw*1.25}" y="{-l/2-0.04}" width="{2*hw*1.25}" '
                  f'height="0.04" fill="#455a64" rx="0.01"/>')

        svg_body = (f'<g transform="translate({x}, {y}) rotate({td})">'
                    f'{body}{band}{window}{nose}{fin_l}{fin_r}{nozzle}</g>')

        # --- Flamme ---
        svg_flame = ""
        if f > 1e-10:
            fL = (f / (M * g)) * (l / 2.0)  # ℓ/2 quand f=Mg
            bx, by = 0.0, -l / 2.0 - 0.04
            dx, dy = math.sin(phi), -math.cos(phi)   # direction flamme
            px, py = math.cos(phi), math.sin(phi)     # perpendiculaire

            # Couches de flamme: (couleur, opacité, w_base, w_tip, facteur_longueur)
            layers = [
                ("#ff6f00", 0.65, 0.11, 0.035, 1.00),
                ("#ff9800", 0.75, 0.08, 0.025, 0.80),
                ("#ffeb3b", 0.85, 0.045, 0.015, 0.55),
                ("#ffffff", 0.90, 0.020, 0.008, 0.25),
            ]
            polys = ""
            for color, opacity, wb, wt, lf in layers:
                L = fL * lf
                tx, ty = bx + L * dx, by + L * dy
                polys += (
                    f'<polygon points="'
                    f'{bx-wb*px:.4f},{by-wb*py:.4f} '
                    f'{bx+wb*px:.4f},{by+wb*py:.4f} '
                    f'{tx+wt*px:.4f},{ty+wt*py:.4f} '
                    f'{tx-wt*px:.4f},{ty-wt*py:.4f}" '
                    f'fill="{color}" opacity="{opacity}"/>'
                )
            svg_flame = (f'<g transform="translate({x}, {y}) rotate({td})">'
                          f'{polys}</g>')

        return svg_body + svg_flame


    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    # Tests : trois configurations du booster
    mo.hstack(
        [
            # (1) Booster posé au sol, réacteur éteint
            mo.Html(
                world([-3, 3, -2, 4], booster(0, l/2, 0, 0, 0))
            ),
            # (2) Vol stationnaire : f = Mg => flamme de longueur ℓ/2
            mo.Html(
                world([-3, 3, -2, 4], booster(0, l, 0, M * g, 0))
            ),
            # (3) Incliné, forte poussée décalée
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, math):
    def booster_anim(x, y, theta, f, phi, T):
        N = 100  # keyframes pour animation fluide
        dt = T / N
        times = [i * dt for i in range(N + 1)]

        xs     = [x(t)     for t in times]
        ys     = [y(t)     for t in times]
        thetas = [theta(t) for t in times]
        fs     = [f(t)     for t in times]
        phis   = [phi(t)   for t in times]

        tr_vals = ";".join(f"{xs[i]},{ys[i]}" for i in range(N + 1))
        rot_vals = ";".join(f"{math.degrees(thetas[i]):.4f}" for i in range(N + 1))

        hw = 0.09
        # Éléments statiques du corps (dans le groupe animé)
        body_el = (f'<rect x="{-hw}" y="{-l/2}" width="{2*hw}" height="{l}" '
                   f'fill="#78909c" rx="0.04"/>')
        band_el = (f'<rect x="{-hw}" y="{-l*0.05}" width="{2*hw}" height="{l*0.10}" '
                   f'fill="#e53935" rx="0.01"/>')
        win_el  = (f'<circle cx="0" cy="{l*0.20}" r="{hw*0.40}" fill="#b3e5fc" '
                   f'stroke="#546e7a" stroke-width="0.015"/>')
        nose_el = (f'<path d="M{-hw},{l/2} Q{-hw},{l/2+0.22} 0,{l/2+0.28} '
                   f'Q{hw},{l/2+0.22} {hw},{l/2} Z" fill="#90a4ae"/>')
        fin_l_el = (f'<polygon points="{-hw},{-l/2+0.22} {-hw-0.10},{-l/2} '
                    f'{-hw},{-l/2}" fill="#546e7a"/>')
        fin_r_el = (f'<polygon points="{hw},{-l/2+0.22} {hw+0.10},{-l/2} '
                    f'{hw},{-l/2}" fill="#546e7a"/>')
        noz_el = (f'<rect x="{-hw*1.25}" y="{-l/2-0.04}" width="{2*hw*1.25}" '
                  f'height="0.04" fill="#455a64" rx="0.01"/>')

        # Couches de flamme
        flame_layers = [
            ("#ff6f00", 0.65, 0.11, 0.035, 1.00),
            ("#ff9800", 0.75, 0.08, 0.025, 0.80),
            ("#ffeb3b", 0.85, 0.045, 0.015, 0.55),
            ("#ffffff", 0.90, 0.020, 0.008, 0.25),
        ]

        flame_anims = ""
        for color, opacity, wb, wt, lf in flame_layers:
            frames = []
            for i in range(N + 1):
                fv = fs[i]
                pv = phis[i]
                if fv > 1e-10:
                    fL_val = (fv / (M * g)) * (l / 2.0) * lf
                    # léger scintillement pour les couches internes
                    if lf < 0.6:
                        flicker = 1.0 + 0.04 * math.sin(i * 2.3) + 0.03 * math.cos(i * 3.7)
                        fL_val *= flicker
                    fdx = math.sin(pv)
                    fdy = -math.cos(pv)
                    ppx = math.cos(pv)
                    ppy = math.sin(pv)
                    bx, by = 0.0, -l / 2.0 - 0.04
                    tx, ty = bx + fL_val * fdx, by + fL_val * fdy
                    frames.append(
                        f"{bx-wb*ppx:.4f},{by-wb*ppy:.4f} "
                        f"{bx+wb*ppx:.4f},{by+wb*ppy:.4f} "
                        f"{tx+wt*ppx:.4f},{ty+wt*ppy:.4f} "
                        f"{tx-wt*ppx:.4f},{ty-wt*ppy:.4f}"
                    )
                else:
                    p = f"0,{-l/2-0.04:.4f}"
                    frames.append(f"{p} {p} {p} {p}")
            vals = ";".join(frames)
            flame_anims += (
                f'<polygon fill="{color}" opacity="{opacity}">'
                f'<animate attributeName="points" values="{vals}" '
                f'dur="{T}s" repeatCount="indefinite"/></polygon>'
            )

        return (
            f'<g>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="{tr_vals}" dur="{T}s" repeatCount="indefinite"/>'
            f'<animateTransform attributeName="transform" type="rotate" '
            f'values="{rot_vals}" dur="{T}s" repeatCount="indefinite" '
            f'additive="sum"/>'
            f'{body_el}{band_el}{win_el}{nose_el}{fin_l_el}{fin_r_el}{noz_el}'
            f'{flame_anims}'
            f'</g>'
        )


    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, mo, world):
    # Test de booster_anim
    def booster_anim_0():
        x = lambda t: 0.0
        y = lambda t: 2.0
        theta = lambda t: 0.0
        f = lambda t: M * g
        phi = lambda t: 0.0
        T = 3.0
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    T1 = 4.5
    sol1 = redstart_solve([0.0, T1], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], lambda t, y: np.array([0.0, 0.0]))
    anim1 = booster_anim(lambda t: float(sol1(t)[0]), lambda t: float(sol1(t)[2]),
                         lambda t: float(sol1(t)[4]), lambda t: 0.0, lambda t: 0.0, T=T1)

    # ── 2. Vol stationnaire ──
    T2 = 5.0
    sol2 = redstart_solve([0.0, T2], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], lambda t, y: np.array([M*g, 0.0]))
    anim2 = booster_anim(lambda t: float(sol2(t)[0]), lambda t: float(sol2(t)[2]),
                         lambda t: float(sol2(t)[4]), lambda t: M*g, lambda t: 0.0, T=T2)

    # ── 3. Poussée décalée ──
    T3 = 5.0
    phi3 = np.pi / 8.0
    sol3 = redstart_solve([0.0, T3], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], lambda t, y: np.array([M*g, phi3]))
    anim3 = booster_anim(lambda t: float(sol3(t)[0]), lambda t: float(sol3(t)[2]),
                         lambda t: float(sol3(t)[4]), lambda t: M*g, lambda t: phi3, T=T3)

    # ── 4. Atterrissage contrôlé ──
    a_c, b_c = 8.0/125.0, -7.0/25.0
    T4 = 5.0
    def f_phi_land(t, y):
        return np.array([M * (6.0*a_c*t + 2.0*b_c + g), 0.0])

    sol4 = redstart_solve([0.0, T4], [0.0, 0.0, 10.0, -2.0, 0.0, 0.0], f_phi_land)
    anim4 = booster_anim(lambda t: float(sol1(t)[0]), lambda t: float(sol4(t)[2]),
                         lambda t: float(sol4(t)[4]), lambda t: M*(6.0*a_c*t + 2.0*b_c + g),
                         lambda t: 0.0, T=T4)

    # ── Rendu final ──
    mo.vstack([
        mo.md("#  Redstart : Simulations Style SpaceX"),
        mo.md("✅ Rotation centrée au CM • ✅ Flamme alignée sur `θ+φ` • ✅ Jambes déployées à `y<2.5m` • ✅ Échappement multi-couches + expansion altitude"),
        mo.hstack([
            mo.vstack([mo.md("### 🌌 1. Chute Libre"), mo.md("Aucune poussée. Chute verticale pure (θ=0)."), mo.Html(world([-3, 3, -2, 12], anim1))], gap=0.4),
            mo.vstack([mo.md("### 🚁 2. Vol Stationnaire"), mo.md("`f=Mg`, `φ=0`. Compensation exacte du poids."), mo.Html(world([-3, 3, -2, 12], anim2))], gap=0.4)
        ], justify="space-around", align="start"),
        mo.hstack([
            mo.vstack([mo.md("### 📐 3. Poussée Décalée"), mo.md("`φ=π/8`. Couple → rotation + dérive."), mo.Html(world([-5, 5, -2, 12], anim3))], gap=0.4),
            mo.vstack([mo.md("### 🎯 4. Atterrissage Contrôlé"), mo.md("Loi polynomiale. Arrivée douce sur ASDS."), mo.Html(world([-3, 3, -2, 12], anim4))], gap=0.4)
        ], justify="space-around", align="start")
    ], gap=1.2)
    return


if __name__ == "__main__":
    app.run()
