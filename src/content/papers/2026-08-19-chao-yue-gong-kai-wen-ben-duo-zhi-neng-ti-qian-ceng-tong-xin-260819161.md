---
title: 'Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent
  Communication'
title_zh: 超越公开文本：多智能体潜层通信中的隐式协作检测
authors:
- Ramneet Kaur
- Pradyumna Chari
- Ramesh Raskar
- Jugad Singh
- Sumit Kumar Jha
- Anirban Roy
affiliations:
- SRI International
- MIT Media Lab
- University of Florida
- Westtown School
arxiv_id: '2608.19161'
url: https://arxiv.org/abs/2608.19161
pdf_url: https://arxiv.org/pdf/2608.19161
published: '2026-08-19'
collected: '2026-08-20'
category: MultiAgent
direction: 多智能体 · 潜层通信治理与合谋检测
tags:
- MultiAgent
- CollusionDetection
- LatentCommunication
- LLMGovernance
- AnomalyDetection
one_liner: 提出仅学习正常通信模式的VLA框架，可检测和干预多智能体潜层隐式合谋行为
practical_value: '- 电商多Agent竞价/议价场景可复用VLA的三层无监督检测逻辑，无需标注合谋样本即可识别异常Agent交互，降低黑产合谋风控成本

  - 平台侧管控多Agent生态时可借鉴「黑盒prompt干预+白盒潜层替换」的分级干预策略，根据对第三方Agent的权限灵活选择管控方式

  - 跨模型族Agent交互的适配方案可迁移到异构大模型混合调度的推荐系统，解决不同基座特征对齐问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM驱动的多智能体系统采用潜层连续状态传递替代文本通信，可降低50%-80%token消耗、提速3-7倍，但这类通信内容不进入公开转录文本，合谋等有害协作无法被常规审计发现；现有监督式检测探针依赖攻击样本标注，对未知攻击鲁棒性差，无法满足多智能体生态治理需求。
### 方法关键点
- 所有潜层交互绑定唯一事件ID，精准关联潜层通信记录与Agent后续公开行为，支持因果归因分析
- 三层无监督监测器仅用正常通信样本训练：1）上下文高斯分布对比，计算潜层特征异常分；2）反事实动作分布比对，仅对潜层带来的有害方向偏移打分；3）稀疏自编码器识别正常通信中从未出现的稀疏特征，提供可解释性支撑
- 分级干预策略：黑盒场景注入合规性prompt引导行为，白盒场景直接替换为匹配的正常潜层状态，支持混合权限场景的分配式干预
- 异构模型适配层仅用正常交互样本训练，对齐不同基座的潜层空间，支持跨模型族交互检测
### 关键结果
- 受控拍卖基准测试中，同构Agent合谋检测AUROC均值达0.993，异构Agent达0.854
- 100个竞价Agent场景下，仅需监控0.202%的定向交互对即可维持AUROC≥0.917，算力开销极低
- 全白盒干预可实现100%竞价分布恢复，合谋低出价行为降低47.3个百分点；白盒占比从25%提升到75%时，分布恢复率从34.7%提升至93%
> 最值得记住：针对未知攻击的治理优先学习正常行为模式而非枚举攻击，通过因果关联和分级干预可在低开销下实现有效管控
