#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>

struct board
{
  int contestant;
  int nproblem;
  int problem[10];
  int penalty[10];
  int time;
  board(int c): contestant(c), nproblem(0)
  {
    time = 0;
    for ( int i = 0; i < 10; ++i )
      {
          problem[i] = 0;
          penalty[i] = 0;
      }
  }
  void calc_time()
  {
    for ( int i = 1; i < 10; ++i )
      {
          if ( problem[i] == 1 )
          time += penalty[i];
      }
  }
};

inline void init(int index[])
{
  for ( int i = 0; i < 101; ++i )
    index[i] = -1;
}

void judge(board &b, const int &problem, const int &time, const char &L)
{
  if (b.problem[problem] == 1)
    {
      return;
    }
  if ( L == 'C' )
    {
      ++b.nproblem;
      b.problem[problem] = 1;
      b.penalty[problem] += time;
    }
  else if ( L == 'I' )
    {
      b.penalty[problem] += 20;
    }
}

bool operator<(const board &b1, const board &b2)
{
  if ( b1.nproblem > b2.nproblem )
    return true;
  if ( b1.nproblem == b2.nproblem && b1.time < b2.time )
    return true;
  if ( b1.nproblem == b2.nproblem && b1.time == b2.time
       && b1.contestant < b2.contestant )
    return true;
  return false;
}

int main()
{
  int T;
  std::string s;
  int contestant, problem, time;
  char L;

  std::cin >> T;
  getline(std::cin, s);
  getline(std::cin, s);
  for ( int t = 1; t <= T; ++t )
    {
      int index[101];
      std::fill(index, index + 101, -1);
      std::vector<board> v;

      while( getline(std::cin, s) )
    {
      if ( s == "" ) break;

      std::istringstream iss(s);
      iss >> contestant >> problem >> time >> L;

      if ( index[contestant] == -1 )
        {
          v.push_back(*new board(contestant));
          index[contestant] = (int)v.size() - 1;
        }
      judge(v[index[contestant]], problem, time, L);
    }


      for ( std::vector<board>::iterator it = v.begin(); it != v.end(); ++it )
          it->calc_time();

      sort(v.begin(), v.end());
      for ( std::vector<board>::iterator it = v.begin(); it != v.end(); ++it )
          std::cout << it->contestant << ' ' << it->nproblem << ' ' << it->time << std::endl;
      if ( t < T )
          std::cout << std::endl;
    }
  return 0;
}