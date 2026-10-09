---
title: 'System Switch: When Should a Fast Decision Model Stop and Think?'
title_zh: 系统切换：实时场景下快决策模型触发慢思考的时机研究
authors:
- Gian Luca Bailo
affiliations:
- Independent Researcher, Recco (Genoa), Italy
arxiv_id: '2610.09683'
url: https://arxiv.org/abs/2610.09683
pdf_url: https://arxiv.org/pdf/2610.09683
published: '2026-10-06'
collected: '2026-10-09'
category: Agent
direction: Agent 双系统决策触发优化
tags:
- Dual-Process Agent
- Decision Deferral
- Metacognition
- Real-time Agent
- Confidence AUROC
one_liner: 提出置信度+进展双触发的快慢模型切换机制，在Doom场景验证实时决策效率
practical_value: '- 双系统推荐/广告Agent架构可直接复用：用快模型（小LLM、排序模型）处理全量常规请求，仅将置信度低于阈值、用户行为无进展（如3次点击同品类不转化、停留超30s无动作）的10%~30%请求路由给大模型推理，兼顾
  latency、成本和效果

  - 决策模型选型不要唯准确率论：优先选置信度AUROC高的模型作为快模块，实验中准确率相近的模型置信度区分度差达0.29，直接决定决策deferral的最终收益

  - 实时交互场景（直播推荐、智能导购Agent）可复用进展触发逻辑：检测到用户状态停滞时触发大模型干预，生成探索性推荐/回复，打破行为循环，比持续调用大模型成本低70%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有双系统Agent要么在实时场景下让慢推理模型持续运行，算力成本极高；要么仅在回合制场景下触发切换，无法适配动态变化的实时环境；同时行业对快决策模型的选型通常只关注准确率，忽略其置信度的区分价值。
### 方法关键点
- 架构：快模块采用0.15B~9B参数的System One单步决策模型，承接全量请求输出决策；慢模块采用35B/26B多模态推理模型，仅门控触发时异步调用，输出的计划持续生效直到完成/超时/被中断
- 门控逻辑：两类信号组合触发切换：① 置信度触发：连续3次决策最高概率低于阈值；② 进展触发：卡住、执行失败、行为循环、无新探索四类停滞信号
- 评估范式：离线用900条Doom游戏标注决策样本验证deferral收益，闭环用33局实时Doom游戏验证端到端表现
### 关键结果
- 离线deferral收益与快模型置信度AUROC秩相关达0.87：将30%最低置信度决策路由给推理模型，最高可提升准确率0.15，是随机deferral收益的3倍
- 准确率相近的快模型置信度AUROC差可达0.29，部分高准确率模型的置信度无区分度，deferral收益为0
- 闭环场景下，快慢切换架构比单用快模型地图覆盖度提升27%；门控触发固定探索规则即可达到和调用推理模型相近的覆盖度，后者死亡数降低67%
### 核心结论
快决策模块选型优先看置信度的区分能力，而非单纯的准确率，仅将10%~30%的低置信度/无进展请求路由给大模型即可拿到大部分收益
