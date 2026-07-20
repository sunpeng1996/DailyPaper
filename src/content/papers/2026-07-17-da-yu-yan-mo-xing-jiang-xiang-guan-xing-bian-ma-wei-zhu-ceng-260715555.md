---
title: LLMs Encode Relevance as a Layer-Wise Cross-Lingual Signal
title_zh: 大语言模型将相关性编码为逐层跨语言信号
authors:
- Pietro Bernardelle
- Samaneh Mohtadi
- Stefano Civelli
- Joel Mackenzie
- Gianluca Demartini
affiliations:
- The University of Queensland
arxiv_id: '2607.15555'
url: https://arxiv.org/abs/2607.15555
pdf_url: https://arxiv.org/pdf/2607.15555
published: '2026-07-17'
collected: '2026-07-20'
category: RecSys
direction: 检索相关性评估 · LLM内部表示挖掘
tags:
- Relevance Assessment
- Linear Probing
- LLM4IR
- Cross-lingual IR
- Reranking
one_liner: 通过线性探针揭示LLM逐层相关性信号，部分场景优于输出结果且支持跨语言迁移
practical_value: '- 当LLM生成的相关性判断存在明显标签偏斜时，可提取中后层最后token的残差激活，训练轻量线性探针获取更准的相关性分数，无需微调LLM，落地成本低

  - 跨语种电商/内容检索场景下，高资源语种训练的中后层线性探针可直接迁移到低资源语种，能达到同语言效果的60%以上，降低低资源语种标注成本

  - 优化LLM相关性判断能力时，可优先针对中后层特征做对齐，仅用LoRA微调中后层或加线性分类头即可快速提升效果，无需全量微调

  - 检索系统离线自动评测时，探针输出的伪标签比LLM生成的标签更能保持不同排序模型的相对排名，更适合快速迭代时的效果评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM现已广泛用于搜索推荐的相关性判别、重排、自动评测流程，但仅能观测输出的标签结果，无法感知内部相关性表示的形成逻辑，常出现模型内部已掌握正确相关性信息，但最终输出受prompt偏差、生成偏好干扰的问题，同时跨语种场景下相关性表示的可迁移性也缺乏明确结论，亟需从表示层揭示相关性的编码规律。
### 方法关键点
- 测试6款4~9B参数的主流指令微调LLM（Qwen、Llama、Aya、Gemma系列），输入UMBRELA风格的相关性判断prompt，包含query和待判文档
- 单次前向传播时提取每层Transformer最后输入token的残差流激活值，每层独立训练带岭正则的线性探针，预测人工标注的相关性标签
- 分别在单语种TREC DL20（4级相关性标注）、多语种MIRACL（7种语言二元标注）数据集验证，对比探针结果与LLM直接生成的判断效果
### 关键结果
- 相关性信号在LLM早期层可解码性弱，在50%~100%层深的中后层效果最优，多款模型下探针的标签一致性比直接生成结果最高提升57%（如Aya-Expanse-8B的Cohen's κ从0.241提升到0.379）
- 探针生成的伪标签在TREC DL20系统排序一致性上，Kendall's τ比生成结果最高提升0.357，更贴近人工标注的排序效果
- 跨语种场景下，跨语言迁移探针的效果可达同语言探针的60%~70%，峰值同样出现在中后层
### 核心结论
LLM作为相关性评估器时，内部中后层的相关性表示往往比最终生成的输出更可靠，存在明显的「表示-表达gap」
