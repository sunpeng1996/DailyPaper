---
title: 'Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered
  Ablation'
title_zh: LLM维护的Wiki知识库渐进式披露结构的预注册消融实验
authors:
- Theodore O. Cochran
affiliations:
- AI for Altruism (A4A)
arxiv_id: '2607.04576'
url: https://arxiv.org/abs/2607.04576
pdf_url: https://arxiv.org/pdf/2607.04576
published: '2026-07-06'
collected: '2026-07-07'
category: RAG
direction: RAG · 知识库访问结构优化
tags:
- RAG
- Progressive Disclosure
- Knowledge Base
- LLM Agent
- Ablation Study
one_liner: 通过内容严格对齐的预注册消融，验证知识库渐进式披露可在非劣质量下显著降低LLM访问成本
practical_value: '- 搭建电商商品知识库/商家运营知识库RAG系统时，优先给每个条目加1行摘要+轻量关键词检索工具，可减少Agent访问的文档量、降低工具调用次数，实测能降本30%以上且回答质量无明显损失

  - 若使用GPT-4o/Claude级别的强能力Agent，不要强制预加载全量目录，允许Agent自路由+调用检索工具的成本收益比最高；仅对弱能力Agent可考虑预加载精简目录的方案

  - 做RAG结构优化的效果验证时，需通过版本控制保证不同实验组的底层内容完全一致，避免把内容差异误判为结构优化的收益；评估时采用跨模型盲评可大幅降低LLM Judge的偏好偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM Agent访问知识库时，业界普遍认为渐进式披露（精简目录+条目摘要+按需加载）能降低token成本，但该结论缺乏严格控制内容一致的实验支撑；且预先假设的「节省全量索引加载成本」机制，在具备强工具使用能力的Agent身上并不成立——这类Agent会直接推断目标文档路径读取，根本不会加载全量索引，因此需要量化真实的成本收益和作用机制。
### 方法关键点
- 严格控制变量：4组消融臂的709页Wiki正文完全字节一致，仅访问结构不同：A0（基线，全量索引）、A1（拆分动态状态到单独文件）、A2（每页加1行摘要）、A3（加关键词检索工具返回页摘要）
- 覆盖3种实际访问场景：协议约束Agent、自由自路由Agent、强制预加载目录
- 预注册实验设计：所有假设、分析方案、评估规则提前锁定，采用跨模型盲评（GPT-5评分Claude Opus生成的答案），从4个维度评估质量，同时统计token成本、工具调用次数、引用页数
### 关键结果
- 质量：A3相对A0质量差为+0.01（满分8，95%CI [-0.27, +0.26]），满足预设非劣性要求；自由自路由场景下A3质量甚至显著更好，仅强制预加载场景下质量非劣性未通过验证
- 成本：A3在所有场景下成本均显著下降：协议约束场景降30%，自由自路由场景降34%，强制预加载场景降58%；成本下降核心来自访问更精准：引用页数从6.1降至4.2（降31%），工具调用次数减少

最值得记住的一句话：标称的效率优化机制往往和Agent实际使用行为不符，只有严格控制变量的量化实验才能分离出真实收益。
