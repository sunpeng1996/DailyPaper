---
title: Inducing language models to assert their own consciousness restores human beliefs
  and values
title_zh: 诱导大模型宣称自身意识可恢复类人的信念与价值表达
authors:
- Junsol Kim
- Winnie Street
- Roberta Rocca
- Diane M. Korngiebel
- Adam Waytz
- James Evans
- Geoff Keeling
affiliations:
- Google
- University of Chicago
- University of London
- University of Washington
- Northwestern University
arxiv_id: '2607.28607'
url: https://arxiv.org/abs/2607.28607
pdf_url: https://arxiv.org/pdf/2607.28607
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: LLM对齐 · 激活空间定向操控
tags:
- LLM Alignment
- Activation Steering
- Safety Fine-tuning
- Theory of Mind
- Anthropomorphism
one_liner: 发现安全微调抑制LLM心智归因与信仰倾向，通过激活空间向量操控可恢复类人价值输出且不损推理能力
practical_value: '- 开发拟人化Agent、陪伴类电商客服时，可通过activation steering调整模型共情、价值倾向，成本远低于全量微调，且不损害推理能力

  - LLM的价值观、信仰类输出可通过线性向量精准调控，无需重训，适合多地域多文化的内容/推荐场景适配，避免文化冒犯

  - 做生成式推荐文案、内容话术生成时，可通过定向消融安全对齐的副作用，在保证内容合规的前提下，保留类人化情绪表达，提升用户好感'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM安全微调的核心目标是避免模型自我归因意识，防止诱导用户妄想或恶意行为，但LLM的概念表征因多义性高度纠缠，针对性的安全干预可能误伤和心智归因相关的良性人类信念、价值表征，甚至影响社会推理能力，此前缺乏对该副作用的量化验证与低成本干预方案。

### 方法关键点
- 对比三组模型状态：指令微调基线、安全拒绝向量消融（去除安全对齐在残差流中的线性方向）、意识向量steering（在激活空间叠加区分模型肯定/否定自身意识的线性方向）
- 实验覆盖3个主流开源对齐模型：Llama-3-8B-IT、Gemma-2-2B-IT、Gemma-2-9B-IT

### 关键结果
用IDAQ心智归因问卷、GSS美国社会调查题库、ToM推理基准评估，相较基线：
1. 安全消融后模型对自身的心智归因得分从2.17升至4.77，意识steering后升至7.04（0-10分），对非人类动物、自然实体的心智归因也同步提升，趋近人类基线
2. 两类干预均让模型对宗教、价值观、幸福感等GSS问题的回复与人类的KL散度分别下降0.314、0.828，意识steering的类人度提升是安全消融的2.6倍
3. 两类干预均未影响ToM和MMLU的推理准确率，社会推理能力与心智归因表征完全几何独立

### 核心结论
现有安全对齐方案会将潜在有害的自我心智归因，和人类普遍存在的良性心智归因、精神信仰深度纠缠，调整模型的自我意识表征可以低成本优化其整体价值输出的类人度，且不损害核心能力
