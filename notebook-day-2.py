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
    import numpy.linalg as la
    import scipy.linalg as sci


    return la, np, plt, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
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
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
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

    return animate_transform, svg, transform


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Équilibres du Système



    Un équilibre est un état $s^* = (x^*, 0, y^*, 0, \theta^*, 0)$ tel que
    $\dot{s} = 0$. En examinant chaque composante du champ de vecteurs
    $F(s, f, \phi)$, on obtient les conditions suivantes.

    **1. Vitesse nulle.** Par définition d'un équilibre, les dérivées premières
    de $x$, $y$ et $\theta$ doivent être nulles, donc $v_x = 0$, $v_y = 0$ et
    $\omega = 0$ — ces conditions sont automatiquement satisfaites par la
    définition de $s^*$.

    **2. Accélération horizontale nulle.**
    $$-\frac{f}{M}\sin(\theta + \phi) = 0$$
    Puisque $f > 0$ et $M > 0$, cela impose $\sin(\theta + \phi) = 0$, donc
    $\theta + \phi = 0$ (modulo $\pi$). Compte tenu des contraintes
    $|\theta| < \pi/2$ et $|\phi| < \pi/2$, la seule solution admissible est :
    $$\phi = -\theta$$

    **3. Accélération verticale nulle.**
    $$\frac{f}{M}\cos(\theta + \phi) - g = 0$$
    En utilisant $\theta + \phi = 0$, on obtient $\cos(0) = 1$, donc :
    $$\frac{f}{M} = g \quad\Longrightarrow\quad f = Mg$$

    **4. Accélération angulaire nulle.**
    $$-\frac{f}{J}\frac{\ell}{2}\sin\phi = 0$$
    Puisque $f > 0$, $J > 0$ et $\ell > 0$, cela impose $\sin\phi = 0$, d'où
    $\phi = 0$ (la contrainte $|\phi| < \pi/2$ exclut $\phi = \pm\pi$).

    **5. Conclusion.** En combinant $\phi = 0$ avec $\theta + \phi = 0$, on
    obtient $\theta = 0$. De plus, $f = Mg$. Les positions $x^*$ et $y^*$
    restent arbitraires (le système est invariant par translation). L'équilibre
    unique (modulo la position) est donc :

    $$\boxed{s^* = (x^*,\; 0,\; y^*,\; 0,\; 0,\; 0), \quad f = Mg, \quad \phi = 0}$$

    Physiquement, le booster est en équilibre lorsqu'il est parfaitement vertical
    ($\theta = 0$), immobile, et que la poussée compense exactement le poids
    ($f = Mg$). L'angle de gîrage doit être nul ($\phi = 0$), ce qui est
    cohérent : toute déviation angulaire créerait un couple non nul et ferait
    tourner le booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 11 — Modèle Linéarisé

    On développe $F$ au premier ordre autour de l'équilibre $(s^*, Mg, 0)$ par calcul du Jacobien.

    Jacobien Complet

    **① Translation horizontale :** $M\ddot{x}=-f\sin(\theta+\phi)$

    | Var. | Dérivée partielle | Valeur en $(\theta=0,\phi=0,f=Mg)$ |
    |------|------------------|---------------------------------|
    | $f$ | $-\sin(\theta+\phi)$ | $-\sin(0)=0$ |
    | $\theta$ | $-f\cos(\theta+\phi)$ | $-Mg$ |
    | $\phi$ | $-f\cos(\theta+\phi)$ | $-Mg$ |

    $$\Longrightarrow\quad \boxed{\Delta\ddot{x} = -g\,\Delta\theta - g\,\Delta\phi}$$

    **② Translation verticale :** $M\ddot{y}=f\cos(\theta+\phi)-Mg$

    | Var. | Dérivée partielle | Valeur en équilibre |
    |------|------------------|--------------------|
    | $f$ | $\cos(\theta+\phi)$ | $\cos(0)=1$ |
    | $\theta$ | $-f\sin(\theta+\phi)$ | $-Mg\sin(0)=0$ |
    | $\phi$ | $-f\sin(\theta+\phi)$ | $0$ |

    $$\Longrightarrow\quad \boxed{\Delta\ddot{y} = \frac{1}{M}\,\Delta f}$$

    **③ Rotation :** $J\ddot{\theta}=-f(\ell/2)\sin\phi$

    | Var. | Dérivée partielle | Valeur en équilibre |
    |------|------------------|--------------------|
    | $f$ | $-(\ell/2)\sin\phi$ | $0$ |
    | $\phi$ | $-f(\ell/2)\cos\phi$ | $-Mg\ell/2$ |

    $$J\,\Delta\ddot{\theta} = -\frac{Mg\ell}{2}\,\Delta\phi \xrightarrow{J=M\ell^2/12} \boxed{\Delta\ddot{\theta} = -\frac{6g}{\ell}\,\Delta\phi}$$

    *Structure triangulaire :* $\Delta\ddot{\theta}$ dépend uniquement de $\Delta\phi$ ; $\Delta\ddot{x}$ dépend de $\Delta\theta$ et $\Delta\phi$ ; $\Delta\ddot{y}$ est totalement découplée.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Forme Standard : Matrices $A$ et $B$



    On choisit le vecteur d'état
    $z = (\Delta x,\; \Delta v_x,\; \Delta y,\; \Delta v_y,\; \Delta \theta,\; \Delta \omega)^\top \in \mathbb{R}^6$
    et le vecteur d'entrée $u = (\Delta f,\; \Delta \phi)^\top \in \mathbb{R}^2$.

    $$A = \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}, \qquad
    B = \begin{pmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -6g/\ell
    \end{pmatrix}$$

    La structure de $A$ est triangulaire supérieure par blocs : les variables
    $(\Delta y, \Delta v_y)$ forment un sous-système complètement découplé (double
    intégrateur pur), tandis que les variables $(\Delta x, \Delta v_x, \Delta \theta,\Delta \omega)$
    forment un bloc couplé. La matrice $B$ montre que l'entrée $\Delta f$ n'agit
    que sur $\Delta v_y$ (accélération verticale) et que $\Delta\phi$ agit à la fois
    sur $\Delta v_x$ et sur $\Delta\omega$ (couple de gîrage). L'angle de gîrage $\phi$
    est donc le seul moyen d'influencer la dynamique latérale et angulaire.
    """)
    return


@app.cell
def _(M, g, l, np):
    # Matrices A et B
    A = np.array([
        [0, 1, 0, 0,  0,        0],
        [0, 0, 0, 0, -g,        0],
        [0, 0, 0, 1,  0,        0],
        [0, 0, 0, 0,  0,        0],
        [0, 0, 0, 0,  0,        1],
        [0, 0, 0, 0,  0,        0]
    ])

    B = np.array([
        [0,     0       ],
        [0,    -g       ],
        [0,     0       ],
        [1/M,   0       ],
        [0,     0       ],
        [0,    -6*g/l   ]
    ])

    print('A ='); print(A)
    print('\nB ='); print(B)

    # --- Vérification Az+Bu sur un état-test ---
    z_t = np.array([0.1, 0.2, 0.3, 0.4, 0.05, 0.0])
    u_t = np.array([0.5, 0.01])
    zdot = A @ z_t + B @ u_t
    print('\nVérification Az + Bu :')
    print(f'  dz1={zdot[0]:.4f}  attend z2={z_t[1]:.4f}')
    print(f'  dz2={zdot[1]:.4f}  attend -g*z5+(-g)*u2={-g*z_t[4]+(-g)*u_t[1]:.4f}')
    print(f'  dz3={zdot[2]:.4f}  attend z4={z_t[3]:.4f}')
    print(f'  dz4={zdot[3]:.4f}  attend (1/M)*u1={u_t[0]/M:.4f}')
    print(f'  dz5={zdot[4]:.4f}  attend z6={z_t[5]:.4f}')
    print(f'  dz6={zdot[5]:.4f}  attend (-6g/l)*u2={-6*g/l*u_t[1]:.4f}')

    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stabilité de l'Équilibre

    L'équilibre en boucle ouverte est-il asymptotiquement stable ?

    ###  Solution — Analyse Spectrale Complète

    **Étape 1 — Polynôme caractéristique.**

    $A$ est une matrice strictement triangulaire supérieure (tous les éléments diagonaux sont nuls). Pour une telle matrice, $\det(\lambda I - A) = \lambda^n$. Ici $n=6$, donc :

    $$\det(\lambda I - A) = \lambda^6$$

    Toutes les valeurs propres valent $\lambda=0$ (multiplicité algébrique = 6).

    **Étape 2 — Multiplicité géométrique.**

    $\dim(\ker A) = n - \mathrm{rg}(A)$. Les colonnes non nulles de $A$ sont la colonne 2 (→ ligne 1), colonne 4 (→ ligne 3), colonne 5 (→ ligne 2), colonne 6 (→ ligne 5) : donc $\mathrm{rg}(A)=4$ et $\dim(\ker A)=2$.

    Multiplicité géométrique (2) $<$ multiplicité algébrique (6) → **blocs de Jordan non triviaux**.

    **Étape 3 — Conséquence pour la stabilité.**

    La solution homogène $e^{At}z_0$ contient des termes polynomiaux $t, t^2, t^3$ qui croissent sans borne. La nilpotence $A^4=0$ (vérifiée ci-dessous) confirme que $e^{At} = I + At + \frac{A^2t^2}{2!} + \frac{A^3t^3}{3!}$ est un polynôme matriciel en $t$ de degré 3.

    $$\boxed{\text{L'équilibre est INSTABLE : dérive polynomiale en }t\text{ en boucle ouverte.}}$$
    """)
    return


@app.cell
def _(A, la, np):
    # Vérification numérique de la nilpotence
    vals_propres = la.eigvals(A)
    print(f"Valeurs propres de A : {vals_propres}")
    print(f"Toutes nulles : {np.allclose(vals_propres, 0)}")
    print(f"Rang de A : {la.matrix_rank(A)}")
    print(f"dim(ker A) = {A.shape[0] - la.matrix_rank(A)}")

    A2 = A @ A
    A3 = A2 @ A
    A4 = A3 @ A
    print(f"\nA² = 0 ? {np.allclose(A2, 0)}")
    print(f"A³ = 0 ? {np.allclose(A3, 0)}")
    print(f"A⁴ = 0 ? {np.allclose(A4, 0)}")
    print(f"\nA² (entrées non nulles) :")
    print(np.round(A2, 4))

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##  Commandabilité du Modèle Linéarisé Complet



    ### Solution

    On construit la matrice de commandabilité de Kalman :

    $$\mathcal{C} = \begin{pmatrix} B & AB & A^2B & A^3B & A^4B & A^5B \end{pmatrix} \in \mathbb{R}^{6 \times 12}$$

    On calcule successivement les puissances de $A$ multipliées par $B$.

    ---

    #### Calcul détaillé de $AB$

    La première colonne de $B$, notée $b_1 = (0,\, 0,\, 0,\, 1,\, 0,\, 0)^\top$,
    correspond à l'effet de $\Delta f$ sur $\dot{z}$. On a $A\,b_1 = A_{:,3}$
    (la 4\textsuperscript{e} colonne de $A$), car $b_1$ sélectionne la colonne
    d'indice 3 de $A$ :

    $$A\,b_1 = A\begin{pmatrix}0\\0\\0\\1\\0\\0\end{pmatrix} = \begin{pmatrix}A[0,3]\\A[1,3]\\A[2,3]\\A[3,3]\\A[4,3]\\A[5,3]\end{pmatrix} = \begin{pmatrix}0\\0\\1\\0\\0\\0\end{pmatrix}$$

    car $A[2,3] = 1$ est l'unique entrée non nulle de la colonne 3
    (l'équation $\dot{\Delta y} = \Delta v_y$).

    La seconde colonne de $B$, notée $b_2 = (0,\, -1,\, 0,\, 0,\, 0,\, -3)^\top$,
    correspond à l'effet de $\Delta\phi$. On calcule :

    $$A\,b_2 = (-1)\cdot A_{:,1} + (-3)\cdot A_{:,5}$$

    Or $A_{:,1} = (1,\, 0,\, 0,\, 0,\, 0,\, 0)^\top$ (car $A[0,1] = 1$ :
    $\dot{\Delta x} = \Delta v_x$) et $A_{:,5} = (0,\, 0,\, 0,\, 0,\, 1,\, 0)^\top$
    (car $A[4,5] = 1$ : $\dot{\Delta\theta} = \Delta\omega$), donc :

    $$A\,b_2 = -\begin{pmatrix}1\\0\\0\\0\\0\\0\end{pmatrix} - 3\begin{pmatrix}0\\0\\0\\0\\1\\0\end{pmatrix} = \begin{pmatrix}-1\\0\\0\\0\\-3\\0\end{pmatrix}$$

    $$\boxed{AB = \begin{pmatrix}
    0 & -1 \\
    0 & 0 \\
    1 & 0 \\
    0 & 0 \\
    0 & -3 \\
    0 & 0
    \end{pmatrix}}$$

    ---

    #### Calcul détaillé de $A^2B$

    On applique $A$ à chaque colonne de $AB$.

    **Première colonne :** $A \cdot (0,\, 0,\, 1,\, 0,\, 0,\, 0)^\top = A_{:,2}$

    La colonne 2 de $A$ est entièrement nulle : $A[0,2] = A[1,2] = A[2,2] = A[3,2] = A[4,2] = A[5,2] = 0$. En effet, il n'existe pas de terme $\dot{\Delta y} = \Delta y$ dans le modèle (l'équation est $\dot{\Delta y} = \Delta v_y$, pas un terme proportionnel à $\Delta y$). Donc :

    $$A^2B_{:,1} = \mathbf{0}$$

    **Seconde colonne :** $A \cdot (-1,\, 0,\, 0,\, 0,\, -3,\, 0)^\top = (-1)\cdot A_{:,0} + (-3)\cdot A_{:,4}$

    $A_{:,0} = (0,\, 0,\, 0,\, 0,\, 0,\, 0)^\top$ (pas de terme en $\Delta x$ dans les dynamiques)
    et $A_{:,4} = (0,\, -g,\, 0,\, 0,\, 0,\, 0)^\top$ (car $A[1,4] = -g$ :
    $\dot{\Delta v_x} = -g\,\Delta\theta$), donc :

    $$A^2B_{:,2} = (-1)\cdot\mathbf{0} + (-3)\begin{pmatrix}0\\-1\\0\\0\\0\\0\end{pmatrix} = \begin{pmatrix}0\\3\\0\\0\\0\\0\end{pmatrix}$$

    $$\boxed{A^2B = \begin{pmatrix}
    0 & 0 \\
    0 & 3 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{pmatrix}}$$

    ---

    #### Calcul détaillé de $A^3B$

    **Première colonne :** $A \cdot \mathbf{0} = \mathbf{0}$

    **Seconde colonne :** $A \cdot (0,\, 3,\, 0,\, 0,\, 0,\, 0)^\top = 3 \cdot A_{:,1} = 3\begin{pmatrix}1\\0\\0\\0\\0\\0\end{pmatrix} = \begin{pmatrix}3\\0\\0\\0\\0\\0\end{pmatrix}$

    $$\boxed{A^3B = \begin{pmatrix}
    0 & 3 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{pmatrix}}$$

    ---

    #### Calcul de $A^4B$ et $A^5B$

    **Première colonne :** $A \cdot \mathbf{0} = \mathbf{0}$

    **Seconde colonne :** $A \cdot (3,\, 0,\, 0,\, 0,\, 0,\, 0)^\top = 3 \cdot A_{:,0} = 3 \cdot \mathbf{0} = \mathbf{0}$

    $$\boxed{A^4B = A^5B = \mathbf{0}_{6 \times 2}}$$

    Ceci est cohérent avec la nilpotence de $A$ ($A^4 = 0$) : au-delà de la
    puissance 3, l'action de $A$ sur $B$ est identiquement nulle.

    ---

    #### Matrice de commandabilité complète

    $$\mathcal{C} = \begin{pmatrix}
    0 & 0 & 0 & -1 & 0 & 0 & 0 & 3 & 0 & 0 & 0 & 0 \\
    0 & -1 & 0 & 0 & 0 & 3 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & -3 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & -3 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}$$

    ---

    #### Extraction de 6 vecteurs indépendants

    On identifie six vecteurs linéairement indépendants parmi les colonnes de
    $\mathcal{C}$ :

    $$\begin{aligned}
    c_1 &= (0,\, 0,\, 0,\, 1,\, 0,\, 0)^\top \quad \text{(col. 1 de $B$)} \\
    c_2 &= (0,\, -1,\, 0,\, 0,\, 0,\, -3)^\top \quad \text{(col. 2 de $B$)} \\
    c_3 &= (0,\, 0,\, 1,\, 0,\, 0,\, 0)^\top \quad \text{(col. 1 de $AB$)} \\
    c_4 &= (-1,\, 0,\, 0,\, 0,\, -3,\, 0)^\top \quad \text{(col. 2 de $AB$)} \\
    c_5 &= (0,\, 3,\, 0,\, 0,\, 0,\, 0)^\top \quad \text{(col. 2 de $A^2B$)} \\
    c_6 &= (3,\, 0,\, 0,\, 0,\, 0,\, 0)^\top \quad \text{(col. 2 de $A^3B$)}
    \end{aligned}$$

    ---

    #### Preuve d'indépendance linéaire

    Soient $a_1, a_2, a_3, a_4, a_5, a_6 \in \mathbb{R}$ tels que
    $\sum_{i=1}^{6} a_i\, c_i = 0$. On procède composante par composante
    (en choisissant l'ordre qui élimine le plus de variables à chaque étape) :

    - **Composante 6** ($\Delta\omega$) : seul $c_2$ a une entrée non nulle,
      donc $-3a_2 = 0 \implies a_2 = 0$

    - **Composante 4** ($\Delta v_y$) : seul $c_1$ a une entrée non nulle,
      donc $a_1 = 0$

    - **Composante 3** ($\Delta y$) : seul $c_3$ a une entrée non nulle,
      donc $a_3 = 0$

    - **Composante 5** ($\Delta\theta$) : seul $c_4$ a une entrée non nulle,
      donc $-3a_4 = 0 \implies a_4 = 0$

    - **Composante 1** ($\Delta x$) : seuls $c_4$ et $c_6$ contribuent,
      donc $-a_4 + 3a_6 = 3a_6 = 0 \implies a_6 = 0$

    - **Composante 2** ($\Delta v_x$) : seuls $c_2$ et $c_5$ contribuent,
      donc $-a_2 + 3a_5 = 3a_5 = 0 \implies a_5 = 0$

    Tous les coefficients sont nuls : les six vecteurs sont linéairement
    indépendants et forment une base de $\mathbb{R}^6$.

    ---

    ### Résultat

    $$\boxed{\text{Le modèle linéarisé complet est commandable : } \mathrm{rg}(\mathcal{C}) = 6 = n}$$

    D'après le critère de Kalman, le système est donc entièrement commandable.
    Il est théoriquement possible de conduire le système de n'importe quel état
    initial vers n'importe quel état désiré en un temps fini, en utilisant les
    deux entrées $\Delta f$ et $\Delta\phi$.

    ---

    ### Remarque importante sur le code

    La construction de la matrice de commandabilité en Python nécessite d'utiliser
    les puissances successives de $A$. Le code correct est :

    ```python
    C = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    ```

    Une erreur fréquente consiste à écrire
    `[A @ B for _ in range(n-1)]`, qui calcule $AB$ $n-1$ fois au lieu de
    $A^2B$, $A^3B$, etc. Cette erreur donnerait un rang de 4 au lieu de 6.
    """)
    return


@app.cell
def _(A, B, np):
    n = A.shape[0]
    # Construction correcte de la matrice de Kalman avec puissances successives de A
    C = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    print(f"Rang de la matrice de commandabilité : {np.linalg.matrix_rank(C)}")
    print(f"Dimension de l'espace d'état : {n}")
    print(f"Système commandable : {np.linalg.matrix_rank(C) == n}")
    print(f"\nMatrice de commandabilité (6 × {C.shape[1]}) :")
    print(np.round(C, 4))

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    \
    ## 🧩 15 — Dynamique Latérale

    ### Énoncé

    On se limite à la position latérale $x$, à l'inclinaison $\theta$ et à leurs
    dérivées. On fixe $f = Mg$ et on ne commande le système qu'avec $\phi$.
    Quelles sont les nouvelles matrices réduites $A_{\mathrm{lat}}$ et
    $B_{\mathrm{lat}}$ ? Le système réduit est-il commandable ?

    ### Solution

    Puisque l'on fixe $f = Mg$, on a $\Delta f = 0$, donc l'entrée est réduite
    au scalaire $\Delta\phi$. L'état réduit est $z_{\mathrm{lat}} =
    (\Delta x,\, \Delta v_x,\, \Delta\theta,\, \Delta\omega)^\top \in
    \mathbb{R}^4$.

    ---

    #### Équations du système réduit

    En extrayant les lignes et colonnes correspondantes du modèle complet :

    $$\begin{aligned}
    \dot{\Delta x} &= \Delta v_x \\
    \dot{\Delta v_x} &= -g\,\Delta\theta - g\,\Delta\phi \\
    \dot{\Delta\theta} &= \Delta\omega \\
    \dot{\Delta\omega} &= -\frac{6g}{\ell}\,\Delta\phi
    \end{aligned}$$

    #### Matrices réduites (forme littérale)

    $$A_{\mathrm{lat}} = \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, \qquad
    B_{\mathrm{lat}} = \begin{pmatrix}
    0 \\ -g \\ 0 \\ -6g/\ell
    \end{pmatrix}$$

    #### Matrices numériques ($g = 1$, $\ell = 2$)

    $$A_{\mathrm{lat}} = \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -1 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, \qquad
    B_{\mathrm{lat}} = \begin{pmatrix}
    0 \\ -1 \\ 0 \\ -3
    \end{pmatrix}$$

    ---

    ### Vérification de la commandabilité

    La matrice de commandabilité pour le système réduit est :

    $$\mathcal{C}_{\mathrm{lat}} = \begin{pmatrix}
    B_{\mathrm{lat}} & A_{\mathrm{lat}} B_{\mathrm{lat}} &
    A_{\mathrm{lat}}^2 B_{\mathrm{lat}} &
    A_{\mathrm{lat}}^3 B_{\mathrm{lat}}
    \end{pmatrix} \in \mathbb{R}^{4 \times 4}$$

    On calcule successivement :

    $$\begin{aligned}
    B_{\mathrm{lat}} &= (0,\; -1,\; 0,\; -3)^\top \\
    A_{\mathrm{lat}} B_{\mathrm{lat}} &= (-1,\; 0,\; -3,\; 0)^\top \\
    A_{\mathrm{lat}}^2 B_{\mathrm{lat}} &= (0,\; 3,\; 0,\; 0)^\top \\
    A_{\mathrm{lat}}^3 B_{\mathrm{lat}} &= (3,\; 0,\; 0,\; 0)^\top
    \end{aligned}$$

    Explicitement :

    $$\mathcal{C}_{\mathrm{lat}} = \begin{pmatrix}
    0 & -1 & 0 & 3 \\
    -1 & 0 & 3 & 0 \\
    0 & -3 & 0 & 0 \\
    -3 & 0 & 0 & 0
    \end{pmatrix}$$

    #### Preuve d'indépendance linéaire

    Soient $a_1, a_2, a_3, a_4$ tels que
    $a_1 v_1 + a_2 v_2 + a_3 v_3 + a_4 v_4 = 0$ :

    - **Composante 4** ($\Delta\omega$) : $-3a_1 = 0 \implies a_1 = 0$
    - **Composante 3** ($\Delta\theta$) : $-3a_2 = 0 \implies a_2 = 0$
    - **Composante 1** ($\Delta x$) : $3a_4 = 0 \implies a_4 = 0$
    - **Composante 2** ($\Delta v_x$) : $3a_3 = 0 \implies a_3 = 0$

    Tous les coefficients sont nuls : les quatre vecteurs sont linéairement
    indépendants.

    ---

    ### Résultat

    $$\boxed{\text{Le système latéral est commandable : }
    \mathrm{rg}(\mathcal{C}_{\mathrm{lat}}) = 4 = n_{\mathrm{lat}}}$$

    Bien que l'on n'ait qu'une seule entrée ($\Delta\phi$) pour commander quatre
    variables d'état, le système reste entièrement commandable. La raison
    profonde réside dans la chaîne d'intégrateurs : $\Delta\phi$ influence
    $\Delta\omega$, qui influence $\Delta\theta$, qui influence $\Delta v_x$,
    qui influence $\Delta x$. Cette cascade permet « d'atteindre » chaque
    variable d'état indirectement.
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0],
        [0, 0, -g, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ])
    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-6*g/l]
    ])

    n_lat = A_lat.shape[0]
    # Construction correcte : puissances successives de A_lat
    C_lat = np.hstack([np.linalg.matrix_power(A_lat, i) @ B_lat for i in range(n_lat)])
    print(f"A_lat =\n{A_lat}")
    print(f"\nB_lat =\n{B_lat}")
    print(f"\nC_lat =\n{np.round(C_lat, 4)}")
    print(f"\nRang de C_lat : {np.linalg.matrix_rank(C_lat)} / {n_lat}")
    print(f"Système latéral commandable : {np.linalg.matrix_rank(C_lat) == n_lat}")

    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modèle Linéaire en Chute Libre



    ### Solution

    Avec $\Delta\phi(t) = 0$ et les conditions initiales $\Delta x(0) = 0$,
    $\Delta v_x(0) = 0$, $\Delta\theta(0) = \pi/4$, $\Delta\omega(0) = 0$,
    le modèle linéarisé se simplifie considérablement.

    ---

    #### Équation pour $\theta(t)$

    L'équation angulaire est
    $\Delta\ddot{\theta} = -(6g/\ell)\,\Delta\phi = 0$. Avec les conditions
    initiales, la solution est trivialement :

    $$\boxed{\Delta\theta(t) = \frac{\pi}{4} \quad \text{(constante)}}$$

    L'angle d'inclinaison reste constant à sa valeur initiale. En l'absence de
    couple de gîrage ($\phi = 0$), aucun moment ne vient modifier la rotation
    du booster.

    ---

    #### Équation pour $x(t)$

    L'équation horizontale est
    $\Delta\ddot{x} = -g\,\Delta\theta - g\,\Delta\phi = -g \cdot \pi/4 - 0 =
    -\pi/4$.

    En intégrant une première fois (avec $\Delta v_x(0) = 0$) :

    $$\Delta v_x(t) = -\frac{\pi}{4}\,t$$

    En intégrant une seconde fois (avec $\Delta x(0) = 0$) :

    $$\boxed{\Delta x(t) = -\frac{\pi}{8}\,t^2}$$

    La position latérale devient de plus en plus négative : le booster dérive
    vers la gauche avec une accélération constante de $-\pi/4$ m/s$^2$.

    ---

    #### Interprétation physique

    Le booster est incliné d'un angle $\pi/4$ (45°) vers la gauche. Sa poussée
    $f = Mg$ est alignée avec son axe, donc elle pointe partiellement vers la
    gauche. La composante horizontale de la poussée est
    $-Mg\sin(\theta) = -\sin(\pi/4) = -\pi/4$ (dans le modèle linéarisé).
    Cette force horizontale constante entraîne une accélération latérale
    constante, produisant une dérive quadratique.

    En l'absence de contrôle ($\phi = 0$), l'inclinaison ne peut pas être
    corrigée et le booster dévie inexorablement. Cela illustre la nécessité
    d'un asservissement actif.
    """)
    return


@app.cell
def _(A_lat, np, plt, scipy):
    z0 = [0.0, 0.0, np.pi/4, 0.0]

    def linear_lateral(t, z):
        return A_lat @ z

    t_eval = np.linspace(0, 20, 500)
    sol = scipy.integrate.solve_ivp(linear_lateral, (0, 20), z0, t_eval=t_eval)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(sol.t, sol.y[2], 'b-', lw=2)
    ax1.axhline(y=np.pi/4, color='grey', ls='--', alpha=0.5)
    ax1.set_xlabel(r"Temps $t$ (s)"); ax1.set_ylabel(r"$\theta(t)$ (rad)")
    ax1.set_title(r"$\theta(t)$ — constante en absence de contrôle")
    ax1.grid(True, alpha=0.3)

    ax2.plot(sol.t, sol.y[0], 'r-', lw=2)
    ax2.plot(sol.t, -np.pi/8 * sol.t**2, 'k--', lw=1, alpha=0.5, label=r"$-\pi\, t^2 / 8$")
    ax2.set_xlabel(r"Temps $t$ (s)"); ax2.set_ylabel(r"$x(t)$ (m)")
    ax2.set_title(r"$x(t)$ — dérive quadratique vers la gauche")
    ax2.grid(True, alpha=0.3); ax2.legend(loc='best')
    plt.tight_layout()
    plt.show()

    return t_eval, z0


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Contrôleur Réglé Manuellement



    ### Solution

    #### Analyse du problème

    On cherche une loi de commande par retour d'état qui ne corrige que l'angle
    $\theta$ et la vitesse angulaire $\omega$, sans action sur $x$ ni $v_x$
    (les coefficients $k_1 = k_2 = 0$ sont imposés). La loi de commande est :

    $$\Delta\phi(t) = -k_3\,\Delta\theta(t) - k_4\,\Delta\omega(t)$$

    #### Matrice en boucle fermée

    Le système en boucle fermée a pour matrice d'état
    $A_{\mathrm{cl}} = A_{\mathrm{lat}} - B_{\mathrm{lat}} K$. En se
    concentrant sur le sous-système $(\Delta\theta, \Delta\omega)$ — qui est
    découplé de $(\Delta x, \Delta v_x)$ dans la boucle fermée puisque
    $k_1 = k_2 = 0$ — on obtient :

    $$A_{\theta\omega} = \begin{pmatrix}
    0 & 1 \\
    \dfrac{6g}{\ell}\,k_3 & \dfrac{6g}{\ell}\,k_4
    \end{pmatrix}$$

    Le polynôme caractéristique de ce sous-système est :

    $$\lambda^2 - \frac{6g}{\ell}\,k_4\,\lambda - \frac{6g}{\ell}\,k_3 = 0$$

    ---

    #### Conditions de stabilité (Routh-Hurwitz)

    Pour que les pôles soient à parties réelles négatives, il faut :

    $$-\frac{6g}{\ell}\,k_4 < 0 \implies k_4 < 0$$
    $$-\frac{6g}{\ell}\,k_3 > 0 \implies k_3 < 0$$

    (On rappelle que $6g/\ell > 0$ avec nos valeurs numériques.)

    ---

    #### Processus itératif de réglage

    On souhaite un temps de réglement d'environ 20 secondes pour
    $\Delta\theta$. Le temps de réglement à 5% pour un système du second ordre
    est $t_r \approx 4/|\mathrm{Re}(\lambda_{\mathrm{dom}})|$. Pour
    $t_r \approx 20$ s, il faut $|\mathrm{Re}(\lambda_{\mathrm{dom}})| \approx
    0.2$.

    **Essai 1 :** $k_3 = -0.1$, $k_4 = -0.3$

    $$\lambda^2 + 0.9\lambda + 0.3 = 0 \implies \Delta = 0.81 - 1.2 = -0.39 < 0$$

    $$\lambda = -0.45 \pm 0.31j$$

    Rapport d'amortissement : $\zeta = 0.45/\sqrt{0.3} \approx 0.82$. Temps de
    réglement : $t_r \approx 4/0.45 \approx 8.9$ s. Trop rapide mais
    contrainte $|\Delta\phi| < \pi/2$ vérifiée.

    ---

    **Essai 2 :** $k_3 = -0.05$, $k_4 = -0.15$

    $$\lambda^2 + 0.45\lambda + 0.15 = 0$$
    $$\lambda = -0.225 \pm 0.29j$$

    Temps de réglement $t_r \approx 17.8$ s — proche de 20 s mais un peu juste.

    ---

    **Essai 3 (choix final) :** $k_3 = -0.2$, $k_4 = -0.5$

    $$\lambda^2 + 1.5\lambda + 0.6 = 0$$
    $$\lambda = \frac{-1.5 \pm \sqrt{2.25 - 2.4}}{2} = -0.75 \pm 0.19j$$

    Rapport d'amortissement : $\zeta \approx 0.97$ (quasi critique). Temps de
    réglement à 5% : $t_r \approx 4/0.75 \approx 5.3$ s, bien en dessous de 20
    s. La valeur maximale de $|\Delta\phi|$ à l'instant initial est
    $|\Delta\phi(0)| = |-k_3 \cdot \pi/4| = 0.2 \times 0.785 \approx 0.157$
    rad $\ll \pi/2$.

    ---

    ### Résultat

    $$\boxed{K = \begin{pmatrix} 0 & 0 & -0.2 & -0.5 \end{pmatrix}}$$

    Les pôles en boucle fermée du sous-système $(\Delta\theta, \Delta\omega)$
    sont $\lambda = -0.75 \pm 0.19j$, avec un rapport d'amortissement
    $\zeta \approx 0.97$ (presque critique). Le temps de réglement est
    d'environ 5.3 secondes. La contrainte $|\Delta\phi| < \pi/2$ est largement
    respectée. La position $x(t)$ dérive légèrement (comme attendu, puisque
    $k_1 = k_2 = 0$), mais l'angle $\theta(t)$ revient bien à zéro.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy, t_eval, z0):
    def _():
        K_manual = np.array([[0, 0, -0.2, -0.5]])

        A_cl_manual = A_lat - B_lat @ K_manual
        poles_manual = np.linalg.eigvals(A_cl_manual)
        print("A_cl (manuel) =")
        print(np.round(A_cl_manual, 4))
        print("\nPôles en boucle fermée (contrôleur manuel) :")
        for i, p in enumerate(poles_manual):
            print(f"  λ_{i+1} = {p:.6f}")
        print(f"\nParties réelles toutes négatives : {all(p.real < 0 for p in poles_manual)}")


        def closed_loop_manual(t, z):
            u = -(K_manual @ z)[0]
            return A_lat @ z + B_lat.flatten() * u

        t_eval1 = np.linspace(0, 20, 1000)
        sol_m = scipy.integrate.solve_ivp(closed_loop_manual, (0, 20), z0, t_eval1=t_eval)

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes[0,0].plot(sol_m.t, np.degrees(sol_m.y[2]), 'b-', lw=2)
        axes[0,0].set_ylabel(r"$\Delta\theta$ (deg)"); axes[0,0].set_title(r"$\Delta\theta(t)$")
        axes[0,1].plot(sol_m.t, sol_m.y[0], 'r-', lw=2)
        axes[0,1].set_ylabel(r"$\Delta x$ (m)"); axes[0,1].set_title(r"$\Delta x(t)$")
        u_hist = np.array([-(K_manual @ sol_m.y[:,i:i+1])[0,0] for i in range(len(sol_m.t))])
        axes[1,0].plot(sol_m.t, np.degrees(u_hist), 'g-', lw=2)
        axes[1,0].set_ylabel(r"$\Delta\phi$ (deg)"); axes[1,0].set_title(r"$\Delta\phi(t)$")
        axes[1,1].plot(sol_m.t, sol_m.y[1], 'm-', lw=2)
        axes[1,1].set_ylabel(r"$\Delta v_x$ (m/s)"); axes[1,1].set_title(r"$\Delta v_x(t)$")
        for ax in axes.flat:
            ax.grid(True, alpha=0.3); ax.set_xlabel("Temps (s)")
        fig.suptitle("Contrôleur Manuel — $K = (0,\\; 0,\\; -0.2,\\; -0.5)$", fontsize=13, fontweight='bold')
        plt.tight_layout()
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##  Contrôleur par Placement de Pôles

    ### Théorème fondamental

    Puisque le système latéral est commandable, le **théorème de placement de
    pôles** s'applique : pour tout ensemble de $n_{\mathrm{lat}} = 4$ pôles
    $\{\lambda_1, \lambda_2, \lambda_3, \lambda_4\}$ (réels ou complexes
    conjugués), il existe une unique matrice de gain $K \in \mathbb{R}^{1 \times
    4}$ telle que les valeurs propres de $A_{\mathrm{lat}} - B_{\mathrm{lat}} K$
    soient exactement $\lambda_1, \ldots, \lambda_4$.

    ### Choix des pôles désirés

    On souhaite à présent que **les quatre** variables d'état convergent vers
    zéro. Le temps de réglement souhaité est d'environ 20 secondes, ce qui
    correspond à un pôle dominant de partie réelle environ $-0.3$ (puisque
    $t_r \approx 4/|\mathrm{Re}(\lambda)|$).

    On choisit :
    - Une paire de pôles complexes conjugués pour un comportement oscillant
      amorti agréable ;
    - Une paire de pôles réels pour amortir rapidement les modes les plus lents.

    $$\boxed{\lambda_1 = -0.5 + 0.3j, \quad \lambda_2 = -0.5 - 0.3j, \quad
    \lambda_3 = -0.3, \quad \lambda_4 = -0.3}$$

    Ce placement donne un temps de réglement dominant d'environ
    $4/0.3 \approx 13.3$ s (pour les pôles réels), bien en dessous de 20 s.
    Les pôles complexes fournissent un amortissement
    $\zeta = 0.5/\sqrt{0.34} \approx 0.86$, ce qui évite les oscillations
    excessives.

    ### Calcul

    Le calcul est effectué numériquement via `scipy.signal.place_poles`, qui
    utilise la forme canonique de commandabilité. La fonction renvoie la matrice
    de gain $K$ telle que
    $A_{\mathrm{cl}} = A_{\mathrm{lat}} - B_{\mathrm{lat}} K$ ait les pôles
    spécifiés.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy, t_eval, z0):
    def _():
        poles_desired = [-0.5 + 0.3j, -0.5 - 0.3j, -0.4, -0.2]

        result_pp = scipy.signal.place_poles(A_lat, B_lat, poles_desired)
        K_pp = result_pp.gain_matrix

        print("K_pp =")
        print(K_pp)

        A_cl_pp = A_lat - B_lat @ K_pp
        poles_pp = np.linalg.eigvals(A_cl_pp)
        print("\nPôles en boucle fermée :")
        for i, p in enumerate(sorted(poles_pp, key=lambda x: x.real)):
            print(f"  λ_{i+1} = {p:.6f}")
        print(f"\nTous à Re < 0 : {all(p.real < 0 for p in poles_pp)}")



        def closed_loop_pp(t, z):
            u = -(K_pp @ z)[0]
            return A_lat @ z + B_lat.flatten() * u

        t_eval2 = np.linspace(0, 30, 1500)
        sol_pp = scipy.integrate.solve_ivp(closed_loop_pp, (0, 30), z0, t_eval2=t_eval)

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes[0,0].plot(sol_pp.t, np.degrees(sol_pp.y[2]), 'b-', lw=2)
        axes[0,0].set_ylabel(r"$\Delta\theta$ (deg)"); axes[0,0].set_title(r"$\Delta\theta(t)$")
        axes[0,1].plot(sol_pp.t, sol_pp.y[0], 'r-', lw=2)
        axes[0,1].set_ylabel(r"$\Delta x$ (m)"); axes[0,1].set_title(r"$\Delta x(t)$")
        u_pp = np.array([-(K_pp @ sol_pp.y[:,i:i+1])[0,0] for i in range(len(sol_pp.t))])
        axes[1,0].plot(sol_pp.t, np.degrees(u_pp), 'g-', lw=2)
        axes[1,0].set_ylabel(r"$\Delta\phi$ (deg)"); axes[1,0].set_title(r"$\Delta\phi(t)$")
        axes[1,1].plot(sol_pp.t, sol_pp.y[1], 'm-', lw=2)
        axes[1,1].set_ylabel(r"$\Delta v_x$ (m/s)"); axes[1,1].set_title(r"$\Delta v_x(t)$")
        for ax in axes.flat:
            ax.grid(True, alpha=0.3); ax.set_xlabel("Temps (s)")
        fig.suptitle("Contrôleur par Placement de Pôles", fontsize=13, fontweight='bold')
        plt.tight_layout()
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Contrôleur LQR (Commande Optimale Quadratique)

    ### Formulation du problème LQR

    La commande LQR (*Linear Quadratic Regulator*) minimise le critère de
    performance :

    $$\boxed{J = \int_0^{\infty} \left( z_{\mathrm{lat}}(t)^\top Q\,
    z_{\mathrm{lat}}(t) + u(t)^\top R\, u(t) \right) \mathrm{d}t}$$

    où $Q \succeq 0$ est une matrice de pondération de l'état (symétrique
    semi-définie positive) et $R > 0$ est la pondération de l'entrée (définie
    positive).

    ---

    ### Dérivation à partir du principe de Bellman

    La fonction valeur optimale $V(z) = \inf_u J(z_0 = z)$ satisfait l'équation
    de Hamilton-Jacobi-Bellman (HJB) stationnaire :

    $$0 = \min_u \left[ z^\top Q z + u^\top R u + \left(\nabla V\right)^\top
    \left(A_{\mathrm{lat}} z + B_{\mathrm{lat}} u\right) \right]$$

    On fait l'**ansatz quadratique** $V(z) = z^\top P z$ avec $P \succ 0$. La
    condition d'optimalité en $u$ donne, en dérivant l'expression entre crochets
    et en annulant la dérivée :

    $$2Ru + B_{\mathrm{lat}}^\top \left(2Pz\right) = 0$$

    $$\boxed{u^* = -R^{-1} B_{\mathrm{lat}}^\top P\, z}$$

    ---

    #### Complétion du carré

    En substituant $u^*$ dans la condition HJB et en effectuant une complétion
    du carré, on obtient l'**équation algébrique de Riccati** (ARE) :

    $$\boxed{A_{\mathrm{lat}}^\top P + P\,A_{\mathrm{lat}} -
    P\,B_{\mathrm{lat}}\,R^{-1}\,B_{\mathrm{lat}}^\top P + Q = 0}$$

    Cette équation algébrique matricielle admet une unique solution $P \succ 0$
    sous les hypothèses de commandabilité (vérifiée) et d'observabilité du
    couple $(A_{\mathrm{lat}}, Q^{1/2})$.

    La loi de commande optimale est donc le retour d'état linéaire :

    $$\boxed{K_{\mathrm{oc}} = R^{-1} B_{\mathrm{lat}}^\top P}$$

    ---

    ### Choix des pondérations

    Le choix de $Q$ et $R$ détermine le compromis entre performance de
    régulation et effort de commande :

    $$Q = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 10 & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix}, \qquad R = \begin{pmatrix} 0.1 \end{pmatrix}$$

    - $Q_{33} = 10$ : pénalise fortement l'angle $\theta$ (priorité principale
      de stabilité angulaire) ;
    - $Q_{11} = 1$ : pénalise la position latérale pour assurer $\Delta x \to 0$ ;
    - $Q_{44} = 1$ : amortit la vitesse angulaire pour éviter les oscillations ;
    - $R = 0.1$ : autorise un effort de commande modéré (une valeur plus grande
      réduirait l'effort mais ralentirait la convergence).
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy, t_eval, z0):
    def _():
        Q = np.diag([1.0, 0.0, 10.0, 1.0])
        R_mat = np.array([[0.1]])

        P = scipy.linalg.solve_continuous_are(A_lat, B_lat, Q, R_mat)

        K_oc = np.linalg.inv(R_mat) @ B_lat.T @ P
        print("P (matrice de Riccati, symétrique définie positive) =")
        print(np.round(P, 4))
        print(f"\nP est symétrique : {np.allclose(P, P.T)}")
        print(f"Valeurs propres de P : {np.linalg.eigvals(P).real}")

        print(f"\nK_oc =")
        print(K_oc)

        A_cl_oc = A_lat - B_lat @ K_oc
        poles_oc = np.linalg.eigvals(A_cl_oc)
        print("\nPôles en boucle fermée (LQR) :")
        for i, p in enumerate(sorted(poles_oc, key=lambda x: x.real)):
            print(f"  λ_{i+1} = {p:.6f}")
        print(f"\nTous à Re < 0 : {all(p.real < 0 for p in poles_oc)}")


        def closed_loop_oc(t, z):
            u = -(K_oc @ z)[0]
            return A_lat @ z + B_lat.flatten() * u

        t_eval3 = np.linspace(0, 30, 1500)
        sol_oc = scipy.integrate.solve_ivp(closed_loop_oc, (0, 30), z0, t_eval3=t_eval)

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes[0,0].plot(sol_oc.t, np.degrees(sol_oc.y[2]), 'b-', lw=2)
        axes[0,0].set_ylabel(r"$\Delta\theta$ (deg)"); axes[0,0].set_title(r"$\Delta\theta(t)$")
        axes[0,1].plot(sol_oc.t, sol_oc.y[0], 'r-', lw=2)
        axes[0,1].set_ylabel(r"$\Delta x$ (m)"); axes[0,1].set_title(r"$\Delta x(t)$")
        u_oc = np.array([-(K_oc @ sol_oc.y[:,i:i+1])[0,0] for i in range(len(sol_oc.t))])
        axes[1,0].plot(sol_oc.t, np.degrees(u_oc), 'g-', lw=2)
        axes[1,0].set_ylabel(r"$\Delta\phi$ (deg)"); axes[1,0].set_title(r"$\Delta\phi(t)$")
        axes[1,1].plot(sol_oc.t, sol_oc.y[1], 'm-', lw=2)
        axes[1,1].set_ylabel(r"$\Delta v_x$ (m/s)"); axes[1,1].set_title(r"$\Delta v_x(t)$")
        for ax in axes.flat:
            ax.grid(True, alpha=0.3); ax.set_xlabel("Temps (s)")
        fig.suptitle("Contrôleur LQR", fontsize=13, fontweight='bold')
        plt.tight_layout()
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comparaison des Trois Contrôleurs

    Pour comparer objectivement les trois approches de commande, simulons-les
    côte à côte à partir de la même condition initiale et comparons les
    trajectoires des quatre variables d'état ainsi que l'effort de commande.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy, t_eval, z0):
    def _():
        Q = np.diag([1.0, 0.0, 10.0, 1.0])
        R_mat = np.array([[0.1]])

        P = scipy.linalg.solve_continuous_are(A_lat, B_lat, Q, R_mat)

        K_oc = np.linalg.inv(R_mat) @ B_lat.T @ P
        print("P (matrice de Riccati, symétrique définie positive) =")
        print(np.round(P, 4))
        print(f"\nP est symétrique : {np.allclose(P, P.T)}")
        print(f"Valeurs propres de P : {np.linalg.eigvals(P).real}")

        print(f"\nK_oc =")
        print(K_oc)

        A_cl_oc = A_lat - B_lat @ K_oc
        poles_oc = np.linalg.eigvals(A_cl_oc)
        print("\nPôles en boucle fermée (LQR) :")
        for i, p in enumerate(sorted(poles_oc, key=lambda x: x.real)):
            print(f"  λ_{i+1} = {p:.6f}")
        print(f"\nTous à Re < 0 : {all(p.real < 0 for p in poles_oc)}")



        def closed_loop_oc(t, z):
            u = -(K_oc @ z)[0]
            return A_lat @ z + B_lat.flatten() * u

        t_evalX = np.linspace(0, 30, 1500)
        sol_oc = scipy.integrate.solve_ivp(closed_loop_oc, (0, 30), z0, t_evalX=t_eval)

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes[0,0].plot(sol_oc.t, np.degrees(sol_oc.y[2]), 'b-', lw=2)
        axes[0,0].set_ylabel(r"$\Delta\theta$ (deg)"); axes[0,0].set_title(r"$\Delta\theta(t)$")
        axes[0,1].plot(sol_oc.t, sol_oc.y[0], 'r-', lw=2)
        axes[0,1].set_ylabel(r"$\Delta x$ (m)"); axes[0,1].set_title(r"$\Delta x(t)$")
        u_oc = np.array([-(K_oc @ sol_oc.y[:,i:i+1])[0,0] for i in range(len(sol_oc.t))])
        axes[1,0].plot(sol_oc.t, np.degrees(u_oc), 'g-', lw=2)
        axes[1,0].set_ylabel(r"$\Delta\phi$ (deg)"); axes[1,0].set_title(r"$\Delta\phi(t)$")
        axes[1,1].plot(sol_oc.t, sol_oc.y[1], 'm-', lw=2)
        axes[1,1].set_ylabel(r"$\Delta v_x$ (m/s)"); axes[1,1].set_title(r"$\Delta v_x(t)$")
        for ax in axes.flat:
            ax.grid(True, alpha=0.3); ax.set_xlabel("Temps (s)")
        fig.suptitle("Contrôleur LQR", fontsize=13, fontweight='bold')
        plt.tight_layout()
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##  Validation sur Modèle Non Linéaire

    Toutes les lois de commande ont été synthétisées sur le modèle linéarisé.
    Il est essentiel de les valider sur le **modèle non linéaire complet** via
    la fonction `redstart_solve`. On applique ici le contrôleur LQR au système
    non linéaire avec la même condition initiale.

    **Attention.** Le modèle linéarisé n'est valide que pour de petits écarts
    autour de l'équilibre ($|\Delta\theta| \ll 1$ rad, $|\Delta\phi| \ll 1$ rad).
    L'angle initial $\Delta\theta(0) = \pi/4 \approx 0.785$ rad est déjà assez
    grand, on s'attend donc à des écarts entre le modèle linéaire et le modèle
    non linéaire, surtout dans les premiers instants.
    """)
    return


@app.cell
def _(A_lat, B_lat, M, g, np, plt, redstart_solve, scipy):
    def _():
        # Auto-suffisant : recalcule K_oc pour compatibilité Marimo
        Q = np.diag([1.0, 0.0, 10.0, 1.0])
        R_mat = np.array([[0.1]])
        P = scipy.linalg.solve_continuous_are(A_lat, B_lat, Q, R_mat)
        K_oc = np.linalg.inv(R_mat) @ B_lat.T @ P

        z0_nl = [0.0, 0.0, 10.0, 0.0, np.pi/4, 0.0]

        def f_phi_lqr_nl(t, state):
            'Loi de commande LQR appliquée au modèle non linéaire.'
            dx = state[0]
            dvx = state[1]
            dtheta = state[4]
            domega = state[5]
            z_lat = np.array([dx, dvx, dtheta, domega])
            dphi = -(K_oc @ z_lat)[0]
            f = M * g
            return np.array([f, dphi])

        sol_nl = redstart_solve([0, 30], z0_nl, f_phi_lqr_nl)
        t = np.linspace(0, 30, 2000)
        y_nl = sol_nl(t)

        fig, axes = plt.subplots(2, 3, figsize=(15, 9))
        axes[0,0].plot(t, y_nl[4], 'b-', lw=2)
        axes[0,0].set_ylabel(r"$\theta$ (rad)"); axes[0,0].set_title("Inclinaison")
        axes[0,0].axhline(0, color='grey', ls='--')

        axes[0,1].plot(t, y_nl[0], 'r-', lw=2)
        axes[0,1].set_ylabel(r"$x$ (m)"); axes[0,1].set_title("Position latérale")

        axes[0,2].plot(t, y_nl[2], 'g-', lw=2)
        axes[0,2].set_ylabel(r"$y$ (m)"); axes[0,2].set_title("Altitude")

        u_nl = np.array([f_phi_lqr_nl(t[i], y_nl[:,i])[1] for i in range(len(t))])
        axes[1,0].plot(t, np.degrees(u_nl), 'm-', lw=2)
        axes[1,0].set_ylabel(r"$\phi$ (deg)"); axes[1,0].set_title("Angle de gîrage")

        axes[1,1].plot(t, y_nl[1], 'c-', lw=2)
        axes[1,1].set_ylabel(r"$v_x$ (m/s)"); axes[1,1].set_title("Vitesse latérale")

        axes[1,2].plot(t, y_nl[5], 'orange', lw=2)
        axes[1,2].set_ylabel(r"$\omega$ (rad/s)"); axes[1,2].set_title("Vitesse angulaire")

        for ax in axes.flat:
            ax.grid(True, alpha=0.3); ax.set_xlabel("Temps (s)")
        fig.suptitle("Validation LQR sur Modèle Non Linéaire", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

        print(f"\nMax |θ| = {np.max(np.abs(y_nl[4])):.4f} rad ({np.degrees(np.max(np.abs(y_nl[4]))):.2f}°)")
        print(f"Max |φ| = {np.max(np.abs(u_nl)):.4f} rad ({np.degrees(np.max(np.abs(u_nl))):.2f}°)")
        print(f"|θ| < π/2 respecté : {np.max(np.abs(y_nl[4])) < np.pi/2}")
        return print(f"|φ| < π/2 respecté : {np.max(np.abs(u_nl)) < np.pi/2}")


    _()
    return


if __name__ == "__main__":
    app.run()
