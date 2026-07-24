# {{PROJECT_ID}} 项目看板

```dataview
TABLE status, owner, due, depends_on, output
FROM ""
WHERE type = "task"
SORT priority ASC, due ASC
```

## 待人工确认

```dataview
TABLE gate, object, version, note
FROM "00-admin/reviews"
WHERE status = "pending"
```
