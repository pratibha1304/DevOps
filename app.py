from flask import Flask, render_template_string

app = Flask(__name__)

NAV_BAR_HTML = """
<nav style="background-color: #333; padding: 15px; text-align: center; border-radius: 8px; margin-bottom: 20px;">
    <a href="/" style="color: white; text-decoration: none; margin: 0 15px; font-weight: bold;">Home</a>
    <a href="/max-verstappen" style="color: white; text-decoration: none; margin: 0 15px; font-weight: bold;">Max Verstappen</a>
    <a href="/red-bull-racing" style="color: white; text-decoration: none; margin: 0 15px; font-weight: bold;">Red Bull Racing</a>
    <a href="/formula-1" style="color: white; text-decoration: none; margin: 0 15px; font-weight: bold;">Formula 1</a>
    <a href="/championships" style="color: white; text-decoration: none; margin: 0 15px; font-weight: bold;">Championships</a>
</nav>
"""

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            width: 100%;
            box-sizing: border-box;
        }
        h1, h2 {
            color: #cc0000;
            text-align: center;
            margin-bottom: 20px;
        }
        p {
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: #e6e6e6;
            margin-bottom: 8px;
            padding: 10px;
            border-radius: 5px;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        """ + NAV_BAR_HTML + """
        <h1>{{ title }}</h1>
        {{ content | safe }}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    title = "Welcome to the F1 Fan Zone!"
    content = """
    <p>Dive into the thrilling world of Formula 1, focusing on the incredible journey of Max Verstappen and the powerhouse that is Red Bull Racing.</p>
    <p>Use the navigation above to explore different aspects of their success!</p>
    """
    return render_template_string(BASE_HTML, title=title, content=content)

@app.route('/max-verstappen')
def max_verstappen():
    title = "Max Verstappen: The Flying Dutchman"
    content = """
    <p>Max Emilian Verstappen (born 30 September 1997) is a Belgian-Dutch racing driver who competes under the Dutch flag in Formula 1 for Red Bull Racing.</p>
    <p>He is a multiple Formula 1 World Champion, known for his aggressive driving style, exceptional talent, and unwavering determination.</p>
    <p>Max made his Formula 1 debut at the age of 17, becoming the youngest driver to compete in F1. He quickly rose through the ranks, securing his first win at the Spanish Grand Prix in 2016 on his debut for Red Bull Racing, also making him the youngest ever Grand Prix winner.</p>
    """
    return render_template_string(BASE_HTML, title=title, content=content)

@app.route('/red-bull-racing')
def red_bull_racing():
    title = "Red Bull Racing: The Energy Drink Giant in F1"
    content = """
    <p>Red Bull Racing, also known simply as Red Bull, is a Formula 1 racing team based in the United Kingdom.</p>
    <p>The team was founded in 2005 by the Austrian beverage company Red Bull GmbH. Under the leadership of Team Principal Christian Horner and Chief Technical Officer Adrian Newey, Red Bull Racing has become one of the most dominant forces in modern Formula 1.</p>
    <p>They are renowned for their innovative car designs, strategic prowess, and ability to develop young talent through their junior driver program.</p>
    """
    return render_template_string(BASE_HTML, title=title, content=content)

@app.route('/formula-1')
def formula_1():
    title = "Formula 1: The Pinnacle of Motorsport"
    content = """
    <p>Formula 1 (F1) is the highest class of international racing for open-wheel single-seater formula racing cars sanctioned by the Fédération Internationale de l'Automobile (FIA).</p>
    <p>The Formula 1 World Championship has been one of the premier forms of racing around the world since its inaugural season in 1950.</p>
    <p>It is a global spectacle, combining cutting-edge technology, incredible athletic skill, and intense strategic battles, attracting millions of fans worldwide.</p>
    """
    return render_template_string(BASE_HTML, title=title, content=content)

@app.route('/championships')
def championships():
    title = "Max Verstappen's Formula 1 World Championships"
    content = """
    <p>Max Verstappen has achieved remarkable success in his Formula 1 career, securing multiple World Drivers' Championships:</p>
    <ul>
        <li><strong>2021 Formula 1 World Champion:</strong> A thrilling season-long battle culminating in a dramatic final race.</li>
        <li><strong>2022 Formula 1 World Champion:</strong> A dominant performance throughout the season, showcasing his and Red Bull's strength.</li>
        <li><strong>2023 Formula 1 World Champion:</strong> Continued his incredible form, breaking numerous records.</li>
    </ul>
    <p>These championships solidify his place among the sport's legends.</p>
    """
    return render_template_string(BASE_HTML, title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)
