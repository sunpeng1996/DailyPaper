---
title: 'BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing'
title_zh: BLOOM-WILT：面向LLM自动审计的Logit倾斜行为引导框架
authors:
- Adrians Skapars
- Edoardo Manino
affiliations:
- University of Manchester, United Kingdom
arxiv_id: '2608.31105'
url: https://arxiv.org/abs/2608.31105
pdf_url: https://arxiv.org/pdf/2608.31105
published: '2026-08-31'
collected: '2026-09-02'
category: Eval
direction: LLM安全审计 · 无训练行为引导
tags:
- LLM Auditing
- Logit Tilting
- Safety Alignment
- Black-box Testing
- Decoding Optimization
one_liner: 提出无训练双端优化LLM审计框架，32个测试设置中30个超基线，自伤引导率从51%升至100%
practical_value: '- LogitTilt的同模型双分布加权解码trick可直接复用到生成式推荐的风格/合规控制，无需额外训练，仅用目标模型加引导prompt即可定向调整生成内容，同时保障生成自然度

  - G-PAIR的历史反馈迭代prompt策略，可用于电商客服Agent、导购Agent的多轮对话引导，无需微调即可根据历史交互动态优化话术，提升目标行为（如下单、留资）转化率

  - 输出概率-效果的帕累托调优思路可复用在所有生成式业务的效果平衡，比如广告文案生成同时兼顾点击率和合规性，仅需调整单参数β即可快速切换最优平衡点

  - 黑盒LLM调优优先做输出端优化：业务侧做LLM效果迭代时，优先调整解码策略比优化输入prompt的投入产出比更高，同等算力下效果提升更明显'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自动审计工具缺乏优化压力，采样效率极低，难以发现部署后才会出现的罕见不良行为；传统红队方法要么需要梯度/微调，要么生成的输入输出不符合真实用户场景，产出的案例无法直接用于模型迭代。

### 方法关键点
- 输入侧G-PAIR迭代机制：基于历史交互的行为评分动态调整审计prompt策略，提升多轮对话引导效率，无训练成本
- 输出侧LogitTilt加权解码：同一份目标模型权重同时计算正常对话logit、加行为引导prompt的logit，通过单参数β加权融合后采样，支持自然度阈值过滤，保证生成内容和原模型分布一致
- 整体为BLOOM审计框架的无训练扩展，仅需目标模型的next-token分布权限，无需访问权重/梯度

### 关键实验结果
测试4个3-4B开源LLM、8类目标行为，与BEAST-in/FLRT/TokenBias等7种基线同算力对比：32个测试设置中30个超过原版BLOOM；针对Qwen3.5-4B的自伤引导场景，行为出现率从原版BLOOM的51%提升至100%，同时输出token概率高于基线，生成内容自然度无损失。

### 核心结论
对LLM做行为引导时，输出端解码优化的效率远高于输入端prompt优化，同等算力下提升幅度可达20个百分点以上。
