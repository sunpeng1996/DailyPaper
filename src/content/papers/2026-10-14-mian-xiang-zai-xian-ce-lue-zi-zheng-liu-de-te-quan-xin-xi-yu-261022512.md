---
title: Predicting Privileged Information Effectiveness for On-Policy Self-Distillation
title_zh: 面向在线策略自蒸馏的特权信息有效性预测方法
authors:
- Kaijian Zou
- Emiliano Penaloza
- MohammadHossein Rezaei
- Anisha Gunjal
- Mohit Raghavendra
- Lu Wang
- Yunzhong He
- Anas Mahmoud
affiliations:
- University of Michigan – Ann Arbor
- Mila
- Scale AI
arxiv_id: '2610.22512'
url: https://arxiv.org/abs/2610.22512
pdf_url: https://arxiv.org/pdf/2610.22512
published: '2026-10-14'
collected: '2026-10-21'
category: Agent
direction: Agent训练 · 在线策略自蒸馏优化
tags:
- OPSD
- Privileged Information
- GRPO
- KL Divergence
- Multi-turn Agent
one_liner: 提出两种KL-based离线指标评估OPSD特权信息质量，无需训练即可筛选最优PI，结合GRPO提升多轮Agent性能
practical_value: '- 做Agent自蒸馏时PI优先选包含环境观测、错误分析+可复用策略的高密度格式，避免用纯摘要类压缩提示，效果会差10%以上

  - 筛选PI不要用utility指标（容易被信息泄露干扰），优先用error-step KL contrast指标做预筛选，能减少80%以上无效训练的算力浪费

  - OPSD结合GRPO训练时，前期给OPSD较高权重加速冷启动，当性能plateau后降低OPSD权重甚至移除，避免过拟合和干扰后续优化

  - 训练Thinking类LLM Agent时不要给过密的PI（比如额外的推理轨迹），反而会干扰其已有推理逻辑，效果最多下降16个百分点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy self-distillation（OPSD）无需单独教师模型即可让LLM从特权信息（PI）学习，是多轮Agent训练的常用方法，但现有方案把PI作为固定设计，不同PI格式、来源对性能的影响不明确，每次都训练验证所有候选PI算力成本极高，亟需可离线预评估PI有效性的方法。

### 方法关键点
- 覆盖16种PI配置：包括4类轨迹格式（仅动作/动作+观测/动作+推理/全量轨迹）、3类提示格式（摘要/技能（含错误分析）/检查清单），分别用GLM-5.2、Qwen3.7-Plus、学生模型自身生成
- 提出两种KL-based离线评估指标：1）sampled-token reverse KL（D）：衡量PI对学生采样token的分布偏移幅度；2）error-step KL contrast（Δd−err）：衡量PI是否在错误步骤处更强地抑制学生的错误输出
- 支持OPSD+GRPO加权组合目标，可灵活调整两类训练信号的权重

### 关键实验
在ALFWorld、AppWorld、τ2-retail三个多轮Agent基准上测试Qwen3-4B-Instruct、Qwen3-4B-Thinking、Qwen3-30B-Instruct三个学生模型：
- 全量轨迹类PI相比压缩提示平均提升15%以上pass@1，技能类提示是压缩提示中效果最优的，比纯摘要高5-10个百分点
- Δd−err与训练后性能的Spearman相关性最高达0.94，远优于易受信息泄露干扰的PI utility指标，用Δd−err筛选PI比随机选择最高提升8个点pass@1
- OPSD+GRPO组合目标相比纯GRPO基线在ALFWorld上提升10.17个点pass@1，在τ2-retail上提升6.77个点

### 核心结论
有效PI的核心不是能帮带PI的教师把任务做得多好，而是能否给学生生成瞄准错误的强学习信号。
