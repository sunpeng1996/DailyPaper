---
title: Language Models as AI Research World Models
title_zh: 大语言模型作为AI研究世界模型的效果验证与迁移研究
authors:
- Zijun Wang
- Zewen Liu
- Minhua Lin
- Zhaotian Weng
- Zhan Shi
- Bing He
- Yisi Sang
- Dakuo Wang
- Benoit Dumoulin
- Wei Jin
affiliations:
- Amazon
- UC Santa Cruz
- Emory University
- Pennsylvania State University
- UC Santa Barbara
arxiv_id: '2610.12235'
url: https://arxiv.org/abs/2610.12235
pdf_url: https://arxiv.org/pdf/2610.12235
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: AI研究Agent 世界模型能力验证
tags:
- World Model
- LLM Agent
- Experimental Prediction
- Knowledge Transfer
- In-context Learning
one_liner: 验证大语言模型可作为研究世界模型，复用跨环境实验知识预测干预效果、降低实验成本
practical_value: '- 高试错成本场景（如推荐算法AB测、大模型调参、广告策略迭代）可复用RWM思路：先让LLM基于历史实验数据预测候选方案效果，仅落地TopK高潜力方案，大幅降低测试成本

  - 冷启动新业务场景实验时，可注入相似场景的历史实验记录作为in-context示例，该方案的提升效果远优于更换更强LLM、增加推理步数

  - 实验知识可结构化沉淀：无论成功/失败实验，均统一存储环境配置、干预手段、效果指标等字段，作为后续RWM的输入，长期降低业务迭代试错成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
AI研究Agent可快速生成大量候选实验方案，但真实执行成本极高（单实验动辄几十上百H100小时），预算有限的情况下无法全部落地，亟需在执行前预测实验效果的能力，优先分配资源到高潜力方案。

### 方法关键点
- 提出Research World Model（RWM）框架：输入研究环境配置、候选干预方案、历史实验记录，由LLM直接预测该干预在对应环境下的效果增益
- 设计三类预测范式：无历史记录零样本预测、同环境历史记录预测、跨环境历史记录迁移预测，验证知识复用能力
- 仅通过in-context学习注入历史实验数据，无需微调LLM参数，落地成本低

### 关键实验
- 数据集覆盖预训练、后训练、推理3大类共9个研究环境，包含2653条真实实验记录，对应17.1万+ H100 GPU时的实验成本
- 核心结果：同环境预测下注入历史记录将Spearman相关性从0.506提升至0.774；跨环境预测时注入其他环境历史记录将Spearman相关性从0.628提升至0.729，Qwen3场景下选择后悔度比零样本降低78%；多轮自动研究场景下，注入同/跨环境历史知识分别将最终最优增益提升15.8%、11.6%
- 消融实验：13款LLM测试显示，注入历史实验知识的提升效果远大于换更强模型、调高推理步数，最弱模型加知识的表现超过无知识的最强模型

### 核心结论
对于需要大量试错、实验成本高的场景，结构化沉淀的历史实验知识的价值，远大于单纯提升模型能力或推理复杂度。
