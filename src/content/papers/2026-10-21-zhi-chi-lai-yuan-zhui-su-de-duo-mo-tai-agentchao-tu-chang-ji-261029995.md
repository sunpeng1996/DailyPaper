---
title: 'Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal
  Agents'
title_zh: 支持来源追溯的多模态Agent超图长时记忆框架MHG-Mem
authors:
- Jielong Tang
- Ling-An Zeng
- Xujie Yuan
- Xiao Dong
- Zhiqian Xia
- Qingfeng Li
- Shixiong Kai
- Kaichao Liang
- Rong Yao
- Jian Yin
affiliations:
- Sun Yat-sen University
- Huawei Noah's Ark Lab
- Shandong Normal University
- Southeast University
arxiv_id: '2610.29995'
url: https://arxiv.org/abs/2610.29995
pdf_url: https://arxiv.org/pdf/2610.29995
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 多模态Agent · 长时记忆结构设计
tags:
- Multimodal Agent
- Long-term Memory
- Hypergraph
- Provenance Tracking
- Agentic Search
one_liner: 提出带三类可追溯超边的多模态超图记忆框架，跨基准较最强基线提升8.20~9.98%
practical_value: '- 电商导购Agent的用户交互记忆可复用这套三层节点+三类超边的架构，绑定商品实体、浏览/交互事实、价格/库存演化状态，既保留商品原图、详情页截图等原始证据，又能跨会话跟踪同个商品的状态变化，解决用户问「之前看的那款背包有没有降价」这类历史查询的准确性问题

  - Agent记忆检索可借鉴自适应Agentic Search设计，根据查询类型灵活选择入口层：查属性细节直接走事实层搜原图，查历史变化走演化层看状态序列，无需固定单一路径，平衡检索效率与准确率

  - 多模态实体对齐可复用文本+视觉区域相似度加权打分的trick，匹配同实体的跨会话不同提及，解决不同截图/不同场景下同个商品的实体关联问题，避免将相似款误判为同一款'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态Agent长时记忆存在两类显著缺陷：基于抽象的记忆将图像压缩为文本描述，丢失拉链样式、商品外观等细粒度视觉信息，无法满足细节查询需求；像素保留类记忆虽存储原始观测，但无法关联同个实体的跨会话异构观测，无法跟踪商品价格、库存等状态的时序演化，两类方案均无法支撑复杂跨会话多模态交互场景。
### 方法关键点
- 三层节点架构：FactNode存储带原图、会话时间元数据的原子观测；EntityNode存储文本/视觉实体提及；EvolutionNode存储实体属性的时序演化状态
- 三类超边绑定关联：Occurrence超边关联同实体的所有提及和对应事实；Evolutionary超边关联演化状态与对应实体；Evidential超边关联演化状态与支撑事实，全链路保留来源追溯能力
- 自适应Agentic检索：根据查询类型自适应选择实体/演化/事实层作为检索入口，跨层遍历超边，需细粒度验证时直接溯源原始观测
### 关键实验
在MemEye、Mem-Gallery、WorldMemArena-S三个多模态记忆基准测试，覆盖Qwen3-VL-8B、GPT-4.1-mini、Qwen3.8-27B三类骨干模型，较最强基线平均LLM-Judge得分提升8.20%~9.98%；其中时序推理任务相对提升最高达39%，视觉细粒度查询准确率提升15%以上，记忆召回、正确性、检索覆盖度均为所有对比方案最优。
> 最值得记住的一句话：多模态长时记忆的核心不是单纯提升存储容量，而是要结构化关联同实体的跨模态跨会话观测，同时保留每个结论到原始证据的追溯链路，才能同时满足细粒度验证和跨会话演化推理需求。
