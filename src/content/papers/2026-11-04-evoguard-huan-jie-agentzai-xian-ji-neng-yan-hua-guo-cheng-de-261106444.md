---
title: 'EvoGuard: Mitigating Degradation in Online Skill Evolution'
title_zh: EvoGuard：缓解Agent在线技能演化过程中的性能退化
authors:
- Yanli Wang
- Zichen Bai
- Tianyue Jiang
- Kunming Shao
- Junhao Shi
- Xueqin Liu
- Jinguo Sun
- Muye Li
- Tingting Bi
- Yanlin Wang
affiliations:
- JD.Com
- Sun Yat-sen University
- The University of Melbourne
- The Hong Kong University of Science and Technology
arxiv_id: '2611.06444'
url: https://arxiv.org/abs/2611.06444
pdf_url: https://arxiv.org/pdf/2611.06444
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 在线技能演化优化
tags:
- LLM-Agent
- Skill-Evolution
- Pairwise-Preference
- LoRA
- Online-Learning
one_liner: 提出低延迟成对技能选择器，低成本缓解Agent在线技能演化的性能退化
practical_value: '- 电商导购/客服Agent等需要在线迭代技能的业务，可复用这套低开销选择框架，无需每次更新跑全量验证，单forward pass决策延迟极低，适配线上实时场景

  - 偏好分类器训练trick可复用：用基础+专家双源技能池制造效用差足够的样本，再通过拒绝采样过滤模糊对，大幅提升分类准确率，还可缓解LLM Judge位置偏置

  - 仅用LoRA训练选择器无需动基座，训练成本极低，且选择器可跨不同规模的执行器迁移，小参数选择器配大参数执行器的架构适合降本

  - 推荐/广告场景的prompt/话术迭代也可借鉴：每次生成新prompt后用该方法快速判断是否替换，避免单次迭代过拟合导致效果退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent在线技能演化存在3个核心痛点：1）离线多轨迹演化逻辑不匹配线上单任务到达、单次执行的真实部署场景；2）全量接收新技能会导致近42%的劣化技能被采纳，引发技能漂移、效果持续下降；3）每次更新都跑全量验证集的成本远高于任务本身开销，线上完全不可行。

### 方法关键点
- 多源技能池构建：用基础+专家双生成器生成覆盖不同质量的技能，避免单源技能质量范围过窄、缺少有效训练信号
- 效用打标与采样：每个技能在私有测试集上计算效用分，用拒绝采样保留同任务族下效用差≥δ的技能对，消除标注噪声
- 成对偏好训练：用LoRA训练跨编码器，仅优化A/B两个标签token的logit，损失采用Bradley–Terry偏好损失，大幅缓解位置偏置
- 线上推理：仅需一次forward pass判断新旧技能优劣，无额外环境rollout，计算成本极低

### 关键实验
在ALFWorld、ScienceWorld、LiveCodeBench三个基准测试，对比无技能、全量接收、LLM Judge等基线：
1. ALFWorld上对比全量接收新技能，成功率提升11.0%，平均成功率达56.5%，无技能基线仅36.7%
2. ScienceWorld上成功率从10.2%提升至15.3%，LiveCodeBench上pass rate提升2.7%达28.4%
3. 选择器在未见过的技能对的选优准确率达95%，位置一致性达98.3%，几乎无位置偏置

### 核心结论
在线技能迭代的核心矛盾是单次迭代的不稳定性和验证成本的矛盾，通过离线预训练偏好选择器把验证成本一次性摊销，是兼顾效果和效率的可行路径。
