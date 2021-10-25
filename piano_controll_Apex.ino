#include <Mouse.h>
#include <Keyboard.h>

void setup()
{
  Serial.begin(115200);
  Keyboard.begin();
  Mouse.begin();
}

byte piano_input;
int l, r, u, d;

void loop()
{ 
  if (Serial.available() > 0);
  {
    piano_input = (byte)Serial.read();
    /*移動*/
    if (piano_input == 51)
    {
      Keyboard.press('w');
    }

    else if (piano_input == 51+88)
    {
      Keyboard.release('w');
    }

    else if (piano_input == 52)
    {
      Keyboard.press('s');
    }

    else if (piano_input == 52+88)
    {
      Keyboard.release('s');
    }

    else if (piano_input == 50)
    {
      Keyboard.press('a');
    }

    else if (piano_input == 50+88)
    {
      Keyboard.release('a');
    }

    else if (piano_input == 53)
    {
      Keyboard.press('d');
    }

    else if (piano_input == 53+88)
    {
      Keyboard.release('d');
    }

    else if (piano_input == 47)
    {
      Keyboard.press(KEY_LEFT_CTRL);
    }

    else if (piano_input == 47+88)
    {
      Keyboard.release(KEY_LEFT_CTRL);
    }

    else if (piano_input == 55)
    {
      Keyboard.press(' ');
    }

    else if (piano_input == 55+88)
    {
      Keyboard.release(' ');
    }

    else if (piano_input == 48)
    {
      Keyboard.press(KEY_LEFT_SHIFT);
    }

    else if (piano_input == 48+88)
    {
      Keyboard.release(KEY_LEFT_SHIFT);
    }
    /*移動*/

    /*武器・アビリティ*/
    else if (piano_input == 49)
    {
      Keyboard.press('q');
    }

    else if (piano_input == 49+88)
    {
      Keyboard.release('q');
    }
    
    else if (piano_input == 45)
    {
      Keyboard.press('z');
    }

    else if (piano_input == 45+88)
    {
      Keyboard.release('z');
    }

    else if (piano_input == 54)
    {
      Keyboard.press('e');
    }

    else if (piano_input == 54+88)
    {
      Keyboard.release('e');
    }

    else if (piano_input == 56)
    {
      Keyboard.press('x');
    }

    else if (piano_input == 56+88)
    {
      Keyboard.release('x');
    }

    else if (piano_input == 46)
    {
      Keyboard.press(KEY_TAB);
    }

    else if (piano_input == 46+88)
    {
      Keyboard.release(KEY_TAB);
    }

    else if (piano_input == 63)
    {
      Keyboard.press('m');
    }

    else if (piano_input == 63+88)
    {
      Keyboard.release('m');
    }

    else if (piano_input == 191)
    {
      Mouse.press(MOUSE_LEFT);
    }

    else if (piano_input == 192)
    {
      Mouse.release(MOUSE_LEFT);
    }

    else if (piano_input == 58)
    {
      Keyboard.press('b');
    }

    else if (piano_input == 58+88)
    {
      Keyboard.release('b');
    }

    else if (piano_input == 83)
    {
      Mouse.press(MOUSE_RIGHT);
    }

    else if (piano_input == 83+88)
    {
      Mouse.release(MOUSE_RIGHT);
    }

    else if (piano_input == 59)
    {
      Keyboard.press('v');
    }

    else if (piano_input == 59+88)
    {
      Keyboard.release('v');
    }

    else if (piano_input == 57)
    {
      Keyboard.press('r');
    }

    else if (piano_input == 57+88)
    {
      Keyboard.release('r');
    }

    else if (piano_input == 73)
    {
      Keyboard.press('1');
    }

    else if (piano_input == 73+88)
    {
      Keyboard.release('1');
    }

    else if (piano_input == 82)
    {
      Keyboard.press('2');
    }

    else if (piano_input == 82+88)
    {
      Keyboard.release('2');
    }

    else if (piano_input == 71)
    {
      Keyboard.press('3');
    }

    else if (piano_input == 71+88)
    {
      Keyboard.release('3');
    }

    else if (piano_input == 60)
    {
      Keyboard.press('g');
    }

    else if (piano_input == 60+88)
    {
      Keyboard.release('g');
    }
/*
    else if (piano_input == 61)
    {
      Keyboard.press('t');
    }

    else if (piano_input == 61+88)
    {
      Keyboard.release('t');
    }
*/
    else if (piano_input == 44)
    {
      Keyboard.press('4');
    }

    else if (piano_input == 44+88)
    {
      Keyboard.release('4');
    }

    else if (piano_input == 43)
    {
      Keyboard.press('5');
    }

    else if (piano_input == 43+88)
    {
      Keyboard.release('5');
    }

    else if (piano_input == 42)
    {
      Keyboard.press('6');
    }

    else if (piano_input == 42+88)
    {
      Keyboard.release('6');
    }

    else if (piano_input == 41)
    {
      Keyboard.press('7');
    }

    else if (piano_input == 41+88)
    {
      Keyboard.release('7');
    }

    else if (piano_input == 40)
    {
      Keyboard.press('8');
    }

    else if (piano_input == 40+88)
    {
      Keyboard.release('8');
    }

    else if (piano_input == 39)
    {
      Keyboard.press('9');
    }

    else if (piano_input == 39+88)
    {
      Keyboard.release('9');
    }

    else if (piano_input == 62)
    {
      Keyboard.press('f');
    }

    else if (piano_input == 62+88)
    {
      Keyboard.release('f');
    }

    else if (piano_input == 64)
    {
      Keyboard.press('n');
    }

    else if (piano_input == 64+88)
    {
      Keyboard.release('n');
    }
    /*武器・アビリティ*/
    
    /*通信*/
    else if (piano_input == 85)
    {
      Keyboard.press('j');
    }

    else if (piano_input == 85+88)
    {
      Keyboard.release('j');
    }
    
    else if (piano_input == 70)
    {
      Keyboard.press('h');
    }

    else if (piano_input == 70+88)
    {
      Keyboard.release('h');
    }

    else if (piano_input == 92)
    {
      Keyboard.press('u');
    }

    else if (piano_input == 92+88)
    {
      Keyboard.release('u');
    }

    else if (piano_input == 93)
    {
      Keyboard.press('i');
    }

    else if (piano_input == 93+88)
    {
      Keyboard.release('i');
    }

    else if (piano_input == 94)
    {
      Keyboard.press('o');
    }

    else if (piano_input == 94+88)
    {
      Keyboard.release('o');
    }

    else if (piano_input == 95)
    {
      Keyboard.press('p');
    }

    else if (piano_input == 95+88)
    {
      Keyboard.release('p');
    }

    else if (piano_input == 96)
    {
      Keyboard.press('k');
    }

    else if (piano_input == 96+88)
    {
      Keyboard.release('k');
    }
    /*通信*/

    /*マウス*/
    if (piano_input == 76 || l == 1)
    {
      Mouse.move(-1, 0, 0);
      l = 1;
    }

    if (piano_input == 76+88)
    {
      l = 0;
    }

    if (piano_input == 79 || r == 1)
    {
      Mouse.move(1, 0, 0);
      r = 1;
    }

    if (piano_input == 79+88)
    {
      r = 0;
    }

    if (piano_input == 78 || u == 1)
    {
      Mouse.move(0, -1, 0);
      u = 1;
    }

    if (piano_input == 78+88)
    {
      u = 0;
    }

    if (piano_input == 77 || d == 1)
    {
      Mouse.move(0, 1, 0);
      d = 1;
    }

    if (piano_input == 77+88)
    {
      d = 0;
    }

    /*マウス*/
  }
}
