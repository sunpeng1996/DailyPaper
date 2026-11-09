---
title: 'ENGRAM: From Agent Experience to Weights through Verified Consolidation'
title_zh: ENGRAM：经验证的Agent经验到模型权重整合框架
authors:
- Ruiyi Yang
- Zechen Li
- Lihuan Li
- Du Yin
- Hao Xue
- Flora D. Salim
affiliations:
- University of New South Wales
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.09472'
url: https://arxiv.org/abs/2611.09472
pdf_url: https://arxiv.org/pdf/2611.09472
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 记忆管理与自进化优化
tags:
- LLM Agent
- Memory Management
- LoRA
- Self-Evolution
- Verified Consolidation
one_liner: 分离训练准入与内存释放决策，兼顾Agent性能提升与检索存储成本降低
practical_value: '- 电商导购Agent、搜索Query改写Agent可复用演示感知准入机制：除Agent自身成功经验外，可纳入人工标注的优质示范作为LoRA训练数据，解决低熟练度技能无训练样本的问题

  - 推荐/搜索系统的RAG记忆库裁剪可复用验证释放逻辑：对每个技能/类目，对比微调后无检索的模型性能与原模型带检索的性能，达标即可移除对应检索记录，降低RAG检索时延和存储成本，实测该方法相比随机释放可提升3.3个F1点

  - 多技能Agent部署可采用技能级路由方案：不同技能独立控制是否启用LoRA适配器、是否开启检索，在保证性能的前提下降低输入token消耗，实测ALFWorld场景下可减少42.8%输入token'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent同时依赖外部检索记忆和参数更新两类经验复用方式，但存在两个核心痛点：仅基于模型当前熟练度的训练准入规则会错过优质教师示范；训练后直接删除检索记录会导致模型尚未完全掌握的技能失去外部支撑引发性能下降，而全量保留检索记录会带来过高的存储、检索时延和token成本。

### 方法关键点
- 双门控决策机制：训练准入门同时考虑模型当前熟练度和成功教师示范数量，满足任意条件即可将对应技能纳入LoRA训练集，扩大训练样本来源
- 构建Engram Trace Graph (ETG) 按技能、结果、来源结构化组织经验轨迹，为训练提供上下文支撑
- 内存释放前先验证：对比微调后无检索的候选模型与原模型带检索的性能，同时满足相对阈值（不低于原带检索性能的可接受范围）和绝对阈值（达到最低性能要求），才可删除对应技能的检索记录
- 部署时按技能路由，达标技能用微调权重无检索，未达标技能保留检索辅助

### 关键实验
在Crafter、ALFWorld、WebShop等交互任务和HotpotQA、FinQA等推理任务上测试，对比MAGE、EDGE、SkillRL等SOTA基线：ALFWorld任务成功率达90.3%，超基线最高的SkillRL 0.4个百分点；HotpotQA F1达71.5%，超次优EmbQA 15.7个百分点；验证释放相比全量保留记录仅下降0.2个F1，检索记录减少55.2%；相比相同存储预算的随机释放，F1提升3.3个百分点。

**最值得记住的一句话**：Agent经验整合中，训练准入和记忆释放是两个独立决策，不能默认训练完成就可以删除外部检索记忆，必须经过性能验证才能保证业务效果。
