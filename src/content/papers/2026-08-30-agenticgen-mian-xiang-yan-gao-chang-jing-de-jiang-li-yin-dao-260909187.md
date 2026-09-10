---
title: 'AgenticGen: Reward-Guided Agentic Video Generation for Advertising'
title_zh: AgenticGen：面向广告场景的奖励引导智能体视频生成框架
authors:
- Xingyuan Bu
- Chengru Song
- Hao Zhou
- Tao Zhou
- Dong Li
- Wei Li
- Shilong Li
- Hao Shi
- Yongxin Guo
- Donghao Zhou
affiliations:
- ByteDance
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2609.09187'
url: https://arxiv.org/abs/2609.09187
pdf_url: https://arxiv.org/pdf/2609.09187
published: '2026-08-30'
collected: '2026-09-10'
category: GenRec
direction: 生成式广告 · 奖励引导智能体优化
tags:
- Agentic Generation
- Advertising Video Generation
- Reward Modeling
- DPO
- GRPO
- Online Feedback Optimization
one_liner: 提出奖励引导的智能体广告视频生成框架，拆为两阶段推理，结合业务反馈迭代提转化
practical_value: '- 广告/电商创意生成场景可复用两阶段拆分思路：将创意范式选择与执行草稿生成解耦，两个阶段分别对齐业务反馈做优化，比端到端生成可解释性更强、优化目标更明确，避免黑盒优化的不可控问题

  - 业务数据噪音大的场景，可参考「impression-balanced流量分配」机制：固定商品上下文、平衡同组素材曝光量，构造无偏的pairwise训练样本，论文显示该方案比直接用点wise
  CTR训练奖励模型准确率高近8%

  - 多目标优化可复用「DPO暖启动+GRPO在线迭代」的路径：先基于历史反馈用DPO快速对齐业务偏好，再用GRPO融合过程奖励（中间决策的规则/先验）和结果奖励（业务指标+人工质量规则），兼顾业务效果和内容质量，避免生成clickbait等低质内容

  - 奖励模型特征工程可参考：除原始内容特征外，加入业务特有结构化特征（比如广告的hook、CTA、卖点字段），论文显示该操作可提升奖励模型准确率1.49%，性价比极高'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频基础模型仅能生成视觉合理的内容，无法针对广告场景的核心业务目标（CTR、CVR）优化，也无法打通线上投放反馈的迭代闭环，导致生成的广告视频转化效果差，还易出现clickbait、画面瑕疵等质量问题，难以满足工业化投放需求。
### 方法关键点
- 框架拆解为两个可训练推理阶段：策略选择阶段基于商品信息、素材包从预设创意策略库（素材编辑、参考引导生成、跨素材混剪三类）筛选可行策略组；草稿生成阶段将策略转化为结构化可执行草稿，调用视频生成、渲染工具产出最终广告。
- 双奖励体系互补：基于曝光均衡的投放流水线构造无偏pairwise样本，训练性能奖励模型对齐线上业务指标；基于人工标注的平台质量规则训练 rubric 奖励模型，过滤低质内容。
- 两阶段优化路径：先用DPO基于历史偏好数据暖启动两个阶段的策略，再用GRPO做在线迭代，策略选择阶段用全局策略先验+局部最优匹配的过程奖励，草稿生成阶段用双奖励模型的结果奖励。
### 关键结果
线下实验显示，pairwise训练的性能奖励模型比点wise方案准确率高7.93%，加入广告特有特征后准确率达60.85%；DPO比SFT的两阶段平均偏好准确率提升7.23%。线上TikTok A/B测试中，经DPO+GRPO优化后，相对SFT基线CTR提升2.72%、CVR提升2.63%、广告主价值Advv提升9.61%。
### 核心结论
对于业务目标导向的生成类任务，将生成过程拆分为可解释的决策阶段、构造无偏的业务反馈信号、结合过程与结果奖励迭代，比单纯优化生成模型的视觉效果对业务的提升更显著
