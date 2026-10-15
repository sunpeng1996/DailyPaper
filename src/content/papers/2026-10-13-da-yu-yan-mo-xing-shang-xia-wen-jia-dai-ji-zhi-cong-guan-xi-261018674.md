---
title: 'From Relation-Specific Heads to Shared Interventions: Contextual Entrainment
  in Language Models'
title_zh: 大语言模型上下文夹带机制：从关系专属注意力头到共享干预靶点
authors:
- Jinghan Zheng
- Jiajun Shi
affiliations:
- McGill University
- Dalian University of Technology
arxiv_id: '2610.18674'
url: https://arxiv.org/abs/2610.18674
pdf_url: https://arxiv.org/pdf/2610.18674
published: '2026-10-13'
collected: '2026-10-15'
category: LLM
direction: 大模型可解释性 · 幻觉缓解
tags:
- contextual entrainment
- attention heads
- mechanistic interpretability
- hallucination mitigation
- RAG
one_liner: 揭示LLM上下文夹带的混合电路机制，提出跨关系可复用的全局干预靶点
practical_value: '- 电商RAG/客服Agent场景可复用全局干预思路，针对多类型无关上下文干扰问题，优先用异构攻击数据挖掘共享注意力头 ablation
  靶点，比单关系干预的副作用更小，不会大幅破坏正常事实回答能力

  - 多轮对话、个性化推荐prompt拼接等存在大量重复结构上下文的场景，可基于混合电路思路，用少量关系族+亚型专属头补充全局干预，进一步降低错误复制历史上下文token的概率

  - LLM对齐迭代时可减少针对单个任务/关系的干预优化，优先覆盖全局共享靶点，大幅降低对齐成本，同时保留模型in-context learning等通用能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM的上下文夹带现象（前置无关上下文的token被错误复用至后续回答）是RAG、长上下文问答、工具增强Agent等场景幻觉的重要来源，过往研究认为介导该行为的注意力头是关系专属的，导致干预成本极高，且无法适配混合多种关系的真实业务场景。
### 方法关键点
- 构建覆盖4大语义族（关联/属性/部分-整体/分类）、19种子关系的事实干扰基准，每个样本前置结构一致的无关真实事实作为干扰项，隔离token级复用效应
- 基于Gumbel-Sigmoid可微掩码搜索可降低夹带的注意力头集合，对比单亚型、单语义族、全局混合关系三种搜索策略的头集合跨场景迁移效果
- 干预方式为零消融选定注意力头的输出，无需修改模型原有参数
### 关键结果
在LLaMA-3.1-8B上验证：全局混合搜索得到的共享头干预归一化恢复率达1.464，优于单语义族搜索的1.306，接近单亚型搜索的1.404；全局干预仅使外部干净关系完成的Top3准确率下降1.2%，远低于单亚型干预的10.7%；干预效果迁移随语义相关度梯度变化，同亚型迁移中心恢复率+0.512，同语义族+0.069，跨语义族为-0.054。
### 核心结论
上下文夹带的干预不需要针对每个关系单独优化，优先用异构攻击数据挖掘共享全局靶点，可在降低幻觉的同时最小化对模型正常能力的破坏。
