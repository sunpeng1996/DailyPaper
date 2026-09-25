---
title: Self-Evolving Multimedia Verification through Memory Consolidation of Contestation
  Experiences
title_zh: 基于争议经验记忆整合的自演进多媒体验证框架
authors:
- Truong Thanh Hung Nguyen
- Vo Thanh Khang Nguyen
- Hoang-Loc Cao
- Phuc Ho
- Truong Thinh Nguyen
- Van Pham
- Hung Cao
affiliations:
- University of New Brunswick
- FPT Software
- University of Science and Technology of Hanoi
arxiv_id: '2609.27175'
url: https://arxiv.org/abs/2609.27175
pdf_url: https://arxiv.org/pdf/2609.27175
published: '2026-09-23'
collected: '2026-09-25'
category: MultiAgent
direction: 多智体自演进 · 可验证记忆整合
tags:
- MultiAgent
- SelfEvolution
- MemoryConsolidation
- ContestableAI
- MultimediaVerification
one_liner: 提出多Agent自演进多媒体验证框架SEMV，融合因果争议修正与验证门控记忆提升验证效果
practical_value: '- 多Agent系统的人类反馈路由设计可直接复用：将用户异议定位到最早依赖节点，仅重算下游依赖链路，实测可节省52.8%算力，适合电商大模型客服、内容审核场景的用户反馈快速迭代

  - 验证门控记忆整合机制可迁移到生成式推荐/广告系统：经验入库前必须经过来源、正确性、适用范围三重校验，仅沉淀多案例交叉验证的规则，可将记忆负迁移率从5.7%降至0.2%

  - 可争议AI的决策回溯架构可直接借鉴：将所有决策拆解为「证据-论点-主张」的全链路可追溯结构，每个节点保留来源凭证，适合电商虚假内容治理、广告素材合规审核的溯源需求'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多媒体验证系统普遍缺乏中间推理修正机制，人类反馈仅能作用于最终输出，经验复用无校验容易出现负迁移，无法满足开放场景下验证决策可追溯、可修正、可争议的核心要求。
### 方法关键点
- 多Agent协作的SEMV框架：以带完整来源的论点为核心接口，串联证据感知、推理、人类争议、记忆复用全链路
- 自适应因果争议机制：将人类修正路由到最早受影响的流水线阶段，仅重算下游依赖锥，保留独立结果降低算力开销
- 验证门控自演进记忆：经验需要经过来源校验、多案例合并、冲突留存三步才能进入长期记忆库，仅在适用范围内复用，避免跨场景负迁移
### 关键实验结果
在COSMOS基准数据集上，SEMV最高准确率达91.88%，比最强基线提升2.78个百分点；验证门控记忆将负迁移率从5.7%降至0.2%；在自研CTR争议修正数据集上，细粒度因果修正可纠正96.7%的初始错误，同时节省52.8%的计算量。
### 核心洞察
不需要微调模型参数，仅通过非参数化的验证门控记忆整合+细粒度因果修正，就能实现AI系统的安全自演进，同时保持决策全链路可追溯。
