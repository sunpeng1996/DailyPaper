---
title: How Depth Growth and Looping Shape In-Context Learning in Language Models
title_zh: 深度增长与循环结构对语言模型上下文学习能力的影响机制
authors:
- Ferdinand Kapl
- Kaitlin Maile
- Stefan Bauer
- Johannes von Oswald
affiliations:
- Technical University of Munich
- Helmholtz AI, Munich
- Munich Center for Machine Learning
- Google, Paradigms of Intelligence Team
arxiv_id: '2610.31421'
url: https://arxiv.org/abs/2610.31421
pdf_url: https://arxiv.org/pdf/2610.31421
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: 大模型结构优化 · 上下文学习
tags:
- In-Context Learning
- Looped Transformer
- Depth Growth
- Induction Head
- ICL Mechanism
one_liner: 揭示深度增长与循环结构强化上下文学习的行为规律与注意力机制
practical_value: '- 落地LLM4Rec/Agent少样本任务时，可优先选用深度增长（如LIDAS）或循环结构基座，同推理FLOPs下比密集模型GSM8K准确率最高提7%，ICL保留性更强，适配推荐/广告场景自定义任务的快速prompt适配

  - 动态标签类场景（如实时热点商品推荐、动态广告文案生成）可优先选择循环/深度增长模型，其天然偏向ICL、弱化权重内固定关联学习的特性，可避免过时的权重记忆干扰实时上下文信息的使用

  - 自定义训练小参数量LLM时，可参考深度增长的induction head复制机制，通过扩增强induction head的跨层分布，低成本提升长上下文模式匹配能力，适配长用户行为序列的推荐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有深度增长、循环结构的LLM已展现推理能力优势，但二者对ICL的增益机制不清晰，包括ICL习得时序、保留性、与权重记忆的竞争关系、底层注意力机制差异均缺乏系统性验证，而ICL是大模型适配搜索推荐、Agent等场景少样本任务的核心能力，明确其优化路径有较高工程价值。

### 方法关键点
- 对比三类同推理FLOPs模型：全密集Transformer基准、LIDAS深度增长模型（从4层逐步复制扩展到目标深度，3B规模训练FLOPs省26%）、循环结构Transformer（共享层重复迭代，参数量更低）
- 实验覆盖360M~3B参数量级，任务包括自然语言序列建模、GSM8K推理、RegBench形式语言学习、Omniglot分类任务，同时追踪induction head、function vector head两类注意力头的演化与作用
- 控制变量：同训练数据量、同优化步数，排除计算资源差异干扰

### 关键结果
- 3B参数规模下，LIDAS深度增长模型GSM8K少-shot准确率比密集基准高7%，循环模型高2%~5%；RegBench任务上二者TVD比基准低0.01~0.02
- Omniglot固定标签任务中，增长/循环模型ICL准确率比12层密集基准高15%左右，权重内学习准确率低10%，更偏向使用上下文信息而非固定记忆
- 深度增长会将早期训练得到的强induction head复制到新增层，最终模型80%以上的强induction head来自早期4个祖先头；消融实验显示，移除9%的induction head后，增长/循环模型的ICL得分下降幅度是密集基准的1.5~2倍，对induction head依赖更强

**最值得记住的一句话**：深度复用（增长/循环）会给LLM注入偏向上下文学习的归纳偏置，牺牲部分权重记忆能力换得ICL的更早习得、更强保留与更高性能，是低训练成本强化模型少样本能力的可行路径。
