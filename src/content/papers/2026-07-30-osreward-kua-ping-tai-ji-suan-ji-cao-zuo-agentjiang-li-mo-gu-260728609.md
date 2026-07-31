---
title: 'OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use
  Reward Models'
title_zh: OSReward：跨平台计算机操作Agent奖励模型标准化评估基准
authors:
- Qiushi Sun
- Kanzhi Cheng
- Yian Wang
- Bowen Yang
- Hang Yan
- Liheng Chen
- Fangzhi Xu
- Zichen Ding
- Nuo Chen
- Jialin Cao
affiliations:
- 香港大学
- 南京大学
- 新加坡国立大学
- 中国科学技术大学
- 西安交通大学
arxiv_id: '2607.28609'
url: https://arxiv.org/abs/2607.28609
pdf_url: https://arxiv.org/pdf/2607.28609
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: Agent 操作轨迹奖励模型评估与开源实现
tags:
- Computer-Using-Agent
- Reward-Model
- VLM-Judge
- Benchmark
- Open-Source
one_liner: 发布跨平台CUA轨迹评估基准和低成本开源奖励模型OS-Shepherd，填补可靠性与成本的空白
practical_value: '- 构建电商操作类Agent（如自动化运营、导购闭环Agent）的奖励数据集时，可复用「多强模型一致标注+过滤歧义样本」的弱监督构造方法，大幅降低人工标注成本

  - 训练VLM judge时可针对性加入假成功轨迹作为hard negative，优先修正共性leniency bias，能以最低成本提升评估准确率

  - 评估Agent轨迹时优先保留全量text历史（动作、思考过程），仅需保留最后5-9帧截图即可，视觉特征对判决影响极小，可大幅降低推理算力开销

  - OS-Shepherd开源奖励模型可直接二开，作为电商领域Agent RL训练的奖励信号，成本比商用API低30~60倍，可支撑规模化训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
计算机操作Agent（CUA）的轨迹完成度校验是评估、数据治理、RL训练的核心环节，人工标注和规则校验无法覆盖规模化生产场景，当前主流的VLM judge可靠性未被系统验证，高准确率商用模型成本过高，开源模型效果差距显著，缺乏兼顾可靠性与低成本的落地方案。

### 方法关键点
- 构建OSReward基准：覆盖Web、Windows、Ubuntu、Mobile四大平台，包含1019条多阶段人工金标长轨迹，拆分出OSReward-Hard（284条难例，侧重假成功场景）、OSReward-Multi（细粒度效率、对齐度打分）子集
- 系统评估27款主流VLM judge的表现，验证共性leniency bias（宽待失败、漏判假成功），定位判决核心依赖轨迹的text历史（动作、思考过程），视觉输入对结果影响极小
- 构造OS-Shepherd-100K训练集：基于多强模型共识标注过滤歧义样本，包含100K带推理标注的轨迹数据，通过SFT+GRPO两阶段训练得到9B/35B开源奖励模型

### 关键结果
- 商用SOTA VLM在OSReward全集准确率最高达89.7%，但在OSReward-Hard上骤降至69.7%，平均准确率仅52%，普遍漏判假成功轨迹
- OS-Shepherd-35B在OSReward-Hard上准确率达62.7%，表现接近商用中高级VLM，成本仅为前沿商用模型的1/30~1/60，可支撑规模化RL训练

### 核心结论
VLM judge对CUA轨迹的判决核心依赖文本历史而非视觉信息，优先修正宽待假成功的bias，小参数开源模型即可达到接近商用模型的高性价比
