---
title: 'Same Entity, Different Script: Diagnosing Cross-Script Entity Matching Failures
  in Language Models'
title_zh: 大模型跨文字体系实体匹配失败的诊断与优化方法
authors:
- Athira Gopal
- Patil Prathamesh Pravin
- Ankush Kadu
- Arpit Jain
- Ashwanth Krishnan
affiliations:
- QpiAI India
arxiv_id: '2610.31407'
url: https://arxiv.org/abs/2610.31407
pdf_url: https://arxiv.org/pdf/2610.31407
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 多语言LLM · 跨脚本实体匹配优化
tags:
- Multilingual-LLM
- Entity-Matching
- Activation-Patching
- Cross-Script
- Model-Intervention
one_liner: 定位跨脚本实体匹配失败因果位点，干预将马拉地语同实体准确率从6.5%提至33.5%
practical_value: '- 跨境电商多语言搜索/商品实体对齐场景，若遇到非拉丁文字实体匹配准确率低的问题，可优先做输出得分标量校准，无需微调即可恢复87%的性能gap，成本极低

  - 多语言LLM相关业务的效果优化可参考本文的激活位点定位方法，针对任务关键位置（如实体比较任务的第二实体中层）做轻量干预，效果优于零散调参

  - 做跨语言模型评测时需同时观测AUROC和准确率，前者衡量模型的表征区分能力，后者反映决策阈值合理性，避免误判模型能力边界'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言大模型对同一实体的不同文字写法（如天城文/拉丁文字的人名、商品名）判断一致性差，直接影响跨境搜索、多语言实体对齐、多语种Agent的事实准确性，现有研究缺少对该问题的机制定位和可落地优化方案。

### 方法关键点
- 构建601条经过人工审计的天城文-拉丁文人名对、374条马拉雅拉姆文-拉丁文人名对数据集，固定提问模板、实体关系，仅改变实体文字写法控制变量
- 用线性探针检测隐藏状态中的实体匹配信号，通过激活补丁定位因果敏感位点，基于梯度提取共享干预向量
- 对比tokenization优化、标量校准、激活干预等多种方案的效果差异

### 关键结果
- Qwen2.5-7B在马拉地语prompt下同实体判断准确率从拉丁文字的35.1%降至天城文的8.5%，负样本准确率始终保持98%以上，马拉雅拉姆文场景下准确率仅5.3%
- 仅通过标量校准即可恢复87%的性能gap，说明大部分失败来自决策阈值偏移而非表征缺失
- 在第二实体的中间层（12-17层）施加共享向量干预，可将马拉地语同实体准确率从6.5%提升至33.5%，负样本准确率仍保持98.5%

**最值得记住的一句话**：多语言模型跨脚本实体匹配的大部分性能损失不是来自表征能力不足，而是顶层决策阈值的偏移，针对性干预可低成本大幅提升效果
