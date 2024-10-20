```sql
 
SELECT a.state, avg(a.ranking) as average_ranking
FROM udugeorgiaoffersdb a
JOIN udugeorgiacommitsdb b
ON a.name = b.name
GROUP BY a.state
ORDER BY a.state DESC;

```

```response from databricks
[Row(state='PA', average_ranking=0.9612500071525574), Row(state='GA', average_ranking=0.9381333192189535)]
```

