---
title: 'Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated
  Real-Time Monte Carlo Engine'
title_zh: Pitwall：基于校准实时蒙特卡洛引擎的高忠实度自然语言赛车策略简报系统
authors:
- Juan S. Santillana
affiliations:
- Independent Researcher
arxiv_id: '2607.06495'
url: https://arxiv.org/abs/2607.06495
pdf_url: https://arxiv.org/pdf/2607.06495
published: '2026-07-07'
collected: '2026-07-08'
category: LLM
direction: 大模型忠实生成 · 实时接地生成
tags:
- Grounded Generation
- Fact Verification
- Hallucination Mitigation
- Monte Carlo Simulation
- Real-time Generation
one_liner: 提出架构内嵌事实校验的实时生成系统，可输出高忠实度多语言F1赛事策略简报
practical_value: '- 可将事实校验升级为架构级能力而非后处理：电商生成商品文案、直播话术、营销活动通知时，将输出拆分为价格、参数、权益等类型化fact
  claim，与商品库/实时库存/规则库逐一校验后再发布，从根源避免虚假宣传

  - 微调数据可通过统一校验器做过滤：不满足事实要求的样本直接替换为可证忠实的模板生成样本，避免大模型在微调阶段学习到幻觉内容，可复用在商品文案、个性化推荐话术微调场景

  - 稀疏上下文场景需单独审计选型：当输入状态信息少（如冷启动用户、刚上架无行为商品的推荐话术生成）时，幻觉风险显著提升，需针对性做base模型选型和稀疏场景专项测试'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
实时赛事解说类生成属于强时效性接地生成任务，状态每秒动态更新、生成时无参考文本，现有方案普遍存在幻觉风险，忠实度无法得到刚性保障

### 方法关键点
1. 架构内置事实校验模块：每个生成句子拆解为位置、差距、轮胎、pace、overtakes等类型化事实claim，与实时Monte Carlo引擎输出的概率化赛事状态逐一校验，未通过则切换为忠实模板兜底输出
2. 校验器复用于微调数据过滤：仅保留所有claim均符合状态的训练样本（占总模型生成样本的81.9%），其余样本替换为模板生成结果，确保模型从未接触未接地训练数据
3. 底层搭载校准后的向量化Monte Carlo引擎：每圈生成2000种赛事延续预测，基于2018-2024年126场赛事校准，2025-2026年全留空赛季验证

### 关键结果数字
- 留空测试集赛事预测胜者进入TOP3准确率90.3%，Brier得分0.0745
- 2026年奥地利、英国F1大奖赛全链路实跑验证通过，银石站提前10圈锁定最终胜者
