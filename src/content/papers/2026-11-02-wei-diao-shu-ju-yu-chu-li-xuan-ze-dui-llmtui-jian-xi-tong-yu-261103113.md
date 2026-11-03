---
title: 'Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic
  Sensitivity in LLM-Based Recommendation'
title_zh: 微调数据预处理选择对LLM推荐系统效用与人口统计敏感度的影响
authors:
- Furkan Yasir Goksu
- Yaren Yilmaz
- Sule Gunduz Oguducu
affiliations:
- Istanbul Technical University
arxiv_id: '2611.03113'
url: https://arxiv.org/abs/2611.03113
pdf_url: https://arxiv.org/pdf/2611.03113
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 微调数据预处理与公平性
tags:
- GenRec
- LLM4Rec
- Fairness
- SFT
- Preprocessing
- Constrained Decoding
one_liner: 量化三类微调数据预处理策略对LLM推荐效用、输出稳定性与人群公平性的异质性影响
practical_value: '- 生成式LLM推荐落地可直接复用「<SOI>/<EOI>特殊标记训练+前缀树约束解码」方案，能100%消除out-of-catalog输出，保证推荐列表长度合规

  - 微调阶段加入30+种同义prompt模板做增强，可将prompt带来的HR@10波动从2.18pp降至0.26pp，同时提升整体效用、降低重复推荐率

  - item文本表示（如商品标题格式化规则）会显著影响效果：降低标题前缀共享率的表示方案可提升HR@10约1.8pp、Coverage@10约6.5pp，标题格式需作为核心设计选择而非工程细节

  - 做人群公平性优化时不要盲目做全属性数据平衡：年龄平衡几乎无损效用且缩小组间差距，性别平衡反而会降低效用且无公平性收益，需分属性测试效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式LLM推荐普遍存在输出不合规、prompt波动大、人群敏感等问题，现有优化多聚焦prompt、推理层策略，对微调数据预处理的影响缺乏系统量化，且极少同时权衡效用与公平性表现。

### 方法关键点
- 搭建受控生成式推荐pipeline：引入<SOI>/<EOI>特殊标记包裹item，前缀树约束解码彻底消除out-of-catalog输出，微调阶段加入37种同义指令模板做prompt增强，降低输出对prompt措辞的敏感性
- 控制变量测试三类预处理策略：item标题表示（原始格式/归一化格式）、微调数据人口属性平衡（性别/年龄分群重采样）、辅助item知识增强（新增item属性/描述类QA样本）
- 统一评估体系：覆盖推荐效用、输出合规性、prompt一致性、人群敏感度四大维度

### 关键实验结果
基于MovieLens-1M数据集，以Llama-3-8B-Instruct为基座做QLoRA微调：
1. 原始标题相比归一化标题，HR@10从10.67%提升至12.47%，Coverage@10从41.36%提升至47.88%
2. 年龄平衡微调几乎无损效用（HR@10仅从12.47%降至12.39%），同时将年龄组间效用差从0.69pp降至0.38pp；性别平衡反而降低效用且无公平性收益
3. 辅助知识微调仅损失0.23pp HR@10，同时将性别组间效用差从0.45pp降至0.1pp，年龄组间从0.69pp降至0.32pp

微调数据预处理不是无关紧要的工程细节，而是同时影响推荐效用、输出稳定性与人群公平性的核心设计选择，需多维度综合评估。
