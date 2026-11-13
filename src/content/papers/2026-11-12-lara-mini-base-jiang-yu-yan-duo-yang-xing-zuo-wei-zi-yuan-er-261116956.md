---
title: 'Lara Mini Base: Language Diversity as a Resource, Not a Trade-off'
title_zh: 《Lara Mini Base：将语言多样性作为资源而非性能权衡》
authors:
- Translated
- Maria Pia Adinolfi
- Isabelle Andrieu
- Grazia Fiorella Anfuso
- Melania Annunziata
- Daniele Antonini
- Marta Arena
- Luca Barone
- Dana Barras Franco
- Francesca Basiricò
affiliations:
- Translated
arxiv_id: '2611.16956'
url: https://arxiv.org/abs/2611.16956
pdf_url: https://arxiv.org/pdf/2611.16956
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 多语言小参数量MoE LLM基座优化
tags:
- MoE
- Multilingual LLM
- Long Context
- Base Model
- Parameter Efficient
one_liner: 推出总参7.2B/活参0.6B的多语言MoE基座，在2B活参以下开源模型中综合性能登顶，支持128k上下文
practical_value: '- 跨地域多语言电商/广告推荐场景的Agent可直接复用该开源模型：覆盖45种语言（含所有欧盟官方语言），活参仅0.6B，推理成本远低于同性能大模型，小语种理解效果优于同规模英语单语模型

  - 训练多领域/多语言小模型可复用其MoE路由设计：不同语言共享中间层专家，避免容量竞争，无需为单语言单独拆分模型，大幅降低训练和部署成本

  - 预训练课程学习策略可直接迁移：训练后期逐步提升高质量数据、QA/代码/数学数据占比，同时提升非英语数据占比，仅损失0.3点英语性能即可换取2.7点多语言性能提升，适合跨语言业务的模型增量训练

  - 长上下文扩展trick可复用：仅用1.7%的额外训练token做续训，几乎不损失短上下文性能即可将窗口从4k拉到128k，适合处理长用户行为序列、长商品描述的推荐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前开源小参数量通用LLM的非英语预训练数据占比最高仅12%，专门的多语言小模型性能远低于同规模通用单语模型；行业普遍认为小模型下不同语言会争抢容量，多语言训练会损失通用性能，亟需探索小参数量下兼顾多语言能力和通用性能的落地方案。
### 方法关键点
- 架构：采用MoE设计，总参7.2B、单token活参仅0.6B，每层含128个路由专家+1个共享专家，每token激活top4专家；混合部署Gated DeltaNet、滑动窗口注意力、全局注意力，仅7层用全局注意力，大幅降低长上下文推理内存开销
- 数据：预训练共6T token，英语占比仅41%，覆盖44种其他语言（含所有欧盟官方语言）；三阶段课程学习，训练后期非英语数据占比超过英语，97%的训练token为首次读取的非重复数据；额外用100B token（占总训练量1.7%）做长上下文续训，将窗口扩展到128k
- 训练：采用Muon+AdamW混合优化器，比纯AdamW少用33%~47%的token即可达到相同训练损失，加入z-loss、负载均衡loss保障训练稳定性
### 关键结果
在2B活参以下的36个开源基座模型中，综合基准得分57.0，比第二名高3.1分，性能超过训练token量多4~6倍的同规模模型；多语言基准得分56.7，比第二名高3.4分；英语基准得分66.4，仅比同组第一名低2分；单A100无量化推理速度比所有更高分模型快至少1.8倍。
### 核心结论
小参数量多语言训练不需要做性能权衡，通过合理的MoE架构和数据配比，多语言数据不仅不会损失通用性能，反而能提升模型的整体表征能力。
