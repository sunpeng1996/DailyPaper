---
title: 'AutoAssumption: Searching over Assumptions Discovers ML-Systems Algorithms'
title_zh: AutoAssumption：基于假设空间搜索的ML系统算法自动发现框架
authors:
- Igor Sadalski
- Minghao Guo
- Benjamin Jones
- Wojciech Matusik
affiliations:
- MIT CSAIL
arxiv_id: '2611.14844'
url: https://arxiv.org/abs/2611.14844
pdf_url: https://arxiv.org/pdf/2611.14844
published: '2026-11-10'
collected: '2026-11-13'
category: Agent
direction: Agent 算法自动发现 · 形式化证明
tags:
- Agent
- Formal Verification
- KV Cache
- Model Pruning
- Algorithm Discovery
one_liner: 将现有算法转为带显式假设的可校验证明图，通过修改假设自动发现SOTA ML系统算法
practical_value: '- 业务策略迭代时可将现有推荐/广告的召回、排序策略拆解为显式假设集合，每次仅修改单条假设验证效果，彻底解决多变量耦合的效果归因难题

  - 可复用「形式化证明→代码映射→单假设修改」的迭代框架，针对业务规则类逻辑做正确性校验，避免上线后出现逻辑漏洞

  - 做LLM推理服务的业务团队可直接复用本文产出的SOTA KV-cache eviction、权值剪枝算法，降低大模型推理的时延和算力成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有ML系统算法迭代多基于代码修改，单次代码变更往往耦合多个设计决策，效果归因难度大；且已有算法的隐含假设未被显式沉淀，算法创新高度依赖专家经验，门槛高、迭代效率低。
### 方法关键点
- 构建覆盖KV-cache eviction、推测解码、LLM权值剪枝3个领域共89个公开算法的证明图库，每个算法被拆解为<假设-定义-定理>构成的有向无环图，所有证明通过Lean形式化校验，且保证每行代码与证明节点一一映射
- AutoAssumption框架每次仅修改证明图中的1条假设，自动推导受影响的定理节点、重新生成可执行代码，经证明校验通过后再进入性能评测环节，大幅减少无效GPU算力浪费
- 搜索过程基于benchmark性能反馈迭代选择最优父算法和待修改假设，优化方向可解释、可控
### 关键结果
- KV-cache eviction方向：生成的RestoreKV GM算法在RULER-4K基准上得分75.7，超过已有SOTA KVGrad的74.1，16×~32×高压缩比场景下较父算法最高提升12.0分
- LLM权值剪枝方向：生成的Pruner-Zero LG算法在4个LLaMA模型上的剪枝困惑度均为最低，LLaMA-7B 50%稀疏度下困惑度仅为稠密模型的1.195倍，优于父算法Pruner-Zero的1.213
- 和OpenEvolve、AIDE等代码级搜索框架对比，相同预算下得分仅比OpenEvolve低0.4分，重复实验标准差仅0.75，远低于OpenEvolve的1.39和AIDE的4.09，结果稳定性更强

**最值得记住的一句话**：算法创新的核心单元不是代码行，而是隐含在设计中的可被推翻的假设
