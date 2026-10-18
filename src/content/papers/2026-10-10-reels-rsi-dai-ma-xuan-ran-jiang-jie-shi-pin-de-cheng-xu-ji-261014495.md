---
title: 'Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos'
title_zh: Reels-RSI：代码渲染讲解视频的程序级自优化框架
authors:
- Wei Lin
affiliations:
- Agentic Loops X
arxiv_id: '2610.14495'
url: https://arxiv.org/abs/2610.14495
pdf_url: https://arxiv.org/pdf/2610.14495
published: '2026-10-10'
collected: '2026-10-18'
category: Agent
direction: Agent 自优化 · 规则型记忆落地
tags:
- Agentic Self-Improvement
- Rule-based Memory
- Program-level Optimization
- Preference Bias Mitigation
- Content Generation
one_liner: 提出无需调整权重或Prompt的程序级自优化开源代码渲染讲解视频生成Agent框架
practical_value: '- 做Agent生成内容（如电商短视频、种草文案）自优化时，可优先采用程序级规则迭代方案，无需调参改Prompt，落地成本低

  - 沉淀Agent经验记忆时，可给每条规则配置必过/必拒用例做单元测试，避免规则退化，还可回溯校验历史产出

  - 做偏好标注/人工评测时需提前校正位置偏差，本研究显示用户偏好第二个展示样本的概率高达62-81%，易干扰评测结论'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有讲解视频生成多聚焦像素端优化，产出不可审计、无法回溯修改逻辑；基于权重/Prompt调整的自优化方案落地成本高、可解释性差
### 方法关键点
1. 自优化全部发生在脚本、分镜、动画代码的程序层，不改动模型权重或Prompt
2. 每次修改留存代码快照，复盘时将修复经验转为带必过/必拒用例的可测试规则，新规则自动校验所有历史产出
3. 规则、剧本迭代需通过盲测+人工双重校验才会正式落地
### 关键结果
111条视频实验显示：规则100%拦截新产出同类缺陷，检出4个历史潜伏缺陷；弱Agent配置规则后违规数从30降至5；人工评测位置偏差最高达81%，可完全掩盖真实效果差异
