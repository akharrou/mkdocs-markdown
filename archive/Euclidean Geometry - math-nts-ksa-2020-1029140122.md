# Euclidean Geometry

## Ranges

Say we wanted[^1] to run something every hour between 1 and 5 AM, i.e every hour
in the range of 1AM - 5AM. We can use a dash (`-`) between the time value
Examples:
       `0 0-5 * * *`, run once, every hour between midnight and 5AM, every day
                      of the month, of every month
       `0 12 * 5-8 *`, run once, at noon, of every day of the month, of every
                       month between the 5th and 8th month.

## Common Mistakes

Never forget to fill in the first two columns, otherwise the command will
run every minute of every hour of what ever day/month specified.

<!-- ![[lion.jpg]] -->

[[about|Nice]]

## Real Applications

Examples:
Every 30minutes, during every regular business hours.
Common business hours are monday-friday, from 9am-5pm:

```bash
*/30 9-17 * * 1-5
```

[[about]]

---
**See also:**

- [[index|See the index page !]]

<!-- Foonotes -->
[^1]: some rather long footnote
<!-- >Foonotes -->
