---
title: Log-Depth Recurrent Language Modeling
title_zh: 对数深度循环语言建模
authors:
- Yiqin Wang
- Nuri Cingillioglu
- Charles Pert
affiliations:
- Imperial College London
arxiv_id: '2609.28212'
url: https://arxiv.org/abs/2609.28212
pdf_url: https://arxiv.org/pdf/2609.28212
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: 大语言模型 · 高效长上下文架构
tags:
- LLM
- Language Modeling
- Parallel Scan
- Length Extrapolation
- Efficient Inference
one_liner: 引入并行扫描下扫操作构建对数深度自回归语言模型，兼具线性复杂度与强长度外推能力
practical_value: '- 长上下文Agent、长用户行为序列建模等场景可尝试引入该架构，无需显式位置编码即可获得媲美ALiBi的长度外推能力，3000token长度下推理速度比Transformer快5倍，大幅降低长序列推理延迟

  - 并行扫描的上扫+下扫计算范式可复用在推荐系统的用户行为序列编码模块，替换自注意力层，在损失少量精度的前提下换取长序列下的线性推理效率

  - Gated Recursive Cell的三元门控融合设计可迁移到现有序列特征融合模块，提升层级化序列信息的建模效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer自回归推理复杂度随序列长度平方增长，常规RNN存在线性深度的顺序计算瓶颈，现有树形递归模型仅支持序列编码任务，无法高效实现自回归预测，长上下文场景亟需兼顾计算效率与外推能力的新架构。
### 方法关键点
- 基于Blelloch并行扫描的上扫+下扫操作：上扫构建平衡二叉树的层级中间表示，下扫复用中间结果并行生成所有前缀表示，整体计算深度为O(logN)、总运算量为O(N)
- 采用Gated Recursive Cell（GRC）作为可学习二元组合算子，通过三元门控融合前后状态与候选特征，无需显式位置编码
- 采用标准下一词预测交叉熵损失训练，参数规模与Transformer基线严格对齐
### 关键结果
在PTB、WikiText-2、OpenWebText2三个数据集上对比ALiBi Transformer、正弦位置编码Transformer基线，参数覆盖3.5M~100M：
- WikiText-2上AR-GRC困惑度比ALiBi Transformer高6.1%，比正弦Transformer低3.8%
- 训练时最大上下文为512token，测试时支持近6倍长度（3000token）的稳定预测，长度外推能力媲美ALiBi Transformer，远优于正弦Transformer
- 3000token长度下推理速度比Transformer快5倍，推理耗时随序列长度线性增长
> 最值得记住：对数深度递归语言模型无需显式位置编码即可实现强长度外推，长序列下的线性复杂度优势使其成为Transformer之外的高潜力替代架构
