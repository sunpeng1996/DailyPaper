---
title: Resisting Harmful Instructions through Training-Free Weight Editing
title_zh: 基于免训练权重编辑的大模型有害指令抵御方法
authors:
- Ali Ebrahimpour-Boroojeny
- Xiaocong Yang
- Samuel Schapiro
- Zahra Borhani
- Francisco R. Ortega
- Yujia Zheng
- ChengXiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
- AI Interpretability @ Illinois
arxiv_id: '2610.21189'
url: https://arxiv.org/abs/2610.21189
pdf_url: https://arxiv.org/pdf/2610.21189
published: '2026-10-14'
collected: '2026-10-19'
category: LLM
direction: LLM安全对齐 · 免训练权重编辑
tags:
- Weight Editing
- Safety Alignment
- Training-Free
- Activation Contrast
- LLM Safety
one_liner: 提出基于激活对比的免训练权重编辑方案，无需额外推理逻辑即可降低LLM对有害指令的遵从率
practical_value: '- 电商导购、客服类Agent可复用该激活对比编辑框架，仅需25对正反指令做前向传播，无需训练即可快速屏蔽特定有害指令（如诱导退货、恶意比价引导），落地成本极低

  - 生成式推荐、广告文案生成场景可通过该方法定向编辑权重，避免模型生成虚假宣传、性别歧视类违规内容，鲁棒性优于固定系统prompt，不会被prompt注入绕过

  - 部署无额外推理开销，无需添加系统prompt或推理层激活干预，适配高QPS的电商搜索、推荐、广告业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM安全干预方案存在明显缺陷：系统prompt易被prompt注入绕过，激活steering泛化性差、依赖推理层修改，微调成本高且需要大量标注数据；而电商、Agent场景下大模型一旦遵从有害指令，会直接造成用户投诉、合规风险甚至财产损失，亟需轻量、鲁棒的低成本安全干预方案。
### 方法关键点
- 构造正反配对prompt集：针对目标有害行为（如要求撒谎、生成歧视内容），固定底层内容分别附加有害/合规指令，仅需25对即可完成校准
- 计算激活对比度：仅通过前向传播计算每个输入通道在两类指令下的激活范数差值，默认筛选有害指令下激活度高于合规场景2.7倍的通道
- 权重编辑：按「权重绝对值×通道对比度」打分，每层矩阵选取前4%高权重做系数衰减（α默认-1.25），全程无需梯度、无需训练
### 关键实验
覆盖Llama-3.1-8B、Phi-4-mini等5款主流开源指令微调模型，对比未编辑模型、诚实系统prompt、激活steering、set-difference权重编辑等基线：
- 指令说谎场景：LIARS' BENCH诚实率平均84.9%，较最优基线高6.2pp；AI Liar诚实率平均79.4%，较最优基线高4.6pp
- 指令性别歧视场景：平均性别歧视回复率从57.9%降至24.3%，搭配公平性系统prompt可进一步降至11.9%
- 跨prompt格式迁移性显著优于激活steering，单轮unseen格式下诚实率高12.4pp，对构造prompt格式的敏感度仅为steering的1/4
最值得记住的一句话：仅需25对prompt、10分钟即可完成的免训练权重编辑，安全干预效果和鲁棒性超过系统prompt与常规激活steering，且完全不增加推理成本。
