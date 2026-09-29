---
title: Reinforcing Agentic Creativity in Scientific Ideation with Night Science
title_zh: 引入夜间科学范式强化智能体的科研创意生成能力
authors:
- Priyanka Kargupta
- Silviu Cucerzan
- Shweti Mahajan
- Allen Herring
- Jiawei Han
- Ryen W. White
- Sujay Kumar Jauhar
affiliations:
- University of Illinois Urbana-Champaign
- Microsoft
- Microsoft Research
arxiv_id: '2609.35706'
url: https://arxiv.org/abs/2609.35706
pdf_url: https://arxiv.org/pdf/2609.35706
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent · 创造力对齐与RL优化
tags:
- Agentic Creativity
- GRPO
- Reinforcement Learning
- Scientific Ideation
- LLM Agent
one_liner: 基于GRPO的三层创造力对齐框架提升科研智能体的创意多样性与成果影响力
practical_value: '- 电商/推荐领域的创意生成类Agent（营销文案、新品策划、推荐理由生成、活动idea）可直接复用三层创造力框架：给检索、联想、改写等工具定义1-5级创意程度（比如检索从同品类匹配到跨品类跨界联想），让Agent自主选择动作与创意等级，效果远优于单纯调解码温度

  - 开放式生成任务的RL优化优先使用最终业务结果奖励（如文案点击率、创意采纳率），可兼顾多样性与实用性；若需更强原创性可叠加过程奖励，需接受一定程度的实用性下降

  - 训练初期加入随机高创意动作替换策略，可避免Agent陷入局部最优，探索更多未覆盖的创意方向，可直接复用在生成式推荐、营销创意Agent的冷启动训练阶段'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM存在低熵输出偏见，开放式创意生成任务易产出同质化、可预测结果，仅调高解码温度只能增加随机性，无法可控生成兼具新颖性与实用性的创意；过往科研Agent框架仅将创意视为结果属性，未覆盖推理过程中「何时、如何」发挥创意的决策逻辑。
### 方法关键点
- 三层创造力建模：行动层为检索、跨域辩论、假设反转等每个动作定义1-5级语义化创意等级（从常规执行到高度探索）；流程层由Agent根据推理轨迹自主选择切换高低创意动作的时机；结果层从新颖性、可行性、相关性三个维度评估产出。
- 基于GRPO做RL优化，核心奖励仅针对最终产出的原子化拆解结果，训练初期加入概率性随机动作swap引导探索，可选叠加过程奖励进一步提升原创性。
### 关键实验
基于NSF 2018年后491个科研基金项目标题数据集，对比零样本、调温、ReAct等基线，14B版本较基线提升预测引用影响力32.0pp、原创性66.2pp，研究方向覆盖度提升27.8%、贡献类型覆盖度提升14.9%，上述增益无法通过单纯调高解码温度复现。
### 核心结论
创造力不是单纯的采样随机性，而是可学习的多层级推理能力，语义级创意引导的效果远优于盲目增加输出噪声。
