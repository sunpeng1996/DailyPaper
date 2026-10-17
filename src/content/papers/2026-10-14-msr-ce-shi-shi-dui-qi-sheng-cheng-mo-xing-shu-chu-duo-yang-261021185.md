---
title: 'Mine, Sample, Render: Test-Time Diversity Alignment Of Generative Models'
title_zh: MSR：测试时对齐生成模型输出多样性的无训练框架
authors:
- Kostas Triaridis
- Morris E. Sharp
- Nebojsa Jojic
affiliations:
- Stony Brook University
- Microsoft
arxiv_id: '2610.21185'
url: https://arxiv.org/abs/2610.21185
pdf_url: https://arxiv.org/pdf/2610.21185
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: 生成模型 · 测试时多样性对齐
tags:
- Diversity Alignment
- Test-Time Generation
- Attribute Mining
- Generative Model
- Zero Training
one_liner: 无需微调的测试时框架MSR，通过语料属性显式采样引导生成，大幅提升生成多样性且不降低质量
practical_value: '- 电商文案/商品图生成场景可复用MSR三阶段流程：先从历史优质语料挖掘风格、属性维度，按真实分布采样属性组合后引导LLM/文生图模型生成，解决AI内容同质化问题，提升用户新鲜感

  - 推荐系统用户行为模拟器场景，可通过MSR从真实用户交互日志挖掘行为属性，按真实分布采样引导生成用户轨迹，解决模拟用户行为偏离真实分布的问题，提升离线A/B测试、策略预训练可信度

  - Agent驱动的商品3D建模、虚拟展示场景，可复用属性采样+条件渲染的解耦架构，无需微调Agent就能生成符合真实设计分布的多样化3D资产，降低内容生产成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有生成模型单输出质量高，但相同prompt下生成内容同质化严重，RLHF等后训练流程进一步加剧模式坍塌，仅调整温度、要求模型“多样化”无法匹配真实数据的分布特征，无法满足用户模拟器、创意内容生成、Agent设计等场景对输出多样性的要求。

### 方法关键点
- 无训练测试时框架MSR分为三步：1）Mine阶段：分批次对比真实语料样本，用LLM挖掘可解释的属性schema，合并同义属性后对全语料标注得到属性共现矩阵；2）Sample阶段：基于共现矩阵，通过主题采样/祖先采样/混合采样方式，结合用户prompt匹配特征，采样得到属性组合；3）Render阶段：将属性组合加入prompt，引导生成模型作为条件渲染器输出结果
- 采样阶段动态调整条件集合避免数据稀疏问题，支持显式固定指定属性（如电商场景固定商品品类），其余属性按真实分布采样

### 关键结果数字
跨5个场景验证效果：1）天气报告生成：较纯prompt基线Forward KL从0.57降至0.18，覆盖度从21%升至68%；2）用户模拟：较纯prompt基线KL最高降低43%，真实行为簇覆盖度最高提升116%；3）网页生成：多样性指标Vendi Score最高提升89%；4）文生图：DINOv2 Vendi Score较prompt改写基线最高提升57%；5）Agent 3D折叠椅生成：多样性远超基线且质量从70.8提升至83.55，无质量下降

### 核心结论
将生成的“属性分布采样”和“内容渲染”解耦，用真实语料的统计特征引导生成，是无需微调解决生成内容同质化的高效路径
