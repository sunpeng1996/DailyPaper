---
title: 'When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap'
title_zh: 隐式推理中激活引导失效的原因：隐空间到语言的转换鸿沟
authors:
- Gaoxiang Huang
- Lei Qi
affiliations:
- HKUSTGZ
- SEU
arxiv_id: '2609.21662'
url: https://arxiv.org/abs/2609.21662
pdf_url: https://arxiv.org/pdf/2609.21662
published: '2026-09-18'
collected: '2026-09-21'
category: Reasoning
direction: LLM推理控制 · 隐空间转换鸿沟
tags:
- Activation Steering
- Latent CoT
- Chain of Thought
- LLM Control
- Representation Engineering
one_liner: 发现隐式CoT激活引导效果远弱于显式CoT，提出隐空间到语言转换鸿沟解释失效原因
practical_value: '- 做基于隐式CoT的Agent推理控制时，不能仅验证隐空间任务信息可解码，必须实测跨转换边界后的输出控制效果，避免控制失效

  - 做LLM输出对齐（如推荐文案立场控制、商品评价情感引导）时，优先选择显式CoT路径做激活引导，控制效果比隐式CoT稳定9~70倍

  - 若采用隐式CoT优化推理效率，需额外增加隐空间到语言转换层的token级监督，确保隐空间干预能传递到输出端

  - 评估激活引导效果时，可复用文中bidirectional steering gain、normalized displacement指标，避免仅靠LLM judge带来的评估偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
激活引导是显式CoT推理场景下控制LLM输出的成熟方案，随着隐式CoT技术（省略显式推理token提升效率）的普及，其在隐式推理场景下的适用性尚未验证，实际测试发现隐式推理中激活引导普遍失效，亟需定位根本原因。
### 方法关键点
- 对比Llama-3.1-8B、Llama-2-7B的显式CoT和COCONUT风格隐式CoT变体，两类模型均在同一ProSQA数据集训练，隐式版本采用5步连续隐向量推理
- 采用Contrastive Activation Addition（CAA）提取任务相关方向，在第16层残差流做干预，λ取值范围为±1/±5/±10
- 评估体系覆盖四类指标：steering success rate（LLM judge评估输出是否符合目标）、stance margin变化（无采样偏差的next token分布统计）、normalized displacement（验证隐空间干预是否生效）、bidirectional steering gain（衡量干预对输出的双向控制效果）
### 关键结果
- 测试数据集覆盖情感分类、TruthGen（真实性判断）、TwinViews-13k（政治立场）三类任务
- 相同隐空间位移下，隐式CoT的立场token概率偏移仅为显式CoT的1%~5%
- 隐式CoT的隐空间到语言转换的token分布变化幅度是显式CoT的5.6~24.2倍
- 隐式CoT的双向控制增益比显式CoT弱9.4~70.2倍

激活引导的三个核心要素（隐空间存在任务信息、干预可移动隐向量、移动可传递到输出）不可等同，隐式推理场景下必须验证跨转换边界的实际输出效果。
