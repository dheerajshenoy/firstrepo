// FUNCTION TO FIND THE GCD OF TWO NUMBERS
int gcd(int a,int b) {
  int A,B,q,r;
    if(a>b) {
        A = a;
        B = b;
        q = A/B;
        r = A%B;
        while(r!=0) {
          A = q;
          B = r;
          q = A/B;
          r = A%B;
        }
        return B;
      }
    else {
        B = a;
        A = b;
        q = A/B;
        r = A%B;
        while(r!=0) {
          A = q;
          B = r;
          q = A/B;
          r = A%B;
        }
        return B;
    }
}

//FUNCTION TO FIND THE FACTORIAL
int factorial(int n) {
  int i,res=1;
  for(i=0;i<n;i++)
      res = res*(n-i);
  return res;
}

//FUNCTION FOR COMBINATION
int comb(int n,int r) {
  int c;
  c = factorial(n)/(factorial(n-r)*factorial(r));
  return c;
}

//FUNCTION FOR PERMUTATION
int permut(int n,int r) {
  int p;
  p = factorial(n)/factorial(n-r);
  return p;
}

//FUNCTION TO CHECK IF A GIVEN NUMBER IS A PRIME
const char* isPrime(int n) {
  int j,count=0;

  for(j=1;j<=n/2;j++)
    if(n%j!=0)
      count++;
  if(count == n/2-1)
    return "True";
  else
    return "False";
}

// FUNCTION FOR POWER
float POW(float x,float n) {
  int i;
  float mul=x,num=x;
  for(i=1;i<=n;i++)
      mul=mul*num;
  return mul/x;
}

int APPEND(auto array,auto value) {
  int i;
  int l;
  return sizeof(array)/sizeof(int);

}
// FUNCTION TO GENERATE PRIME NUMBERS
int prime(int from,int to) {

  int i,j,count,arr[to-from];
  for(i=from;i<=to;i++) {
    for(j=2;j<=i/2;j++)
        if(i%j!=0)
          count++;
    if(count == i/2-1)
      return i;
}
}

//FUNCTION TO REVERSE A NUMBER
auto reverse(int num,bool p)  {
  int n,rem;
  long int rev=0;
  n = num;
  while(n>0) {
    rem = n%10;
    rev = rev*10 + rem;
    n   = n/10;
  }
  if(p == true){
    if(num == rev)
      return("\ntrue",rev);
    else
      return("\nfalse",rev);
}
  else
      return(rev);
}
//FUNCTION TO PRINT FIRST N FIBONACCI NUMBERS 
int fibonacci(int n) {
    int f;
    if (n==1)
        return 1;
    else if (n==2)
        return 1;
    else 
        f = fibonacci(n-1) + fibonacci(n-2);
    return f;
}
