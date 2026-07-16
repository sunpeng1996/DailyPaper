---
title: Policy-Conditioned Constrained Decoding for Column-Level Access Control in
  Text-to-SQL
title_zh: 面向Text-to-SQL列级访问控制的策略条件约束解码方法
authors:
- Ryoto Miyamoto
- Xin Fan
- Hayato Yamana
affiliations:
- Waseda University
arxiv_id: '2607.12341'
url: https://arxiv.org/abs/2607.12341
pdf_url: https://arxiv.org/pdf/2607.12341
published: '2026-07-14'
collected: '2026-07-16'
category: LLM
direction: LLM安全解码 · Text-to-SQL列级权限控制
tags:
- Text-to-SQL
- Constrained Decoding
- Access Control
- Logits Mask
- LLM Safety
one_liner: 通过逐token logits掩码实现Text-to-SQL列级访问零泄露，兼顾高覆盖率与低推理开销
practical_value: '- 搭建Agent调用内部数据库的Text-to-SQL模块时，可复用逐token logits掩码的约束解码方案，相比传统拒答类权限控制方案覆盖率更高，可确定性避免敏感数据泄露

  - 对于需要按语义角色做权限控制的生成场景（如电商用户标签查询、运营数据分析），可借鉴将权限规则对齐生成语法产生式的思路，无需依赖prompt或微调即可消除违规输出

  - 业务侧高吞吐敏感数据访问控制场景，可优先选用单解码pass完成约束的方案，相比多轮纠错/校验方案推理开销仅增加10%以内，性能损失可控'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
Text-to-SQL跨数据提供方与用户的信任边界部署时，需同时满足政策合规、回答覆盖率、成本可控三个要求；现有方案仅基于列是否被提及做随机拒答，既无法区分列的语义使用角色导致误判，也不能确定性杜绝违规输出。
### 方法关键点
1. 将列级访问要求形式化为基于语义使用角色（输出/过滤条件/聚合参数）的列使用策略
2. 提出PCC-SQL，将每个列使用角色与解码器跟踪的语法产生式对齐，通过逐token logits掩码，在单次解码过程中确定性消除支持SQL片段内的列使用违规
### 关键结果
在3个基准、3个开源模型上测试，Spider-CU数据集上实现0%泄露率，覆盖率最高达88.7%，生成token数仅比直接prompt高10%以内，同时可保障执行准确率的语义对齐。
