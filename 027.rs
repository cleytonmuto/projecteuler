use std::time::Instant;

/// Sieve of Eratosthenes - O(1) primality lookup
fn prime_sieve(limit: usize) -> Vec<bool> {
    let mut is_prime = vec![true; limit];
    is_prime[0] = false;
    is_prime[1] = false;
    let mut i = 2;
    while i * i < limit {
        if is_prime[i] {
            let mut j = i * i;
            while j < limit {
                is_prime[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    is_prime
}

/// Primes up to n (excluding n)
fn primes_up_to(n: i32) -> Vec<i32> {
    let sieve = prime_sieve(n as usize);
    (2..n).filter(|&p| sieve[p as usize]).collect()
}

fn count_consecutive_primes(a: i32, b: i32, is_prime: &[bool]) -> i32 {
    let mut n = 0i64;
    loop {
        let t = n * n + n * (a as i64) + (b as i64);
        if t < 0 || t >= is_prime.len() as i64 || !is_prime[t as usize] {
            return n as i32;
        }
        n += 1;
    }
}

fn solution() -> i32 {
    // Problem bounds: |a| < 1000, |b| <= 1000
    // Max value of n²+an+b: for n~80, a=999, b=1000 => ~80²+80*999+1000 < 90_000
    const SIEVE_LIMIT: usize = 2_000000;
    let is_prime = prime_sieve(SIEVE_LIMIT);

    // b must be prime (n=0 gives b)
    let primes: Vec<i32> = primes_up_to(1000001);

    let mut max_c = 0;
    let mut max_ab = 0;

    for &b in &primes {
        // a in [-999, 999]; when b is odd, 1+a+b must be odd => a must be odd
        let a_start = if b == 2 { -999999 } else { -999999 };
        let step = if b == 2 { 1 } else { 2 };
        let mut a = a_start;
        while a <= 999999 {
            let c = count_consecutive_primes(a, b, &is_prime);
            if c > max_c {
                max_c = c;
                max_ab = a * b;
            }
            a += step;
        }
    }
    max_ab
}

fn main() {
    let t = Instant::now();
    println!("{}, {:?}", solution(), t.elapsed());
}
