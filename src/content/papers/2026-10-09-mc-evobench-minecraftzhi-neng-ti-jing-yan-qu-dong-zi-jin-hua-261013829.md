---
title: 'MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents'
title_zh: MC-EvoBench：Minecraft智能体经验驱动自进化能力审计基准
authors:
- Jingwei Song
- Zhisheng Chen
- Bingfan Zeng
- Jing Tang
- Yubo Hou
- Jinhao Jing
- Zhengwei Xie
- Linfeng Zhang
affiliations:
- Shanghai Jiao Tong University
- University of the Chinese Academy of Sciences
- South China University of Technology
- Huazhong University of Science and Technology
- Beihang University
arxiv_id: '2610.13829'
url: https://arxiv.org/abs/2610.13829
pdf_url: https://arxiv.org/pdf/2610.13829
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: 具身Agent · 自进化能力评估
tags:
- Embodied Agent
- Benchmark
- Self-Improvement
- Transfer Learning
- Evaluation
one_liner: 构建受控Minecraft基准测试集，可隔离评估具身智能体的可迁移持续进化能力
practical_value: '- 做Agent能力迁移评估时，可借鉴「源/目标任务环境隔离、仅允许指定Agent产物跨边界」的设计，排除资源携带等干扰因素，提升评估可信度

  - 多场景推荐系统的迁移效果评估，可参考其「无先验/相关/无关/打乱输入」的对照实验设计，精准量化迁移增益的显著性

  - 长期进化类Agent的能力审计，可复用其「任务状态分阶段校验、多种子重复实验置信区间校验」的方法，避免偶发成功误判能力提升'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有具身Agent评估仅关注最终任务结果，无法区分真正的可复用能力获取、资源携带、环境差异、执行偶发失败等干扰因素，无法支撑经验驱动自进化能力的精准审计。

### 方法关键点
1. 构建MC-EvoBench基准，包含19条进化链（12条主评估链+7条校准探针链）、3组图对齐的迁移探针对；
2. 采用任务状态图建模、分阶段环境校验、源目标任务环境重置、仅允许指定Agent产物跨边界的控制设计；
3. 设计4组对照实验，固定环境步数预算+5次随机种子重复，用TSR、WGP、VMP三个指标量化结果。

### 关键结果数字
1. 带规划器的Agent对比纯控制器Agent存在稳定的能力差距；
2. 相关经验未带来稳定迁移增益：工具类探针无提升，木材类小增益仅依赖单一种子，所有增益置信区间均包含零点；
3. 早期资源收集/合成瓶颈会导致70%以上的后续能力无法被有效观测。
