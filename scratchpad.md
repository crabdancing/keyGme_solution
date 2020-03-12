# Scratchpad

* Must be >= 16 chars
* character cannot be less than A (65) or greater than Z (90)
    * thus, MUST be between A and Z
* similar check for being between '0' (48) and '9' (57) (range is below A!)
    * Thus, must be alphanumeral

* `summation = (summation + key[index] >> 1) % 0xf00 + 10;`
    * `v = (v ch >> 1) % 3840 + 10`
    * Decompiled key handling line
    * This is executed over and over for every single char in the key (`index`), with `local_c` outside of loop scope.


