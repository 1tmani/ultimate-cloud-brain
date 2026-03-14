from theme_engine import theme
from particle_engine import particles

def page(output):
    style = theme("neon")
    spark = particles()
    return f"""
    <!DOCTYPE html>
    <html>
    <body style="{style} text-align:center; padding-top:50px;">
        <h1>Ultimate Cloud Brain</h1>
        {spark}
        <form method='POST'>
            <input name='command' placeholder='Enter command'>
            <button type='submit'>Run</button>
        </form>
        <div style='border:1px solid white; padding:20px; width:60%; margin:auto; margin-top:40px;'>{output}</div>
    </body>
    </html>
    """
