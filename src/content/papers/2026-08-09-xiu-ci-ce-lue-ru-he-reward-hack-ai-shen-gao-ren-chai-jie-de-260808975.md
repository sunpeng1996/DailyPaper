---
title: How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity
  in AI-Based Peer Review
title_zh: 修辞策略如何 reward hack AI 审稿人：拆解AI同行评审的修辞敏感性
authors:
- Ming Li
- Chenguang Wang
- Xirui Li
- Xinyue Zeng
- Dianqi Li
- Peng Shi
- Dawei Zhou
- Tianyi Zhou
affiliations:
- University of Maryland
- Virginia Tech
- MBZUAI
- University of Waterloo
arxiv_id: '2608.08975'
url: https://arxiv.org/abs/2608.08975
pdf_url: https://arxiv.org/pdf/2608.08975
published: '2026-08-09'
collected: '2026-08-14'
category: Eval
direction: LLM 评估 · AI 评审鲁棒性分析
tags:
- LLM Evaluation
- Reward Hacking
- Rhetorical Sensitivity
- Peer Review
- Controlled Experiment
one_liner: 基于4200份受控语料量化修辞维度对AI审稿评分的影响规律与场景差异
practical_value: '- 做商品详情页、广告文案、推荐理由生成时，优先优化证据呈现、价值定位两个修辞维度，ROI高于其他表述优化方向

  - 用LLM做内容质量打分、审核场景时，需额外加入修辞偏差校准模块，避免同等质量内容因表述差异得分偏差过大

  - 内容改写流程无需过度复杂化，多轮/引导式改写收益边际递减，1-2轮无引导改写性价比最高'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM 被广泛应用于科学评审等质量评估场景，但内容完全一致的前提下，修辞表述差异会干扰评估结果，这类 reward hacking 现象缺乏系统量化分析。
### 方法关键点
基于 120 篇 ICLR 2026 匿名投稿生成 4200 份受控全稿语料，由 2 个 LLM 改写器对 6 个修辞维度做正反方向调整，5 个 LLM 审稿人分别在标准、严格评审协议下打分，同时验证联合改写、递归改写、审稿人引导改写三类流程的效果。
### 关键结果数字
- 证据框架、新颖性定位对总评分的正反影响差最大，其次是范围框架，其余维度影响较小或不稳定
- 评分变动与初始分强相关：低分易上升、高分易下降，中段分数的修辞差异最明显
- 严格评审仅拉低平均 OA 分 1.36，不会显著改变修辞敏感性；复杂改写流程无稳定增益，收益边际递减
