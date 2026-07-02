---
title: Autonomous Scientific Discovery via Iterative Meta-Reflection
title_zh: 基于迭代元反思的自主科学发现框架DiscoPER
authors:
- Bingchen Zhao
- Sara Beery
- Oisin Mac Aodha
affiliations:
- University of Edinburgh
- Massachusetts Institute of Technology
arxiv_id: '2607.01131'
url: https://arxiv.org/abs/2607.01131
pdf_url: https://arxiv.org/pdf/2607.01131
published: '2026-06-30'
collected: '2026-07-02'
category: Agent
direction: 自主Agent · 迭代元反思开放式探索
tags:
- LLM Agent
- Meta-Reflection
- Autonomous Discovery
- Multimodal
- Statistical Validation
one_liner: 提出无预设目标的多模态自主科学发现框架，基于元反思引导探索并通过统计检验保障结果可信
practical_value: '- 元反思机制可直接迁移到推荐系统的兴趣挖掘链路：定期聚合已挖掘的用户兴趣、物品关联规则，识别未探索的特征维度、混淆变量（如地域/季节的调节作用），引导后续召回/探索策略，避免重复推荐和信息茧房

  - 双拆分统计检验机制可复用在电商新策略/新物料的效果验证：训练拆分调优分析规则，验证拆分仅执行一次检验，避免p-hacking导致的假阳效果，减少线上放量风险

  - 多模态特征自动关联的思路可用于商品规则挖掘：调用VLM从商品图文提取风格、场景等未入库特征，自动关联用户下单的地域、季节、人群属性，挖掘新的可落地推荐规则'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自主科学发现系统普遍存在三大局限：要么搜索空间受限于预设的变量关联范式，要么需要人工指定初始研究目标，要么仅独立生成单步假设、无法聚合已有发现挖掘复杂高阶关联，难以实现真正的无干预开放式探索。
### 方法关键点
- 核心采用**PROPOSE-EVALUATE-REFLECT**三段迭代框架，无需预设研究目标，支持全开放式探索
- PROPOSE模块由LLM Agent基于数据schema、历史发现集、元反思引导信息生成可执行的假设检验代码，支持调用VLM提取图像等多模态特征扩展分析维度
- EVALUATE模块采用训练/验证双拆分统计检验，假设需同时在两个拆分上满足效应量≥0.2、p≤0.05、效应量衰减不超过40%才会被纳入可信发现集，从机制上避免p-hacking
- REFLECT模块每5轮迭代聚合所有已接受/拒绝的假设，识别探索缺口、混淆变量、潜在高阶关联，生成非强制性引导信息指导下一轮探索
### 关键实验
在自建的iNatDisco生态多模态基准（标注了已发表的生态规律作为ground truth）上对比经典因果发现、带外部引导的LLM基线：
- iNatDisco-800数据集上恢复9个已知规律中的8个，假设支持率达72.7%，比无元反思版本召回提升1/9
- iNatDisco-50K数据集上恢复12个已知规律中的8个，假设支持率达74.2%，比无元反思版本召回提升2/12
### 核心结论
AI辅助探索类系统的核心竞争力不仅是生成单个合理假设，更要具备聚合已有证据动态调整探索方向的元反思能力
